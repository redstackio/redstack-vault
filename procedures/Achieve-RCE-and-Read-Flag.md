---
tags:
  - rce
  - reverse-shell
  - flag-retrieval
type: procedure
tools:
  - '[[tools/netcat]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/read-flag-file]]'
  - '[[commands/listen-for-reverse-shell-with-netcat]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:23:50.023Z'
sub_techniques: []
id: e07385de-8897-4418-b760-34755eaac521
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Achieve-RCE-and-Read-Flag

## Summary

This procedure uses the reverse shell from unpickling RCE to navigate the filesystem and read the flag file in a CTF environment.

## Description

After unpickling executes the reverse shell one-liner, a netcat listener catches the connection. In the shell, cd to /app and cat flag.txt to retrieve the flag.

## Requirements

1. Reverse shell payload executed
2. Netcat listener on attacker's server (port 443)
3. Target in Linux environment with /app/flag.txt

## Defense

Defensive measures and detection strategies:

- Firewall internal ports and monitor outbound connections
- Disable unnecessary scripting interpreters
- Use integrity checks on flag/secrets files

## Objectives

1. Establish interactive shell
2. Access sensitive directories
3. Extract flag or secrets

## Instructions

### Step 1: Listen for Shell

**Context**: Set up receiver for incoming connection.

**Command** ([[commands/listen-for-reverse-shell-with-netcat]]):
```bash
nc -lvnp 443
```

> Wait for connection from target.

### Step 2: Read Flag

**Context**: In the shell, retrieve the flag.

**Command** ([[commands/read-flag-file]]):
```bash
cd /app && cat flag.txt
```

> Outputs the CTF flag.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Unix Shell]] Command and Scripting Interpreter: Unix Shell

### Sub-Techniques


## Commands Used

- [[commands/listen-for-reverse-shell-with-netcat]]
- [[commands/read-flag-file]]

## Tools Used

- [[tools/netcat]]

## Tags

- rce
- reverse-shell
- flag-retrieval
