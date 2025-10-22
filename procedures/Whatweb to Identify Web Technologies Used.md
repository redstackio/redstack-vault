---
id: b5b8827f-98ad-4585-8705-dfee242943cb
name: Whatweb to Identify Web Technologies Used
type: procedure
verified: true
submitted: true
created_at: '2020-08-31T17:47:18.057705+00:00'
updated_at: '2023-05-26T01:30:35.330888+00:00'
platforms:
- Web
tags:
- '[[owasp]]'
- '[[Web Applications]]'
commands:
- '[[whatweb http://192.168.1.11/vcart/login.php]]'
---

# Whatweb to Identify Web Technologies Used

**Status**: ✓ Verified

## Summary

Whatweb tool helps in identifying the technologies involved in developing the application. The details include web server details, versions, programming languages used etc. 

## Description

# Description

Whatweb tool helps in identifying the technologies involved in developing the application. The details include web server details, versions, programming languages used etc.

# Procedure

1. Use the below command to run the whatweb tool and the output gives the details about the application.

**Command** ([[whatweb http://192.168.1.11/vcart/login.php]]):

```bash
whatweb http://192.168.1.11/vcart/login.php
```

## Platforms

- Web

## Commands Used

- [[whatweb http://192.168.1.11/vcart/login.php]]

## Tags

- [[owasp]]
- [[Web Applications]]
