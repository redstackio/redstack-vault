---
id: 156e682a-001e-4e3f-9653-bb5c6798220f
name: Dump Secrets from a Remote System
type: procedure
verified: true
submitted: true
created_at: '2020-03-16T01:39:57.862422+00:00'
updated_at: '2023-05-25T19:44:04.905834+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
platforms:
- Windows
tags:
- '[[Active Directory]]'
- '[[administrator]]'
- '[[NTLM]]'
- '[[pass the hash]]'
commands:
- '[[Dump Password Hashes from a Remote System (Authenticated)]]'
---

# Dump Secrets from a Remote System

**Status**: ✓ Verified

## Summary

Use Impacket's secretsdump.py to dump password hashes on a remote system, using a variety of methods, including SAM/SYSTEM hive dumps, NTDS, LSA, etc. This typically requires authentication with Administrator rights. 

## Description

# Description

Use Impacket's secretsdump.py to dump password hashes on a remote system, using a variety of methods, including SAM/SYSTEM hive dumps, NTDS, LSA, etc. This typically requires authentication with Administrator rights.

## Objectives

Credential dumping is a critical step in the attack process, as it allows the attacker to obtain valid credentials for use in lateral movement, privilege escalation, and other activities. It is also a key method used by attackers to evade detection and bypass security controls, as the use of stolen credentials can make it difficult to detect unauthorized access to systems or data.

1. Dump hahses from a remote machine

- **LM**, **NTLM** and **TGT **can be cracked using a password cracking tool

- **LM** and **NTLM** can be used for Pass-the-Hash

# Instructions

**Command** ([[Dump Password Hashes from a Remote System (Authenticated)]]):

```bash
python3 secretsdump.py $_DOMAIN/$_USER:$_PASSWORD@$_TARGET_IP
```

## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]

## Commands Used

- [[Dump Password Hashes from a Remote System (Authenticated)]]

## Tags

- [[Active Directory]]
- [[administrator]]
- [[NTLM]]
- [[pass the hash]]
