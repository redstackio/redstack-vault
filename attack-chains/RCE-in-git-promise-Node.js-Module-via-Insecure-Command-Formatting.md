---
id: ac-uuid-1234
tags:
  - rce
  - node-js
  - command-injection
  - supply-chain
type: attack_chain
tools:
  - '[[tools/npm]]'
  - '[[tools/node]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Linux
  - Node.js
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Malicious-POC-Script-for-git-promise-RCE]]'
  - '[[procedures/Verify-Clean-Filesystem-Before-Exploitation]]'
  - '[[procedures/Install-and-Execute-git-promise-RCE-POC]]'
  - '[[procedures/Confirm-RCE-Exploitation-Success]]'
step_count: 4
techniques:
  - '[[Unix Shell]]'
  - '[[Compromise Hardware Supply Chain]]'
updated_at: '2025-12-14T17:23:24.770Z'
description: >-
  Demonstrates remote code execution by exploiting command injection in the
  vulnerable git-promise Node.js module version 0.3.1, allowing arbitrary OS
  commands on the target system.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
  - '[[Compromise Hardware Supply Chain]]'
---
# RCE in git-promise Node.js Module via Insecure Command Formatting

Multi-stage attack chain demonstrating exploitation of a command injection vulnerability in the git-promise Node.js module, leading to arbitrary OS command execution on a Linux system running Node.js.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create PoC Script] --> B[Verify Clean Filesystem]
    B --> C[Install Module and Run PoC]
    C --> D[Verify Exploitation Success]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/npm]]
- [[tools/node]]

### Target Environment

- Node.js runtime (version compatible with npm)
- Linux OS
- No specific services or ports required; local execution

### Initial Access Requirements

- Local access to a development environment or server with Node.js installed
- No credentials needed; assumes ability to run npm and node commands
- Prior access to install packages

## Detailed Attack Procedures

### Step 1: Create PoC Script
procedure: [[procedures/Create-Malicious-POC-Script-for-git-promise-RCE]]

**Objective**: Craft a JavaScript script that injects a malicious command into the git-promise module to demonstrate RCE.

**Instructions**: Write a file named `poc.js` using a text editor, requiring the git-promise module and calling its git function with a concatenated command like `init;touch HACKED` to initialize a git repo and create a marker file.

**Expected Output**: A valid JavaScript file ready for execution.

**Success Indicators**:
- `poc.js` file created without syntax errors
- Script content includes the malicious git call

### Step 2: Verify Clean Filesystem
procedure: [[procedures/Verify-Clean-Filesystem-Before-Exploitation]]

**Objective**: Ensure no existing `HACKED` file is present to validate post-exploitation changes.

**Instructions**: Manually inspect the current directory using `ls` or a file explorer to confirm absence of `HACKED`.

**Expected Output**: No `HACKED` file listed.

**Success Indicators**:
- Filesystem shows no `HACKED` file
- Clean state confirmed before proceeding

### Step 3: Install Module and Run PoC
procedure: [[procedures/Install-and-Execute-git-promise-RCE-POC]]

**Objective**: Set up the vulnerable environment and trigger the RCE by executing the PoC.

**Instructions**: First, install the vulnerable module using [[commands/npm-install-git-promise]]:

```bash
npm i git-promise
```

Then, run the PoC script with [[commands/node-execute-poc]]:

```bash
node poc.js
```

**Expected Output**: Installation logs confirming git-promise@0.3.1, followed by branch log from git init and creation of `HACKED` via injection.

**Success Indicators**:
- Module installed successfully
- PoC executes without errors and injects command

### Step 4: Confirm Exploitation Success
procedure: [[procedures/Confirm-RCE-Exploitation-Success]]

**Objective**: Validate that the injected command executed by checking for the created file.

**Instructions**: Re-inspect the filesystem using `ls` to locate the `HACKED` file.

**Expected Output**: `HACKED` file present in the directory.

**Success Indicators**:
- `HACKED` file created
- Proof of arbitrary command execution

## Attack Chain Summary

### Key Achievements

1. Successful installation of vulnerable git-promise module
2. Injection and execution of arbitrary shell command via child_process.exec
3. Creation of marker file demonstrating RCE impact
4. Full system compromise potential highlighted

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Unix Shell]]
- [[Compromise Hardware Supply Chain]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
