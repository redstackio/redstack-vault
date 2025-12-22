---
id: 12b10285-290c-411e-b284-650c8cbd5a33
name: crack-as-rep-hashes-with-hashcat
type: procedure
verified: true
submitted: true
created_at: '2020-03-17T04:34:06.715518+00:00'
updated_at: '2023-05-25T19:59:26.357810+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Brute Force]]'
sub_techniques: []
tags:
  - cryptography
  - password-cracking
commands:
  - '[[commands/hashcat-crack-mode-18200]]'
tools:
  - '[[tools/Hashcat]]'
platforms:
  - Linux
  - Windows
skill_level: intermediate
impact_level: high
detection_risk: low
validated: true
---

# crack-as-rep-hashes-with-hashcat

## Summary

Use Hashcat to crack Kerberos AS-REP hashes offline with dictionary attacks, recovering plaintext passwords for domain access.

## Description

This procedure applies wordlist-based cracking to AS-REP etype 23 hashes (mode 18200), leveraging GPU acceleration and rules to guess weak passwords common in AD environments.

## Requirements

- AS-REP hash file
- Wordlist (e.g., rockyou.txt)
- Hashcat with GPU support ([[tools/Hashcat]])

## Defense

- Enforce complex password policies
- Rotate passwords regularly
- Detect offline cracking attempts via hash exposure logs

## Objectives

1. Recover plaintext from hashes
2. Obtain valid credentials
3. Enable lateral movement

## Instructions

### Step 1: Prepare Cracking Environment

**Context**: Ensure Hashcat is configured; select mode 18200 for AS-REP.

No command; verify with `hashcat --help | grep 18200`.

> GPU recommended for speed.

### Step 2: Execute Dictionary Attack

**Context**: Run attack with wordlist and rules for mutations.

**Command** ([[commands/hashcat-crack-mode-18200]]):
```bash
hashcat -m 18200 asrep_hashes.txt /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best64.rule
```

> Cracks weak passwords quickly.

### Step 3: Review Results

**Context**: Check cracked hashes in potfile or output.

No command; `hashcat --show asrep_hashes.txt`.

> Expected: username:password pairs.

## Expected Output

Cracked credentials displayed, e.g., $krb5asrep$...:password.
