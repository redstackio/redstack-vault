---
id: fe5d5fef-d6bb-4967-83f0-71300fd43c29
name: Query LDAP and Enumerate the Base DN (Nmap)
type: procedure
verified: true
submitted: true
created_at: '2020-03-17T22:45:52.428344+00:00'
updated_at: '2023-05-25T19:57:51.161999+00:00'
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
- '[[Nmap LDAP Enumeration with Scripts]]'
---

# Query LDAP and Enumerate the Base DN (Nmap)

**Status**: ✓ Verified

## Summary

Connect to LDAP with anonymous bind and enumerate the base DN. 

## Description

# Description

Connect to LDAP with anonymous bind and enumerate the base DN.





## Objectives

By scanning the LDAP service and enumerating objects such as users, groups, ACLs, trusts, and other data, the attacker can gain a better understanding of the target environment, including the organizational structure, user accounts, group memberships, and other information that may be useful in future attacks.



1. Identify potential targets that could be further exploited

2. Determine the organization structure including domain and forest names, domain controllers and trust



# Instructions





**Command** ([[Nmap LDAP Enumeration with Scripts]]):

```bash
nmap -p $_TARGET_PORT -script ldap-search $_TARGET_IP
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

- [[Nmap LDAP Enumeration with Scripts]]

## Tags

- [[Active Directory]]
- [[Enumeration]]


