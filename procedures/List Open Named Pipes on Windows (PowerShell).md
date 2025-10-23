---
id: 6ccdca75-5cb4-4df8-9cac-f39510cc4d6d
name: List Open Named Pipes on Windows (PowerShell)
type: procedure
verified: true
submitted: true
created_at: '2020-04-29T00:05:04.370427+00:00'
updated_at: '2023-05-25T19:42:12.099710+00:00'
platforms:
- Windows
tags:
- '[[Enumeration]]'
commands:
- '[[List Open Named Pipes on Windows (PowerShell)]]'
---

# List Open Named Pipes on Windows (PowerShell)

**Status**: ✓ Verified

## Summary

Use PowerShell to list open named pipes on a local Windows system. Named pipes are one-way or duplex FIFO (first in first out) pipes used to communicate between the pipe server and client. 

## Description

# Description

Use PowerShell to list open named pipes on a local Windows system. Named pipes are one-way or duplex FIFO (first in first out) pipes used to communicate between the pipe server and client.



# Instructions





**Command** ([[List Open Named Pipes on Windows (PowerShell)]]):

```bash
[System.IO.Directory]::GetFiles("\\.\pipe\")
```





## Platforms

- Windows

## Commands Used

- [[List Open Named Pipes on Windows (PowerShell)]]

## Tags

- [[Enumeration]]


