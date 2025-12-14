---
id: cmd-uuid-001
data: >-
  GET /static/javascripts/vendor/bugsnag.v7.4.0.min.js HTTP/1.1

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
  - cdn-request
type: command
output: |-
  HTTP/1.1 200 OK
  Content-Type: application/javascript

  [JavaScript file content]
executor: http
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:56.667Z'
verified: false
validated: true
submitted: true
---
# Legitimate-GET-Request-to-CDN-File

## Command

```http
GET /static/javascripts/vendor/bugsnag.v7.4.0.min.js HTTP/1.1
Host: cdn.shopify.com
Connection: close
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
```

## Description

This HTTP GET request fetches a static JavaScript file from Shopify's CDN using standard browser headers. Use it to demonstrate normal access before modification in cache poisoning attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Host | Target domain (cdn.shopify.com) | Yes |
| User-Agent | Client browser identifier | Yes |
| Accept | Accepted content types | Yes |
| Path | File path with forward slashes | Yes |

## Examples

### Basic Usage

```http
GET /static/javascripts/vendor/bugsnag.v7.4.0.min.js HTTP/1.1
Host: cdn.shopify.com
...
```

### With Cache Buster

```http
GET /static/javascripts/vendor/bugsnag.v7.4.0.min.js?cachebuster=123 HTTP/1.1
Host: cdn.shopify.com
...
```

## Expected Output

Successful 200 OK response with the JavaScript file content in the body.

## Related

- [[commands/Modified-GET-Request-with-Backslashes-and-Cache-Buster]]
- [[procedures/Intercept-Legitimate-CDN-Request-with-Burp-Suite]]
