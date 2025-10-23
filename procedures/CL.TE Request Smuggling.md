---
id: a65b54fa-786b-4643-b643-c76457d0df48
name: CL.TE Request Smuggling
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:31.953452+00:00'
updated_at: '2023-04-10T20:23:23.926815+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Forge Web Credentials|T1606 - Forge Web Credentials]]'
- '[[System Service Discovery|T1007 - System Service Discovery]]'
tags:
- '[[About CL.TE | TE.CL Vulnerabilities]]'
- '[[Request Smuggling]]'
commands:
- '[[Introduction]]'
---

# CL.TE Request Smuggling

## Summary

CL.TE Request Smuggling is a technique that can be used to bypass security controls and smuggle malicious requests into a web application. The technique leverages a combination of the CL.TE and TE.CL vulnerabilities to manipulate the way that a web server processes HTTP requests. This can result in

## Description

# Description

CL.TE Request Smuggling is a technique that can be used to bypass security controls and smuggle malicious requests into a web application. The technique leverages a combination of the CL.TE and TE.CL vulnerabilities to manipulate the way that a web server processes HTTP requests. This can result in an attacker being able to perform actions that they should not be authorized to do, such as accessing sensitive data or executing commands on the server. 

Technical Explanation: CL.TE Request Smuggling involves sending a specially crafted HTTP request to a web server that has both the CL.TE and TE.CL vulnerabilities. The request is manipulated in such a way that the web server processes it differently than intended, allowing the attacker to bypass security controls and send malicious requests to the server. 

Business Value: An attacker can use CL.TE Request Smuggling to gain unauthorized access to sensitive information or execute commands on a server, which can lead to significant financial and reputational damage for a business.

 

## Requirements

1. Access to a web application that has both the CL.TE and TE.CL vulnerabilities

 

## Defense

1. Implement strict input validation and sanitization to prevent malicious input from being processed

1. Implement secure coding practices to prevent vulnerabilities like CL.TE and TE.CL from being introduced into web applications

1. Implement a web application firewall (WAF) that can detect and block CL.TE Request Smuggling attacks

 

## Objectives

1. To bypass security controls and smuggle malicious requests into a web application

1. To gain unauthorized access to sensitive information or execute commands on a server

 

# Instructions

1. To calculate the chunk size for the second request in TE.CL vulnerability, follow these steps:
1. Calculate the length of the first request body.
2. Calculate the length of the second request body.
3. Subtract the length of the first request body from the length of the second request body.
4. Add the length of the chunk extension (which is 5 for TE.CL vulnerability).
5. The resulting value is the chunk size for the second request.

 



**Code**: [[Manually fixing the length fields in request smugg]]



> In TE.CL vulnerability, the attacker sends a request with Transfer-Encoding: chunked header and a chunk size that is less than the actual size of the request body, causing the server to wait for more data that will never arrive. The attacker then sends a second request with a Content-Length header that is less than the actual size of the request body. This causes the second request body to be interpreted as a chunk of the first request body, resulting in request smuggling. To calculate the chunk size for the second request, the length of the first and second request bodies must be known, along with the length of the chunk extension (which is 5 for TE.CL vulnerability). This calculation allows the attacker to craft a second request that will be interpreted as a separate request by the server, allowing them to smuggle their payload.



**Command** ([[Introduction]]):

```bash
Manually fixing the length fields in request smuggling attacks can be tricky.
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Forge Web Credentials|T1606 - Forge Web Credentials]]
- [[System Service Discovery|T1007 - System Service Discovery]]

## Commands Used

- [[Introduction]]

## Tags

- [[About CL.TE | TE.CL Vulnerabilities]]
- [[Request Smuggling]]


