---
id: b8832e7f-f1a3-4267-baaa-3248feb1032c
name: Mount a Windows VHD Image on Linux
type: procedure
verified: false
submitted: false
created_at: '2019-10-11T22:11:00.298490+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
platforms:
- Windows
tags:
- '[[Hypervisors]]'
commands:
- '[[guestmount Mount a VHD file]]'
---

# Mount a Windows VHD Image on Linux

## Summary

Windows Hyper-V Virtual Hard Disk (VHD) files can be mounted on many Linux distributions using tools like guestmount. 

## Description

# Description

Windows Hyper-V Virtual Hard Disk (VHD) files can be mounted on many Linux distributions using tools like guestmount.



# Instructions





**Command** ([[guestmount Mount a VHD file]]):

```bash
guestmount --add $_IMAGE.vhd --inspector --ro $_DEST_DIRECTORY
```





## Platforms

- Windows

## Commands Used

- [[guestmount Mount a VHD file]]

## Tags

- [[Hypervisors]]


