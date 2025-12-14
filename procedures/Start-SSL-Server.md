---
tags:
  - ssl-hosting
  - local-server
type: procedure
tools:
  - '[[tools/ssl-server-py]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/start-ssl-server]]'
platforms:
  - Linux
  - macOS
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: ebb96abb-dda7-4ebf-8ae1-85da56fe36c5
created_at: '2025-12-14T17:29:36.444Z'
updated_at: '2025-12-14T17:29:36.444Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Start-SSL-Server

## Summary

This procedure starts a local SSL-protected web server to host the exploit page on the lookalike domain, simulating the attacker's malicious site.

## Description

Using ssl_server.py, the server binds to port 443 with a self-signed certificate, serving exploit_admin_bar.html over HTTPS. Admin privileges are needed for port binding. In production, the attacker would use a valid cert on their domain.

## Requirements

1. Python 3 installed
2. Admin privileges (sudo)
3. Downloaded ssl_server.py in working directory

## Defense

Defensive measures and detection strategies:

- Block self-signed certs in browsers
- Monitor for unauthorized local servers on low ports
- Use HSTS to enforce valid HTTPS

## Objectives

1. Host exploit over HTTPS
2. Enable postMessage from secure context
3. Simulate real attack with cert acceptance

## Instructions

### Step 1: Run Server Script

**Context**: Launch the SSL server with admin rights.

**Command** ([[commands/start-ssl-server]]):
```bash
sudo python3 ssl_server.py
```

> Starts server on HTTPS port 443. Expected output: Listening message.

### Step 2: Confirm Server Status

**Context**: Verify it's serving files.

No command; access https://foo.myshopify.co in browser.

> Expected: Page loads after cert acceptance.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/start-ssl-server]]

## Tools Used

- [[tools/ssl-server-py]]

## Tags

- [[ssl-hosting]]
- [[local-server]]
