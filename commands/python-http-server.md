---
id: c3g4h5i6-j7k8-9013-ghij-7890123456
data: |
  python3 -m http.server 80
tags:
  - http
  - server
  - hosting
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T04:51:26.511Z'
verified: false
validated: true
submitted: true
---
# python-http-server

## Command

```bash
python3 -m http.server 80
```

## Description

Starts a simple HTTP server to host files for POC demonstration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-m http.server` | Module to run | Yes |
| `80` | Port | Yes |

## Examples

### Basic Usage

```bash
python3 -m http.server 80
```

### Advanced Usage

```bash
python3 -m http.server 8080 --bind 127.0.0.1
```

## Expected Output

Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...

## Related

- [[procedures/Host-Proof-of-Concept-and-Redirect-Traffic]]
