---
data: python -m http.server 8000
tags:
  - http
  - server
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 2690d2c4-be7c-4c0a-9bc0-231f41c06eae
created_at: '2025-12-13T09:00:27.242Z'
updated_at: '2025-12-13T09:00:27.242Z'
verified: false
validated: true
submitted: true
---
# Start Python HTTP Server

## Command

```bash
python -m http.server 8000
```

## Description

This command starts a simple HTTP server using Python's built-in module, useful for receiving and logging incoming connections during exploits like XXE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `8000` | Port number to listen on | No (default 8000) |

## Examples

### Basic Usage

```bash
python -m http.server 8000
```

### Advanced Usage

```bash
python -m http.server 8080 --bind 0.0.0.0
```

## Expected Output

Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...

## Related

- [[tools/Python-HTTP-Server]]
