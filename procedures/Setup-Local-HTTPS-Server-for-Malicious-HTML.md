---
id: proc-002
tags:
  - https-server
  - local-hosting
type: procedure
tools:
  - '[[tools/Python-3]]'
  - '[[tools/server-py]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:29:36.223Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Setup Local HTTPS Server for Malicious HTML

## Summary

This procedure sets up a simple local HTTPS server using Python to host the malicious HTML file that exploits the Kaspersky vulnerability, simulating a secure site with an invalid certificate.

## Description

The server.py script provides a rudimentary HTTPS server on port 5000, allowing the disable_features2.html file to be served over HTTPS. This setup is necessary to mimic a real webpage and bypass basic checks, while the invalid cert forces user interaction in IE. The HTML contains JavaScript to intercept prototype methods.

## Requirements

1. Python 3 installed on Windows
2. Downloaded server.py and disable_features2.html files
3. Port 5000 available (no conflicts)

## Defense

Defensive measures and detection strategies:

- Monitor for unauthorized local servers on non-standard ports
- Firewall rules to block inbound localhost HTTPS on 5000
- Log Python executions for suspicious scripts

## Objectives

1. Host exploit payload locally over HTTPS
2. Ensure accessibility via fake domain
3. Handle invalid cert for IE navigation

## Instructions

### Step 1: Download Files

**Context**: Obtain the server script and HTML payload.

Download server.py (rudimentary HTTPS server) and disable_features2.html from the exploit source.

> Expected: Files saved in a working directory.

### Step 2: Run Server

**Context**: Start the server with Python 3.

Open Command Prompt, navigate to the directory, and execute:

```bash
python server.py
```

> Expected: Output like "Serving HTTPS on 0.0.0.0:5000"; server active.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Python-3]]
- [[tools/server-py]]

## Tags

- [[https-server]]
- [[local-hosting]]
