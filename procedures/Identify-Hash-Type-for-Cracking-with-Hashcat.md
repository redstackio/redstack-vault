---
id: 39f5c20b-f3b1-4390-b984-efd051b667be
name: Identify-Hash-Type-for-Cracking-with-Hashcat
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
commands: []
platforms:
  - Linux
  - Windows
tools:
  - '[[tools/Hashcat]]'
validated: true
---

# Identify-Hash-Type-for-Cracking-with-Hashcat

## Summary

This procedure analyzes captured password hashes to determine their type and corresponding Hashcat mode, essential for effective offline cracking in credential access attacks.

## Description

Hashes from sources like AS-REP roasting or NTDS dumps vary in format (e.g., NTLM, Kerberos). Identifying the type via prefix, length, or structure ensures the correct cracking mode is used, maximizing success rates without wasting compute resources.

## Requirements

- Captured hash string or file
- Access to Hashcat example hashes documentation
- Basic knowledge of hash formats

## Defense

- Enforce strong password policies to resist cracking
- Use salted hashes and monitor for dump attempts
- Implement HIPS to block hash extraction tools

## Objectives

1. Parse hash format and identifier
2. Match to Hashcat mode
3. Prepare for brute-force attack

## Instructions

### Step 1: Examine Hash Structure

**Context**: Look for identifiers like '$krb5asrep$' or length (e.g., 32 chars for MD5).

No command; manual review, e.g., hash = '$krb5asrep$23$user@domain:hash'.

### Step 2: Reference Hashcat Examples

**Context**: Search Hashcat wiki for matching samples to confirm mode.

No command; visit https://hashcat.net/wiki/doku.php?id=example_hashes, search for prefix.

> For AS-REP, matches mode 18200 (Kerberos 5, etype 23).

### Step 3: Validate Mode

**Context**: Test with hashcat --example to confirm.

No command; note mode for next step.

**Expected Output**: Confirmed mode, e.g., 'Mode: 18200 - Kerberos 5 AS-REP etype 23'.

## Expected Output

Hash identified as Kerberos AS-REP, ready for mode 18200 cracking.
