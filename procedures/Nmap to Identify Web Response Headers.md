---
id: 918bd23b-4f51-4bf1-b5e4-99c53eb27eb4
name: Nmap to Identify Web Response Headers
type: procedure
verified: true
submitted: true
created_at: '2020-08-31T19:08:46.868113+00:00'
updated_at: '2023-05-26T15:57:43.937610+00:00'
platforms:
- Web
tags:
- '[[HTTP Headers]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
commands:
- '[[Nmap Command to Find Response Headers]]'
---

# Nmap to Identify Web Response Headers

**Status**: ✓ Verified

## Summary

Web headers will reveal web technologies used, version details etc. http-headers nmap script will reveal the HTTP response headers. 

## Description

# Description



Web headers will reveal web technologies used, version details etc. *http-headers *nmap script will reveal the HTTP response headers.



# Procedure



1. Following nmap command can be used to identify the web response headers on a website.







**Command** ([[Nmap Command to Find Response Headers]]):

```bash
nmap -sV --script=http-headers 192.168.1.11
```





## Platforms

- Web

## Commands Used

- [[Nmap Command to Find Response Headers]]

## Tags

- [[HTTP Headers]]
- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]


