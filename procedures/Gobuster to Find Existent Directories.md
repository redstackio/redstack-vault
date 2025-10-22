---
id: 6a599974-bd2f-4db9-83d2-a831a8a432fc
name: Gobuster to Find Existent Directories
type: procedure
verified: true
submitted: true
created_at: '2020-08-31T18:06:27.214569+00:00'
updated_at: '2023-05-26T15:55:15.039069+00:00'
platforms:
- Web
tags:
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
commands:
- '[[Gobuster Command to Find Existent Directories]]'
---

# Gobuster to Find Existent Directories

**Status**: ✓ Verified

## Summary

Gobuster tool is used to find directories in the web application. The tool brute-forces the directories with the provided list. 

## Description

# Description

Gobuster tool is used to find directories in the web application. The tool brute-forces the directories with the provided list.

# Procedure

Use the below *gobuster*  command to provide the list of directories to brute-force. Directories listing status code 301 exist in the application.

**Command** ([[Gobuster Command to Find Existent Directories]]):

```bash
gobuster -w list.txt -u http://192.168.1.11/vcart/
```

## Platforms

- Web

## Commands Used

- [[Gobuster Command to Find Existent Directories]]

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]
