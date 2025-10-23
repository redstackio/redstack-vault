---
id: 3164654e-cfc7-4929-8ddd-e295c99ffeb7
name: Extract LM/NTLM Hashes from SAM/SYSTEM Hives
type: procedure
verified: true
submitted: true
created_at: '2019-12-28T01:37:58.777175+00:00'
updated_at: '2023-05-25T19:59:52.138912+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
platforms:
- Windows
tags:
- '[[authentication]]'
- '[[Cryptography]]'
- '[[data exposure]]'
commands:
- '[[samdump2 Extract LM/NTLM Hashes from SAM and SYSTEM]]'
---

# Extract LM/NTLM Hashes from SAM/SYSTEM Hives

**Status**: ✓ Verified

## Summary

Attackers who are able to copy a Windows system's SAM and SYSTEM files (generally stored in %SystemRoot%\System32\Config\), can extract LM and NTLM hashes contained within. Not only can attackers use these hashes in Pass the Hash attacks, they may also be able to use brute force techniques to ident

## Description

# Description

Attackers who are able to copy a Windows system's SAM and SYSTEM files (generally stored in %SystemRoot%\System32\Config\), can extract LM and NTLM hashes contained within. Not only can attackers use these hashes in Pass the Hash attacks, they may also be able to use brute force techniques to identify the password.



# Instructions





**Command** ([[samdump2 Extract LM/NTLM Hashes from SAM and SYSTEM]]):

```bash
samdump2 SYSTEM SAM
```





## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]

## Commands Used

- [[samdump2 Extract LM/NTLM Hashes from SAM and SYSTEM]]

## Tags

- [[authentication]]
- [[Cryptography]]
- [[data exposure]]


