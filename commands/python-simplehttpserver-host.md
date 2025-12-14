---
data: python -m SimpleHTTPServer 8000
tags:
  - hosting
  - ssrf
type: command
output: Serving HTTP on 0.0.0.0 port 8000 ...
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:53:38.706Z'
id: 5a2f22be-372c-4433-9a9f-db37d1bc9395
verified: false
validated: true
submitted: true
---
# python-simplehttpserver-host

## Command

```bash
python -m SimpleHTTPServer 8000
```

## Description

Starts a basic HTTP server using Python's SimpleHTTPServer module to serve static files like HTML from the current directory, useful for hosting PoC pages in SSRF attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 8000 | Port to listen on for HTTP requests | Yes |

## Examples

### Basic Usage

```bash
python -m SimpleHTTPServer 8000
```

Serves files at http://localhost:8000.

### Advanced Usage

For Python 3, use: python3 -m http.server 8000

## Expected Output

Serving HTTP on 0.0.0.0 port 8000 ...

## Related

- [[Related Procedure]]
