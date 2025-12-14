---
id: proc-setup-redirect-server-001
tags:
  - flask
  - redirect
  - ssrf
type: procedure
tools:
  - '[[tools/Flask]]'
  - '[[tools/pip]]'
tactics:
  - '[[Command and Control]]'
commands:
  - '[[commands/install-flask]]'
  - '[[commands/run-flask-redirect-server]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Web Protocols]]'
updated_at: '2025-12-14T04:08:55.702Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Command and Control]]'
mitre_techniques:
  - '[[Web Protocols]]'
---
# Setup-Attacker-Controlled-Redirect-Server

## Summary

Deploy a Flask-based web server to intercept webhook requests and redirect them to internal targets for SSRF exploitation.

## Description

The server receives AdmissionReview requests, logs headers, and issues 302 redirects to cloud metadata endpoints (e.g., 169.254.169.254). Customize poc2.py for specific redirects.

## Requirements

1. Python 3 and pip installed
2. Port 8067 free
3. poc2.py script prepared (prints headers, redirects non-/test paths)

## Defense

- Block outbound requests from apiserver to untrusted IPs
- Monitor for new web servers on unusual ports
- Use network policies to restrict webhook traffic

## Objectives

1. Install and run Flask server
2. Configure for request logging and redirects
3. Verify redirect functionality

## Instructions

### Step 1: Install Flask

**Context**: Prepare dependencies for the server.

**Command** ([[commands/install-flask]]):
```bash
pip install Flask
```

> Installs Flask framework. Expected: Success message, no errors.

### Step 2: Run Server

**Context**: Start the application in dev mode on port 8067.

**Command** ([[commands/run-flask-redirect-server]]):
```bash
FLASK_ENV=development FLASK_APP=poc1 flask run
```

> Note: App file is poc1 but code in poc2.py sets port=8067. Server handles /test without redirect, others to http://www.tencent.com/ (adapt for metadata). Expected: Running on 127.0.0.1:8067.

### Step 3: Test Redirect

**Context**: Verify behavior.

**Command** ([[commands/test-flask-redirect]]):
```bash
curl -v http://127.0.0.1:8067/test
curl -v http://127.0.0.1:8067/other
```

> First returns plain, second 302 to target.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control]] Command and Control

### Techniques

- [[Web Protocols]] Web Protocols

### Sub-Techniques


## Commands Used

- [[commands/install-flask]]
- [[commands/run-flask-redirect-server]]
- [[commands/test-flask-redirect]]

## Tools Used

- [[tools/Flask]]
- [[tools/pip]]
- [[tools/curl]]

## Tags

- flask
- server
- redirect
