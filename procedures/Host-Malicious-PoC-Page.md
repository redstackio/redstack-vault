---
tags:
  - hosting
  - poc
  - web-server
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:28:04.880Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: f08360b9-e794-4e97-9252-b223ca66acf2
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Host-Malicious-PoC-Page

## Summary

This procedure hosts the ClickJacking PoC HTML page on a local or remote web server to make it accessible for exploitation testing.

## Description

After creating poc.html, host it using a simple web server to simulate a malicious site. This allows the iframe to load the Weblate debug page and enables user interaction testing, mimicking a real attack scenario.

## Requirements

1. Local web server capability (e.g., Python built-in server)
2. The poc.html file from previous procedure
3. Port 8000 or similar available

## Defense

Defensive measures and detection strategies:

- Scan for and block known malicious hosts
- Use browser sandboxing to limit iframe interactions
- Monitor server logs for unusual HTML uploads

## Objectives

1. Serve the PoC over HTTP/HTTPS
2. Verify accessibility and functionality
3. Prepare for user deception simulation

## Instructions

### Step 1: Prepare the Hosting Directory

**Context**: Place the PoC file in a directory for serving.

Create a folder (e.g., poc-host) and save poc.html inside it.

> Ensures the file is ready for server exposure.

### Step 2: Start Local Web Server

**Context**: Launch a simple server to host the page.

Navigate to the poc-host directory in terminal and run a Python HTTP server (Python 3).

```bash
python3 -m http.server 8000
```

> Server starts on http://localhost:8000; access poc.html via http://localhost:8000/poc.html.

### Step 3: Test Hosting

**Context**: Verify the page loads correctly.

Open a browser to http://localhost:8000/poc.html and confirm the iframe and overlay work.

> Iframe should embed the debug page; clicks should trigger the exploit.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used

- [[commands/python3-http-server]]

## Tools Used


## Tags

- [[hosting]]
- [[poc]]
- [[web-server]]
