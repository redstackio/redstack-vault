---
id: 552c9bc6-debd-4436-aed7-489a2522a74b
name: Browse an SMB Share
type: procedure
verified: false
submitted: false
created_at: '2019-12-11T19:01:24.467538+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
techniques:
- '[[Data from Network Shared Drive|T1039 - Data from Network Shared Drive]]'
platforms:
- Linux
- Windows
tags:
- '[[Network]]'
- '[[Service Attacks]]'
commands:
- '[[smbclient Connect to an SMB Share (Autenticated)]]'
---

# Browse an SMB Share

## Summary

Use smbclient to connect to an SMB share and browse with an interactive shell. 

## Description

# Description

Use smbclient to connect to an SMB share and browse with an interactive shell.

# Instructions

If attempting to connected without a username and password (a NULL session), omit the "-U" argument and the username and password values.

**Command** ([[smbclient Connect to an SMB Share (Autenticated)]]):

```bash
smbclient -U $_USERNAME%$_PASSWORD //$_TARGET_IP/$_SHARE_NAME
```

## Platforms

- Linux
- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]

### Techniques

- [[Data from Network Shared Drive|T1039 - Data from Network Shared Drive]]

## Commands Used

- [[smbclient Connect to an SMB Share (Autenticated)]]

## Tags

- [[Network]]
- [[Service Attacks]]
