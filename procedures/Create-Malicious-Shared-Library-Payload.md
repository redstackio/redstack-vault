---
tags:
  - rce
  - payload-creation
  - constructor
type: procedure
tools:
  - '[[tools/gcc-compiler]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Linux
  - POSIX
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Dynamic Linker Hijacking]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: bf9b5105-d7dd-424f-8218-287954f361f8
created_at: '2025-12-14T17:23:31.220Z'
updated_at: '2025-12-14T17:23:31.220Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Dynamic Linker Hijacking]]'
---
# Create-Malicious-Shared-Library-Payload

## Summary

This procedure creates a C source file for a malicious shared library that uses a constructor attribute to execute arbitrary code (e.g., a system command) immediately upon loading, targeting curl's --engine option for RCE demonstration.

## Description

In the attack scenario, an attacker crafts a .so file loadable by curl without path validation. The constructor function runs code like system('id > /tmp/RCE_VIA_ENGINE') when the library is loaded, proving RCE on POSIX systems. This is useful in environments where curl arguments are attacker-controlled, such as automated scripts or backend processes. Prerequisites include a C development environment and knowledge of GCC attributes.

## Requirements

1. Access to a text editor or echo command to write files
2. GCC installed for later compilation
3. Write permissions in the working directory

## Defense

Defensive measures and detection strategies:

- Restrict curl usage to trusted arguments; avoid user-controlled --engine inputs
- Use containerization or sandboxing for curl executions in CI/CD
- Monitor library loading events via auditd or strace for suspicious .so paths

## Objectives

1. Generate source code that executes on library load
2. Demonstrate payload for RCE testing
3. Prepare for compilation into exploitable .so

## Instructions

### Step 1: Write the C Source Code

**Context**: Create evil_engine.c with a constructor that runs a system command to write user ID to a proof file, simulating RCE.

**Command** (Manual file creation):

Create the file evil_engine.c with the following content:

```c
#include <stdlib.h>

void __attribute__((constructor)) init() {
    system("id > /tmp/RCE_VIA_ENGINE");
}
```

> This code defines an init function marked as constructor, which executes system("id > /tmp/RCE_VIA_ENGINE") upon library loading. Save the file in the current directory.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation for Client Execution]]
- [[Dynamic Linker Hijacking]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/gcc-compiler]]

## Tags

- [[rce]]
- [[payload-creation]]
