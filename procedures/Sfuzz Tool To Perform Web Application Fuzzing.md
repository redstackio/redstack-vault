---
id: 7da9d61d-c0af-43a9-b673-a210c0c47d82
name: Sfuzz Tool To Perform Web Application Fuzzing
type: procedure
verified: true
submitted: true
created_at: '2020-09-03T17:39:57.892018+00:00'
updated_at: '2023-05-26T18:07:06.522412+00:00'
platforms:
- Web
tags:
- '[[Fuzz]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
commands:
- '[[Sfuzz Command to Fuzz the Web Application]]'
---

# Sfuzz Tool To Perform Web Application Fuzzing

**Status**: ✓ Verified

## Summary

Fuzzing is a process to identify unknown or unidentified vulnerabilities. Sfuzz is a simple fuzzer that can be used to perform fuzzing on web applications. 

## Description

# Description

Fuzzing is a process to identify unknown or unidentified vulnerabilities. Sfuzz is a simple fuzzer that can be used to perform fuzzing on web applications.

# Procedure

1. The below Sfuzz tool command can be used to perform fuzzing on the application.

**Command** ([[Sfuzz Command to Fuzz the Web Application]]):

```bash
sfuzz -S 192.168.1.5 -p 80 -T -f /usr/share/sfuzz-db/basic.http
```

2. The above output contains two fuzzed instances and the response from the application.

## Platforms

- Web

## Commands Used

- [[Sfuzz Command to Fuzz the Web Application]]

## Tags

- [[Fuzz]]
- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]
