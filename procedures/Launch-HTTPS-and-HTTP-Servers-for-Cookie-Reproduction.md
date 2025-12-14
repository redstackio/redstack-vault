---
tags:
  - server
  - http
  - https
  - python
type: procedure
tools:
  - '[[tools/Python3]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/python3-server-py]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:26:22.102Z'
sub_techniques: []
id: 3d7dbe47-0439-4aa8-a531-31bd4fb577a4
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Launch-HTTPS-and-HTTP-Servers-for-Cookie-Reproduction

## Summary

This procedure starts a Python-based HTTPS server on port 9443 (sets Secure cookie with path=/ and redirects to HTTP) and HTTP server on port 9080 (sets non-secure cookie with path=/foo/) to reproduce the curl cookie handling vulnerability.

## Description

Using Python's http.server and ssl modules, the server.py script simulates the mixed protocol scenario: HTTPS endpoint sets a secure cookie and redirects, triggering cookie replacement in curl. The empty path after sanitization leads to the OOB read. Prerequisites: Python 3 and generated cert/key files.

## Requirements

1. Python 3 installed
2. server.py script present (assumed provided)
3. Ports 9443/9080 free
4. cert.pem and key.pem available

## Defense

Defensive measures and detection strategies:

- Firewall ports to prevent unauthorized servers
- Monitor for unexpected HTTP redirects
- Validate cookie paths in applications

## Objectives

1. Simulate secure-to-non-secure cookie flow
2. Enable redirect-based cookie setting
3. Prepare environment for curl trigger

## Instructions

### Step 1: Run Server Script

**Context**: Launch both servers via the Python script.

**Command** ([[commands/python3-server-py]]):
```bash
python3 server.py
```

> Starts servers; output shows listening on ports, ready for requests.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Unix Shell]] Unix Shell

### Sub-Techniques


## Commands Used

- [[commands/python3-server-py]]

## Tools Used

- [[tools/Python3]]

## Tags

- server
- http
- https
- python
