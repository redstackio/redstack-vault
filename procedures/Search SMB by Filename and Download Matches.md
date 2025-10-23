---
id: 4d1e4a4d-cd7e-4614-be4b-805795cce47a
name: Search SMB by Filename and Download Matches
type: procedure
verified: true
submitted: true
created_at: '2019-12-04T18:19:37.061420+00:00'
updated_at: '2023-05-25T19:47:12.339932+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
techniques:
- '[[Data from Network Shared Drive|T1039 - Data from Network Shared Drive]]'
platforms:
- Linux
- Windows
tags:
- '[[data exposure]]'
- '[[Network]]'
- '[[Service Attacks]]'
commands:
- '[[SMBMap Search an SMB Share Recursively by File Name]]'
---

# Search SMB by Filename and Download Matches

**Status**: ✓ Verified

## Summary

SMB shares often contain sensitive information, which can be easily enumerated. Tools such as smbmap can crawl a SMB share, looking for and downloading files which match certain name criteria. 

## Description

# Description

SMB shares often contain sensitive information, which can be easily enumerated. Tools such as smbmap can crawl a SMB share, looking for and downloading files which match certain name criteria.



# Instructions





**Command** ([[SMBMap Search an SMB Share Recursively by File Name]]):

```bash
smbmap -u $_USERNAME -p $_PASSWORD -R $_SHARE_NAME -H $_TARGET_IP -A $_FILENAME -q
```



Note: If attempting to list SMB shares without a valid username and password, try ommitting the "-u" and "-p" flags to attempt to authenticate with a null session.

## Platforms

- Linux
- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]

### Techniques

- [[Data from Network Shared Drive|T1039 - Data from Network Shared Drive]]

## Commands Used

- [[SMBMap Search an SMB Share Recursively by File Name]]

## Tags

- [[data exposure]]
- [[Network]]
- [[Service Attacks]]


