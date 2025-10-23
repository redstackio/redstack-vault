---
id: 278f4fb0-5909-4764-9f60-59b5661a6409
name: HTTP/2 Request Smuggling
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:32.048180+00:00'
updated_at: '2023-04-10T20:23:23.524855+00:00'
tactics:
- '[[Impact|TA0040 - Impact]]'
techniques:
- '[[System Shutdown/Reboot|T1529 - System Shutdown/Reboot]]'
tags:
- '[[HTTP/2 Request Smuggling]]'
- '[[Request Smuggling]]'
---

# HTTP/2 Request Smuggling

## Summary

HTTP/2 Request Smuggling is a technique that allows an attacker to bypass security controls and smuggle an HTTP request to the back-end server. This technique is possible due to the way HTTP/2 handles requests and responses. By manipulating the headers of the HTTP requests, an attacker can send mul

## Description

# Description

HTTP/2 Request Smuggling is a technique that allows an attacker to bypass security controls and smuggle an HTTP request to the back-end server. This technique is possible due to the way HTTP/2 handles requests and responses. By manipulating the headers of the HTTP requests, an attacker can send multiple requests in a single connection, leading to a misinterpretation of the request by the back-end server. This technique can be used to bypass security controls, such as firewalls, and gain unauthorized access to sensitive data.

Technical Explanation: HTTP/2 allows multiple requests to be sent over a single connection, using a technique called multiplexing. When a client sends multiple requests, the server may receive them in a different order than they were sent. This can lead to a misinterpretation of the request by the back-end server. An attacker can exploit this behavior by sending a request with a malformed header, causing the back-end server to interpret the subsequent request in a different way than intended.

Business Value: An attacker can use HTTP/2 Request Smuggling to bypass security controls and gain unauthorized access to sensitive data. This can lead to data theft, financial loss, and reputational damage to the organization.

 

## Requirements

1. Access to a vulnerable HTTP/2 server

1. Knowledge of HTTP/2 Request Smuggling techniques

 

## Defense

1. Implement strict input validation on the server side

1. Use a Web Application Firewall (WAF) to detect and block HTTP/2 Request Smuggling attacks

1. Regularly update and patch the HTTP/2 server to address known vulnerabilities

 

## Objectives

1. Bypass security controls

1. Gain unauthorized access to sensitive data

 

# Instructions

1. Send an HTTP GET request to www.example.com with the specified headers and path.

 



**Code**: [[:method GET
:path /
:authority www.example.com
hea]]



> The command sends an HTTP GET request to the specified host and path with the specified headers. The :method field specifies the HTTP method used, in this case GET. The :path field specifies the path of the resource being requested, in this case the root directory. The :authority field specifies the host name of the server being requested. The 'Host' header specifies the same information as the :authority field. The 'header ignored' field can be ignored. This command can be used to retrieve information from a web server.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact|TA0040 - Impact]]

### Techniques

- [[System Shutdown/Reboot|T1529 - System Shutdown/Reboot]]

## Tags

- [[HTTP/2 Request Smuggling]]
- [[Request Smuggling]]


