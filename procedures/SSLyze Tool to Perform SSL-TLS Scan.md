---
id: 3e4f1bfb-c209-407a-9f02-5cd38a8909a1
name: SSLyze Tool to Perform SSL/TLS Scan
type: procedure
verified: true
submitted: true
created_at: '2020-09-03T13:49:07.614494+00:00'
updated_at: '2023-05-26T18:22:32.819104+00:00'
platforms:
- Web
tags:
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[SSL]]'
- '[[Web Applications]]'
commands:
- '[[SSLyze Command to Scan a Website]]'
---

# SSLyze Tool to Perform SSL/TLS Scan

**Status**: ✓ Verified

## Summary

SSL/TLS implementation enables secure communication between client and server. Any misconfiguration in the SSL/TLS implementation can be identified using the SSLyze tool. 

## Description

# Description

SSL/TLS implementation enables secure communication between client and server. Any misconfiguration in the SSL/TLS implementation can be identified using the SSLyze tool.



# Procedure



1. Use the below SSLyze command to scan the website and analyse the implementation of SSL/TLS.







**Command** ([[SSLyze Command to Scan a Website]]):

```bash
sslyze --regular demo.testfire.net:443
```





2. Output reveals enabled ciphers, certificate details etc. Certificate trust can also be identified using the SSLyze tool.



## Platforms

- Web

## Commands Used

- [[SSLyze Command to Scan a Website]]

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[SSL]]
- [[Web Applications]]


