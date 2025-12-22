---
id: 39f5c20b-f3b1-4390-b984-efd051b667be
name: identify-hash-type-with-hashcat
type: procedure
verified: true
submitted: true
created_at: '2020-03-14T02:00:51.380679+00:00'
updated_at: '2023-05-25T19:45:09.356398+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Brute Force]]'
sub_techniques: []
tags:
  - cryptography
  - password-cracking
commands:
  - '[[commands/hashcat-identify-hash]]'
tools:
  - '[[tools/Hashcat]]'
platforms:
  - Linux
  - Windows
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
---

# identify-hash-type-with-hashcat

## Summary

Analyze captured password hashes to determine their type and select the appropriate Hashcat cracking mode for efficient offline attacks.

## Description

Hash identification is crucial before cracking; this procedure uses Hashcat's built-in tools or manual inspection to classify formats like Kerberos AS-REP, ensuring the correct mode (e.g., 18200) is used.

## Requirements

- Hash file (e.g., asrep_hashes.txt)
- Hashcat installed ([[tools/Hashcat]])

## Defense

- Use strong, unique passwords resistant to cracking
- Monitor for hash extraction attempts
- Implement account lockouts

## Objectives

1. Classify hash format
2. Determine Hashcat mode
3. Prepare for cracking

## Instructions

### Step 1: Run Hashcat Identify

**Context**: Use Hashcat to auto-detect hash type from file.

**Command** ([[commands/hashcat-identify-hash]]):
```bash
hashcat --identify asrep_hashes.txt
```

> Identifies as Kerberos 5 AS-REP etype 23.

### Step 2: Manual Verification

**Context**: If needed, reference Hashcat example hashes wiki for confirmation.

No command; search for prefix like $krb5asrep$.

> Confirms mode 18200.

## Expected Output

Output indicating hash mode, e.g., Mode: 18200 (Kerberos 5, etype 23).
