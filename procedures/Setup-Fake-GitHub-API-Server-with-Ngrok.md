---
tags:
  - fake-server
  - ngrok
  - api-simulation
type: procedure
tools:
  - '[[tools/Ruby]]'
  - '[[tools/Flask]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: c77d1ccf-bc50-4ff1-a2c4-d69d7c44ad69
created_at: '2025-12-11T03:48:06.042Z'
updated_at: '2025-12-11T03:48:06.042Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Setup Fake GitHub API Server with Ngrok

## Summary

This procedure sets up a local Flask-based fake GitHub API server exposed via ngrok to deliver malicious JSON responses for exploiting GitLab's import feature.

## Description

The fake server mimics GitHub API endpoints, returning JSON that triggers the vulnerability in GitLab's Sawyer library handling. Ngrok provides a public URL for the local server on port 5000. This is used to bypass hostname validation and inject payloads.

## Requirements

1. Ngrok installed
2. Flask and Python installed
3. fake_server3.py script edited with payload and ngrok URL

## Defense

Defensive measures and detection strategies:

- Restrict GitHub import hostnames to trusted domains
- Monitor for unexpected ngrok-like URLs in import requests
- Log and alert on Flask or similar server activity in unusual contexts

## Objectives

1. Expose local server publicly
2. Serve malicious API responses
3. Prepare for import triggering

## Instructions

### Step 1: Start Ngrok Tunnel

**Context**: Expose the local port 5000 to the internet.

**Command** ([[commands/ngrok-expose-local-server]]):
```bash
ngrok http 5000
```

> Copy the forwarding URL (e.g., https://9895-45-248-49-157.ngrok.io).

### Step 2: Update and Run Fake Server

**Context**: Edit fake_server3.py with the payload and ngrok URL, then start the server.

**Command** ([[commands/flask-run-fake-server]]):
```bash
FLASK_APP=fake_server3.py flask run
```

> Server runs on http://127.0.0.1:5000, ready to handle requests.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/ngrok-expose-local-server]]
- [[commands/flask-run-fake-server]]

## Tools Used

- #ngrok
- [[tools/Flask]]

## Tags

- [[commands/flask-run-fake-server]]
- #ngrok
