---
id: 12b10285-290c-411e-b284-650c8cbd5a33
name: brute-force-hashes-with-hashcat-dictionary
type: procedure
verified: true
submitted: true
created_at: '2020-03-17T04:34:06.715518+00:00'
updated_at: '2023-05-25T19:59:26.357810+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Password Spraying]]'
sub_techniques: []
tags:
  - cryptography
  - password-cracking
commands:
  - '[[commands/hashcat-brute-force-dictionary]]'
platforms:
  - Linux
  - Windows
tools:
  - '[[tools/Hashcat]]'
validated: true
---

# Brute Force Hashes with Hashcat Dictionary

## Summary

This procedure uses Hashcat to perform dictionary attacks on identified hashes (e.g., Kerberos TGS) with wordlists like rockyou.txt, recovering plaintext passwords for service accounts.

## Description

Dictionary attacks test common passwords against hashes offline. For Kerberoasting, mode 13100 targets RC4-encrypted TGS. Success depends on weak service passwords; combine with rules for mutations.

## Requirements

1. Identified hash mode (e.g., 13100)
2. Hash file
3. Wordlist (rockyou.txt)
4. GPU for acceleration

## Defense

- Enforce password policies (length, complexity) for service accounts
- Use managed service accounts with auto-rotation
- Detect offline cracking via stolen hash indicators (e.g., EDR on hash files)

## Objectives

1. Load hashes and wordlist
2. Execute dictionary attack
3. Recover and validate passwords

## Instructions

### Step 1: Prepare Files

**Context**: Ensure hashes and wordlist ready.

```bash
ls kerb_hashes.txt /usr/share/wordlists/rockyou.txt
```

### Step 2: Run Dictionary Attack

**Context**: Specify mode, input files; monitor progress.

**Command** ([[commands/hashcat-brute-force-dictionary]]):
```bash
hashcat -m 13100 $_HASH_FILE /usr/share/wordlists/rockyou.txt
```

> Expected: Cracked lines like 'hash:password'.

### Step 3: Extract Results

**Context**: View cracked passwords.

```bash
hashcat ... --show
```

> Outputs recovered creds for use in PSExec.
