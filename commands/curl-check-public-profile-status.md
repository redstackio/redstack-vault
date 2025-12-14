---
data: 'curl -Is https://liberapay.com/Liberapay/charts.json?callback=rip | head -1'
tags:
  - recon
  - http-status
type: command
output: HTTP/2 200
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:13.221Z'
id: 905e5682-c6d7-4191-bc0c-a1dc5e9e1b52
verified: false
validated: true
submitted: true
---
# curl-check-public-profile-status

## Command

```bash
curl -Is https://liberapay.com/Liberapay/charts.json?callback=rip | head -1
```

## Description

This command checks the HTTP status of a public Liberapay profile's JSONP endpoint without authentication, verifying successful access with a 200 OK response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I` | Fetch headers only | Yes |
| `-s` | Silent mode (no progress meter) | Yes |
| `https://liberapay.com/Liberapay/charts.json?callback=rip` | Target public endpoint with JSONP callback | Yes |
| `| head -1` | Pipe to show only the first line (status) | Yes |

## Examples

### Basic Usage

```bash
curl -Is https://liberapay.com/Liberapay/charts.json?callback=rip | head -1
```

### Advanced Usage

```bash
curl -Is -H "User-Agent: Mozilla/5.0" https://liberapay.com/Liberapay/charts.json?callback=rip | head -1
```

## Expected Output

HTTP/2 200 

This confirms public profiles are accessible unauthenticated, contrasting the private bypass.

## Related

- [[commands/curl-check-private-profile-status]]
