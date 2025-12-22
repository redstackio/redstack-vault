---
id: uuid-start-ssl-server
tags:
  - https-server
  - ssl
type: procedure
tools:
  - '[[tools/ssl-server-py]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/python3-ssl-server]]'
verified: false
platforms:
  - Linux
  - Windows
  - macOS
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:21.051Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Start-Local-SSL-Server

## Summary

This procedure launches a local HTTPS server using ssl_server.py to host the exploit_preview.html on port 443, simulating a secure malicious site under the spoofed domain.

## Description

The custom ssl_server.py script uses Python's ssl and http.server modules to provide HTTPS on port 443, necessary because postMessage origins include the scheme. Run with admin privileges to bind low ports. This hosts the exploit page that will frame the Shopify preview and send the malicious postMessage.

## Requirements

1. Python 3 installed
2. ssl_server.py in current directory
3. Administrator/root privileges for port 443
4. Self-signed certificate accepted in browser later

## Defense

Defensive measures and detection strategies:

- Block unauthorized local servers via firewall rules on port 443
- Monitor for Python processes binding to privileged ports

## Objectives

1. Serve exploit content over HTTPS on spoofed domain
2. Ensure accessibility before triggering exploit
3. Maintain server uptime during attack

## Instructions

### Step 1: Launch Server

**Context**: Start the HTTPS server in the exploit directory.

Execute [[commands/python3-ssl-server]]:

```bash
sudo python3 ssl_server.py
```

> Expected: Output like "Serving HTTPS on 0.0.0.0 port 443"; no bind errors.

### Step 2: Test Server

**Context**: Verify hosting of exploit file.

Open https://roolee.co/exploit_preview.html in browser and accept cert.

> Expected: Page loads with iframe to shop preview; no 404.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/python3-ssl-server]]

## Tools Used

- [[tools/ssl-server-py]]

## Tags

- https-server
- ssl
