---
id: proc-004
tags:
  - verification
  - root-shell
  - escalation
  - linux
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/id-verify-root]]'
  - '[[commands/ls-explore]]'
  - '[[commands/gitlab-rake-env]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:29:56.994Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Capture-and-Verify-Root-Shell

## Summary

This procedure triggers the payload by logging in as root, captures the reverse shell, and verifies privilege escalation through user ID checks and environment exploration.

## Description

Upon root login (e.g., SSH), bash sources the malicious .log.1.gz in /etc/bash_completion.d/, executing the netcat shell to the listener. In the received shell, confirm root via 'id' and explore with 'ls'. Optionally, run GitLab rake tasks. Requires active listener and payload deployment. Outcome: Confirmed root access for arbitrary execution.

## Requirements

1. Active nc listener on port 3333
2. Deployed payload in symlinked directory
3. Ability to trigger root login (e.g., SSH as root)
4. GitLab environment for verification

## Defense

Defensive measures and detection strategies:

- Disable direct root login (PermitRootLogin no in sshd_config)
- Monitor login events and anomalous processes (nc spawning from bash)
- Use multi-factor for root; audit bash sourcing
- Log all shell executions via pam or auditd

## Objectives

1. Receive and interact with root reverse shell
2. Validate escalation success
3. Explore escalated environment

## Instructions

### Step 1: Trigger Payload

**Context**: Log in as root to execute the completion script.

**Command** (No direct command; simulate login):
Login as root via SSH or su. The payload auto-executes.

> Expected: Connection to listener.

### Step 2: Verify User ID

**Context**: Confirm uid=0 in the shell.

**Command** ([[commands/id-verify-root]]):
```bash
id
```

> Displays user info. Expected output: 'uid=0(root) gid=0(root) groups=0(root)'.

### Step 3: Explore Directory

**Context**: List root files to demonstrate access.

**Command** ([[commands/ls-explore]]):
```bash
ls -la
```

> Long listing. Expected output: Detailed files in current dir (e.g., root's home).

### Step 4: Check GitLab Env

**Context**: Verify GitLab context in root shell.

**Command** ([[commands/gitlab-rake-env]]):
```bash
gitlab-rake gitlab:env:info
```

> Outputs env. Expected output: System info, GitLab version, Ruby/PostgreSQL details.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Unix Shell]] Unix Shell

### Sub-Techniques


## Commands Used

- [[commands/id-verify-root]]
- [[commands/ls-explore]]
- [[commands/gitlab-rake-env]]

## Tools Used


## Tags

- [[verification]]
- [[root-shell]]
- [[escalation]]
- [[linux]]
