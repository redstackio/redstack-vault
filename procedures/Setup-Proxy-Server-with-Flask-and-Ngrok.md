---
id: 1f4a76b2-4277-4d87-8e48-45c78dd81909
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T03:48:05.910Z'
updated_at: '2025-12-11T03:48:05.910Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - proxy
  - flask
  - ngrok
commands: []
platforms:
  - Linux
tools:
  - '[[tools/Flask]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
validated: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---

# Setup Proxy Server with Flask and Ngrok

## Summary

This procedure sets up a Flask-based proxy server to serve the malicious uploads.tar.gz and exposes it externally using ngrok for use in the GitLab import process.

## Description

A simple Flask app (api.py) is run to intercept requests and replace the uploads.tar.gz with the malicious version. Ngrok tunnels the local server to provide an external URL. This is crucial for injecting the payload during remote import, targeting GitLab's bulk import API.

## Requirements

1. Python with Flask installed
2. Ngrok installed
3. Malicious uploads.tar.gz prepared

## Defense

Defensive measures and detection strategies:

- Validate import sources and URLs
- Monitor for external proxy usage in imports

## Objectives

1. Launch local proxy to serve payload
2. Expose proxy for remote access
3. Prepare for import injection

## Instructions

### Step 1: Run Flask Server

**Context**: Launching proxy to replace uploads.tar.gz with malicious version during import.

**Command** ([[commands/flask-run-proxy]]):
```bash
FLASK_APP=api flask run
```

> Starts the server on port 5000.

### Step 2: Expose with Ngrok

**Context**: Making the proxy accessible for GitLab import process.

**Command** ([[commands/ngrok-expose-server]]):
```bash
ngrok http 5000
```

> Provides an HTTPS URL for external access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/flask-run-proxy]]
- [[commands/ngrok-expose-server]]

## Tools Used

- [[tools/Flask]]
- #ngrok

## Tags

- [[commands/flask-run-proxy]]
- [[tools/Flask]]
- #ngrok
