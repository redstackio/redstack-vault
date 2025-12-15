---
id: proc-receive-reverse-shell-001
tags:
  - reverse-shell
  - interactive-shell
  - jenkins
type: procedure
tools:
  - '[[tools/nc]]'
tactics:
  - '[[Lateral Movement]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Web Protocols]]'
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:24:08.281Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Web Protocols]]'
  - '[[Unix Shell]]'
---
# Receive-and-Interact-with-Reverse-Shell

## Summary

This procedure handles the incoming reverse shell connection via netcat, allowing interactive commands on the target host as the jenkins user for exploration and exploitation.

## Description

Once the listener is set and the target connects, the attacker gains a raw TCP shell. This enables running Linux commands, file transfers, or privilege escalation. Assumes prior setup of listener and reverse payload execution on a Jenkins-hosted Linux server.

## Requirements

1. Active netcat listener on attacker's host
2. Successful reverse shell initiation from target
3. Basic Linux command knowledge

## Defense

Defensive measures and detection strategies:

- Deploy EDR tools to detect shell spawns and outbound connections
- Log all process creations on Jenkins hosts
- Use anomaly detection for jenkins user activities

## Objectives

1. Confirm shell access and user context
2. Perform post-exploitation tasks
3. Maintain access if needed

## Instructions

### Step 1: Accept Connection

**Context**: Monitor the nc output for the incoming connection from the target.

No command; the connection auto-establishes, showing target IP and a shell prompt.

> Output: "Connection from target_ip 12345 received!" followed by bash prompt.

### Step 2: Interact with Shell

**Context**: Run commands to verify access and explore the system.

Example commands in the shell:
```bash
whoami
id
ls /home/jenkins
```

> 'whoami' should return 'jenkins'; use for navigation, e.g., 'cat /etc/passwd' or upload tools.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]] Lateral Movement

### Techniques

- [[Web Protocols]] Web Protocols
- [[Unix Shell]] Unix Shell

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/nc]]

## Tags

- reverse-shell
- shell-access
