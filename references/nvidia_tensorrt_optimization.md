# NVIDIA TensorRT-LLM for Hebrew — Production Optimization Guide

When you need to serve Hebrew LLM inference at scale (hundreds of QPS, low-latency, cost-controlled), the production-grade path is **DictaLM-2.0 + NVIDIA TensorRT-LLM + Triton Inference Server**.

This document is the integration recipe. **Source:** [NVIDIA Developer Blog — Accelerating Hebrew LLM Performance with NVIDIA TensorRT-LLM](https://developer.nvidia.com/blog/accelerating-hebrew-llm-performance-with-nvidia-tensorrt-llm/).

---

## When this matters

The skill itself doesn't require this — Claude runs in the cloud. But when:

- You're building a **product** that exposes Hebrew LLM (chatbot, agent, RAG over Hebrew docs) at scale
- You need **predictable latency** under load (panel-grade demo, broadcast, live event)
- You have **compliance constraints** that prohibit calling a foreign LLM API for Hebrew data
- You want **cost control** for high-volume inference

…then you deploy DictaLM-2.0 with TensorRT-LLM on NVIDIA H100 / A100 GPUs.

---

## The performance picture

From NVIDIA's measurements on A100:

- **Baseline (Python backend)** — linear latency growth with concurrent requests. Doesn't scale.
- **TensorRT-LLM (FP16)** — near-constant latency as concurrent requests grow. Tensor parallelism handles the load.
- **TensorRT-LLM (INT4)** — same scaling behavior as FP16, with significantly reduced memory bandwidth. Slight quality cost; for most Hebrew tasks, indistinguishable from FP16 in human evaluation.

Concretely, on a single A100:
- The Python backend at 16 concurrent requests = unusable latency
- TensorRT-LLM at 16 concurrent requests = production-acceptable
- Async workloads with 1024-token outputs: handled.

---

## Why Hebrew specifically benefits

The NVIDIA article identifies five linguistic challenges that Hebrew LLMs face — and that an optimized runtime helps with:

1. **Root-pattern morphology** — Hebrew word formation requires sophisticated modeling. Loanwords integrate via pi'el / hif'il / nif'al binyanim. The LLM must produce the *right* binyan for context — and that depends on quality + tokenizer.

2. **Absent capitalization and limited punctuation** — Sentence segmentation in Hebrew is harder than English. Example: *הקפה* can mean "the coffee" or "encircle." Disambiguation depends on full context — costly without optimization.

3. **Flexible word order** — Hebrew supports VSO / SVO / OS structures. The LLM must produce natural ordering for the register; an optimized runtime can serve longer contexts without latency penalty.

4. **High morphological ambiguity** — a single Hebrew word can take 5+ readings before context. Quality requires longer context windows, which an optimized runtime enables.

5. **Missing diacritical marks** — Modern Hebrew normally omits nikud; the LLM infers vowels from context. Quality + speed both matter.

---

## The model: DictaLM-2.0-Instruct

[`dicta-il/dictalm2.0-instruct`](https://huggingface.co/dicta-il/dictalm2.0-instruct)

- **Base architecture:** Mistral 7B
- **Hebrew adaptation:** continually pre-trained with custom Hebrew tokenizer
- **Performance position:** led the HuggingFace Open Leaderboard for Hebrew LLMs at time of NVIDIA benchmarking
- **Why it's the TensorRT target:** the article specifically optimizes this model; tooling is proven against it

For newer DictaLM-3.0 variants, the same pipeline applies — verify each model's TensorRT compatibility per release.

---

## Step-by-step deployment

### 1. Environment setup

```sh
# NVIDIA TensorRT-LLM (verify latest version for your CUDA / Python)
pip install tensorrt-llm
# OR for stable: follow https://nvidia.github.io/TensorRT-LLM/

# Triton Inference Server
docker pull nvcr.io/nvidia/tritonserver:24.XX-trtllm-python-py3
```

Hardware required:
- **Minimum:** A100 40GB single GPU
- **Recommended:** H100 80GB single GPU
- **For high concurrency:** multi-GPU with tensor parallelism

### 2. Convert HuggingFace checkpoint → TensorRT-LLM

```sh
# Pull the model
huggingface-cli download dicta-il/dictalm2.0-instruct \
  --local-dir ./dictalm2.0-instruct-hf

# Convert to TensorRT-LLM FP16
python convert_checkpoint.py \
  --model_dir ./dictalm2.0-instruct-hf \
  --output_dir ./fp16_dictalm/ \
  --dtype float16

# Build engine
trtllm-build \
  --checkpoint_dir ./fp16_dictalm/ \
  --output_dir ./fp16_dictalm_engine/ \
  --max_input_len 4096 \
  --max_output_len 1024 \
  --max_batch_size 16
```

### 3. (Optional) INT4 quantization with Hebrew calibration

For reduced memory bandwidth and faster inference, post-training quantization (PTQ) with a Hebrew-specific calibration dataset:

```sh
python quantize.py \
  --model_dir ./dictalm2.0-instruct-hf \
  --output_dir ./int4_dictalm/ \
  --qformat int4_weights_only \
  --calib_dataset /path/to/hebrew_calibration_data.jsonl \
  --calib_size 512
```

**Calibration dataset:** ideally 500+ Hebrew text samples representative of your production workload. If you're serving talking-cards / pitches / blog generation, calibrate on a mix of those.

### 4. Deploy to Triton Inference Server

```sh
# Copy the engine to Triton's model repository
mkdir -p ./triton_models/dictalm/1/
cp -r ./fp16_dictalm_engine/* ./triton_models/dictalm/1/

# Write the config.pbtxt for Triton
cat > ./triton_models/dictalm/config.pbtxt <<EOF
name: "dictalm"
backend: "tensorrtllm"
max_batch_size: 16
# … see Triton TRT-LLM backend docs for full config
EOF

# Launch Triton
docker run --gpus all --rm -p 8000:8000 -p 8001:8001 -p 8002:8002 \
  -v $(pwd)/triton_models:/models \
  nvcr.io/nvidia/tritonserver:24.XX-trtllm-python-py3 \
  tritonserver --model-repository=/models
```

### 5. Invoke via HTTP

```sh
curl -X POST http://localhost:8000/v2/models/ensemble/generate \
  -H "Content-Type: application/json" \
  -d '{
    "text_input": "כתוב פיסקה קצרה על אבטחת מידע בעידן ה-AI agents.",
    "max_tokens": 256,
    "stop_words": ["</s>"],
    "temperature": 0.7
  }'
```

Response:
```json
{
  "text_output": "אבטחת מידע בעידן ה-AI agents היא אתגר חדש לחלוטין...",
  "tokens": [...]
}
```

---

## How the skill uses TensorRT-LLM

The skill itself runs on Claude — so TensorRT-LLM is **not** invoked by the skill at runtime. But the skill **recommends** this path when:

1. The user states **goal = "production deployment"** in STEP 0
2. The user mentions **compliance / data-residency** requirements
3. The user asks **"how do I serve this Hebrew LLM at scale?"**

In those cases, the skill recommends the user:
- Build the DictaLM-2.0 + TensorRT-LLM pipeline as above
- Use the skill's `corpus/jargon.json` as a few-shot prompt prefix in their serving stack
- Use the skill's `personas/*.md` as system-prompt templates

The skill can also output the system-prompt that the user should attach to their TensorRT-LLM-served model — see the `--export-system-prompt` flag on `scripts/hebrew_toolkit.py` (planned for v0.5.0).

---

## Cost / latency picture

Rough estimates from the NVIDIA blog + extrapolation:

| Deployment | Latency (single request) | Throughput (concurrent) | Cost |
|---|---|---|---|
| Claude API call | 800ms–2s (network + inference) | Limited by rate limit | $$$$ per million tokens |
| DictaLM-2.0 on Triton + TensorRT-LLM (A100, FP16) | 200–400ms | 16+ concurrent at constant latency | $ (hardware amortized) |
| DictaLM-2.0 on Triton + TensorRT-LLM (A100, INT4) | 150–350ms | 16+ concurrent | $ (less memory) |
| DictaLM-2.0 on Triton + TensorRT-LLM (H100, FP16) | 100–250ms | 32+ concurrent | $$ (better hardware, much better throughput) |

For most teams the cost crossover from Claude-API to self-hosted DictaLM is around **5–10M Hebrew tokens / month**. Below that, Claude API is cheaper. Above that, self-hosted wins.

---

## Failure modes to watch

1. **Tokenizer mismatch** — if you swap DictaLM-2.0 for a different Hebrew LLM, re-build the TensorRT engine. Don't reuse engines across tokenizers.

2. **Quantization-quality drift** — INT4 calibrated on the wrong dataset can degrade output quality on edge cases. Always validate INT4 against FP16 on a held-out test set before production.

3. **Concurrent-batch padding** — Hebrew long-context generation can dominate batches. If you mix short (50-token) and long (1024-token) requests, the long ones bottleneck throughput. Bucket your traffic.

4. **Diacritization absence** — DictaLM-2.0 outputs niqqud-less Hebrew (modern convention). If you need TTS or ceremonial text, route through Dicta Nakdan post-processing.

---

## When NOT to use this path

- **Low volume** (under 1M Hebrew tokens / month) — Claude API is simpler and cheaper
- **Highest quality required** — Claude 4.7 + Hebrew prompt outperforms DictaLM-2.0 on most subjective quality benchmarks
- **No GPU available** — TensorRT-LLM requires NVIDIA hardware; for CPU-only deployment use `dictalm-3.0-1.7b-gguf` via llama.cpp instead

---

## See also

- **`sources/hebrew_ai_models.json`** — full Hebrew model catalog
- **`sources/source_selection.md`** — decision tree for picking models per task
- **NVIDIA Developer Blog source:** https://developer.nvidia.com/blog/accelerating-hebrew-llm-performance-with-nvidia-tensorrt-llm/
- **DictaLM-2.0 model card:** https://huggingface.co/dicta-il/dictalm2.0-instruct
- **TensorRT-LLM docs:** https://nvidia.github.io/TensorRT-LLM/
- **Triton Inference Server:** https://github.com/triton-inference-server/server

---

*Last updated: 2026-05-22 for v0.4.0.*
