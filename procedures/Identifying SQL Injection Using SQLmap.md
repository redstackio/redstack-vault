---
id: 10397121-926c-4962-9146-6153496c0777
name: Identifying SQL Injection Using SQLmap
type: procedure
verified: true
submitted: true
created_at: '2020-07-24T15:21:51.657523+00:00'
updated_at: '2023-05-26T18:18:37.982602+00:00'
platforms:
- Web
tags:
- '[[injection]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[SQL]]'
- '[[sqli]]'
- '[[SQLMap]]'
- '[[Web Applications]]'
commands:
- '[[SQLMap on URL Parameter]]'
---

# Identifying SQL Injection Using SQLmap

**Status**: ✓ Verified

## Summary

SQL injection tests are automated using SQLMap tool. SQLMap is pre-installed in Kali Linux. 

## Description

# Description

SQL injection tests are automated using SQLMap tool. SQLMap is pre-installed in Kali Linux.

# Instructions

# 

1. Any URL with parameter that accepts input can be used with SQLMap. In the following screenshot, *term* parameter in the URL is found to be vulnerable and payload that is successfully executed is listed at the end.

**Command** ([[SQLMap on URL Parameter]]):

```bash
sqlmap -u http://$_Target_URL
```

# 

## Platforms

- Web

## Commands Used

- [[SQLMap on URL Parameter]]

## Tags

- [[injection]]
- [[owasp]]
- [[owasp top 10]]
- [[SQL]]
- [[sqli]]
- [[SQLMap]]
- [[Web Applications]]
