---
id: 08f7d6ec-71a4-4563-82b2-23f66791205f
name: Brute Force SMB Usernames and Passwords
type: procedure
verified: true
submitted: true
created_at: '2019-12-27T20:37:12.139314+00:00'
updated_at: '2023-05-25T19:56:21.281849+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
platforms:
- Linux
- Windows
tags:
- '[[authentication]]'
- '[[Network]]'
- '[[Service Attacks]]'
commands:
- '[[CrackMapExec Brute Force SMB Usernames and Passwords]]'
---

# Brute Force SMB Usernames and Passwords

**Status**: ✓ Verified

## Summary

Various tools can be used to brute force valid username and password combinations of exposed SMB shares, and is a common approach when attacking Active Directory environments. This attack is noisy, and should be avoided is stealth is a requirement. 

## Description

# Description

Various tools can be used to brute force valid username and password combinations of exposed SMB shares, and is a common approach when attacking Active Directory environments. This attack is noisy, and should be avoided is stealth is a requirement.

# Instructions

Run CrackMapExec with a username and password list.

**Command** ([[CrackMapExec Brute Force SMB Usernames and Passwords]]):

```bash
crackmapexec smb $_TARGET_IP -u $_USERNAME -p $_PASSWORD
```

Note: when using CrackMapExec version 3 or older, omit  the protocol (smb) after the command.

## Platforms

- Linux
- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Brute Force|T1110 - Brute Force]]

## Commands Used

- [[CrackMapExec Brute Force SMB Usernames and Passwords]]

## Tags

- [[authentication]]
- [[Network]]
- [[Service Attacks]]
