---
id: 24e71d8c-6361-458f-ae4e-a4f62af920d0
name: ruby-start-simple-http-server
type: command
executor: bash
data: ruby -run -ehttpd . -p8080
output: null
created_at: '2023-04-06T03:56:42.227921+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
tags:
  - web-server
  - listener
verified: true
validated: true
---

# ruby-start-simple-http-server

## Command

```bash
ruby -run -ehttpd . -p8080
```

## Description

This command starts a basic HTTP server using Ruby's built-in capabilities, serving files from the current directory on port 8080. It is useful for quickly hosting a listener to capture data exfiltrated from blind XSS payloads or testing simple web interactions without installing additional software.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-run -ehttpd` | Executes the HTTP server module | Yes |
| `.` | Serves files from the current directory | Yes |
| `-p8080` | Specifies the listening port (default is 8080 if omitted) | No |

## Examples

### Basic Usage

```bash
ruby -run -ehttpd . -p8080
```

Starts the server on port 8080, accessible at http://localhost:8080.

### Advanced Usage

```bash
ruby -run -ehttpd /path/to/files -p9000
```

Serves from a specific directory on port 9000.

## Expected Output

Server startup message like:

[2023-10-01 12:00:00] INFO  WEBrick 1.8.1
[2023-10-01 12:00:00] INFO  ruby 3.1.0 (2022-...) [x86_64-linux]
[2023-10-01 12:00:00] INFO  WEBrick::HTTPServer#start: pid=1234 port=8080

Subsequent requests will log to stdout, e.g.,

[2023-10-01 12:01:00] INFO  GET /XSS/grabber.php?c=example.com 200

## Related

- [[procedures/Blind-XSS-Data-Exfiltration]]
