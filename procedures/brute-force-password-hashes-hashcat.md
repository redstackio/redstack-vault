---
id: 12b10285-290c-411e-b284-650c8cbd5a33
name: brute-force-password-hashes-hashcat
type: procedure
verified: true
submitted: false
created_at: '2020-03-17T04:34:06.715518+00:00'
updated_at: '2023-05-25T19:59:26.357810+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Brute Force|T1110 - Brute Force]]'
sub_techniques: []
tags:
  - cryptography
  - password-cracking
commands:
  - '[[commands/hashcat-brute-force-password-hashes]]'
platforms:
  - Linux
  - Windows
tools:
  - '[[tools/Hashcat]]'
skill_level: intermediate
impact_level: high
detection_risk: none
validated: true
---

# brute-force-password-hashes-hashcat

## Summary

This procedure employs Hashcat to perform dictionary-based brute-force attacks on password hashes extracted from memory or services, recovering plaintext for reuse in authentication like SMB or WinRM.

## Description

Offline cracking leverages GPU acceleration in Hashcat for high-speed attempts against wordlists. After identifying the mode, attackers use rules or masks to guess passwords efficiently. In Windows AD, NTLM hashes are prime targets post-dump.

## Requirements

1. Identified hash file and mode from prior procedure
2. GPU-enabled system with Hashcat
3. Wordlist (e.g., rockyou.txt)

## Defense

- Enforce password complexity and rotation
- Detect offline attacks via missing logs (focus on dump prevention)
- Use Windows Credential Guard to protect hashes

## Objectives

1. Crack hashes to plaintext
2. Obtain credentials for lateral movement
3. Escalate if admin passwords recovered

## Instructions

### Step 1: Prepare Files

**Context**: Ensure hash file format matches mode; one hash per line.

No command; edit hashes.txt.

> Remove salts if needed per mode docs.

### Step 2: Run Dictionary Attack

**Context**: Attack with wordlist; add -r rules for mutations.

**Command** ([[commands/hashcat-brute-force-password-hashes]]):
```bash
hashcat -m $_MODE $_HASH_FILE /usr/share/wordlists/rockyou.txt
```

> Press 's' for status; cracks show as hash:plain. Use --potfile-path to save.

### Step 3: Recover and Test

**Context**: Extract cracked passwords and validate.

hashcat --show -m MODE hashes.txt

> Success if 50%+ cracked; resume with --restore if interrupted.
