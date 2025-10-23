---
id: f1e7dffb-48e4-4fad-b3a8-ac49380a527b
name: Query LDAP for Root DSE Object Information
type: procedure
verified: true
submitted: true
created_at: '2020-03-17T22:31:20.816208+00:00'
updated_at: '2023-05-25T20:00:20.591866+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Domain Trust Discovery|T1482 - Domain Trust Discovery]]'
platforms:
- Linux
- Windows
tags:
- '[[Active Directory]]'
- '[[Enumeration]]'
commands:
- '[[Nmap Query LDAP for Root DSE Object Information]]'
---

# Query LDAP for Root DSE Object Information

**Status**: ✓ Verified

## Summary

Connect to LDAP and enumerate the root DSE for information. This discloses information necessary for domain enumeration, such as domain names, user names, etc. 

## Description

# Description

Connect to LDAP and enumerate the root DSE for information. This discloses information necessary for domain enumeration, such as domain names, user names, etc.



# Instructions





**Command** ([[Nmap Query LDAP for Root DSE Object Information]]):

```bash
nmap -script ldap-rootdse -p 389 $_TARGET_IP
```





## Platforms

- Linux
- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Domain Trust Discovery|T1482 - Domain Trust Discovery]]

## Commands Used

- [[Nmap Query LDAP for Root DSE Object Information]]

## Tags

- [[Active Directory]]
- [[Enumeration]]


