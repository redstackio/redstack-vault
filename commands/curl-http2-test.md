---
id: cmd-uuid-4
data: 'curl --http2 https://localhost:3000 -I'
tags:
  - test
  - http2
type: command
output: HTTP/2 200
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:30.657Z'
verified: false
validated: true
submitted: true
---
# curl-http2-test

## Command

```bash
curl --http2 https://localhost:3000 -I
```

## Description

Tests HTTP/2 connectivity to the server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--http2` | Enable HTTP/2 | Yes |
| `-I` | HEAD request only | Yes |

## Examples

### Basic Usage

```bash
curl --http2 https://localhost:3000 -I
```

## Expected Output

HTTP/2 response headers indicating successful connection.

## Related

- [[procedures/Start-Node-js-HTTP2-Server]]
