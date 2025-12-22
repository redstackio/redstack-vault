---
data: python -m SimpleHTTPServer 8000
tags:
  - testing
  - http-server
type: command
executor: bash
platforms:
  - Linux
id: 1745d791-a3fc-49a0-a486-b533b3fefc9a
created_at: '2025-12-14T17:26:30.098Z'
updated_at: '2025-12-14T17:26:30.098Z'
verified: false
validated: true
submitted: true
---
# python-simplehttpserver-start

## Command

```bash
python -m SimpleHTTPServer 8000
```

## Description

Starts a basic HTTP server using Python's SimpleHTTPServer module to serve files and log requests on port 8000, ideal for local testing of vulnerabilities like curl globbing floods.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `8000` | Port number to bind the server to | Yes |

## Examples

### Basic Usage

```bash
python -m SimpleHTTPServer 8000
```

### Advanced Usage

```bash
python -m SimpleHTTPServer 8080
```

## Expected Output

'Serving HTTP on 0.0.0.0 port 8000 ...' followed by request logs like '127.0.0.1 - - [date] "GET /path HTTP/1.1" 200 -'.

## Related

- [[Related Procedure|procedures/Set-Up-Local-HTTP-Server-for-Testing]]
