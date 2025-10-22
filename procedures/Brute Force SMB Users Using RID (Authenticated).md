---
id: 021d64ab-15d2-49b0-90f1-37dd538bdd14
name: Brute Force SMB Users Using RID (Authenticated)
type: procedure
verified: true
submitted: true
created_at: '2019-12-27T22:38:42.691840+00:00'
updated_at: '2023-05-25T19:42:32.339817+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Account Discovery|T1087 - Account Discovery]]'
- '[[Brute Force|T1110 - Brute Force]]'
platforms:
- Windows
tags:
- '[[Network]]'
- '[[Service Attacks]]'
commands:
- '[[CrackMapExec Brute Force SMB Users Using RID]]'
- '[[lookupsid.py Brute Force SMB Users Using RID]]'
---

# Brute Force SMB Users Using RID (Authenticated)

**Status**: ✓ Verified

## Summary

Various tools can be used to brute force valid SMB users using their relative identifier (RID). This allows attackers to easily enumerate additional users on a system with which they've already authenticated. 

## Description

# Description

Various tools can be used to brute force valid SMB users using their relative identifier (RID). This allows attackers to easily enumerate additional users on a system with which they've already authenticated.

# Instructions

## Using CrackMapExec

**Command** ([[CrackMapExec Brute Force SMB Users Using RID]]):

```bash
crackmapexec smb $_TARGET_IP -u $_USERNAME -p $_PASSWORD --rid-brute
```

Note: CrackMapExec 3 may have issues brute forcing users using RID, and it is recommended to use version 4+.

## Using Impacket's lookupsid.py

**Command** ([[lookupsid.py Brute Force SMB Users Using RID]]):

```bash
lookupsid.py '$_USERNAME:$_PASSWORD'@$_TARGET_IP
```

## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Account Discovery|T1087 - Account Discovery]]
- [[Brute Force|T1110 - Brute Force]]

## Commands Used

- [[CrackMapExec Brute Force SMB Users Using RID]]
- [[lookupsid.py Brute Force SMB Users Using RID]]

## Tags

- [[Network]]
- [[Service Attacks]]
