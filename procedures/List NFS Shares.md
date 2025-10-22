---
id: 7e5b207c-edb4-458d-9075-506fa6498143
name: List NFS Shares
type: procedure
verified: false
submitted: false
created_at: '2019-09-11T21:53:20.976114+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Network Share Discovery|T1135 - Network Share Discovery]]'
platforms:
- Linux
tags:
- '[[Network]]'
commands:
- '[[Showmount List Mounted NFS Directories]]'
- '[[showmount List NFS Exports]]'
---

# List NFS Shares

## Summary

Network File System (NFS) is similar to SMB, in that it allows users to access shared files and folders over a network. Systems with NFS enabled may be queried for information on shared folders, available mounts, and other useful information. 

## Description

# Description

Network File System (NFS) is similar to SMB, in that it allows users to access shared files and folders over a network. Systems with NFS enabled may be queried for information on shared folders, available mounts, and other useful information.

# Instructions

**Command** ([[Showmount List Mounted NFS Directories]]):

```bash
showmount -d $_TARGET_IP
```

**Command** ([[showmount List NFS Exports]]):

```bash
showmount -e $_TARGET_IP
```

## Platforms

- Linux

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Network Share Discovery|T1135 - Network Share Discovery]]

## Commands Used

- [[Showmount List Mounted NFS Directories]]
- [[showmount List NFS Exports]]

## Tags

- [[Network]]
