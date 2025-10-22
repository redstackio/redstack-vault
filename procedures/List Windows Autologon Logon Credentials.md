---
id: 27bc330c-ee4c-4fe5-b1d4-1b3ce0c5fcd8
name: List Windows Autologon Logon Credentials
type: procedure
verified: true
submitted: true
created_at: '2020-03-17T23:49:26.728082+00:00'
updated_at: '2023-05-25T19:47:55.607962+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
platforms:
- Windows
tags:
- '[[data exposure]]'
- '[[Enumeration]]'
- '[[known vulnerability]]'
commands:
- '[[Query Windows Registry for Auto Logon Credentials]]'
---

# List Windows Autologon Logon Credentials

**Status**: ✓ Verified

## Summary

Query the Windows registry for credentials configured with the automatic logon feature. Windows allows users to specify credentials to skip logon prompts, but since these credentials are stored openly in the registry, other users can view them. 

## Description

# Description

Query the Windows registry for credentials configured with the automatic logon feature. Windows allows users to specify credentials to skip logon prompts, but since these credentials are stored openly in the registry, other users can view them. 

## Objectives

This technique is commonly used in post-exploitation activities to obtain valid credentials for lateral movement or privilege escalation. It is also a key method used by attackers to evade detection and bypass security controls, as the use of stolen credentials can make it difficult to detect unauthorized access to systems or data.

1. Obtain credentials, they can be local or domain credentials

# Instructions

**Command** ([[Query Windows Registry for Auto Logon Credentials]]):

```bash
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon"
```

## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]

## Commands Used

- [[Query Windows Registry for Auto Logon Credentials]]

## Tags

- [[data exposure]]
- [[Enumeration]]
- [[known vulnerability]]
