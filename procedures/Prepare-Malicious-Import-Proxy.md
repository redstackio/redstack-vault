---
tags:
  - proxy
  - payload
type: procedure
tools:
  - '[[tools/Flask]]'
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Linux
techniques:
  - '[[Command-Line Interface]]'
skill_level: advanced
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 9d1f54f2-d828-42c8-afe2-84141235e7c6
created_at: '2025-12-11T03:48:06.013Z'
updated_at: '2025-12-11T03:48:06.013Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059]]'
---
# Prepare Malicious Import Proxy

## Summary

This procedure modifies a script to inject malicious commands and sets up a proxy server exposed via ngrok for delivering the payload during GitLab imports.

## Description

Involves editing api_project_ql.py to manipulate import_source for command injection, running it with Flask, and exposing it publicly with ngrok to simulate a malicious GitLab API endpoint.

## Requirements

1. Python with Flask installed
2. Ngrok binary
3. Modified script with injection (e.g., '; malicious command')

## Defense

Defensive measures and detection strategies:

- Validate import sources against whitelists
- Monitor for unexpected external connections during imports

## Objectives

1. Create injectable payload
2. Host proxy server
3. Expose for remote access

## Instructions

### Step 1: Modify Script

**Context**: Edit api_project_ql.py to include malicious import_source.

> Change PROJECT_PATH, PROJECT_ID, and inject command like '; echo lala > /tmp/1234'.

### Step 2: Run Flask App

**Context**: Start the proxy server.

**Command** ([[commands/flask-run]]):
```bash
FLASK_APP=api_project_ql.py flask run
```

> Runs the app on port 5000.

### Step 3: Expose with Ngrok

**Context**: Make the local server accessible externally.

**Command** ([[commands/ngrok-http]]):
```bash
ngrok http 5000
```

> Provides a public URL for the proxy.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques



## Commands Used

- [[commands/flask-run]]
- [[commands/ngrok-http]]

## Tools Used

- [[tools/Flask]]
- #ngrok

## Tags

- #proxy
- #payload
