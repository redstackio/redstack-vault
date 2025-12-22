---
tags:
  - shell
  - verification
  - rce
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/id-shell-command]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:23:54.957Z'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques: []
id: ec841254-a900-4215-9912-5a66bcd82ed2
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Verify-Access-via-Reverse-Shell

## Summary

This procedure uses basic shell commands in the established reverse shell to confirm user privileges and server control post-exploitation.

## Description

After RCE, run 'id' to display the current user and groups, verifying production access. In the Algolia case, it showed uid=1000(prod). This step validates the exploit's success and informs next actions like persistence.

## Requirements

1. Active reverse shell from Metasploit
2. Basic shell knowledge

## Defense

Defensive measures and detection strategies:

- Monitor shell commands via auditd or sysdig for 'id' executions from web contexts
- Implement least-privilege for web servers (non-root)
- Alert on reverse shell connections

## Objectives

1. Confirm shell access and user context
2. Assess privilege level
3. Validate exploit efficacy

## Instructions

### Step 1: Switch to Shell if Needed

**Context**: Ensure interactive shell mode.

In Metasploit, use 'shell' if in Meterpreter.

### Step 2: Run ID Command

**Context**: Check user identity.

Execute [[commands/id-shell-command]]:

```bash
id
```

> Expected output: uid=1000(prod) gid=1000(prod) groups=1000(prod).

### Step 3: Interpret Results

**Context**: Analyze for access level.

If prod user, proceed to file ops; note any escalations needed.

> Success if non-guest user with write access.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Command-Line Interface]] Command and Scripting Interpreter

### Sub-Techniques


## Commands Used

- [[commands/id-shell-command]]

## Tools Used


## Tags

- shell
- linux
- verification
