---
tags:
  - ssh
  - rce
type: procedure
tools:
  - '[[tools/ssh]]'
tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
commands: []
platforms:
  - Linux
techniques:
  - '[[Command-Line Interface]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: ca95f498-9867-414d-8ad7-1b59b55ae6c4
created_at: '2025-12-11T03:47:39.676Z'
updated_at: '2025-12-11T03:47:39.676Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
  - '[[TA0004]]'
mitre_techniques:
  - '[[T1059]]'
---
# Gain SSH Shell Access

## Summary

This procedure uses an injected SSH public key to connect to the GitLab server as the 'git' user, achieving remote code execution.

## Description

After overwriting .ssh/authorized_keys, the attacker can authenticate via SSH without credentials, gaining shell access as the 'git' user, which often has elevated privileges in GitLab environments.

## Requirements

1. Successful key injection via prior exploit
2. SSH private key corresponding to the uploaded public key
3. Network access to port 22 on the target

## Defense

Defensive measures and detection strategies:

- Regularly audit authorized_keys files
- Monitor SSH login attempts for 'git' user

## Objectives

1. Establish remote shell
2. Execute commands as 'git' user
3. Achieve RCE

## Instructions

### Step 1: Connect via SSH

**Context**: Authenticate using the injected key.

**Command** ([[commands/ssh-git-connect]]):
```bash
ssh git@10.26.0.5
```

> This provides an interactive shell.

### Step 2: Verify Access

**Context**: Run commands to confirm RCE.

Execute arbitrary commands in the shell.

> Confirm by running whoami or similar.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Privilege Escalation]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques



## Commands Used

- [[commands/ssh-git-connect]]

## Tools Used

- [[tools/ssh]]

## Tags

- [[tools/ssh]]
- #rce
