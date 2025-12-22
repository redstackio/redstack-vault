---
tags:
  - ssrf
  - image-conversion
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 0b3166f2-df54-443d-ae0b-18279a61a32d
created_at: '2025-12-14T03:46:09.109Z'
updated_at: '2025-12-14T03:46:09.109Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Send-Modified-SVG-for-PNG-Conversion

## Summary

This procedure forwards the tampered SVG to the server, triggering the image converter to process it and fetch resources specified in the malicious xlink:href, resulting in SSRF execution.

## Description

The server-side converter (likely using libraries vulnerable to external fetches) renders the SVG to PNG without checking attributes, making outbound requests to attacker-defined URLs. This can abuse internal trust, scan networks, or chain to other vulns like Imagetragick.

## Requirements

1. Modified SVG payload from prior interception
2. Active proxy session
3. Server endpoint listening for callbacks

## Defense

Defensive measures and detection strategies:

- Validate and sandbox image processing in isolated environments
- Log and block unexpected outbound connections from converters

## Objectives

1. Successfully submit altered data for processing
2. Force server to initiate SSRF requests
3. Confirm fetch attempts via proxy or logs

## Instructions

### Step 1: Forward the Request

**Context**: Release the intercepted WebSocket message to the server.

In Burp, drop the intercept and forward the modified frame.

### Step 2: Monitor Server Processing

**Context**: Watch for PNG generation response.

Observe the server's reply in the WebSocket or HTTP response, which may include the converted image or errors from failed fetches.

**Expected Output**: PNG blob or error image; backend logs (if accessible) show fetch attempts.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[ssrf]]
- [[image-conversion]]
