#!/usr/bin/env node
/**
 * Ah Sheli Gibor — Claude Skill installer
 *
 * Installs the skill to ~/.claude/skills/ah-sheli-gibor by cloning the GitHub
 * repository. Works on macOS, Linux, and Windows.
 *
 * Usage:
 *   npx github:raifalex/Ah-Sheli-Gibor       # install from GitHub directly
 *   npx ah-sheli-gibor                       # after npm publish
 *   npx ah-sheli-gibor --update              # pull latest changes
 *   npx ah-sheli-gibor --uninstall           # remove the skill
 *   npx ah-sheli-gibor --target <path>       # custom install path
 *   npx ah-sheli-gibor --dry-run             # show what would happen
 */

const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');
const os = require('os');

const REPO = 'https://github.com/raifalex/Ah-Sheli-Gibor.git';
const SKILL_NAME = 'ah-sheli-gibor';

const args = process.argv.slice(2);
const flags = {
  update: args.includes('--update') || args.includes('-u'),
  uninstall: args.includes('--uninstall'),
  dryRun: args.includes('--dry-run'),
  help: args.includes('--help') || args.includes('-h'),
  target: null,
};

const targetIdx = args.indexOf('--target');
if (targetIdx !== -1 && args[targetIdx + 1]) {
  flags.target = args[targetIdx + 1];
}

const defaultTarget = path.join(os.homedir(), '.claude', 'skills', SKILL_NAME);
const targetPath = flags.target || defaultTarget;
const skillsDir = path.dirname(targetPath);

function printHelp() {
  console.log(`
Ah Sheli Gibor — Claude Skill installer

Installs an Israeli tech Hebrew rewriting skill into your Claude Code installation.

Usage:
  npx github:raifalex/Ah-Sheli-Gibor       Install from GitHub
  npx ah-sheli-gibor                        Install (after npm publish)
  npx ah-sheli-gibor --update               Pull latest changes
  npx ah-sheli-gibor --uninstall            Remove the skill
  npx ah-sheli-gibor --target <path>        Install to custom path
  npx ah-sheli-gibor --dry-run              Show what would happen
  npx ah-sheli-gibor --help                 Show this help

Default install path: ~/.claude/skills/ah-sheli-gibor

After installation, restart Claude Code. Invoke the skill with:
  "rewrite in Israeli tech Hebrew"
  "make this sound like a Tel Aviv engineer"
  "Israeli LinkedIn version of this"
`);
}

function checkGit() {
  try {
    execSync('git --version', { stdio: 'ignore' });
    return true;
  } catch {
    return false;
  }
}

function installSkill() {
  if (flags.dryRun) {
    console.log(`[dry-run] Would clone ${REPO} into ${targetPath}`);
    return;
  }

  if (!checkGit()) {
    console.error('Error: git is not installed or not in PATH.');
    console.error('Install git from https://git-scm.com/downloads and try again.');
    process.exit(1);
  }

  if (fs.existsSync(targetPath)) {
    if (flags.update) {
      console.log(`Updating Ah Sheli Gibor at ${targetPath}...`);
      try {
        execSync('git pull --ff-only', { cwd: targetPath, stdio: 'inherit' });
        console.log('\nUpdated successfully.');
      } catch (err) {
        console.error('Update failed:', err.message);
        process.exit(1);
      }
      return;
    }
    console.log(`Ah Sheli Gibor is already installed at ${targetPath}.`);
    console.log('To update: npx ah-sheli-gibor --update');
    console.log('To reinstall: npx ah-sheli-gibor --uninstall && npx ah-sheli-gibor');
    return;
  }

  fs.mkdirSync(skillsDir, { recursive: true });
  console.log(`Installing Ah Sheli Gibor to ${targetPath}...`);

  try {
    execSync(`git clone --depth 1 ${REPO} "${targetPath}"`, { stdio: 'inherit' });
  } catch (err) {
    console.error('Clone failed:', err.message);
    process.exit(1);
  }

  console.log('\nInstalled successfully.');
  console.log('');
  console.log('Next steps:');
  console.log('  1. Restart Claude Code so the skill is discovered.');
  console.log('  2. Invoke with natural language: "rewrite in Israeli tech Hebrew"');
  console.log('     Or supply a register: "Israeli tech LinkedIn version"');
  console.log('');
  console.log(`Skill files: ${targetPath}`);
  console.log('Repository:  https://github.com/raifalex/Ah-Sheli-Gibor');
}

function uninstallSkill() {
  if (!fs.existsSync(targetPath)) {
    console.log(`Ah Sheli Gibor is not installed at ${targetPath}.`);
    return;
  }

  if (flags.dryRun) {
    console.log(`[dry-run] Would remove ${targetPath}`);
    return;
  }

  console.log(`Removing ${targetPath}...`);
  fs.rmSync(targetPath, { recursive: true, force: true });
  console.log('Uninstalled.');
}

if (flags.help) {
  printHelp();
  process.exit(0);
}

if (flags.uninstall) {
  uninstallSkill();
} else {
  installSkill();
}
