---
data: python -m SimpleHTTPServer 8009
tags:
  - hosting
  - http-server
type: command
output: Serving HTTP on 0.0.0.0 port 8009
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:37.191Z'
id: 9392449d-0f47-4d2e-8322-3ef8cb4466d1
verified: false
validated: true
submitted: true
---
# python-simplehttpserver-host

## Command

```bash
python -m SimpleHTTPServer 8009
```

## Description

Starts a simple HTTP server using Python to host the malicious HTML payload for the Chromium exploit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-m SimpleHTTPServer` | Module to run | Yes |
| 8009 | Port to listen on | Yes |

## Examples

### Basic Usage

```bash
python -m SimpleHTTPServer 8009
```

### Advanced Usage

```bash
python -m SimpleHTTPServer 8000
```

## Expected Output

'Serving HTTP on 0.0.0.0 port 8009 ...' followed by request logs when accessed.

## Related

- [[procedures/Host-Malicious-HTML-Payload-for-Chromium-RCE]]
- [[tools/Python-SimpleHTTPServer]]
