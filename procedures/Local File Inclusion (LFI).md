---
id: bfac301f-8e8d-47f8-abc2-6760d2ea1f09
name: Local File Inclusion (LFI)
type: procedure
verified: true
submitted: true
created_at: '2020-07-22T17:12:11.994395+00:00'
updated_at: '2023-05-26T01:13:30.576859+00:00'
platforms:
- Web
tags:
- '[[LFI]]'
- '[[Local File Inclusion]]'
- '[[Web Applications]]'
---

# Local File Inclusion (LFI)

**Status**: ✓ Verified

## Summary

Local file inclusion attacks can be performed using the parameters that accept file names/path as input. Local file from the server is included in the web response. The payload contains ../../../ pattern which makes the application to jump to previous directories. 

## Description

# Description

Local file inclusion attacks can be performed using the parameters that accept file names/path as input. Local file from the server is included in the web response. The payload contains ../../../ pattern which makes the application to jump to previous directories.

# Instructions

1. Pass the file path that should be loaded in the response through page parameter

2. The response is loading the *passwd *file from /etc directory

## Platforms

- Web

## Tags

- [[LFI]]
- [[Local File Inclusion]]
- [[Web Applications]]
