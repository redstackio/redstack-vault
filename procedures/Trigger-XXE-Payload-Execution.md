---
tags:
  - xxe
  - xml
type: procedure
tools:
  - '[[tools/Python-HTTP-Server]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/start-python-http-server]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: c71b853e-7470-4065-835a-31cac9cabb09
created_at: '2025-12-13T09:00:27.249Z'
updated_at: '2025-12-13T09:00:27.249Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger XXE Payload Execution

## Summary

This procedure triggers the execution of the XXE payload by having the server parse the uploaded file, resolving external entities to connect to the attacker's Python HTTP server.

## Description

After upload, the server processes the file as XML, resolving the external entity and making a connection to the specified attacker-controlled server, confirming the XXE vulnerability.

## Requirements

1. Uploaded malicious SVG file
2. Running Python HTTP server on attacker machine
3. Network connectivity from target to attacker server

## Defense

Defensive measures and detection strategies:

- Disable external entity processing in XML parsers
- Monitor outbound connections from servers

## Objectives

1. Confirm entity resolution via server connection
2. Log incoming requests on attacker server
3. Validate XXE exploitation

## Instructions

### Step 1: Start Python HTTP Server

**Context**: Set up a server to receive connections from the vulnerable system.

**Command** ([[commands/start-python-http-server]]):
```bash
python -m http.server 8000
```

> This starts a simple HTTP server on port 8000 to log incoming requests.

### Step 2: Monitor for Connections

**Context**: Wait for the target server to parse the file and connect.

> Check the server logs for GET requests from the Coinbase server.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/start-python-http-server]]

## Tools Used

- [[tools/Python-HTTP-Server]]

## Tags

- [[xxe]]
- [[xml]]
