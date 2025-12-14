---
tags:
  - xss
  - postmessage
type: procedure
tools:
  - '[[tools/Browser-DevTools]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/postmessage-setwindowlocation]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 37b6a1ca-2ee8-4190-b324-ab46c36846c1
created_at: '2025-12-13T23:56:03.998Z'
updated_at: '2025-12-13T23:56:03.998Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Verify Self-XSS via PostMessage

## Summary

This procedure verifies self-XSS by posting a message with a javascript: URL to an iframed embedded app using Browser DevTools.

## Description

The procedure tests the DOM XSS vulnerability in a controlled self-environment by sending a postMessage to trigger Shopify.API.setWindowLocation with a payload like javascript:alert(document.domain). This confirms the sink before escalating to victim exploitation. Requires an iframed app and DevTools access.

## Requirements

1. Iframed Shopify embedded app
2. Browser DevTools
3. JavaScript console access

## Defense

Defensive measures and detection strategies:

- Validate protocols in navigation functions
- Monitor postMessage events for suspicious payloads

## Objectives

1. Send malicious postMessage
2. Trigger XSS payload
3. Confirm execution

## Instructions

### Step 1: Open DevTools Console

**Context**: Navigate to the page with the iframed app and open console.

> Identify the iframe element.

### Step 2: Execute PostMessage

**Context**: Send the message to trigger setWindowLocation with XSS payload.

**Command** ([[commands/postmessage-setwindowlocation]]):
```javascript
$$('iframe')[0].contentWindow.postMessage('{"message":"Shopify.API.setWindowLocation","data":"javascript:alert(document.domain);0[0]"}','*')
```

> This sends the payload to execute alert(document.domain).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used

- [[commands/postmessage-setwindowlocation]]

## Tools Used

- [[tools/Browser-DevTools]]

## Tags

- xss
- postmessage
