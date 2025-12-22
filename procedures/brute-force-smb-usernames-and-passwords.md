---
id: 08f7d6ec-71a4-4563-82b2-23f66791205f
name: brute-force-smb-usernames-and-passwords
type: procedure
verified: true
submitted: false
created_at: '2019-12-27T20:37:12.139314+00:00'
updated_at: '2023-05-25T19:56:21.281849+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Brute Force|T1110 - Brute Force]]'
  - '[[techniques/Brute Force.T1110.003 - Password Spraying]]'
sub_techniques: []
tags:
  - authentication
  - network
  - service-attacks
commands:
  - '[[commands/crackmapexec-brute-force-smb-usernames-and-passwords]]'
platforms:
  - Windows
tools:
  - '[[tools/CrackMapExec]]'
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# brute-force-smb-usernames-and-passwords

## Summary

This procedure brute-forces SMB shares using lists of usernames and passwords to discover valid credentials, common in AD environments for initial access.

## Description

SMB authentication is noisy but effective for low-hanging fruit. Tools like CrackMapExec spray combos across the target, identifying valid pairs without lockouts if throttled. Use after user enumeration.

## Requirements

1. Target IP with SMB open
2. Username and password lists
3. CrackMapExec v5+ installed

## Defense

- Enable SMB signing and account lockouts
- Monitor event logs for 4625 failures
- Use MFA or Kerberos for stronger auth

## Objectives

1. Find valid username/password pairs
2. Gain authenticated SMB access
3. Prepare for RID enumeration

## Instructions

### Step 1: Prepare Lists

**Context**: Ensure users.txt and pass.txt are formatted (one per line).

No command.

> Limit to 100 entries to avoid detection.

### Step 2: Execute Brute-Force

**Context**: Spray against SMB; --continue-on-success for multiple hits.

**Command** ([[commands/crackmapexec-brute-force-smb-usernames-and-passwords]]):
```bash
crackmapexec smb $_TARGET_IP -u users.txt -p pass.txt
```

> Output flags valid creds with Pwn3d!; save for next steps.

### Step 3: Verify Access

**Context**: Test single valid pair.

smbclient //$_TARGET_IP/IPC$ -U user%pass

> Success if shares list.
