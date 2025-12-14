---
data: python -m http.server
tags:
  - hosting
  - http-server
type: command
output: 'Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:32.136Z'
id: ccd2146f-2bbe-49a5-a49b-bd703d23b9b3
verified: false
validated: true
submitted: true
---
# python-http-server-start

## Command

```bash
python -m http.server
```

## Description

Starts Python's built-in HTTP server to serve files from the current directory, useful for hosting malicious payloads in web-based attacks like Self-XSS exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-m` | Runs the specified module (http.server) | Yes |
| `http.server` | The module to execute; defaults to port 8000 | Yes |

## Examples

### Basic Usage

```bash
python -m http.server
```

### Advanced Usage

```bash
python -m http.server 8080
```

> Specifies a custom port (e.g., 8080).

## Expected Output

Server running on http://0.0.0.0:8000, accessible via browser or curl. Logs incoming requests for monitoring exfiltrated data.

## Related

- [[Related Procedure: Prepare-and-Serve-Malicious-Payload-for-Self-XSS]]
