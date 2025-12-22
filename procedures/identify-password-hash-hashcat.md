---
id: 39f5c20b-f3b1-4390-b984-efd051b667be
name: identify-password-hash-hashcat
type: procedure
verified: true
submitted: false
created_at: '2020-03-14T02:00:51.380679+00:00'
updated_at: '2023-05-25T19:45:09.356398+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Brute Force|T1110 - Brute Force]]'
sub_techniques: []
tags:
  - cryptography
  - password-cracking
commands:
  - '[[commands/hashcat-identify-hash-type]]'
platforms:
  - Linux
  - Windows
tools:
  - '[[tools/Hashcat]]'
skill_level: intermediate
impact_level: low
detection_risk: none
validated: true
---

# identify-password-hash-hashcat

## Summary

This procedure analyzes a captured password hash to identify its algorithm and corresponding Hashcat mode, enabling efficient offline cracking. Hashes from memory dumps (e.g., NTLM, SHA1) are common in Windows post-exploitation.

## Description

Hashes vary by format (e.g., $ntlm$ for NTLM), and misidentifying the mode wastes compute time. Using Hashcat's example database, attackers match prefixes or lengths to select the right -m flag. This is crucial after extracting from lsass dumps.

## Requirements

1. Captured hash string from memory or config
2. Hashcat installed with example hashes access
3. Internet for Hashcat wiki reference

## Defense

- Use strong hashing (e.g., bcrypt) and salting
- Monitor for hash extraction tools like Mimikatz
- Implement memory protection (e.g., LSA protection)

## Objectives

1. Determine hash algorithm and Hashcat mode
2. Prepare for dictionary or brute-force attack
3. Avoid cracking failures due to wrong mode

## Instructions

### Step 1: Examine Hash Format

**Context**: Look for identifiers like $ or length to narrow options.

No command; manual review, e.g., 32 chars no $ = MD5.

> Search Hashcat wiki for matches.

### Step 2: Query Example Hashes

**Context**: Use Hashcat or wiki to confirm mode.

**Command** ([[commands/hashcat-identify-hash-type]]):
```bash
hashcat --example-hashes | grep -i $_HASH_PREFIX
```

> For $axcrypt_sha1$..., finds mode 13300. Online wiki search if local fails.

### Step 3: Validate Mode

**Context**: Test with a known sample hash.

Run hashcat -m MODE --test to verify hardware support.

> Success if mode loads without errors.
