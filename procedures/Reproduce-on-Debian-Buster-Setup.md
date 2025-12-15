---
id: proc-637840-004
tags:
  - path-traversal
  - mariadb
  - reproduction
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/execute-dlopen-sh]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Dynamic Linker Hijacking]]'
updated_at: '2025-12-14T17:26:06.593Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Dynamic Linker Hijacking]]'
---
# Reproduce-on-Debian-Buster-Setup

## Summary

This procedure reproduces the path traversal exploit on a Debian Buster environment, adjusting traversal depth for the specific plugin path and verifying code execution.

## Description

On Debian Buster, MariaDB plugins are in /lib/x86_64-linux-gnu/mariadb19/plugin. Adjust '../' count to traverse from this path to the target file. Run the PoC script to connect and trigger dlopen, observing init/fini output for success. This validates the vulnerability in a standard setup.

## Requirements

1. Debian Buster with MariaDB installed
2. PoC script ([[commands/execute-dlopen-sh]])
3. Controlled ELF file with init/fini (e.g., init.elf)

## Defense

Defensive measures and detection strategies:

- Patch MariaDB client to version fixing path validation
- Audit client connections for anomalous plugin loads
- Use integrity checks on loaded libraries

## Objectives

1. Adapt traversal for Debian path
2. Execute PoC and confirm load
3. Verify code execution indicators

## Instructions

### Step 1: Prepare Environment

**Context**: Set up Debian Buster and place target file.

No specific command; install MariaDB:

> Ensure plugins in /lib/x86_64-linux-gnu/mariadb19/plugin; place init.elf at target path.

### Step 2: Run Reproduction Script

**Context**: Execute PoC with adjusted path.

Execute [[commands/execute-dlopen-sh]]:

```bash
./dlopen.sh
```

> Adjust '../' in script based on path; success shows init and fini printed.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Dynamic Linker Hijacking]] Dynamic-linker Hijacking

### Sub-Techniques


## Commands Used

- [[commands/execute-dlopen-sh]]

## Tools Used


## Tags

- path-traversal
- mariadb
- debian-repro
