---
id: cmd-curl-obfuscated-ip-redirect
data: 'curl -L -I "http://uber.com//3627735502/calendar"'
tags:
  - phishing
  - obfuscation
type: command
output: |-
  HTTP/1.1 301 Moved Permanently
  Location: https://calendar.google.com/...
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:26.858Z'
verified: false
validated: true
submitted: true
---
# curl-obfuscated-ip-redirect

## Command

```bash
curl -L -I "http://uber.com//3627735502/calendar"
```

## Description

Verifies redirect using decimal-obfuscated IP on Uber.com for phishing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-L` | Follow redirects | Yes |
| `-I` | Headers | Yes |
| URL | Decimal IP URL | Yes |

## Examples

### Basic Usage

```bash
curl -L -I "http://uber.com//3627735502/calendar"
```

## Expected Output

Successful redirect to obfuscated target.

## Related

- [[Related Procedure: Obfuscate-IP-for-Phishing]]
