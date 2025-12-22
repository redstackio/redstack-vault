---
id: cmd-uuid-1
data: >-
  curl -H "Origin: http://evil.com" -I https://client.amplifi.com | grep
  Access-Control-Allow-Origin
tags:
  - cors
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:17.643Z'
verified: false
validated: true
submitted: true
---
# curl-check-cors-headers

## Command

```bash
curl -H "Origin: http://evil.com" -I https://client.amplifi.com | grep Access-Control-Allow-Origin
```

## Description

This command uses curl to send a HEAD request with a fake Origin header to a target URL, then greps for the Access-Control-Allow-Origin response header to check for CORS misconfigurations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Origin: http://evil.com"` | Sets a custom Origin header to simulate cross-origin request | Yes |
| `-I` | Performs a HEAD request to fetch headers only | Yes |
| `https://client.amplifi.com` | Target URL to test | Yes |
| `| grep Access-Control-Allow-Origin` | Filters output to show only the relevant header | Yes |

## Examples

### Basic Usage

```bash
curl -H "Origin: http://evil.com" -I https://client.amplifi.com | grep Access-Control-Allow-Origin
```

### Advanced Usage

```bash
curl -H "Origin: http://evil.com" -H "Access-Control-Request-Method: GET" -X OPTIONS -I https://protect.ubnt.com | grep -i access-control
```

## Expected Output

Access-Control-Allow-Origin: http://evil.com (or *) indicating permissive policy, or no match if restricted.

## Related

- [[Related Procedure: Identify-CORS-Misconfiguration]]
