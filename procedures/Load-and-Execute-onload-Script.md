---
tags:
  - npm
  - script-execution
  - configuration-load
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/npm-help]]'
  - '[[commands/sudo-npm]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:28:44.403Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: d107caf5-ae30-4605-8936-b5d4c363763a
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Load-and-Execute-onload-Script

## Summary

This procedure describes how npm automatically loads and executes the onload-script from .npmrc when invoked in the target directory.

## Description

Upon running any npm command, the CLI scans for .npmrc files in the current and ancestor directories, processing configurations including onload-script. This executes the specified Node.js script in the process context (line 236 in lib/npm.js), without privilege checks, even under sudo. This enables seamless RCE.

## Requirements

1. Malicious .npmrc in directory
2. Victim runs npm command
3. Vulnerable npm version

## Defense

Defensive measures and detection strategies:

- Disable or audit onload-script in npm configs
- Run npm with --no-config or in clean directories
- Log npm process spawns and script executions

## Objectives

1. Trigger automatic script loading
2. Execute code in npm context
3. Maintain stealth during execution

## Instructions

### Step 1: Invoke npm in Directory

**Context**: Run any npm command to process .npmrc.

**Command** ([[commands/npm-help]]):
```bash
npm help
```

> Loads .npmrc and executes onload-script. Expected output: Help text, plus payload effects.

### Step 2: Use Sudo for Escalation

**Context**: Prefix with sudo to run as root.

**Command** ([[commands/sudo-npm]]):
```bash
sudo npm
```

> Executes with root privileges. Expected output: Depends on subcommand, script runs as root.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/npm-help]]
- [[commands/sudo-npm]]

## Tools Used

- [[tools/npm]]

## Tags

- [[script-execution]]
- [[rce]]
