---
id: ae315cde-422c-46d4-b83d-b55bba152ff4
name: TE.CL Request Smuggling
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:31.998363+00:00'
updated_at: '2023-04-10T20:23:25.406174+00:00'
tags:
- '[[Request Smuggling]]'
- '[[TE.CL vulnerabilities]]'
commands:
- '[[HTTP Request Smuggling]]'
---

# TE.CL Request Smuggling

## Summary

HTTP Request Smuggling is a technique that exploits the discrepancy in parsing HTTP requests between two or more systems. TE.CL vulnerabilities are a type of Request Smuggling attack that occur when a server receives multiple requests with different Content-Length and Transfer-Encoding headers. Thi

## Description

# Description

HTTP Request Smuggling is a technique that exploits the discrepancy in parsing HTTP requests between two or more systems. TE.CL vulnerabilities are a type of Request Smuggling attack that occur when a server receives multiple requests with different Content-Length and Transfer-Encoding headers. This can cause the server to interpret the requests incorrectly, leading to cache poisoning, session hijacking, and other attacks. Attackers can use this technique to bypass security controls, steal sensitive information, and compromise the target system.

Technical Explanation: TE.CL vulnerabilities occur when a server receives two or more requests with different Content-Length and Transfer-Encoding headers. The server may interpret the requests incorrectly, leading to cache poisoning, session hijacking, and other attacks. Attackers can use this technique to bypass security controls, steal sensitive information, and compromise the target system.

Business Value: TE.CL Request Smuggling can be used by attackers to gain unauthorized access to sensitive information, bypass security controls, and compromise the target system. This can result in reputational damage, financial loss, and legal liability for the affected organization.

## Requirements

1. Access to the target system

1. Knowledge of the target system's vulnerabilities

1. HTTP Request Smuggling tools

## Defense

1. Configure the server to reject requests with mismatched Content-Length and Transfer-Encoding headers

1. Use a Web Application Firewall (WAF) to detect and block Request Smuggling attacks

1. Regularly scan the target system for vulnerabilities and apply security patches as needed

## Objectives

1. Bypass security controls

1. Steal sensitive information

1. Compromise the target system

# Instructions

1. To perform a basic request smuggling attack, you need to send two requests that are interpreted as a single request by the server. The first request should have a Content-Length header, while the second request should have a Transfer-Encoding: chunked header. The body of the first request should contain the length of the second request's body in hexadecimal format, followed by a newline character and the second request's body. This will cause the server to read the body of the second request as part of the first request, resulting in a request smuggling attack.

**Code**: [[POST / HTTP/1.1
Host: vulnerable-website.com
Conte]]

> The provided data is an example of a basic request smuggling attack. The attack is performed by sending two requests that are interpreted as a single request by the server. The first request has a Content-Length header, which tells the server how many bytes are in the request body. The second request has a Transfer-Encoding: chunked header, which tells the server that the request body is split into chunks, each with its own size specified in hexadecimal format followed by a newline character. The body of the first request contains the length of the second request's body in hexadecimal format, followed by a newline character and the second request's body. This causes the server to read the body of the second request as part of the first request, resulting in a request smuggling attack.

**Command** ([[HTTP Request Smuggling]]):

```bash
POST / HTTP/1.1
Host: vulnerable-website.com
Content-Length: 3
Transfer-Encoding: chunked

8
SMUGGLED
0
```

2. To make an HTTP POST request, use the following command:

**Code**: [[POST / HTTP/1.1
Host: domain.example.com
User-Agen]]

> This command sends a POST request to the specified domain (domain.example.com) with the specified User-Agent header and Content-Type of application/x-www-form-urlencoded. The request body contains a single parameter 'x' with a value of 1. The Content-Length header specifies the length of the request body in bytes. The Accept-Encoding header specifies that the client can handle gzip and deflate encoding. The server response is not included in this command.

## Commands Used

- [[HTTP Request Smuggling]]

## Tags

- [[Request Smuggling]]
- [[TE.CL vulnerabilities]]
