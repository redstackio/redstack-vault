---
id: 4607a28e-dc06-4fe6-b85f-79cfa8107786
name: Sync the Local Clock with a Remote Domain Controller
type: procedure
verified: false
submitted: false
created_at: '2020-06-25T00:16:01.552025+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tags:
- '[[Setup]]'
commands:
- '[[net Display a Remote Server''s Time]]'
- '[[net Sync a Computer''s Time with a Remote Server]]'
---

# Sync the Local Clock with a Remote Domain Controller

## Summary

Set the local system's time using a domain controller's SMB service 

## Description

# Description

Set the local system's time using a domain controller's SMB service



# Instructions

1. Check the time on a remote server's current time





**Command** ([[net Display a Remote Server's Time]]):

```bash
net time -S $_TARGET_IP
```





2. Sync the local system's time with a remote server





**Command** ([[net Sync a Computer's Time with a Remote Server]]):

```bash
net time set -S $_TARGET_IP
```







## Commands Used

- [[net Display a Remote Server's Time]]
- [[net Sync a Computer's Time with a Remote Server]]

## Tags

- [[Setup]]


