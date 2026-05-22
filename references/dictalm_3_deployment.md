# DictaLM 3.0 — Deployment & Variant Selection Guide

**Released**: December 2025 by DICTA (The Israel Center for Text Analysis).
**Status**: state-of-the-art for Hebrew open-weight LLMs in their weight class as of Dec 2025.
**Technical report**: [Dicta-LM 3.0: Advancing The Frontier of Hebrew Sovereign LLMs](https://dicta.org.il/publications/DictaLM_3_0___Techincal_Report.pdf).
**Collection**: [huggingface.co/collections/dicta-il/dictalm-30-collection](https://huggingface.co/collections/dicta-il/dictalm-30-collection)
**Org**: [huggingface.co/dicta-il](https://huggingface.co/dicta-il)

This guide tells the Ah Sheli Gibor skill exactly which DictaLM 3.0 variant to invoke per task and per deployment target. Consulted from STEP 4.5 (Source Selection).

---

## The 3 families

DictaLM 3.0 ships 3 sizes × 3 variants × 4 quant levels = 24 model artifacts. Pick by **size first, variant second, quant third.**

### Size 1 — 24B (flagship)

Initialized from Mistral-Small-3.1-24B. The highest-quality Hebrew LLM that DICTA ships.

| Variant | When |
|---|---|
| **24B-Base** | Pretraining-style completion, downstream fine-tuning, when you need raw next-token quality without chat alignment. |
| **24B-Thinking** | Complex reasoning, multi-step Hebrew prompts, long-form rubric scoring. Produces a `<think>` block before the final answer. Use for STEP 5g rubric grading and STEP 5h disambiguation. |

### Size 2 — Nemotron-12B (production sweet spot)

Nemotron-architecture 12B. Lower memory than 24B, better quality than 1.7B. Default for production API serving.

| Variant | When |
|---|---|
| **Nemotron-12B-Base** | Batch generation pipelines, large-corpus rewriting jobs. |
| **Nemotron-12B-Instruct** | **Production assistants. Default skill backend for STEP 4 (Write) when not using a frontier model.** Customer support, API serving. |

### Size 3 — 1.7B (edge / mobile / embedded)

Compact for on-device. Surprisingly capable for size, especially the Thinking variant.

| Variant | When |
|---|---|
| **1.7B-Base** | Edge text generation. |
| **1.7B-Instruct** | On-device Hebrew assistants, intent classification, low-latency UI suggestions. |
| **1.7B-Thinking** | Edge reasoning. Use over Instruct when quality matters more than latency. |

---

## Quantization decision matrix

| Quant | Memory vs BF16 | Quality cost | Hardware required |
|---|---|---|---|
| **BF16** (default) | 100% | 0% (reference) | H100 / H200 / A100 / B200 |
| **FP8** | ~50% | ~0% on quality benchmarks | H100 / H200 / B200 / MI300X (FP8 tensor cores) |
| **W4A16** | ~25% | ~1–2% on Hebrew benchmarks | RTX 4090 / 5090 / consumer GPUs |
| **GGUF** (q4/q5/q6/q8) | ~25–60% | varies per quant level | Apple Silicon / CPU / llama.cpp ecosystem |

**Rule of thumb for the skill:**
- Frontier-quality generation → BF16 24B-Thinking
- Cost-efficient production → FP8 Nemotron-12B-Instruct
- Consumer GPU dev box → W4A16 Nemotron-12B-Instruct
- Local Mac development → GGUF Nemotron-12B-Instruct or 1.7B-Thinking-GGUF

---

## Skill task → recommended variant table

Updates STEP 4.5 (Source Selection). When the user invokes a task with no explicit model override, default to:

| Skill task | Default variant | Reasoning |
|---|---|---|
| Rewrite (any register) | Nemotron-12B-Instruct | Quality/cost balance |
| Pitch generation | Nemotron-12B-Instruct or 24B-Thinking for high-stakes | Thinking shows working for the pitch's logical flow |
| Speech / keynote | 24B-Thinking | Long-form coherence + emotional arc reasoning |
| Talking cards / panel prep | 24B-Thinking | Two-step refinement (see [[hebrew-offensive-taxonomy]]) for sharp-vs-offensive disambiguation |
| Teleprompter | 24B-Thinking | Read-aloud rhythm + breath-point reasoning |
| Book chapter | 24B-Thinking-FP8 | Long context + cost control |
| Article-feature / op-ed | 24B-Thinking | Argument structure |
| Research paper (Hebrew) | 24B-Thinking | Technical accuracy |
| Legal contract drafting | Nemotron-12B-Instruct + deterministic params (T=0) | Reproducibility |
| Medical Hebrew | Nemotron-12B-Instruct + hebrew_medical_ner | Precision required |
| Slang-cultural variation | 1.7B-Instruct (fast iteration) or Nemotron-12B-Instruct | |
| 4-axis rubric grading (STEP 5g) | 24B-Thinking | Reasoning quality for justifications |
| Bidi-check (STEP 5h) | None — regex sufficient | Tool-only |

---

## Deployment recipes

### vLLM serving (production)

```bash
vllm serve dicta-il/DictaLM-3.0-Nemotron-12B-Instruct-FP8 \
  --tensor-parallel-size 1 \
  --max-model-len 32768 \
  --gpu-memory-utilization 0.9
```

### vLLM with W4A16 on RTX 5090

```bash
vllm serve dicta-il/DictaLM-3.0-Nemotron-12B-Instruct-W4A16 \
  --quantization compressed-tensors \
  --max-model-len 16384
```

### Local Mac development (llama.cpp)

```bash
llama-cli -hf dicta-il/DictaLM-3.0-Nemotron-12B-Instruct-GGUF:Q5_K_M \
  -p "כתוב פיץ' של 60 שניות לחברת סייבר ישראלית"
```

### Local Mac edge (1.7B Thinking)

```bash
llama-cli -hf dicta-il/DictaLM-3.0-1.7B-Thinking-GGUF:Q6_K \
  -p "<think>..." \
  --ctx-size 8192
```

### Python via transformers (HuggingFace)

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

mid = "dicta-il/DictaLM-3.0-Nemotron-12B-Instruct"
tok = AutoTokenizer.from_pretrained(mid)
model = AutoModelForCausalLM.from_pretrained(
    mid, torch_dtype=torch.bfloat16, device_map="auto"
)

msgs = [{"role": "user", "content": "כתוב פיץ' של 60 שניות לסטארטאפ סייבר ישראלי"}]
inputs = tok.apply_chat_template(msgs, return_tensors="pt", add_generation_prompt=True).to(model.device)
out = model.generate(inputs, max_new_tokens=512, temperature=0.7, do_sample=True)
print(tok.decode(out[0][inputs.shape[-1]:], skip_special_tokens=True))
```

---

## Thinking variant — prompt structure

The `-Thinking` models expect a specific structure. Reasoning happens inside a `<think>...</think>` block; the user-visible answer follows.

```
User: <Hebrew question>
Assistant: <think>
[multi-step Hebrew or mixed reasoning]
</think>
<final Hebrew answer>
```

When invoking from the skill, **strip the think block** from delivered output unless the user explicitly asked for "show your reasoning" or "תראה את הניתוח שלך".

---

## When NOT to use DictaLM 3.0

- **Domain-specific specialized models exist**: for diacritization use Dicta Nakdan; for medical NER use `hebrew_medical_ner_v5`; for legal embedding use `Legal-heBERT`; for emotion classification use `hebEMO`. DictaLM 3.0 is a generalist.
- **Frontier reasoning beyond Hebrew context**: for English-only complex reasoning or code generation, use Claude / GPT / Gemini. DictaLM 3.0's strength is Hebrew.
- **Translation EN↔HE for narrow domains**: Helsinki-NLP `opus-mt-tc-big-he-en` and `opus-mt-tc-big-en-he` remain competitive and cheaper per-token.

---

## Integration points in SKILL.md

- **STEP 4.5 (Source Selection)** — consult this doc for task-to-variant routing
- **STEP 4 (Write)** — default backend is `Nemotron-12B-Instruct` unless user specifies otherwise or the task table above routes to a different variant
- **STEP 5g (Rubric)** — invoke `24B-Thinking` for high-stakes grading
- **`scripts/hebrew_toolkit.py recommend`** — should suggest DictaLM 3.0 variants for `task=generate` and `task=reason`

---

## Citation

If a published Hebrew artifact is generated using DictaLM 3.0, cite as:

> DICTA: The Israel Center for Text Analysis (2025). *Dicta-LM 3.0: Advancing The Frontier of Hebrew Sovereign LLMs*. Technical Report. Available: https://dicta.org.il/publications/DictaLM_3_0___Techincal_Report.pdf
