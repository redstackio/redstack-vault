---
id: 39f5c20b-f3b1-4390-b984-efd051b667be
name: Identify-Hash-Type-for-Cracking
type: procedure
verified: true
submitted: true
created_at: '2020-03-14T02:00:51.380679+00:00'
updated_at: '2023-05-25T19:45:09.356398+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Brute Force|T1110 - Brute Force]]'
sub_techniques: []
platforms:
  - Linux
  - Windows
tags:
  - cryptography
  - password-cracking
commands: []
tools:
  - '[[tools/Hashcat]]'
validated: true
---

# Identify-Hash-Type-for-Cracking

## Summary

This procedure analyzes captured hashes to determine their type and select the correct Hashcat mode for cracking.

## Description

Hashes vary by format (e.g., NTLM, Kerberos TGS). Identification via prefix ($krb5tgs$), length, or tools ensures efficient cracking. Reference Hashcat's example hashes wiki.

## Requirements

- Captured hash string
- Access to Hashcat example hashes documentation

## Defense

- Use strong hashing (e.g., bcrypt)
- Implement account lockouts
- Rotate credentials regularly

## Objectives

1. Parse hash format
2. Match to known type
3. Select Hashcat mode

## Instructions

### Step 1: Examine Hash Structure

**Context**: Look for identifiers like $krb5tgs$23$ for Kerberos.

Manual: Check prefix and length; search Hashcat wiki for matches.

> E.g., $krb5tgs$ indicates mode 13100.

### Step 2: Confirm Mode

**Context**: Test small crack if unsure.

hashcat --example-hashes | grep krb5tgs.

> Success if mode identified (e.g., 13100 for TGS etype 23).
