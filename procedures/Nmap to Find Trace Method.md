---
id: e585edc6-c42a-45d5-b980-3fb9daeaa5e5
name: Nmap to Find Trace Method
type: procedure
verified: true
submitted: true
created_at: '2020-09-01T16:56:54.548865+00:00'
updated_at: '2023-05-26T01:12:32.342153+00:00'
platforms:
- Web
tags:
- '[[HTTP Methods]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Trace Method]]'
- '[[Web Applications]]'
commands:
- '[[Nmap Command to Find Trace Method]]'
---

# Nmap to Find Trace Method

**Status**: ✓ Verified

## Summary

Nmap tool can be used to identify HTTP methods that are enabled on the server. http-script is used to find if trace method is enabled. 

## Description

# Description

Nmap tool can be used to identify HTTP methods that are enabled on the server. *http-script *is used to find if trace method is enabled.



# Procedure



1. The below Nmap command and script can be used to find if trace method is enabled on the server.







**Command** ([[Nmap Command to Find Trace Method]]):

```bash
nmap --script http-trace -p80 192.168.1.3
```







## Platforms

- Web

## Commands Used

- [[Nmap Command to Find Trace Method]]

## Tags

- [[HTTP Methods]]
- [[owasp]]
- [[owasp top 10]]
- [[Trace Method]]
- [[Web Applications]]


