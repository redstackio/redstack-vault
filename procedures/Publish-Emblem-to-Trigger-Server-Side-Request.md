---
id: proc-uuid-002
tags:
  - ssrf
  - publish-trigger
type: procedure
tools:
  - '[[tools/requestb-in]]'
tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:14.328Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Publish Emblem to Trigger Server-Side Request

## Summary

This procedure triggers the SSRF by publishing the emblem containing the injected SVG, causing the server to fetch the external URL from its IP address.

## Description

After saving the emblem with the injected SVG, publishing it via the /emblems/publish endpoint processes the SVG server-side, initiating an HTTP GET to the injected URL. This confirms the blind SSRF as requests appear on the attacker's controlled server. The server IP is from Rockstar's infrastructure, and different ports can be tested.

## Requirements

1. Saved emblem with injected SVG
2. Access to publish functionality
3. Monitoring on external request logger

## Defense

Defensive measures and detection strategies:

- Disable or sandbox external resource fetching in SVG processing
- Log and alert on outbound requests from application servers
- Use content security policies to restrict URL schemes

## Objectives

1. Execute server-side fetch to injected URL
2. Verify request origin and capabilities
3. Confirm arbitrary host/port access

## Instructions

### Step 1: Initiate Publish Request

**Context**: Send the publish request after saving to trigger processing.

**Command** (Browser or tool POST to /emblems/publish):
```http
POST /emblems/publish HTTP/1.1
Host: socialclub.rockstargames.com
Content-Type: application/json
{"emblemId": "4YldoM0O"}
```

> Use the emblemId from the save step. Expected output: Emblem published; check logs for incoming GET.

### Step 2: Monitor for Incoming Request

**Context**: Observe the controlled server for the SSRF-triggered request.

**Command** (No command; monitor via tool):

> Expected: HTTP GET to https://requestb.in/15rxmgv1 from Rockstar IP.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Reconnaissance]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/requestb-in]]

## Tags

- ssrf
- publish-trigger
