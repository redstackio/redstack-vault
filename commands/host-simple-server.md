---
id: 123e4567-e89b-12d3-a456-426614174003
data: python3 -m http.server 8080
name: host-simple-server
tags:
  - hosting
  - dos
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-10-04T00:00:00Z'
updated_at: '2025-12-14T17:26:48.707Z'
verified: false
validated: true
submitted: true
---
# host-simple-server

## Command

```bash
python3 -m http.server 8080
```

## Description

Starts a basic HTTP server to host files like malicious payloads for fetch() exploitation. Useful for local testing of DoS vectors.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `8080` | Port to listen on | No (default 8000) |

## Examples

### Basic Usage

```bash
python3 -m http.server
```

### Advanced Usage

```bash
python3 -m http.server 8080 --bind 0.0.0.0
```

## Expected Output

Serving HTTP on 0.0.0.0 port 8080 (http://0.0.0.0:8080/) ... Logs incoming requests.

## Related

- [[Related Procedure|procedures/Exploit-Brotli-Decoding-DoS-in-Node-js]]
