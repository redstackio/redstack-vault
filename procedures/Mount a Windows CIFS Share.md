---
id: 1c2e919b-9077-426d-9bb4-8183af87530f
name: Mount a Windows CIFS Share
type: procedure
verified: false
submitted: false
created_at: '2019-12-16T22:19:45.853063+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Network Share Discovery|T1135 - Network Share Discovery]]'
platforms:
- Windows
tags:
- '[[data exposure]]'
- '[[Network]]'
commands:
- '[[Mount a CIFS Share with a NULL Session]]'
- '[[Mount a CIFS Share with Username and Password]]'
---

# Mount a Windows CIFS Share

## Summary

CIFS shares (Microsoft's implementation of SMB) can be mounted on Linux systems using the mount tool. Once mounted, shares can be navigated like any other mounted drive. 

## Description

# Description

CIFS shares (Microsoft's implementation of SMB) can be mounted on Linux systems using the mount tool. Once mounted, shares can be navigated like any other mounted drive.



# Instructions

Install the ntfs-3g package. It is available in most package managers. Eg:





**Code**: [[apt update && apt install ntfs-3g -y]]









**Command** ([[Mount a CIFS Share with Username and Password]]):

```bash
mount -t cifs //$_TARGET_IP/$_SHARE -o 'username="$_USERNAME",password="$_PASSWORD"' /$_MOUNT_POINT
```





If connecting to a CIFS share without a username and password (NULL session), leave the username and password fields empty.





**Command** ([[Mount a CIFS Share with a NULL Session]]):

```bash
mount -t cifs //$_TARGET_IP/$_SHARE -o 'username="",password=""' /$_MOUNT_POINT
```





## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Network Share Discovery|T1135 - Network Share Discovery]]

## Commands Used

- [[Mount a CIFS Share with a NULL Session]]
- [[Mount a CIFS Share with Username and Password]]

## Tags

- [[data exposure]]
- [[Network]]


