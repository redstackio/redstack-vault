---
id: 1a0538d4-a182-4782-aab1-09a3d6fbec11
name: Oracle SQL Injection Querying the Database Type and Version
type: procedure
verified: true
submitted: true
created_at: '2020-08-28T15:26:14.195419+00:00'
updated_at: '2023-05-26T18:36:45.719649+00:00'
platforms:
- Web
tags:
- '[[injection]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[SQL]]'
- '[[sqli]]'
- '[[SQL Injection]]'
- '[[Web Applications]]'
---

# Oracle SQL Injection Querying the Database Type and Version

**Status**: ✓ Verified

## Summary

Union SQL injection will retrieve data from the database tables. First number of columns in the table has to be identified. Then the payload is customised based on the columns. 

## Description

# Description

Union SQL injection will retrieve data from the database tables. First number of columns in the table has to be identified. Then the payload is customised based on the columns.

# Procedure

1. Access the application and apply filter to observe category parameter in the URL. Inject SQL injection payload through the parameter.

2. Number of columns is observed as two as the application did not show any error message.

3. The below payload is constructed to retrieve version details from the Oracle database.

*'+UNION+SELECT+BANNER,+NULL+FROM+v$version--*

## Platforms

- Web

## Tags

- [[injection]]
- [[owasp]]
- [[owasp top 10]]
- [[SQL]]
- [[sqli]]
- [[SQL Injection]]
- [[Web Applications]]
