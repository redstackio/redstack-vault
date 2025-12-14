---
id: proc-637840-005
tags:
  - password-leak
  - mariadb
  - dialog-plugin
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/execute-dialog-sh]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Credentials In Files]]'
updated_at: '2025-12-14T17:26:06.591Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Credentials In Files]]'
---
# Abuse-Dialog-Plugin-for-Password-Leak

## Summary

This procedure abuses the MariaDB dialog plugin to trick the user into sending unhashed passwords to the server, without relying on path traversal.

## Description

The dialog plugin handles interactive prompts but can be manipulated by the server to request passwords in plain text, bypassing hashing. This side-channel complements the main exploit, enabling credential theft during connection attempts.

## Requirements

1. MariaDB client with dialog plugin enabled
2. Malicious server to trigger dialog
3. PoC script ([[commands/execute-dialog-sh]])

## Defense

Defensive measures and detection strategies:

- Disable or secure dialog plugin usage
- Enforce hashed credential transmission
- Log and alert on plain-text password prompts

## Objectives

1. Trigger unhashed password prompt
2. Capture credentials via server
3. Demonstrate leakage without traversal

## Instructions

### Step 1: Configure Server for Dialog

**Context**: Set server to invoke dialog plugin.

No specific command; modify server response:

> Server requests authentication via dialog.

### Step 2: Connect and Prompt

**Context**: Run client to receive prompt.

Execute [[commands/execute-dialog-sh]]:

```bash
./dialog.sh
```

> User enters password; server receives unhashed value.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Credentials In Files]] Unsecured Credentials: Credentials in Files

### Sub-Techniques


## Commands Used

- [[commands/execute-dialog-sh]]

## Tools Used


## Tags

- password-leak
- mariadb
- dialog-abuse
