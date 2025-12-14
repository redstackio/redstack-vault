---
id: cmd-curl-test
data: curl -I $URL
tags:
  - web
  - test
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:10.567Z'
verified: false
validated: true
submitted: true
---
# curl-test-host

## Command

```bash
curl -I $URL
```

## Description

Tests if arbitrary content is hosted successfully on the subdomain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I` | Head request | Yes |
| `$URL` | Subdomain URL | Yes |

## Examples

### Basic Usage

```bash
curl -I https://vulnerable-subdomain.mozgcp.net
```

## Expected Output

HTTP 200 OK with server headers.

## Related

- [[Related Procedure: Host Arbitrary Content on Subdomain]]
