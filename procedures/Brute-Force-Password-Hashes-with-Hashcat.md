---
id: 12b10285-290c-411e-b284-650c8cbd5a33
name: Brute-Force-Password-Hashes-with-Hashcat
type: procedure
verified: true
submitted: true
created_at: '2020-03-17T04:34:06.715518+00:00'
updated_at: '2023-05-25T19:59:26.357810+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Brute Force]]'
sub_techniques:
  - '[[Password Cracking]]'
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
validated: true
---

# Brute-Force-Password-Hashes-with-Hashcat

## Summary

This procedure uses Hashcat to perform dictionary-based brute-force cracking on captured password hashes, such as those from AS-REP roasting, to recover plaintext credentials for further AD exploitation.

## Description

Hashcat leverages GPU acceleration for high-speed cracking. After identifying the hash mode, a wordlist (e.g., rockyou.txt) is used to test potential passwords. Success depends on password strength and wordlist quality; rules can enhance attacks.

## Requirements

- GPU-enabled machine for speed
- Hash file and wordlist
- Identified hash mode from previous step

## Defense

- Enforce complex, unique passwords
- Monitor for offline cracking attempts via EDR
- Rotate credentials post-breach suspicion

## Objectives

1. Load hashes and select mode
2. Run dictionary attack
3. Recover and validate passwords

## Instructions

### Step 1: Prepare Files

**Context**: Ensure hash file (hashes.txt) and wordlist (e.g., /usr/share/wordlists/rockyou.txt) are ready.

No command; verify paths.

### Step 2: Launch Hashcat Attack

**Context**: Execute in dictionary mode; use -a 0 for straight attack or -a 3 for brute-force if needed.

**Command** ([[commands/hashcat-brute-force-password-hashes]]):
```bash
hashcat -m $_MODE $_HASH_FILE $_WORDLIST
```

> Replace $_MODE with 18200 for AS-REP. Press 's' for status. Cracked hashes shown as username:password.

### Step 3: Extract Results

**Context**: Review potfile or output for recovered creds.

**Command** (hashcat --show):
```bash
hashcat --show -m $_MODE $_HASH_FILE
```

> Displays cracked pairs.

**Expected Output**: Cracked credentials, e.g., 'user:password123'.

## Expected Output

Session cracked: 1/1 (100%), e.g., $krb5asrep$...:password
