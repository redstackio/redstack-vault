---
tags:
  - rce
  - command-injection
  - npm
  - node-js
  - supply-chain
type: attack_chain
tools:
  - '[[tools/npm]]'
  - '[[tools/node]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/npm-install-npm-git-publish]]'
  - '[[commands/node-execute-poc]]'
platforms:
  - Linux
  - Node.js
complexity: medium
procedures:
  - '[[procedures/Prepare-RCE-PoC-for-npm-git-publish]]'
  - '[[procedures/Install-Vulnerable-npm-git-publish-Module]]'
  - '[[procedures/Execute-RCE-via-Malicious-Git-Publish]]'
  - '[[procedures/Verify-RCE-Exploitation-Success]]'
step_count: 5
techniques:
  - '[[Compromise Hardware Supply Chain]]'
  - '[[Unix Shell]]'
description: >-
  Demonstrates remote code execution by exploiting insecure command formatting
  in the npm-git-publish module, allowing arbitrary shell command injection
  through a malicious Git remote URL.
skill_level: intermediate
impact_level: high
id: 8dcd875f-f7de-47c4-b803-edbeaf363db1
created_at: '2025-12-14T17:23:20.112Z'
updated_at: '2025-12-14T17:23:20.112Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Compromise Hardware Supply Chain]]'
  - '[[Unix Shell]]'
---
# RCE via Command Injection in npm-git-publish Module

## Overview

This attack chain exploits a remote code execution (RCE) vulnerability in the npm-git-publish module version 0.2.4-beta. The flaw stems from insecurely interpolating user-supplied remote URL input into a shell command in lib/publish.ts at line 151, without validation or sanitization. An attacker can inject arbitrary shell commands using special characters like semicolons and comments, such as in a malicious URL 'http://gihub.com ;touch HACKED; #'. When the publish function is invoked, this leads to command execution on the victim's local machine, potentially enabling full system compromise through file creation, modification, or further exploitation. The chain assumes a Node.js environment on Linux and demonstrates the full workflow from preparation to verification.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Prepare PoC] --> B[Verify Initial State]
    B --> C[Install Vulnerable Module]
    C --> D[Execute Malicious Publish]
    D --> E[Verify Exploitation]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/npm]]
- [[tools/node]]

### Target Environment

- Node.js runtime (version compatible with npm-git-publish 0.2.4-beta)
- Linux OS for shell command execution
- npm registry access
- Git installed (though not directly used in exploitation)

### Initial Access Requirements

- Local access to a development machine with Node.js installed
- No network credentials needed beyond npm registry (public)
- Prior access to run npm installs and Node scripts

## Detailed Attack Procedures

### Step 1: Prepare Exploitation PoC
procedure: [[procedures/Prepare-RCE-PoC-for-npm-git-publish]]

**Objective**: Create a JavaScript proof-of-concept (PoC) script that invokes the vulnerable publish function with a malicious remote URL to inject shell commands.

**Instructions**: Manually write a file named `poc.js` with the following content:

```javascript
const git = require('npm-git-publish');
git.publish('.', 'http://gihub.com ;touch HACKED; #');
```

This script requires the module and calls `publish` with a fake GitHub URL followed by a semicolon to separate commands and a comment to ignore the rest, executing `touch HACKED` to create a marker file.

**Expected Output**: A `poc.js` file created in the current directory.

**Success Indicators**:
- `poc.js` file exists and contains the malicious publish call
- No errors during manual file creation

### Step 2: Verify Initial State
procedure: [[procedures/Prepare-RCE-PoC-for-npm-git-publish]]

**Objective**: Confirm no evidence of prior exploitation by checking for the absence of the `HACKED` file.

**Instructions**: Manually inspect the current directory using `ls` or file explorer to ensure `HACKED` does not exist.

**Expected Output**: No `HACKED` file found.

**Success Indicators**:
- Directory listing shows no `HACKED` file
- Clean environment confirmed

### Step 3: Install Vulnerable Module
procedure: [[procedures/Install-Vulnerable-npm-git-publish-Module]]

**Objective**: Install the vulnerable version of npm-git-publish from the npm registry to set up the exploitation environment.

**Instructions**: Use [[commands/npm-install-npm-git-publish]] to install the module:

```bash
npm i npm-git-publish
```

This pulls version 0.2.4-beta, which contains the insecure code.

**Expected Output**: npm installation logs showing download and installation of npm-git-publish@0.2.4-beta.

**Success Indicators**:
- Module installed in node_modules
- No installation errors
- Version confirmed as 0.2.4-beta via `npm list npm-git-publish`

### Step 4: Execute Malicious Publish
procedure: [[procedures/Execute-RCE-via-Malicious-Git-Publish]]

**Objective**: Trigger the RCE by running the PoC script, which injects and executes the shell command on the local system.

**Instructions**: Run the PoC using [[commands/node-execute-poc]]:

```bash
node poc.js
```

This invokes the publish function, attempting a git push to the fake URL and injecting `touch HACKED`.

**Expected Output**: Script output may show git push errors (e.g., invalid repo), but the injected command succeeds silently.

**Success Indicators**:
- Script executes without crashing
- Potential git error for fake URL, but no block on injection

### Step 5: Verify Exploitation
procedure: [[procedures/Verify-RCE-Exploitation-Success]]

**Objective**: Confirm successful command injection by checking for the created `HACKED` file.

**Instructions**: Manually recheck the current directory using `ls` to locate the `HACKED` file.

**Expected Output**: `HACKED` file present in the directory.

**Success Indicators**:
- `HACKED` file exists (empty, created by touch)
- Demonstrates arbitrary command execution achieved

## Attack Chain Summary

### Key Achievements

1. Successful installation of the vulnerable npm-git-publish module without suspicion.
2. Injection and execution of arbitrary shell commands via a crafted Git remote URL.
3. Creation of a persistent file marker confirming RCE on the local system.
4. Potential for escalation to full compromise in a real attack scenario.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Compromise Hardware Supply Chain]]
- [[Unix Shell]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
