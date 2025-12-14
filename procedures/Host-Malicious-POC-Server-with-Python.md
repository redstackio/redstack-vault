---
id: proc-host-poc-server
tags:
  - xss
  - poc-server
  - python
type: procedure
tools:
  - '[[tools/Python-3]]'
  - '[[tools/server.py]]'
  - '[[tools/universal_xss.html]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/python-server-start]]'
verified: false
platforms:
  - Windows
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:55.190Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Host-Malicious-POC-Server-with-Python

## Summary

This procedure sets up a local HTTP server using Python to host the proof-of-concept HTML file that exploits the Kaspersky URL Advisor vulnerability via postMessage injection.

## Description

In the attack scenario, a rudimentary HTTP server is needed to serve the universal_xss.html file, which contains JavaScript to send malicious postMessage events to the URL Advisor frame. This frame, served as first-party content in Microsoft Edge, lacks origin validation, allowing the injection. The server runs on localhost:5000, enabling access via the spoofed domain. Prerequisites include Python 3 installed and the server.py and universal_xss.html files downloaded.

## Requirements

1. Python 3 installed on Windows
2. server.py and universal_xss.html files in the working directory
3. Local administrator access not required for this step

## Defense

Defensive measures and detection strategies:

- Monitor for unexpected HTTP servers on non-standard ports like 5000
- Use endpoint detection to block unauthorized Python executions serving web content
- Enable browser sandboxing to limit local server interactions with extensions

## Objectives

1. Serve the malicious PoC to initiate postMessage attack
2. Ensure accessibility via localhost for subsequent steps
3. Validate server readiness before domain spoofing

## Instructions

### Step 1: Prepare Files

**Context**: Download and place the necessary files in a local directory to host the PoC.

**Command** ([[commands/python-server-start]]):
```bash
python server.py
```

> This command starts a basic HTTP server using Python's http.server module on port 5000. Expected output includes logs like 'Serving HTTP on 0.0.0.0 port 5000' confirming the server is running and ready to serve universal_xss.html.

### Step 2: Verify Server

**Context**: Access the server to ensure the PoC file is hosted correctly.

**Command** (Manual verification):
```bash
# No command; open http://localhost:5000/universal_xss.html in a browser
```

> Manually navigate to the URL to confirm the page loads without errors, indicating the server is operational for the attack.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/python-server-start]]

## Tools Used

- [[tools/Python-3]]
- [[tools/server.py]]
- [[tools/universal_xss.html]]

## Tags

- xss
- poc-server
- python
