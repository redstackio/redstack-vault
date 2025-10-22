---
id: 6620ebfc-361c-4441-8717-88ad0391a365
name: SQL Injection in XML Request
type: procedure
verified: true
submitted: true
created_at: '2020-09-05T18:35:21.094312+00:00'
updated_at: '2023-05-26T18:50:18.347221+00:00'
platforms:
- Web
tags:
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[SQL]]'
- '[[sqli]]'
- '[[SQL Injection]]'
- '[[Web Applications]]'
- '[[xml]]'
---

# SQL Injection in XML Request

**Status**: ✓ Verified

## Summary

SQL injection attack is performed by injecting SQL statements through user input fields and executing them. SQL injection can also be performed on the XML requests by intercepting and manipulating the content in the request. 

## Description

# Description

SQL injection attack is performed by injecting SQL statements through user input fields and executing them. SQL injection can also be performed on the XML requests by intercepting and manipulating the content in the request.

# Procedure

1. Intercept the XML login request from login page in the application. Observe that username and password are sent in XML request.

2. Modify the password and replace with ' or '1'='1 payload to authenticate with the application without valid password.

## Platforms

- Web

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[SQL]]
- [[sqli]]
- [[SQL Injection]]
- [[Web Applications]]
- [[xml]]
