---
id: 690c0037-984c-49b8-842c-3daec860685b
name: Cached Domain Credentials
type: sub-technique
mitre_id: T1003.005
mitre_url: null
created_at: '2023-04-06T00:31:26.307352+00:00'
updated_at: '2023-04-06T00:31:26.307352+00:00'
parent_technique: '[[Credential Dumping|T1003 - Credential Dumping]]'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
---

# Cached Domain Credentials

**MITRE ID**: T1003.005

**Parent Technique**: [[Credential Dumping|T1003 - Credential Dumping]]

This is a sub-technique of T1003 - Credential Dumping.

## Summary

Adversaries may attempt to access cached domain credentials used to allow authentication to occur in the event a domain controller is unavailable.(Citation: Microsoft - Cached Creds)

On Windows Vista and newer, the hash format is DCC2 (Domain Cached Credentials version 2) hash, also known as MS-Cac

## Description

Adversaries may attempt to access cached domain credentials used to allow authentication to occur in the event a domain controller is unavailable.(Citation: Microsoft - Cached Creds)

On Windows Vista and newer, the hash format is DCC2 (Domain Cached Credentials version 2) hash, also known as MS-Cache v2 hash.(Citation: PassLib mscache) The number of default cached credentials varies and can be altered per system. This hash does not allow pass-the-hash style attacks, and instead requires [Password Cracking](https://attack.mitre.org/techniques/T1110/002) to recover the plaintext password.(Citation: ired mscache)

With SYSTEM access, the tools/utilities such as [Mimikatz](https://attack.mitre.org/software/S0002), [Reg](https://attack.mitre.org/software/S0075), and secretsdump.py can be used to extract the cached credentials.

Note: Cached credentials for Windows Vista are derived using PBKDF2.(Citation: PassLib mscache)

## Tactics

This sub-technique is used in the following tactics:

- [[Credential Access|TA0006 - Credential Access]]
