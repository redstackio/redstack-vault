---
tags:
  - rce
  - command-injection
  - node-js
  - windows
  - npm
type: attack_chain
tools:
  - '[[tools/npm]]'
  - '[[tools/node]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Windows
  - Node.js
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Install-Vulnerable-treekill-Module]]'
  - '[[procedures/Check-Directory-for-HACKED-File]]'
  - '[[procedures/Execute-treekill-RCE-PoC]]'
step_count: 4
techniques:
  - '[[Windows Command Shell]]'
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:20.604Z'
description: >-
  Demonstrates remote code execution by exploiting insecure command
  concatenation in the treekill Node.js module on Windows systems, allowing
  arbitrary command injection via a malicious PID parameter.
skill_level: intermediate
impact_level: high
id: 18af7fd5-84fa-48f4-bdf8-2843443c2fb8
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Windows Command Shell]]'
  - '[[Exploitation for Client Execution]]'
---
# RCE via Command Injection in treekill Node.js Module on Windows

Multi-stage attack chain demonstrating exploitation of a command injection vulnerability in the treekill Node.js module (version 1.0.0) on Windows, leading to arbitrary remote code execution through unsanitized PID input concatenated into a taskkill command.

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
    A[Install Vulnerable Module] --> B[Verify Initial State]
    B --> C[Execute Malicious PoC]
    C --> D[Confirm RCE Success]

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

- Windows OS
- Node.js runtime installed
- npm package manager available

### Initial Access Requirements

- Local access to a Windows machine with Node.js
- No network access required beyond npm registry
- Ability to install and run Node.js scripts

## Detailed Attack Procedures

### Step 1: Install Vulnerable Module
procedure: [[procedures/Install-Vulnerable-treekill-Module]]

**Objective**: Set up the environment by installing the vulnerable treekill module from npm.

**Instructions**: Use [[commands/install-treekill-module]] to fetch and install the package:

```bash
npm i treekill
```

**Expected Output**: Installation logs showing successful download and installation of treekill@1.0.0.

**Success Indicators**:
- treekill module appears in node_modules
- No errors during installation

### Step 2: Verify Initial State
procedure: [[procedures/Check-Directory-for-HACKED-File]]

**Objective**: Confirm that the HACKED.txt file does not exist prior to exploitation.

**Instructions**: Run [[commands/list-directory-windows]] to list current directory contents:

```bash
dir
```

**Expected Output**: Directory listing without HACKED.txt.

**Success Indicators**:
- HACKED.txt not present in output

### Step 3: Execute Malicious PoC
procedure: [[procedures/Execute-treekill-RCE-PoC]]

**Objective**: Trigger the vulnerability by running a PoC script that passes a malicious PID to treekill, injecting commands into the taskkill execution.

**Instructions**: First, ensure poc.js exists with content importing treekill and calling kill('3333332 & echo "HACKED" > HACKED.txt & ', true). Then execute [[commands/run-node-poc-script]]:

```bash
node poc.js
```

**Expected Output**: Script runs without errors, and the injected command executes silently.

**Success Indicators**:
- No immediate errors from treekill
- Taskkill attempt on non-existent PID

### Step 4: Confirm RCE Success
procedure: [[procedures/Check-Directory-for-HACKED-File]]

**Objective**: Validate the command injection by checking for the created HACKED.txt file.

**Instructions**: Re-run [[commands/list-directory-windows]] to list directory:

```bash
dir
```

**Expected Output**: Directory listing now includes HACKED.txt with content "HACKED".

**Success Indicators**:
- HACKED.txt present and contains expected text

## Attack Chain Summary

### Key Achievements

1. Successful installation of vulnerable dependency
2. Arbitrary command execution via PID injection
3. Confirmation of RCE impact through file creation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Windows Command Shell]] Windows Command Shell
- [[Exploitation for Client Execution]] Exploitation for Client Execution

### MITRE ATT&CK Tactics

- [[Execution]] Execution

---
*Last updated: 2023-10-01T00:00:00Z*
