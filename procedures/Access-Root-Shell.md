---
tags:
  - root-access
  - reverse-shell
  - interactive-shell
type: procedure
tools:
  - '[[tools/Netcat]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/connect-to-reverse-shell]]'
verified: false
platforms:
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:28:59.009Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
id: 312f4ed1-4d38-4604-bae0-5d2682ed25f4
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Access-Root-Shell

## Summary

This procedure connects to the reverse shell established by the exploit payload, providing an interactive root shell for further post-exploitation activities on the macOS system.

## Description

After winning the race and executing the malicious binary as root, the payload starts a netcat listener on localhost:8080. Connecting via netcat allows full interaction with a bash shell running under root privileges, confirming the privilege escalation.

## Requirements

1. Successful execution of prior exploit steps (listener active)
2. Netcat available
3. Localhost access (no firewall blocking 8080)

## Defense

Defensive measures and detection strategies:

- Monitor netcat connections on localhost ports
- Log root shell spawns via sudo/audit logs
- Use endpoint detection to alert on unexpected root processes

## Objectives

1. Gain interactive root access
2. Verify escalation success
3. Enable arbitrary root commands

## Instructions

### Step 1: Connect to Listener

**Context**: Establish connection to the bind shell for root interaction.

**Command** ([[commands/connect-to-reverse-shell]]):
```bash
nc 127.0.0.1 8080
```

> Connects to the port; expected output: Bash prompt (`$ ` or `#`); run `whoami` to confirm 'root'.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Unix Shell]] Unix Shell

### Sub-Techniques


## Commands Used

- [[commands/connect-to-reverse-shell]]

## Tools Used

- [[tools/Netcat]]

## Tags

- root-access
- reverse-shell
- interactive-shell
