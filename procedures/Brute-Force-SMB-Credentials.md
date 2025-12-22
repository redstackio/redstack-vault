---
id: 08f7d6ec-71a4-4563-82b2-23f66791205f
name: Brute-Force-SMB-Credentials
type: procedure
verified: true
submitted: true
created_at: '2019-12-27T20:37:12.139314+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Brute Force]]'
sub_techniques:
  - '[[.001]] Password Guessing'
platforms:
  - Linux
  - Windows
tags:
  - authentication
  - network
  - service-attacks
commands:
  - '[[commands/crackmapexec-smb-brute-force]]'
tools:
  - '[[tools/CrackMapExec]]'
validated: true
---

# Brute-Force-SMB-Credentials

## Summary

This procedure uses CrackMapExec to perform dictionary-based brute force against SMB services, identifying valid credentials for further access in Windows networks.

## Description

SMB brute force targets port 445 to test username/password combinations, common in AD environments with weak credentials. Using a custom dictionary reduces attempts and noise. Success grants share access or lateral movement. It's noisy, so use in low-stealth scenarios. CrackMapExec handles NTLM auth and reports valid creds with 'Pwn3d!'.

## Requirements

- Target IP with SMB exposed (TCP/445)
- Username list (from LDAP enum)
- Password dictionary (built previously)
- CrackMapExec installed

## Defense

- Enable SMB signing and encryption (Group Policy)
- Account lockout thresholds (e.g., 5 failures)
- Network segmentation to limit SMB exposure
- IDS rules for SMB auth failures (e.g., Suricata: smb brute force signatures)

## Objectives

- Test combinations against SMB
- Identify valid credentials
- Avoid detection through targeted lists

## Instructions

### Step 1: Prepare Input Files

**Context**: Ensure users.txt and passwords.txt are ready. If single user, use -u user instead of file.

> Why: Files allow batching; single for quick tests.

### Step 2: Execute SMB Brute Force

**Context**: Run CME to attempt logons. It probes NTLM and reports successes.

**Command** ([[commands/crackmapexec-smb-brute-force]]):
```bash
crackmapexec smb $_TARGET_IP -u users.txt -p passwords.txt
```

> For v3+, include 'smb'; older omit. Expected: [+] for valid creds. If no success, refine dictionary. Decision: If partial successes (e.g., user exists but wrong pass), update list.
