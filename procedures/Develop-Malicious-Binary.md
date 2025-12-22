---
tags:
  - malicious-binary
  - c-program
  - payload-execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/execute-payload]]'
verified: false
platforms:
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:28:59.027Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 108b32e7-e7d7-4dc3-9fac-7f9d143dda13
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Develop-Malicious-Binary

## Summary

This procedure involves writing a simple C program that serves as the malicious replacement for the 'console' binary, executing the reverse shell payload and creating a marker file to indicate successful privilege escalation.

## Description

The C program uses the `system()` function to run `touch pass;bash shell`, which creates a file 'pass' as a success indicator and invokes the reverse shell script. This binary is placed via hardlink replacement during the race condition to hijack execution flow in the SUID Acronis True Image binary, allowing root-level command execution.

## Requirements

1. Text editor or compiler environment on macOS
2. Access to the 'shell' script from previous procedure
3. Basic C programming knowledge

## Defense

Defensive measures and detection strategies:

- Scan for unexpected executables in user directories (`find /tmp -type f -perm -0111`)
- Monitor system() calls in SUID binaries via auditing tools like Auditd
- Harden SUID binaries against TOCTOU races with file locking

## Objectives

1. Create a binary that triggers the reverse shell under root privileges
2. Mark successful exploitation with a file indicator
3. Ensure seamless integration into the race exploit

## Instructions

### Step 1: Write the C Source Code

**Context**: Develop 'test.c' to execute the payload when run as the hijacked 'console' binary.

**Command** ([[commands/execute-payload]]):
```bash
touch pass;bash shell
```

> This is the core command embedded in the C program via system(). The full C code would be: #include <stdlib.h> int main() { system("touch pass;bash shell"); return 0; }. Expected output: When executed as root, 'pass' file created and shell script runs, starting the listener.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Unix Shell]] Unix Shell

### Sub-Techniques


## Commands Used

- [[commands/execute-payload]]

## Tools Used


## Tags

- malicious-binary
- c-program
- payload-execution
