---
id: 89db9662-89b5-4ab8-b1ca-84a063b5e0c9
name: Nmap to Find Directories From Robots.txt File
type: procedure
verified: false
submitted: false
created_at: '2020-09-01T17:18:29.832974+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
platforms:
- Web
tags:
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
commands:
- '[[Nmap Command to Find Directories From Robots.txt File]]'
---

# Nmap to Find Directories From Robots.txt File

## Summary

Robots.txt file contains the disallowed entries of directories that the search engines should not crawl. These directories would reveal sensitive information in some instances. 

## Description

# Description

Robots.txt file contains the disallowed entries of directories that the search engines should not crawl. These directories would reveal sensitive information in some instances.

# Procedure

1. Use the below nmap command to find the sensitive directories in the application using robots.txt file.

**Command** ([[Nmap Command to Find Directories From Robots.txt File]]):

```bash
nmap -p80 --script http-robots.txt 192.168.1.3
```

## Platforms

- Web

## Commands Used

- [[Nmap Command to Find Directories From Robots.txt File]]

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]
