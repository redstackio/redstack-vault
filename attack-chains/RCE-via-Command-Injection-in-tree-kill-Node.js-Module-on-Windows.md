---
tags:
  - rce
  - command-injection
  - node-js
  - windows
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
  - '[[procedures/Install-Vulnerable-tree-kill-Module]]'
  - '[[procedures/Verify-Initial-Directory-State]]'
  - '[[procedures/Execute-PoC-to-Trigger-RCE]]'
  - '[[procedures/Verify-Exploitation-Success]]'
step_count: 4
techniques:
  - '[[Windows Command Shell]]'
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:32.674Z'
description: >-
  A multi-stage attack exploiting a command injection vulnerability in the
  tree-kill Node.js module (v1.2.1) on Windows, leading to arbitrary command
  execution and potential system compromise.
skill_level: intermediate
impact_level: high
id: 97e064b3-5c1d-455a-9148-d6e3c7fa6601
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Windows Command Shell]]'
  - '[[Exploitation for Client Execution]]'
---
# RCE via Command Injection in tree-kill Node.js Module on Windows

Multi-stage attack chain demonstrating exploitation of insecure command concatenation in the tree-kill module, allowing remote code execution on Windows systems through malicious PID input.

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
    C --> D[Verify Command Execution]

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
- No specific services or ports required; local execution

### Initial Access Requirements

- Local access to a Windows machine with Node.js
- No credentials or network access needed; assumes developer environment

## Detailed Attack Procedures

### Step 1: Install Vulnerable Module
procedure: [[procedures/Install-Vulnerable-tree-kill-Module]]

**Objective**: Set up the vulnerable environment by installing tree-kill version 1.2.1.

**Instructions**: Use [[commands/npm-install-tree-kill]] to install the module:

```bash
npm i tree-kill@1.2.1
```

**Expected Output**: Installation logs confirming tree-kill v1.2.1 in node_modules.

**Success Indicators**:
- Module installed without errors
- Version 1.2.1 confirmed via package.json or node_modules

### Step 2: Verify Initial Directory State
procedure: [[procedures/Verify-Initial-Directory-State]]

**Objective**: Confirm no unauthorized files exist before exploitation.

**Instructions**: Run [[commands/dir-list-directory]] to list current directory contents:

```bash
dir
```

**Expected Output**: Directory listing showing no HACKED.txt file.

**Success Indicators**:
- Clean directory without HACKED.txt
- Baseline state established

### Step 3: Execute PoC to Trigger RCE
procedure: [[procedures/Execute-PoC-to-Trigger-RCE]]

**Objective**: Exploit the vulnerability by running a PoC script that injects a malicious command into the PID parameter.

**Instructions**: First, create poc.js with content requiring tree-kill and calling kill with malicious input '3333332 & echo "HACKED" > HACKED.txt &'. Then execute using [[commands/node-execute-poc]]:

```bash
node poc.js
```

**Expected Output**: Silent execution; no errors, but command injection occurs in background.

**Success Indicators**:
- Script runs without crashing
- taskkill command executed with injected payload

### Step 4: Verify Exploitation Success
procedure: [[procedures/Verify-Exploitation-Success]]

**Objective**: Confirm arbitrary command execution by checking for the created file.

**Instructions**: Run [[commands/dir-list-directory]] again to list directory:

```bash
dir
```

**Expected Output**: Directory listing now includes HACKED.txt with content 'HACKED'.

**Success Indicators**:
- HACKED.txt file present
- File contents verify command injection success

## Attack Chain Summary

### Key Achievements

1. Installed vulnerable tree-kill module
2. Triggered RCE via unsanitized PID input in Windows taskkill command
3. Executed arbitrary commands, creating unauthorized files
4. Demonstrated potential for full system compromise

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Windows Command Shell]] Windows Command Shell
- [[Exploitation for Client Execution]] Exploitation for Client Execution

### MITRE ATT&CK Tactics

- [[Execution]] Execution

---

*Last updated: 2023-10-01T00:00:00Z*
