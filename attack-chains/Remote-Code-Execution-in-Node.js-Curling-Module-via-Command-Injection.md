---
id: ac-curling-rce-001
name: Remote Code Execution in Node.js Curling Module via Command Injection
type: attack_chain
description: >-
  Multi-stage attack exploiting a command injection vulnerability in the Node.js
  curling module to achieve remote code execution, file reading, and file
  overwriting on the host system.
verified: false
submitted: true
step_count: 2
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:19.443Z'
procedures:
  - '[[procedures/Install-Vulnerable-Curling-Module]]'
  - '[[procedures/Exploit-Curling-Module-for-RCE]]'
techniques:
  - '[[Unix Shell]]'
  - '[[Exploitation for Client Execution]]'
tactics:
  - '[[Execution]]'
tags:
  - rce
  - command-injection
  - node-js
  - npm
  - curling
platforms:
  - Node.js
  - Linux
tools:
  - '[[tools/npm]]'
  - '[[tools/curling]]'
  - '[[tools/Node.js]]'
complexity: medium
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
  - '[[Exploitation for Client Execution]]'
---

# Remote Code Execution in Node.js Curling Module via Command Injection

The vulnerability in the Node.js 'curling' module (version 1.1.0) stems from a flawed regular expression that fails to properly sanitize curl commands, allowing attackers to inject arbitrary options like file URLs and output flags. This leads to remote code execution (RCE), enabling the reading of sensitive files such as /etc/passwd and overwriting local files on the host system. The attack requires installing the vulnerable module and executing a proof-of-concept script that bypasses the regex check.

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
    A[Install Vulnerable Module] --> B[Execute Malicious Payload]
    B --> C[RCE and File Manipulation]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/npm]]
- [[tools/Node.js]]
- [[tools/curling]]

### Target Environment

- Node.js runtime environment (version compatible with npm)
- Linux host system (for file access like /etc/passwd)
- No specific services or ports required; local execution

### Initial Access Requirements

- Local access to a development or runtime environment where Node.js modules can be installed
- No network credentials needed; assumes control over the Node.js application using the module

## Detailed Attack Procedures

### Step 1: Install Vulnerable Module

procedure: [[procedures/Install-Vulnerable-Curling-Module]]

**Objective**: Set up the environment by installing the vulnerable curling module from the npm registry to prepare for exploitation.

**Instructions**: Use [[commands/npm-install-curling]] to install the package:

```bash
npm i curling
```

**Expected Output**: Installation logs confirming the package is added to node_modules, with version 1.1.0 vulnerable to command injection.

**Success Indicators**:
- Package listed in package.json or node_modules/curling directory created
- No errors during installation

### Step 2: Execute Exploitation Script

procedure: [[procedures/Exploit-Curling-Module-for-RCE]]

**Objective**: Exploit the command injection flaw by running a Node.js script that injects a malicious curl payload to read sensitive files and overwrite local files, demonstrating RCE.

**Instructions**: Create an index.js file with the exploitation code using [[commands/node-execute-curling-poc]] and run it with Node.js:

```bash
node index.js
```

The script requires the curling module and calls run with the payload 'file:///etc/passwd -o ./index.js'.

**Expected Output**: The local index.js file is overwritten with the contents of /etc/passwd; console logs the payload response.

**Success Indicators**:
- Contents of /etc/passwd visible in the overwritten file
- No regex validation errors; successful curl execution

## Attack Chain Summary

### Key Achievements

1. Successful installation of the vulnerable module without detection
2. Bypass of regex sanitization to inject curl options
3. Achievement of RCE, including file read and write operations on the host

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Unix Shell]] Unix Shell (command injection via curl binary)
- [[Exploitation for Client Execution]] Exploitation for Client Execution (exploiting vulnerable library)

### MITRE ATT&CK Tactics

- [[Execution]] Execution

---
*Last updated: 2023-10-01T00:00:00Z*
