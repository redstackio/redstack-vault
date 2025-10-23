---
id: 6d10cb1d-08a9-4d01-811a-33e5fbfc385c
name: List All Active Directory Users
type: procedure
verified: true
submitted: true
created_at: '2019-12-04T19:07:19.064482+00:00'
updated_at: '2023-05-25T19:58:16.378137+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Account Discovery|T1087 - Account Discovery]]'
platforms:
- Windows
tags:
- '[[Active Directory]]'
- '[[Network]]'
- '[[Service Attacks]]'
commands:
- '[[List All Active Directory Users (Authenticated)]]'
---

# List All Active Directory Users

**Status**: ✓ Verified

## Summary

Attackers with valid credentials to an Active Directory domain user can authenticate with a domain controller and list other users in the domain. 

## Description

# Description

Attackers with valid credentials to an Active Directory domain user can authenticate with a domain controller and list other users in the domain.



# Instructions

Enumerate Active Directory users (enabled, disabled, and those without e-mail addresses)  using impacket's GetADUser.py





**Command** ([[List All Active Directory Users (Authenticated)]]):

```bash
GetADUsers.py '$_DOMAIN/$_USERNAME:$_PASSWORD' -dc-ip $_DOMAIN_IP -all
```





## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Account Discovery|T1087 - Account Discovery]]

## Commands Used

- [[List All Active Directory Users (Authenticated)]]

## Tags

- [[Active Directory]]
- [[Network]]
- [[Service Attacks]]


