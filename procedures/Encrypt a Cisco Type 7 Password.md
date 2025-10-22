---
id: 97d44a67-c01f-4300-9b7e-ce1c6af95a39
name: Encrypt a Cisco Type 7 Password
type: procedure
verified: true
submitted: true
created_at: '2020-03-12T21:23:02.453537+00:00'
updated_at: '2023-05-26T00:53:41.960855+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
tags:
- '[[cisco]]'
- '[[Cryptography]]'
- '[[password cracking]]'
commands:
- '[[Encrypt a Password with Cisco Type 7]]'
---

# Encrypt a Cisco Type 7 Password

**Status**: ✓ Verified

## Summary

Cisco Type 7 encrypted passwords use a publicly-known algorithm, making it trivial to encrypt and decrypt passwords with third party tools. 

## Description

# Description

Cisco Type 7 encrypted passwords use a publicly-known algorithm, making it trivial to encrypt and decrypt passwords with third party tools.

# Instructions

**Command** ([[Encrypt a Password with Cisco Type 7]]):

```bash
python ciscot7.py -e -p '$_PASSWORD'
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]

## Commands Used

- [[Encrypt a Password with Cisco Type 7]]

## Tags

- [[cisco]]
- [[Cryptography]]
- [[password cracking]]
