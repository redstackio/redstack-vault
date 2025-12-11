---
id: 66bcdaf8-0fe6-496f-b061-c2f638dc34cf
name: Set Up Timing and Logging Server
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T06:10:15.619Z'
updated_at: '2025-12-11T06:10:15.619Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Command-Line Interface]]'
sub_techniques:
  - '[[Python]]'
tags:
  - dns-rebinding
  - flask-server
commands:
  - '[[commands/flask-app-run]]'
  - '[[commands/flask-sleep]]'
  - '[[commands/flask-print-log]]'
  - '[[commands/flask-set-log-level]]'
platforms:
  - Web
  - GCP
tools:
  - '[[tools/Flask]]'
  - '[[tools/flask_cors]]'
  - '[[tools/XMLHttpRequest]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
validated: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059]]'
---

# Set Up Timing and Logging Server

## Summary

This procedure sets up a Flask-based server to handle timing delays and logging, essential for facilitating DNS rebinding in SSRF attacks.

## Description

The server is hosted on a public domain and includes routes for delaying responses (to allow DNS rebinding) and logging exfiltrated data. It uses Python and Flask with CORS enabled.

## Requirements

1. Python environment with Flask and flask_cors installed
2. Publicly accessible host (e.g., ssh.█████:5000)
3. Control over server execution

## Defense

Defensive measures and detection strategies:

- Monitor for unusual server setups or timing-based requests
- Use DNS caching and rebinding protections like HTTP Host header validation

## Objectives

1. Create a timing mechanism for rebinding
2. Enable logging of exfiltrated data
3. Support SSRF exploitation

## Instructions

### Step 1: Configure and Run Flask App

**Context**: Set up routes for '/' with sleep and '/log' for message logging.

**Command** ([[commands/flask-set-log-level]]):
```python
log.setLevel(logging.ERROR)
```

> Sets logging to ERROR level to reduce noise.

**Command** ([[commands/flask-app-run]]):
```python
app.run(host='0.0.0.0')
```

> Starts the server on all interfaces.

### Step 2: Implement Timing Delay

**Context**: Add delay to the helloWorld route for rebinding timing.

**Command** ([[commands/flask-sleep]]):
```python
sleep(3)
```

> Pauses execution for 3 seconds.

### Step 3: Implement Logging

**Context**: Log messages in the log route.

**Command** ([[commands/flask-print-log]]):
```python
print request.args['msg']
```

> Prints the message from the request.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques

- [[Python]]

## Commands Used

- [[commands/flask-app-run]]
- [[commands/flask-sleep]]
- [[commands/flask-print-log]]
- [[commands/flask-set-log-level]]

## Tools Used

- [[tools/Flask]]
- [[tools/flask_cors]]

## Tags

- [[dns-rebinding]]
- [[tools/Flask]]
