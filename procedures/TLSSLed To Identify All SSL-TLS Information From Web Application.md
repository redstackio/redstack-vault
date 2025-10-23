---
id: e6cf3310-ce05-4839-ab91-b1d24932eb55
name: TLSSLed To Identify All SSL/TLS Information From Web Application
type: procedure
verified: true
submitted: true
created_at: '2020-09-03T15:26:43.807515+00:00'
updated_at: '2023-05-26T18:51:59.389838+00:00'
platforms:
- Web
tags:
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[SSL]]'
- '[[TLS]]'
- '[[Web Applications]]'
commands:
- '[[TLSSLed Command]]'
---

# TLSSLed To Identify All SSL/TLS Information From Web Application

**Status**: ✓ Verified

## Summary

SSL/TLS implementation enables secure communication between client and server. All SSL/TLS information like versions, HSTS header, secure flag on cookie etc. can be identified using the TLSSLed tool. 

## Description

# Description



SSL/TLS implementation enables secure communication between client and server. All SSL/TLS information like versions, HSTS header, secure flag on cookie etc. can be identified using the TLSSLed tool.



# Procedure





1. Below TLSSLed command can be used to scan the host on specific port to obtain SSL/TLS details.







**Command** ([[TLSSLed Command]]):

```bash
tlssled  65.61.137.117 443
```







2. Output contains supported TLS versions, certificate validity, secure flags on cookies, HSTS configuration etc.



## Platforms

- Web

## Commands Used

- [[TLSSLed Command]]

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[SSL]]
- [[TLS]]
- [[Web Applications]]


