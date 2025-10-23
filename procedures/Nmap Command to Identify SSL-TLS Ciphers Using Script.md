---
id: 9b23c626-bf63-4bfc-8687-c8291dda967c
name: Nmap Command to Identify SSL/TLS Ciphers Using Script
type: procedure
verified: true
submitted: true
created_at: '2020-09-03T14:25:24.589585+00:00'
updated_at: '2023-05-26T18:52:13.527834+00:00'
platforms:
- Web
tags:
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[SSL]]'
- '[[Web Applications]]'
commands:
- '[[Nmap Command to Identify SSL/TLS Ciphers Using ssl-enum-ciphers Script]]'
---

# Nmap Command to Identify SSL/TLS Ciphers Using Script

**Status**: ✓ Verified

## Summary

SSL/TLS implementation enables secure communication between client and server. Any misconfiguration in the SSL/TLS implementation can be identified using the Nmap command and SSL Enum Ciphers script. 

## Description

# Description



SSL/TLS implementation enables secure communication between client and server. Any misconfiguration in the SSL/TLS implementation can be identified using the Nmap command and SSL Enum Ciphers script.



# Procedure



1. Use the below Nmap command with SSL Enum Ciphers script to scan the website and analyse the implementation of SSL/TLS.







**Command** ([[Nmap Command to Identify SSL/TLS Ciphers Using ssl-enum-ciphers Script]]):

```bash
nmap --script ssl-enum-ciphers demo.testfire.net:443
```





2. Output contains the supported TLS versions and ciphers.



## Platforms

- Web

## Commands Used

- [[Nmap Command to Identify SSL/TLS Ciphers Using ssl-enum-ciphers Script]]

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[SSL]]
- [[Web Applications]]


