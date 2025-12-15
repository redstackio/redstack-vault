---
tags:
  - python
  - https-server
  - http2
type: procedure
tools:
  - '[[tools/python3]]'
  - '[[tools/http.server]]'
  - '[[tools/ssl]]'
  - '[[tools/threading]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Python]]'
updated_at: '2025-12-14T17:24:19.149Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 3e2eb1f1-8e51-4508-b433-d853b4f5a0f8
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Python]]'
---
# Start-HTTPS-Server-Supporting-HTTP2

## Summary

This procedure starts a local Python-based HTTPS server on port 8443 that supports HTTP/2 via ALPN, using generated server certificates to simulate a target endpoint for curl requests in the TOCTOU demonstration.

## Description

Using Python 3's http.server and ssl modules, create an SSL context with PROTOCOL_TLS_SERVER, load the server cert and key, enable ALPN protocols ['h2', 'http/1.1'], and wrap the socket. Serve a simple handler that responds 'OK' to GET requests on /secure/data1 and /secure/data2 paths. Run in a daemon thread for background operation.

## Requirements

1. Python 3 with ssl and http.server modules
2. Generated server.crt and server.key files
3. Port 8443 available on localhost

## Defense

Defensive measures and detection strategies:

- Firewall rules to restrict localhost services
- Monitor for unexpected Python processes binding to HTTPS ports
- Use production servers with proper logging and rate limiting

## Objectives

1. Launch HTTPS server with HTTP/2 support
2. Handle multiple requests over persistent connections
3. Log incoming requests for verification

## Instructions

### Step 1: Setup SSL Context and Handler

**Context**: Configure SSL and define a custom request handler for secure paths.

No direct command; implement in Python script (poc.py):

```python
import http.server
import ssl
import threading

class SecureHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path in ['/secure/data1', '/secure/data2']:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'OK')
        else:
            super().do_GET()

httpd = http.server.HTTPServer(('localhost', 8443), SecureHandler)
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('server.crt', 'server.key')
context.set_alpn_protocols(['h2', 'http/1.1'])
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
```

> Sets up handler and SSL with ALPN for HTTP/2.

### Step 2: Run Server in Background

**Context**: Start the server in a daemon thread.

In script:

```python
server_thread = threading.Thread(target=httpd.serve_forever, daemon=True)
server_thread.start()
```

> Runs server asynchronously.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Python]] Python

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/python3]]
- [[tools/http.server]]
- [[tools/ssl]]
- [[tools/threading]]

## Tags

- python
- https-server
- http2
