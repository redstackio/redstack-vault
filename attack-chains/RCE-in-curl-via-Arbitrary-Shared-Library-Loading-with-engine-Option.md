---
tags:
  - rce
  - curl
  - library-loading
  - posix
  - shared-object
type: attack_chain
tools:
  - '[[tools/curl-command-line-tool]]'
  - '[[tools/gcc-compiler]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-version-info]]'
  - '[[commands/gcc-build-evil-engine]]'
  - '[[commands/rm-rce-proof-file]]'
  - '[[commands/curl-trigger-engine-rce]]'
  - '[[commands/cat-rce-proof]]'
platforms:
  - Linux
  - POSIX
complexity: medium
procedures:
  - '[[procedures/Create-Malicious-Shared-Library-Payload]]'
  - '[[procedures/Compile-Malicious-Payload-with-gcc]]'
  - '[[procedures/Clean-Verification-Proof-File]]'
  - '[[procedures/Trigger-RCE-with-curl-Engine]]'
  - '[[procedures/Verify-Code-Execution-via-Proof-File]]'
step_count: 5
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Dynamic Linker Hijacking]]'
description: >-
  Exploits curl's --engine option to load a malicious shared library on POSIX
  systems, achieving arbitrary code execution as the user running curl.
skill_level: intermediate
impact_level: high
id: b7255c5d-eaf9-4e45-9fdc-8fc8cc58912f
created_at: '2025-12-14T17:23:31.222Z'
updated_at: '2025-12-14T17:23:31.222Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Dynamic Linker Hijacking]]'
---
# RCE in curl via Arbitrary Shared Library Loading with --engine Option

Multi-stage attack chain demonstrating remote code execution by exploiting curl's --engine option to load an arbitrary malicious shared library (.so file) on POSIX-like systems. The vulnerability allows attackers to execute code as the curl user in environments where command arguments are controllable, such as scripts, CI/CD pipelines, or web backends, potentially leading to full system compromise.

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
    A[Create Malicious Payload] --> B[Compile Shared Library]
    B --> C[Prepare Environment]
    C --> D[Execute curl with --engine]
    D --> E[Verify RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#e67e22
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl-command-line-tool]]
- [[tools/gcc-compiler]]

### Target Environment

- POSIX-like systems (e.g., Linux)
- curl version vulnerable to --engine loading (e.g., 8.13.0 with OpenSSL support)
- gcc compiler installed
- Write access to current directory and /tmp

### Initial Access Requirements

- Local or remote access to execute curl commands
- Ability to influence curl arguments (e.g., via scripted environments or user input)
- No network restrictions for https://example.com (used for test fetch)

## Detailed Attack Procedures

### Step 1: Create Malicious Payload
procedure: [[procedures/Create-Malicious-Shared-Library-Payload]]

**Objective**: Generate C source code for a shared library with a constructor that executes arbitrary code upon loading.

**Instructions**: Write the C code to a file named evil_engine.c, including a constructor function that runs a system command to demonstrate RCE.

**Expected Output**: evil_engine.c file created with the payload code.

**Success Indicators**:
- File evil_engine.c exists and contains the constructor code
- No compilation errors when syntax-checked

### Step 2: Compile Shared Library
procedure: [[procedures/Compile-Malicious-Payload-with-gcc]]

**Objective**: Build the C source into a position-independent shared object (.so) file usable by curl's --engine.

**Instructions**: Use [[commands/gcc-build-evil-engine]] to compile the source:

```bash
gcc -fPIC -shared -o evil_engine.so evil_engine.c
```

**Expected Output**: evil_engine.so file created without errors.

**Success Indicators**:
- evil_engine.so file exists and is executable
- File type confirms shared object (e.g., via file command)

### Step 3: Prepare Environment
procedure: [[procedures/Clean-Verification-Proof-File]]

**Objective**: Ensure a clean state by removing any existing proof file from previous tests.

**Instructions**: Run [[commands/rm-rce-proof-file]] to delete /tmp/RCE_VIA_ENGINE if present:

```bash
rm -f /tmp/RCE_VIA_ENGINE
```

**Expected Output**: No output; file removed if existed.

**Success Indicators**:
- /tmp/RCE_VIA_ENGINE does not exist
- No errors from rm command

### Step 4: Execute curl with Malicious Engine
procedure: [[procedures/Trigger-RCE-with-curl-Engine]]

**Objective**: Load the malicious .so via --engine, triggering the constructor and achieving RCE before the curl operation fails.

**Instructions**: First, confirm curl version with [[commands/curl-version-info]]:

```bash
curl -V
```

Then execute with [[commands/curl-trigger-engine-rce]]:

```bash
curl --engine `pwd`/evil_engine.so https://example.com
```

**Expected Output**: SSL engine error (e.g., 'curl: (53) SSL Engine not found'); RCE occurs silently before error.

**Success Indicators**:
- Command runs and produces expected error
- Proof file /tmp/RCE_VIA_ENGINE is created (verified in next step)

### Step 5: Verify Code Execution
procedure: [[procedures/Verify-Code-Execution-via-Proof-File]]

**Objective**: Confirm RCE by checking the output written by the executed system command.

**Instructions**: Use [[commands/cat-rce-proof]] to display the proof file:

```bash
cat /tmp/RCE_VIA_ENGINE
```

**Expected Output**: User ID info, e.g., 'uid=1000(user) gid=1000(user) groups=...'

**Success Indicators**:
- File contains 'id' command output
- Confirms arbitrary code execution as curl user

## Attack Chain Summary

### Key Achievements

1. Successful creation and compilation of malicious .so payload
2. Triggering of constructor via curl --engine for RCE
3. Verification of code execution in controlled environment

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Client Execution]]
- [[Dynamic Linker Hijacking]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01*
