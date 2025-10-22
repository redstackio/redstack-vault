---
id: b7945f0d-8999-42b9-9ad2-86ad2e06ae3a
name: CRLF Injection and Cookie Stealing
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:54.861560+00:00'
updated_at: '2023-04-06T03:55:54.874644+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Subvert Trust Controls|T1553 - Subvert Trust Controls]]'
sub_techniques:
- '[[Code Signing|T1553.002 - Code Signing]]'
tags:
- '[[Carriage Return Line Feed]]'
- '[[CRLF - Add a cookie]]'
commands:
- '[[Check for Injection Vulnerability]]'
---

# CRLF Injection and Cookie Stealing

## Summary

CRLF Injection is an attack that abuses the line breaks in HTTP headers and can be used to inject malicious headers, steal cookies, and perform other attacks. By adding a CRLF sequence (%0D%0A) to the end of a parameter value, an attacker can inject additional headers and manipulate the response. I

## Description

# Description

CRLF Injection is an attack that abuses the line breaks in HTTP headers and can be used to inject malicious headers, steal cookies, and perform other attacks. By adding a CRLF sequence (%0D%0A) to the end of a parameter value, an attacker can inject additional headers and manipulate the response. In this case, the attacker adds a cookie to the response header and steals the user's session information. This technique can be used to bypass authentication, perform session hijacking, and gain unauthorized access to sensitive information.

## Requirements

1. Access to a vulnerable web application

## Defense

1. Implement input validation to prevent CRLF injection attacks

1. Use secure session management techniques, such as HttpOnly and Secure flags, to protect session information

1. Monitor network traffic for unusual activity and behavior

## Objectives

1. Inject a malicious cookie into the response header

1. Steal the user's session information

# Instructions

1. Send an HTTP request to the vulnerable web application with a CRLF sequence (%0D%0A) followed by a Set-Cookie header to inject a malicious cookie into the response header.

**Code**: [[http://www.example.net/%0D%0ASet-Cookie:mycookie=m]]

> The %0D%0A sequence represents the CRLF sequence, which is added to the end of the URL to inject a new line character into the request. The Set-Cookie header is used to add a new cookie to the response header and steal the user's session information.

2. Capture the response from the vulnerable web application with a CRLF sequence (%0D%0A) followed by a Set-Cookie header to steal the user's session information.

**Code**: [[Connection: keep-alive
Content-Length: 178
Content]]

> The response header includes the injected Set-Cookie header, which contains the stolen session information. The attacker can use this information to impersonate the user and gain unauthorized access to sensitive information.

**Command** ([[Check for Injection Vulnerability]]):

```bash
Connection: keep-alive
Content-Length: 178
Content-Type: text/html
Date: Mon, 09 May 2016 14:47:29 GMT
Location: https://www.example.net/[INJECTION STARTS HERE]
Set-Cookie: mycookie=myvalue
X-Frame-Options: SAMEORIGIN
X-Sucuri-ID: 15016
x-content-type-options: nosniff
x-xss-protection: 1; mode=block
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Subvert Trust Controls|T1553 - Subvert Trust Controls]]

### Sub-Techniques

- [[Code Signing|T1553.002 - Code Signing]]

## Commands Used

- [[Check for Injection Vulnerability]]

## Tags

- [[Carriage Return Line Feed]]
- [[CRLF - Add a cookie]]
