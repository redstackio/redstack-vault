---
data: 'curl -I http://blog.owox.com'
tags:
  - http
  - test
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:23.204Z'
id: 9d7bbd62-beb9-4eaa-9646-6f3954b905f0
verified: false
validated: true
submitted: true
---
# curl-http-test

## Command

```bash
curl -I http://blog.owox.com
```

## Description

Sends a HEAD request to verify if a subdomain serves content, confirming control after takeover.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I` | HEAD request only | Yes |
| `http://blog.owox.com` | Target URL | Yes |

## Examples

### Basic Usage

```bash
curl -I http://blog.owox.com
```

### Advanced Usage

```bash
curl -I -L http://blog.owox.com
```

## Expected Output

HTTP headers, e.g., 'HTTP/1.1 200 OK' indicating successful hosting.

## Related

- [[Related Procedure: Claim and Host on Subdomain]]
