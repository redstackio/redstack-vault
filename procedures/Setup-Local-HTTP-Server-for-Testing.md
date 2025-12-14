---
id: proc-uuid-002
tags:
  - testing
  - server-setup
  - poc
type: procedure
tools:
  - '[[tools/Flask]]'
  - '[[tools/Python]]'
tactics: []
commands:
  - '[[commands/flask-simple-server]]'
verified: false
platforms:
  - Linux
  - macOS
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques: []
updated_at: '2025-12-14T04:39:02.507Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
---
# Setup-Local-HTTP-Server-for-Testing

## Summary

Sets up a simple Flask HTTP server on port 80 to listen for SSRF requests and respond with a marker string for verification.

## Description

This creates a target endpoint for the SSRF PoC, binding to all interfaces on port 80 to capture requests redirected to localhost. It responds with 'FindVuln' to confirm reception.

## Requirements

1. Python 3.x installed
2. Flask library (pip install flask)
3. Port 80 available (may require sudo on Linux)

## Defense

Defensive measures and detection strategies:

- Use firewalls to restrict port 80 access
- Monitor for unexpected local server startups

## Objectives

1. Provide a listener for SSRF validation
2. Log incoming requests
3. Confirm exploitation success

## Instructions

### Step 1: Install Flask

**Context**: Ensure dependencies.

```bash
pip install flask
```

### Step 2: Run Server Script

**Context**: Start the listener using [[commands/flask-simple-server]].

Save the code to a file (e.g., server.py) and execute:

```bash
python server.py
```

> The server starts on 0.0.0.0:80, responding 'FindVuln' to GET /.

**Expected Output**: '* Running on all addresses (0.0.0.0)
* Running on http://127.0.0.1:80'.

## MITRE ATT&CK Mapping

### Tactics


### Techniques


### Sub-Techniques


## Commands Used

- [[commands/flask-simple-server]]

## Tools Used

- [[tools/Flask]]
- [[tools/Python]]

## Tags

- [[testing]]
- [[poc]]
