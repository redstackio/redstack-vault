---
id: 9bbc637e-7c86-4276-9ef9-82511b366a9d
name: Using Nikto to Find Common Web Vulnerabilities
type: procedure
verified: true
submitted: true
created_at: '2020-08-19T16:08:59.051053+00:00'
updated_at: '2023-05-26T18:10:40.891006+00:00'
platforms:
- Web
tags:
- '[[owasp]]'
- '[[Vulnerability Scanning]]'
- '[[Web Applications]]'
commands:
- '[[Nikto Command to Scan an Application]]'
---

# Using Nikto to Find Common Web Vulnerabilities

**Status**: ✓ Verified

## Summary

Nikto tool can be used to identify common web vulnerabilities. 

## Description

# Description

Nikto tool can be used to identify common web vulnerabilities. 

# Procedure

1. Use the below Nikto command to scan an application and list common web application vulnerabilities.

**Command** ([[Nikto Command to Scan an Application]]):

```bash
nikto -h http://192.168.43.68/vcart/login.php
```

## Platforms

- Web

## Commands Used

- [[Nikto Command to Scan an Application]]

## Tags

- [[owasp]]
- [[Vulnerability Scanning]]
- [[Web Applications]]
