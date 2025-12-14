---
tags:
  - oauth
  - dos
  - crash
  - repeat
  - twitter
  - token-exposure
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/curl-repeat-protocol-relative]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:24:35.131Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 03ce2d25-60e2-495e-b48c-d699fb7862bb
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Endpoint Denial of Service]]'
---
# Repeat-Authorization-to-Cause-Server-Crash

## Summary

This procedure repeatedly invokes the flawed OAuth authorization with a protocol-relative redirect URI to overwhelm the Meteor framework's error handling, resulting in a server crash and denial-of-service, with risks of exposing OAuth tokens in clear text.

## Description

Building on the error triggered by protocol-relative URIs, multiple rapid requests to the /_oauth/twitter/ endpoint cause unhandled exceptions during token exchange or state handling. The Meteor application's inadequate validation leads to resource exhaustion or fatal errors, crashing the server. Error rendering may inadvertently display sensitive OAuth tokens, amplifying the impact.

## Requirements

1. Scripting capability for repeated HTTP requests (e.g., bash loop with curl)
2. Monitoring tools to detect server unresponsiveness
3. Understanding of DoS implications

## Defense

Defensive measures and detection strategies:

- Implement request throttling on OAuth endpoints
- Use robust error handling to avoid crashes from malformed inputs
- Scan error logs for repeated failed authorizations and token leaks

## Objectives

1. Induce server crash through repeated malformed requests
2. Achieve DoS condition on the Twitter integration
3. Potentially extract exposed OAuth tokens from errors

## Instructions

### Step 1: Loop Malformed Requests Multiple Times

**Context**: Automate 10-20 requests to the vulnerable endpoint to force error accumulation and crash.

**Command** ([[commands/curl-repeat-protocol-relative]]):
```bash
for i in {1..10}; do curl "https://app.respond.ly/_oauth/twitter/?requestTokenAndRedirect=//hackerone.com"; done
```

> This bash loop sends repeated GET requests. Expected output after several iterations: Server errors escalating to crash, with the application becoming unresponsive. Inspect responses for any clear-text token leaks.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used

- [[commands/curl-repeat-protocol-relative]]

## Tools Used


## Tags

- [[dos]]
- [[crash]]
- [[token-exposure]]
