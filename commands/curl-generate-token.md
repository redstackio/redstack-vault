---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
data: 'curl -H "X-Forwarded-For: 192.168.1.100" http://localhost/generate-token.php'
tags:
  - web
  - proxy
  - csrf
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:27:03.272Z'
verified: false
validated: true
submitted: true
---
# curl-generate-token

## Command

```bash
curl -H "X-Forwarded-For: 192.168.1.100" http://localhost/generate-token.php
```

## Description

This command sends a GET request through a proxy to generate a CSRF token in a PHP application using the Anti-CSRF Library, simulating a client IP while capturing the proxy's IP in $_SERVER['REMOTE_ADDR']. Use it to obtain a token bound to the proxy for later reuse testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "X-Forwarded-For: IP"` | Simulates client IP forwarded by proxy | Yes |
| `URL` | Endpoint to generate token | Yes |

## Examples

### Basic Usage

```bash
curl -H "X-Forwarded-For: 192.168.1.100" http://localhost/generate-token.php
```

### Advanced Usage

```bash
curl -H "X-Forwarded-For: 192.168.1.100" -v http://localhost/generate-token.php
```

## Expected Output

CSRF token string (e.g., "abc123def456"), with server logs showing REMOTE_ADDR as proxy IP.

## Related

- [[Related Procedure: Demonstrate-CSRF-IP-Binding-Failure]]
