---
id: proc-edgeos-login-operator-001
tags:
  - initial-access
  - linux
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/ssh-login]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:29:27.957Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# EdgeOS Login as Operator

## Summary

Establish initial read-only access to Ubiquiti EdgeOS using operator credentials via SSH.

## Description

The operator account provides limited shell access for monitoring but serves as the entry point for escalation due to weak file protections.

## Requirements

1. Operator username/password
2. Network access to device SSH port (22)

## Defense

- Disable operator SSH if not needed
- Use key-based auth and IP whitelisting
- Monitor auth logs

## Objectives

1. Gain shell access
2. Confirm operator context

## Instructions

### Step 1: SSH Connection

**Context**: Connect to the device.

**Command** ([[commands/ssh-login]]):
```bash
ssh operator@192.168.1.1
```

> Prompts for password; enter to login.

### Step 2: Verify Access

**Context**: Confirm privileges.

**Command**:
```bash
whoami
id
```

> Output: uid=1000(operator)

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/ssh-login]]

## Tools Used


## Tags

- [[initial-access]]
