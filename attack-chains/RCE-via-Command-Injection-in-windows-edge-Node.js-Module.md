---
tags:
  - rce
  - command-injection
  - node-js
  - windows
  - npm
  - supply-chain
type: attack_chain
tools:
  - '[[tools/npm]]'
  - '[[tools/Node.js]]'
  - '[[tools/windows-edge]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/npm-install-windows-edge]]'
  - '[[commands/node-execute-poc]]'
platforms:
  - Windows
  - Node.js
complexity: medium
procedures:
  - '[[procedures/Create-POC-for-windows-edge-RCE]]'
  - '[[procedures/Verify-No-HACKED-File]]'
  - '[[procedures/Install-Vulnerable-windows-edge]]'
  - '[[procedures/Execute-POC-to-Exploit]]'
  - '[[procedures/Verify-Exploitation-Success]]'
step_count: 5
techniques:
  - '[[Windows Command Shell]]'
  - '[[JavaScript]]'
  - '[[Compromise Software Supply Chain]]'
description: >-
  Multi-stage attack exploiting a command injection vulnerability in the
  windows-edge Node.js module (v1.0.1) to achieve remote code execution on
  Windows systems by injecting malicious shell commands through a URI parameter.
skill_level: intermediate
impact_level: high
id: 32818cf9-8a4d-4601-b43b-5601ca7a1ce1
created_at: '2025-12-14T17:23:20.070Z'
updated_at: '2025-12-14T17:23:20.070Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Windows Command Shell]]'
  - '[[JavaScript]]'
  - '[[Compromise Software Supply Chain]]'
---
# RCE via Command Injection in windows-edge Node.js Module

The vulnerability in the windows-edge Node.js module (version 1.0.1) allows remote code execution due to insecure command formatting where user-provided URI input is directly interpolated into a shell command without validation or sanitization. Discovered by reviewing the source code at index.js line 8, it can be exploited by crafting a malicious URI that injects shell commands like '; touch HACKED; #'. The impact includes arbitrary command execution on the victim's Windows machine, enabling file creation, data exfiltration, or further compromise.

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
    A[Create PoC] --> B[Verify Environment]
    B --> C[Install Vulnerable Module]
    C --> D[Execute PoC]
    D --> E[Verify Exploitation]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#e67e22
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/npm]]
- [[tools/Node.js]]
- [[tools/windows-edge]]

### Target Environment

- Windows OS
- Node.js runtime installed
- npm package manager available

### Initial Access Requirements

- Local access to a Windows machine with Node.js
- No network credentials required; local exploitation setup

## Detailed Attack Procedures

### Step 1: Create PoC Script
procedure: [[procedures/Create-POC-for-windows-edge-RCE]]

**Objective**: Develop a JavaScript proof-of-concept to trigger the command injection vulnerability in the windows-edge module.

**Instructions**: Write a JavaScript file named `poc.js` that requires the windows-edge module and calls the `edge` function with a malicious URI to inject a shell command.

**Expected Output**: A valid `poc.js` file ready for execution.

**Success Indicators**:
- `poc.js` file created without syntax errors
- Malicious URI properly formatted for injection

### Step 2: Verify Clean Environment
procedure: [[procedures/Verify-No-HACKED-File]]

**Objective**: Ensure no existing 'HACKED' file is present to confirm baseline state before exploitation.

**Instructions**: Manually inspect the filesystem in the working directory for the absence of a file named 'HACKED'.

**Expected Output**: No 'HACKED' file found.

**Success Indicators**:
- Filesystem check confirms clean state
- No prior exploitation artifacts

### Step 3: Install Vulnerable Module
procedure: [[procedures/Install-Vulnerable-windows-edge]]

**Objective**: Install the vulnerable version of the windows-edge module to set up the exploitable environment.

**Instructions**: Use [[commands/npm-install-windows-edge]] to install the module from the npm registry:

```bash
npm i windows-edge
```

**Expected Output**: Installation logs confirming the module is added to `node_modules`.

**Success Indicators**:
- `node_modules/windows-edge` directory created
- Version 1.0.1 installed (vulnerable)

### Step 4: Execute PoC
procedure: [[procedures/Execute-POC-to-Exploit]]

**Objective**: Run the PoC script to invoke the vulnerable module and inject the malicious command.

**Instructions**: Execute the PoC using [[commands/node-execute-poc]]:

```bash
node poc.js
```

**Expected Output**: Script runs without errors, triggering the edge function and injecting the command (side effect: file creation).

**Success Indicators**:
- No runtime errors in Node.js
- Shell command injected successfully

### Step 5: Verify Exploitation
procedure: [[procedures/Verify-Exploitation-Success]]

**Objective**: Confirm the success of the RCE by checking for the created 'HACKED' file.

**Instructions**: Manually recheck the filesystem for the presence of the 'HACKED' file.

**Expected Output**: 'HACKED' file exists in the working directory.

**Success Indicators**:
- 'HACKED' file created as a result of the injected 'touch HACKED' command
- Evidence of arbitrary command execution

## Attack Chain Summary

### Key Achievements

1. Successful installation of the vulnerable windows-edge module
2. Injection of shell commands via URI parameter leading to RCE
3. Verification of command execution through file creation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Windows Command Shell]]
- [[JavaScript]]
- [[Compromise Software Supply Chain]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2024-10-01*
