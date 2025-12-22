---
id: 39f5c20b-f3b1-4390-b984-efd051b667be
name: Identify-Password-Hash-Type-with-Hashcat
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

# Identify-Password-Hash-Type-with-Hashcat

## Summary

Analyze captured password hashes (e.g., from AS-REP roasting) to determine the type and corresponding Hashcat mode for effective cracking.

## Description

Hashes vary by format (NTLM, Kerberos, etc.); misidentifying the mode wastes time. This procedure uses Hashcat's example hashes reference and format analysis to select the correct attack mode, essential for AD credential recovery.

## Requirements

- Captured hash file
- Access to Hashcat documentation
- Basic knowledge of hash formats

## Defense

- Use strong, unique passwords resistant to dictionary attacks
- Implement hash salting and iteration (e.g., PBKDF2)
- Monitor for offline cracking attempts via GPU usage anomalies

## Objectives

1. Parse hash format and length
2. Match to Hashcat mode
3. Confirm compatibility

## Instructions

### Step 1: Examine Hash Format

**Context**: Look for prefixes, delimiters, and length to narrow type.

E.g., AS-REP starts with $krb5asrep$23$; NTLM is 32 hex chars.

### Step 2: Reference Hashcat Examples

**Context**: Search Hashcat wiki for matching samples.

Visit https://hashcat.net/wiki/doku.php?id=example_hashes. For AS-REP, mode 18200.

If prefixed (e.g., $axcrypt_sha1$), search directly.

### Step 3: Test Mode with Hashcat

**Context**: Dry-run Hashcat to validate.

Run `hashcat --example-hashes` or a small test to confirm.

**Expected Output**: Mode identified, e.g., "Kerberos 5, AS-REP Pre-Auth, mode 18200".
