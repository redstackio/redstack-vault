---
id: ac-637840-001
tags:
  - path-traversal
  - mariadb
  - rce
  - code-execution
  - password-leak
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Analyze-MariaDB-Client-Plugin-Loading-Mechanism]]'
  - '[[procedures/Craft-Malicious-Plugin-Path-for-Traversal]]'
  - '[[procedures/Trigger-dlopen-via-Malicious-Server-Connection]]'
  - '[[procedures/Reproduce-on-Debian-Buster-Setup]]'
step_count: 4
techniques:
  - '[[Dynamic Linker Hijacking]]'
  - '[[Dynamic-link Library Injection]]'
updated_at: '2025-12-14T17:26:06.606Z'
description: >-
  Multi-stage attack exploiting path traversal in MariaDB command line client to
  force dlopen of arbitrary files, enabling code execution via init/fini
  functions and potential password leakage.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Dynamic Linker Hijacking]]'
  - '[[Dynamic-link Library Injection]]'
---
# Path Traversal in MariaDB Client for Arbitrary Library Loading and Code Execution

Multi-stage attack chain demonstrating exploitation of a path traversal vulnerability in MariaDB's command line client, allowing a malicious server to force the client to load arbitrary files via dlopen, potentially executing code through init/fini functions in controlled libraries. The attack also includes a side-channel abuse of the dialog plugin to leak unhashed passwords.

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
    A[Analyze Client Mechanism] --> B[Craft Malicious Path]
    B --> C[Connect to Malicious Server]
    C --> D[Reproduce and Execute]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Custom PoC scripts ([[commands/execute-dlopen-sh]] and [[commands/execute-dialog-sh]])

### Target Environment

- Linux (Debian Buster or similar)
- MariaDB client installed with plugins in /lib/x86_64-linux-gnu/mariadb19/plugin
- Access to a controlled file at a known path (e.g., /Users/shinnok/Downloads/h1/init.elf)

### Initial Access Requirements

- Ability to run MariaDB client
- Control over a MariaDB server to specify malicious plugin paths
- No prior credentials needed; triggered on connection

## Detailed Attack Procedures

### Step 1: Analyze Client Mechanism
procedure: [[procedures/Analyze-MariaDB-Client-Plugin-Loading-Mechanism]]

**Objective**: Identify the vulnerable dlopen call in the client code to understand the path traversal opportunity.

**Instructions**: Review the source code of client_plugin.c, focusing on line 368 where dlopen is invoked without path sanitization.

**Expected Output**: Confirmation of unsanitized path handling allowing server-specified plugins.

**Success Indicators**:
- Vulnerable dlopen call identified
- Lack of path validation noted

### Step 2: Craft Malicious Path
procedure: [[procedures/Craft-Malicious-Plugin-Path-for-Traversal]]

**Objective**: Construct a plugin path that exploits traversal and string manipulation to load an arbitrary file.

**Instructions**: Build the path using multiple '/' to pad and truncate the '.so' extension via strxnmov, combined with '../' sequences to reach a target like /Users/shinnok/Downloads/h1/init.elf.

**Expected Output**: Malicious path string ready for server use.

**Success Indicators**:
- Path crafted to bypass extension check
- Traversal to controlled file location

### Step 3: Trigger dlopen Connection
procedure: [[procedures/Trigger-dlopen-via-Malicious-Server-Connection]]

**Objective**: Force the client to load the arbitrary file upon connecting to the malicious server.

**Instructions**: Configure the server to specify the malicious path during handshake; connect the client to trigger dlopen.

**Expected Output**: Library loaded, init/fini functions executed if file exists.

**Success Indicators**:
- dlopen attempt on traversed path
- Code execution via init/fini

### Step 4: Reproduce on Setup
procedure: [[procedures/Reproduce-on-Debian-Buster-Setup]]

**Objective**: Validate the exploit in a controlled environment like Debian Buster.

**Instructions**: Adjust '../' count based on plugin path (/lib/x86_64-linux-gnu/mariadb19/plugin) and run the PoC using [[commands/execute-dlopen-sh]].

**Expected Output**: init and fini messages printed on success.

**Success Indicators**:
- Exploit reproduces successfully
- Code execution confirmed

## Attack Chain Summary

### Key Achievements

1. Identified path traversal in MariaDB client plugin loading
2. Achieved arbitrary library loading via crafted paths
3. Demonstrated code execution and password leakage potential

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Dynamic Linker Hijacking]] Dynamic-linker Hijacking
- [[Dynamic-link Library Injection]] Dynamic-link Library Injection

### MITRE ATT&CK Tactics

- [[Execution]] Execution

---
*Last updated: 2023-10-01T00:00:00Z*
