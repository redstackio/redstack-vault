---
id: 5a61a802-2a16-4a10-9fd9-602ea5276a1a
name: Nmap to Enumerate Directories in Application
type: procedure
verified: true
submitted: true
created_at: '2020-09-01T17:09:05.224000+00:00'
updated_at: '2023-05-26T18:51:33.032919+00:00'
platforms:
- Web
tags:
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
commands:
- '[[Nmap Command to Enumerate Directories]]'
---

# Nmap to Enumerate Directories in Application

**Status**: ✓ Verified

## Summary

Directories that are not referenced in the application can be identified using Nmap script. http-enum script can be used to find directories in the application. 

## Description

# Description

Directories that are not referenced in the application can be identified using Nmap script. *http-enum *script can be used to find directories in the application.

# Procedure

# 

1. The below Nmap script can be used to enumerate the directories that are present in the web application.

**Command** ([[Nmap Command to Enumerate Directories]]):

```bash
nmap -p80 --script http-enum 192.168.1.3
```

## Platforms

- Web

## Commands Used

- [[Nmap Command to Enumerate Directories]]

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]
