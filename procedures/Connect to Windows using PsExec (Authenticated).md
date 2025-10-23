---
id: 2531e058-1a98-452a-9f87-52ac02588cd8
name: Connect to Windows using PsExec (Authenticated)
type: procedure
verified: true
submitted: true
created_at: '2019-12-04T20:10:15.053531+00:00'
updated_at: '2023-05-25T19:58:04.662024+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Windows Admin Shares|T1077 - Windows Admin Shares]]'
platforms:
- Windows
tags:
- '[[Network]]'
- '[[Service Attacks]]'
commands:
- '[[psexec.py Connect and Spawn a Command Shell]]'
---

# Connect to Windows using PsExec (Authenticated)

**Status**: ✓ Verified

## Summary

Use PSExec to connect to a remote Windows system and spawn a Command shell  (cmd.exe). In order to use PSExec, the user must have full permissions to the "$ADMIN" share, which generally requires administrator credentials. 

## Description

# Description

Use PSExec to connect to a remote Windows system and spawn a Command shell  (cmd.exe). In order to use PSExec, the user must have full permissions to the "$ADMIN" share, which generally requires administrator credentials.



# Instructions





**Command** ([[psexec.py Connect and Spawn a Command Shell]]):

```bash
psexec.py $_DOMAIN/$_USERNAME:$_PASSWORD@$_TARGET_IP
```





## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Windows Admin Shares|T1077 - Windows Admin Shares]]

## Commands Used

- [[psexec.py Connect and Spawn a Command Shell]]

## Tags

- [[Network]]
- [[Service Attacks]]


