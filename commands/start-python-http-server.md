---
data: python3 -m http.server
tags:
  - http-server
  - hosting
type: command
output: 'Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.224Z'
id: debe94ae-e426-4a05-aa19-f904bed69c04
verified: false
validated: true
submitted: true
---
# start-python-http-server

## Command

```bash
python3 -m http.server
```

## Description

This command starts a basic static HTTP server using Python's built-in http.server module, serving files from the current directory on port 8000. It is commonly used in security testing to host PoC files locally and avoid CORS issues in browsers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-m` | Runs the specified module as a script (http.server) | Yes |
| `http.server` | The module to execute for HTTP serving | Yes |

## Examples

### Basic Usage

```bash
python3 -m http.server
```

### Advanced Usage

```bash
python3 -m http.server 8080
```

> Specifies a custom port (default is 8000).

## Expected Output

The server prints a message confirming it's running and listening on all interfaces, then waits for requests. It serves any files in the current directory, such as HTML PoCs.

## Related

- [[Related Procedure|procedures/Start-Local-HTTP-Server-for-PoC-Hosting]]
