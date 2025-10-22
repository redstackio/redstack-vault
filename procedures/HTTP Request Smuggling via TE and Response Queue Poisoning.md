---
id: c1c2acc7-00d3-4119-8684-92ac29846fab
name: HTTP Request Smuggling via TE and Response Queue Poisoning
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:32.067584+00:00'
updated_at: '2023-04-10T20:23:25.015185+00:00'
tags:
- '[[Client-side desync]]'
- '[[Request Smuggling]]'
---

# HTTP Request Smuggling via TE and Response Queue Poisoning

## Summary

HTTP Request Smuggling via TE and Response Queue Poisoning is a technique used to exploit a vulnerability in the way HTTP requests are processed by certain web servers. This technique involves sending specially crafted HTTP requests that can bypass security mechanisms and cause client-side desynchr

## Description

# Description

HTTP Request Smuggling via TE and Response Queue Poisoning is a technique used to exploit a vulnerability in the way HTTP requests are processed by certain web servers. This technique involves sending specially crafted HTTP requests that can bypass security mechanisms and cause client-side desynchronization. This can lead to a range of attacks, including session hijacking, data tampering, and unauthorized access to sensitive information.

Technical Explanation: HTTP Request Smuggling is a technique that involves manipulating the way HTTP requests are processed by a web server. By exploiting a vulnerability in the way the server handles requests, an attacker can send specially crafted requests that can bypass security mechanisms and cause client-side desynchronization. This can lead to a range of attacks, including session hijacking, data tampering, and unauthorized access to sensitive information.

Business Value: HTTP Request Smuggling via TE and Response Queue Poisoning can be used by attackers to gain unauthorized access to sensitive information, steal user credentials, and compromise the integrity of web applications. This can lead to reputational damage, loss of revenue, and legal liabilities for organizations.

## Requirements

1. Access to the target web server

1. Knowledge of the target web server's vulnerabilities

1. Ability to send specially crafted HTTP requests

## Defense

1. Implement strict input validation to prevent injection attacks

1. Configure web servers to reject malformed requests

1. Regularly update web servers and applications to patch known vulnerabilities

## Objectives

1. To gain unauthorized access to sensitive information

1. To steal user credentials

1. To compromise the integrity of web applications

# Instructions

1. To perform HTTP Request Smuggling via TE and Response Queue Poisoning, follow the below steps:
1. Send a POST request with Transfer-Encoding: chunked and a chunk size of 0, followed by a GET request with Connection: keep-alive and Transfer-Encoding: chunked headers.
2. The server will queue the GET request, waiting for the next chunk to complete the previous request.
3. Send another POST request with Transfer-Encoding: chunked and a chunk size of 0, followed by a chunk with the value of TE: trailers and Connection: close headers.
4. The server will interpret the chunk with TE: trailers as the end of the previous request and send the queued GET request with the injected headers.
5. The server will then interpret the chunk with Connection: close as the end of the second POST request, closing the connection and preventing the client from receiving the server's response.
6. The client can now assume the response is poisoned and carry out further attacks.

This command exploits a vulnerability in the way that some web servers handle HTTP requests with Transfer-Encoding: chunked headers. By sending a specially crafted sequence of requests, an attacker can smuggle a request through to the server that appears to be part of the previous request. This can be used to bypass security measures and carry out further attacks, such as injecting malicious code into the server's response. The name of this command reflects its purpose, which is to carry out HTTP Request Smuggling via TE and Response Queue Poisoning.

2. To send a POST request to example.com, use the fetch() method with the appropriate URL and parameters. Make sure to include the 'method' parameter set to 'POST', the 'body' parameter set to the appropriate data, and the 'mode' parameter set to 'no-cors'. Also include the 'credentials' parameter set to 'include' if necessary.

**Code**: [[fetch('https://www.example.com/', {method: 'POST',]]

> The fetch() method is used to send HTTP requests to a server and receive a response. In this case, we are sending a POST request to example.com. The 'method' parameter specifies the type of request we are sending, in this case it is 'POST'. The 'body' parameter is used to specify the data we are sending with the request. In this example, we are sending a GET request as the body data. The 'mode' parameter is used to specify the mode of the request, in this case it is 'no-cors'. The 'credentials' parameter is used to specify whether or not to include credentials such as cookies with the request. Once the request is sent, the server will respond with a corresponding response.

## Tags

- [[Client-side desync]]
- [[Request Smuggling]]
