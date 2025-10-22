---
id: 21f61f29-b656-4dd7-a4d3-fdc25dad16f8
name: Nmap Command to Identify SSL Certificate Details
type: procedure
verified: true
submitted: true
created_at: '2020-09-03T14:48:30.714326+00:00'
updated_at: '2023-05-26T18:51:20.333157+00:00'
platforms:
- Web
tags:
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[SSL]]'
- '[[Web Applications]]'
commands:
- '[[Nmap Command to Identify SSL Certificate Details]]'
---

# Nmap Command to Identify SSL Certificate Details

**Status**: ✓ Verified

## Summary

SSL/TLS implementation enables secure communication between client and server. SSL/TLS certificate details like issuer, subject, supported algorithms can be obtained using Nmap ssl-cert script. 

## Description

# Description

SSL/TLS implementation enables secure communication between client and server. SSL/TLS certificate details like issuer, subject, supported algorithms can be obtained using Nmap *ssl-cert* script.

# Procedure

1. Nmap *ssl-cert *script is used to obtain the SSL/TLS certificate details.

**Command** ([[Nmap Command to Identify SSL Certificate Details]]):

```bash
nmap --script ssl-cert demo.testfire.net -p443
```

2. Output contain the details about subject, issuer, signature algorithm, validity etc.

## Platforms

- Web

## Commands Used

- [[Nmap Command to Identify SSL Certificate Details]]

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[SSL]]
- [[Web Applications]]
