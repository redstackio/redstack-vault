---
id: 8d4fe9d6-1762-4539-bd8b-c9aa93353ffe
name: HTTP Methods Enumeration
type: procedure
verified: true
submitted: true
created_at: '2020-07-19T06:50:16.874055+00:00'
updated_at: '2023-05-26T01:01:23.081346+00:00'
platforms:
- Web
tags:
- '[[Enumeration]]'
- '[[misconfiguration]]'
- '[[Web Applications]]'
commands:
- '[[Netcat Command]]'
- '[[Nmap HTTP Methods Script]]'
---

# HTTP Methods Enumeration

**Status**: ✓ Verified

## Summary

Enumeration of HTTP methods will help in identifying allowed methods on the web server. The list can be used to find insecure methods like PUT, DELETE, TRACE/TRACK, OPTIONS. These insecure methods can be leveraged by an attacker to perform attacks like Cross-Site Tracing (XST), Create/Delete resour

## Description

# Description

Enumeration of HTTP methods will help in identifying allowed methods on the web server. The list can be used to find insecure methods like PUT, DELETE, TRACE/TRACK, OPTIONS. These insecure methods can be leveraged by an attacker to perform attacks like Cross-Site Tracing (XST), Create/Delete resources on the web server etc.



# Instructions

## Method 1

Nmap HTTP methods script can be used to enumerate the allowed methods





**Command** ([[Nmap HTTP Methods Script]]):

```bash
nmap --script http-methods demo.testfire.net
```





## Method 2

Using Netcat command to connect to the web server and requesting the OPTIONS method will list the allowed methods





**Command** ([[Netcat Command]]):

```bash
nc demo.testfire.net 80
OPTIONS / HTTP/1.1
Host: demo.testfire.net
```





## Platforms

- Web

## Commands Used

- [[Netcat Command]]
- [[Nmap HTTP Methods Script]]

## Tags

- [[Enumeration]]
- [[misconfiguration]]
- [[Web Applications]]


