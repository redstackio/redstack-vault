---
tags:
  - test
  - verification
  - http
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Defense Evasion]]'
commands:
  - '[[commands/curl-test-without-header]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:36.576Z'
sub_techniques: []
id: e5c4d4fc-89e4-4975-8304-5e44a186df1c
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-Access-Without-Spoofing

## Summary

This procedure tests the IP whitelist enforcement by sending a request without any X-Forwarded-For header to confirm access is blocked.

## Description

With the server running, this step verifies the middleware's protective behavior using a standard HTTP GET request. It simulates a legitimate but unauthorized client (non-whitelisted IP). Expected outcome: 403 response, proving the control works before attempting bypass.

## Requirements

1. Server running on localhost:3000
2. curl installed
3. Local network access

## Defense

Defensive measures and detection strategies:

- Log 403 responses for anomaly detection
- Rate-limit failed access attempts
- Audit access logs for patterns indicating testing

## Objectives

1. Validate whitelist functionality
2. Baseline normal denial behavior
3. Prepare for bypass comparison

## Instructions

### Step 1: Send Plain GET Request

**Context**: Probes the endpoint without spoofing to trigger the block.

**Command** ([[commands/curl-test-without-header]]):
```bash
curl 'http://localhost:3000/'
```

> Issues a GET to the root path. Expected output: HTTP 403 with body "You do not have rights to visit this page".

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-test-without-header]]

## Tools Used

- [[tools/curl]]

## Tags

- test
- verification
- http
