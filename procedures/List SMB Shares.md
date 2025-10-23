---
id: 81533047-cdce-4113-abf3-1ca57817d302
name: List SMB Shares
type: procedure
verified: true
submitted: true
created_at: '2019-12-04T17:49:54.294983+00:00'
updated_at: '2023-05-25T19:45:55.121753+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Network Share Discovery|T1135 - Network Share Discovery]]'
platforms:
- Linux
- Windows
tags:
- '[[data exposure]]'
- '[[Network]]'
- '[[Service Attacks]]'
commands:
- '[[smbclient List SMB Shares]]'
- '[[SMBMap List SMB Shares]]'
---

# List SMB Shares

**Status**: ✓ Verified

## Summary

Query an SMB server and attempt to list available shares using a null session (no login). 

## Description

# Description

Query an SMB server and attempt to list available shares using a null session (no login).



# Instructions

If attempting to connect without a username and password (a NULL session), omit the username and password values, leaving "-U" and the empty quotes.





**Command** ([[smbclient List SMB Shares]]):

```bash
smbclient -U '$_USERNAME%$_PASSWORD' -L $_TARGET_IP
```





smbmap can list shares in a similar fashion as smbclient, but it will also enumerate folder permissions. Omit the username and password values to authenticate with a null session. leaving the empty quotes.





**Command** ([[SMBMap List SMB Shares]]):

```bash
smbmap -u '$_USERNAME' -p '$_PASSWORD' -H $_TARGET_IP
```





## Platforms

- Linux
- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Network Share Discovery|T1135 - Network Share Discovery]]

## Commands Used

- [[smbclient List SMB Shares]]
- [[SMBMap List SMB Shares]]

## Tags

- [[data exposure]]
- [[Network]]
- [[Service Attacks]]


