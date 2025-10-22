---
id: 6b8fdaaf-c983-4d6f-82f0-948ebf766d6f
name: Enumerate Windows Samba Services
type: procedure
verified: false
submitted: false
created_at: '2020-03-16T02:47:29.085634+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Network Service Scanning|T1046 - Network Service Scanning]]'
platforms:
- Windows
tags:
- '[[Enumeration]]'
- '[[Network]]'
commands:
- '[[enum4linux Enumerate SMB/RPC Services]]'
---

# Enumerate Windows Samba Services

## Summary

Use enum4linux to enumerate network facing Samba services for users, groups, services, etc. 

## Description

# Description

Use enum4linux to enumerate network facing Samba services for users, groups, services, etc.

# Instructions

**Command** ([[enum4linux Enumerate SMB/RPC Services]]):

```bash
enum4linux $_TARGET_IP
```

## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Network Service Scanning|T1046 - Network Service Scanning]]

## Commands Used

- [[enum4linux Enumerate SMB/RPC Services]]

## Tags

- [[Enumeration]]
- [[Network]]
