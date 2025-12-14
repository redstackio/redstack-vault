---
id: cmd-uuid-789
data: ngrok http 8080
tags:
  - tunnel
  - ssrf
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:09.495Z'
verified: false
validated: true
submitted: true
---
# ngrok-expose-server

## Command

```bash
ngrok http 8080
```

## Description

This command starts an ngrok tunnel to expose a local HTTP server on port 8080 publicly, allowing reception of inbound requests for SSRF confirmation. Ideal for testing blind exploits where the target fetches your controlled URL.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `http` | Protocol to tunnel | Yes |
| `8080` | Local port to forward | Yes |

## Examples

### Basic Usage

```bash
ngrok http 8080
```

### Advanced Usage

```bash
ngrok http 8080 --subdomain=ssrf-test
```

## Expected Output

Ngrok session started with a public URL like 'https://abc123.ngrok.io -> http://localhost:8080'. Access http://localhost:4040 for inspection.

## Related

- [[Related Procedure: Exploit-Blind-SSRF-via-Sentry-Stacktrace-Injection]]
