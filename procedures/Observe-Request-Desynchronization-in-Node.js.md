---
tags:
  - http-request-smuggling
  - desynchronization
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-observe-response]]'
platforms:
  - Node.js
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 895b59a1-8406-45a2-b73e-d10d148d6faa
created_at: '2025-12-13T09:01:22.539Z'
updated_at: '2025-12-13T09:01:22.539Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Observe Request Desynchronization in Node.js

## Summary

This procedure involves observing how Node.js interprets the smuggled request differently, converting CR to hyphen and treating it as Content-Length, leading to request smuggling.

## Description

Node.js discards bytes as per the interpreted Content-Length, parsing the subsequent request from a different point, which desynchronizes it from the proxy's view.

## Requirements

1. Previously sent malicious request
2. Access to monitor responses or logs
3. Tool for sending follow-up requests

## Defense

Defensive measures and detection strategies:

- Patch Node.js to prevent CR-to-hyphen conversion in headers
- Monitor for desynchronized request patterns in logs
- Use consistent parsing libraries across stack

## Objectives

1. Verify desynchronization
2. Confirm smuggling success
3. Identify opportunities for further exploitation

## Instructions

### Step 1: Monitor Responses

**Context**: Send a follow-up request or check logs to observe desynchronization.

**Command** ([[commands/curl-observe-response]]):
```bash
curl http://proxy.target.com/ -v
```

> Look for signs of smuggled requests or unexpected behavior in responses.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-observe-response]]

## Tools Used

- [[tools/curl]]

## Tags

- [[http-request-smuggling]]
- [[desynchronization]]
