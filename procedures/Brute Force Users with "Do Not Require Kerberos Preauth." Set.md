---
id: a2766e48-3477-4a2a-9807-a89e3ccc67c1
name: Brute Force Users with "Do Not Require Kerberos Preauth." Set
type: procedure
verified: false
submitted: false
created_at: '2020-03-17T21:43:18.756014+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
platforms:
- Windows
tags:
- '[[Active Directory]]'
- '[[Enumeration]]'
commands:
- '[[GetNPUsers.py Brute force Users with "Do Not Require Preauth."]]'
---

# Brute Force Users with "Do Not Require Kerberos Preauth." Set

## Summary

Users with "Do not require Kerberos preauthentication" will disclose their TGT without authenticating with a valid password, as long as the username is correct. This allows attackers to build a wordlist and brute force valid users with GetNPUsers.py, also retreiving their TGT. 

## Description

# Description

Users with "Do not require Kerberos preauthentication" will disclose their TGT without authenticating with a valid password, as long as the username is correct. This allows attackers to build a wordlist and brute force valid users with GetNPUsers.py, also retreiving their TGT.

## Objectives

1. Configure a textfile with a list of user names

 - Username lists could be obtained through O365, from the AD / LDAP, social engineering, shadow IT and more.

2. Obtain the valid users TGTs 

# Instructions

Use a wordlist of usernames, ideally one built specifically for the target, or a generic list of popular names.

**Command** ([[GetNPUsers.py Brute force Users with "Do Not Require Preauth."]]):

```bash
GetNPUsers.py $_DOMAIN/ -no-pass -usersfile $_USERS.txt -dc-ip $_TARGET_IP
```

## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]

## Commands Used

- [[GetNPUsers.py Brute force Users with "Do Not Require Preauth."]]

## Tags

- [[Active Directory]]
- [[Enumeration]]
