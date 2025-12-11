---
tags:
  - reverse-shell
  - execution
type: procedure
tools:
  - '[[tools/ImageMagick]]'
  - '[[tools/Ghostscript]]'
  - '[[tools/Netcat]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/postscript-payload-rce]]'
  - '[[commands/bash-reverse-shell]]'
  - '[[commands/ls-directory-list]]'
  - '[[commands/whoami-user-identification]]'
  - '[[commands/cat-hosts-file]]'
platforms:
  - Linux
techniques:
  - '[[Command-Line Interface]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: a7a739b1-572d-4ed0-b00b-9086ba4fe65e
created_at: '2025-12-11T06:10:33.189Z'
updated_at: '2025-12-11T06:10:33.189Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059]]'
---
# Receive and Interact with Reverse Shell

## Summary

This procedure sets up a listener to receive the reverse shell and executes commands to explore the compromised server.

## Description

After upload, the payload establishes a reverse shell to the attacker's listener on port 8080. Commands like ls, whoami, and cat are run to list files, identify the user, and check /etc/hosts. This confirms shell access and server details.

## Requirements

1. Netcat or similar tool for listening.
2. Attacker's IP and port configured in payload.
3. Successful payload upload.

## Defense

Defensive measures and detection strategies:

- Monitor outbound connections to unusual ports.
- Use firewalls to block reverse shell attempts.

## Objectives

1. Establish interactive shell.
2. Explore filesystem and user context.
3. Gather initial reconnaissance data.

## Instructions

### Step 1: Set Up Listener

**Context**: Listen for incoming reverse shell connection.

Use [[tools/Netcat]] to listen:

```bash
nc -lvnp 8080
```

### Step 2: Execute Exploratory Commands

**Context**: Run commands in the shell to gather information.

**Command** ([[commands/ls-directory-list]]):
```bash
ls
```

> Lists files in the current directory.

**Command** ([[commands/whoami-user-identification]]):
```bash
whoami
```

> Displays the current username.

**Command** ([[commands/cat-hosts-file]]):
```bash
cat /etc/hosts
```

> Displays contents of /etc/hosts to verify server identity.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques



## Commands Used

- [[commands/bash-reverse-shell]]
- [[commands/ls-directory-list]]
- [[commands/whoami-user-identification]]
- [[commands/cat-hosts-file]]

## Tools Used

- [[tools/Netcat]]

## Tags

- [[commands/bash-reverse-shell]]
- [[Execution]]
