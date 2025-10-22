---
id: db2ba71a-0c6a-41b5-8b27-7761aeed6320
name: SQL Injection Using Order By Statement
type: procedure
verified: true
submitted: true
created_at: '2020-07-21T15:20:57.055714+00:00'
updated_at: '2023-05-26T15:58:29.272843+00:00'
platforms:
- Web
tags:
- '[[injection]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[SQL]]'
- '[[sqli]]'
- '[[Web Applications]]'
---

# SQL Injection Using Order By Statement

**Status**: ✓ Verified

## Summary

An attacker will inject SQL queries through user input fields or parameters in the URL to execute them on the database and extract sensitive information. Using order by will help in identifying the number of columns present in the table, which can further be used to construct payloads for Union Bas

## Description

# Description

An attacker will inject SQL queries through user input fields or parameters in the URL to execute them on the database and extract sensitive information. Using *order by *will help in identifying the number of columns present in the table, which can further be used to construct payloads for Union Based SQL Injection.

# Instructions

1. Insert the order by SQL injection payload in the user input field and observe the response for error message

2. Modify the column number in the payload until an error message is observed in the response

3. Error message is observed in the response when the column number is set to 7. This says that the number of columns in the table are 6.

## Platforms

- Web

## Tags

- [[injection]]
- [[owasp]]
- [[owasp top 10]]
- [[SQL]]
- [[sqli]]
- [[Web Applications]]
