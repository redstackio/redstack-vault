---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
type: command
executor: bash
data: python3 -m http.server $_PORT
output: >-
  Serving HTTP on 0.0.0.0 port 8080 (http://0.0.0.0:8080/) ...

  8080 is not in (20, 1024, 8080, 8443) so it will not be possible to set up
  HTTPS encryption.

  127.0.0.1 - - [01/Oct/2023 12:00:00] "GET /shell.ps1 HTTP/1.1" 200 -
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
tags:
  - web-server
  - hosting
verified: true
validated: true
---

# Launch-Python3-Web-Server

## Command

```bash
python3 -m http.server $_PORT
```

## Description

This command starts a basic HTTP server using Python 3's built-in http.server module, serving files from the current directory. It is useful for quickly hosting payload files like PowerShell scripts for download in phishing or exploitation scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PORT | The port to listen on (default 8000 if omitted) | No |

## Examples

### Basic Usage

```bash
python3 -m http.server 8080
```

### Advanced Usage

```bash
python3 -m http.server 80
```

> Note: Port 80 may require sudo on Linux.

## Expected Output

Serving HTTP on 0.0.0.0 port 8080 (http://0.0.0.0:8080/) ...
8080 is not in (20, 1024, 8080, 8443) so it will not be possible to set up HTTPS encryption.
127.0.0.1 - - [01/Oct/2023 12:00:00] "GET /shell.ps1 HTTP/1.1" 200 -

> Indicates the server is running and serving files successfully.

## Related

- [[procedures/Create-LNK-File-with-Custom-PowerShell-Payload]]
