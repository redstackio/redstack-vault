---
type: procedure
description: >-
  Bypass authentication in web applications using SQL injection through raw MD5
  or SHA1 hash insertion in vulnerable queries.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Exploitation for Credential Access]]'
sub_techniques: []
tags:
  - sql-injection
  - authentication-bypass
  - md5
  - sha1
  - web
commands:
  - '[[commands/boolean-sql-injection-test]]'
  - '[[commands/calculate-md5-sha1-raw-hashes-php]]'
platforms:
  - web
tools: []
validated: true
---

# SQL-Injection-Authentication-Bypass-Using-Raw-MD5-and-SHA1-Hashes

## Summary

This procedure exploits SQL injection vulnerabilities in web application login forms that use raw (binary) MD5 or SHA1 hashing of user input directly in SQL queries without proper sanitization or prepared statements. By submitting specially crafted passwords whose binary hash output injects SQL bypass code (e.g., OR 1=1), an attacker can authenticate as an admin user without knowing the actual credentials. This targets legacy applications using insecure hashing and dynamic SQL construction.

## Description

The vulnerability arises when a login query like SELECT * FROM admin WHERE username = '$user' AND pass = '
