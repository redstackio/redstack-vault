---
tags:
  - rce
  - command-injection
  - nodejs
  - imagemagick
type: attack_chain
tools:
  - '[[tools/npm]]'
  - '[[tools/node]]'
  - '[[tools/imagickal]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Node.js
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Install-Vulnerable-imagickal-Module]]'
  - '[[procedures/Create-Exploit-Proof-of-Concept-Script]]'
  - '[[procedures/Execute-imagickal-Command-Injection-Exploit]]'
step_count: 3
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:23:19.217Z'
description: >-
  A multi-stage attack exploiting command injection in the imagickal Node.js
  module to achieve remote code execution by installing the vulnerable package,
  creating an exploit script, and executing it to run arbitrary shell commands.
id: 2ffe652e-4a15-4260-8a7c-7ea1a5a55dac
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Unix Shell]]'
---
# Remote Code Execution in imagickal Node.js Module via Command Injection

Multi-stage attack chain demonstrating exploitation of a command injection vulnerability in the imagickal Node.js module (version 4.2.0), a wrapper for ImageMagick, to achieve arbitrary remote code execution on the host system.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Install Vulnerable Module] --> B[Create Exploit Script]
    B --> C[Execute RCE]
    C --> D[System Compromise]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/npm]]
- [[tools/node]]
- [[tools/imagickal]]

### Target Environment

- Node.js runtime environment
- ImageMagick installed on the host system
- Unix-like OS (e.g., Linux) for shell command execution

### Initial Access Requirements

- Local access to a development or runtime environment where Node.js packages can be installed
- No network access required beyond npm registry
- Administrative privileges not needed, but shell access via ImageMagick is assumed

## Detailed Attack Procedures

### Step 1: Install Vulnerable Module

procedure: [[procedures/Install-Vulnerable-imagickal-Module]]

**Objective**: Install the vulnerable imagickal module (version 4.2.0) using npm to set up the environment for exploitation.

**Instructions**: Use [[commands/npm-install-imagickal]] to fetch and install the package from the npm registry.

```bash
npm i imagickal@4.2.0
```

**Expected Output**: Installation logs confirming the download and setup of the imagickal package in node_modules.

**Success Indicators**:
- Package listed in package.json or node_modules
- No errors during installation

### Step 2: Create Exploit Script

procedure: [[procedures/Create-Exploit-Proof-of-Concept-Script]]

**Objective**: Write a JavaScript proof-of-concept file that loads the imagickal module and invokes the vulnerable im.identify() function with a malicious filename to inject shell commands.

**Instructions**: Create a file named index.js with the following content:

```javascript
const im = require('imagickal');
im.identify('image.jpg; touch HACKED;');
```

Save the file in the project directory. This script requires the imagickal module and passes a filename with shell injection ('; touch HACKED;') to trigger command execution via ImageMagick.

**Expected Output**: No output from script creation itself; the file index.js is created and ready for execution.

**Success Indicators**:
- index.js file exists in the current directory
- Script syntax is valid and loads imagickal without errors

### Step 3: Execute RCE Exploit

procedure: [[procedures/Execute-imagickal-Command-Injection-Exploit]]

**Objective**: Run the proof-of-concept script to trigger the command injection, resulting in arbitrary shell command execution, such as creating a 'HACKED' file.

**Instructions**: Execute the script using [[commands/node-execute-exploit]]:

```bash
node index.js
```

This invokes im.identify() with the injected command, which appends '; touch HACKED;' to execute via ImageMagick's shell call. Verify success by checking for the 'HACKED' file using [[commands/touch-hacked-file]] context.

**Expected Output**: Console output from im.identify() (e.g., image metadata if 'image.jpg' exists) and creation of the 'HACKED' file in the current directory.

**Success Indicators**:
- 'HACKED' file appears (ls -la to confirm)
- No errors in Node.js execution
- Potential ImageMagick output if a real image is processed

## Attack Chain Summary

### Key Achievements

1. Successful installation of the vulnerable imagickal module without detection.
2. Creation of a minimal exploit script demonstrating command injection.
3. Achievement of RCE by injecting and executing shell commands, leading to file system modification and potential full compromise.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution
- [[Unix Shell]] Command and Scripting Interpreter: Unix Shell

### MITRE ATT&CK Tactics

- [[Execution]] Execution

---

*Last updated: 2023-10-01T00:00:00Z*
