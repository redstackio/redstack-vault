---
data: 'curl -Is https://liberapay.com/EdOverflow/charts.json?callback=rip | head -1'
tags:
  - recon
  - http-status
type: command
output: HTTP/2 403
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:13.223Z'
id: 25a4bca4-cbc4-4d50-9ae3-68326e552c0b
verified: false
validated: true
submitted: true
---
# curl-check-private-profile-status

## Command

```bash
curl -Is https://liberapay.com/EdOverflow/charts.json?callback=rip | head -1
```

## Description

This command checks the HTTP status of a private Liberapay profile's JSONP endpoint without authentication, verifying that privacy settings return a 403 Forbidden response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I` | Fetch headers only | Yes |
| `-s` | Silent mode (no progress meter) | Yes |
| `https://liberapay.com/EdOverflow/charts.json?callback=rip` | Target private endpoint with JSONP callback | Yes |
| `| head -1` | Pipe to show only the first line (status) | Yes |

## Examples

### Basic Usage

```bash
curl -Is https://liberapay.com/EdOverflow/charts.json?callback=rip | head -1
```

### Advanced Usage

```bash
curl -Is --cookie "session=invalid" https://liberapay.com/EdOverflow/charts.json?callback=rip | head -1
```

## Expected Output

HTTP/2 403 

This indicates the privacy check blocks unauthenticated access to private donation data.

## Related

- [[commands/curl-check-public-profile-status]]
