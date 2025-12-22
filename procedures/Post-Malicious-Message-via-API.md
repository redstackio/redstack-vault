---
tags:
  - api-post
  - xss-injection
  - message-delivery
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-post-malicious-message-to-rocket-chat]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 422b241e-4390-452c-a74e-ff14e82d5c85
created_at: '2025-12-14T03:47:13.115Z'
updated_at: '2025-12-14T03:47:13.115Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Post-Malicious-Message-via-API

## Summary

This procedure uses the Rocket.Chat REST API to post the crafted JSON payload containing the XSS attachment, injecting the stored vulnerability into the channel for admin viewing.

## Description

The /api/v1/chat.postMessage endpoint accepts attachments without validating 'value' fields, leading to direct HTML rendering. Auth via token and user ID headers. When admins view, the onerror executes, alerting cookies. Impacts: theft, escalation, leakage, RCE potential in Electron, wormability.

## Requirements

1. Personal Access Token and User ID
2. Malicious JSON file ('cookiesplz.json')
3. curl or similar HTTP client
4. Server URL and channel access

## Defense

Defensive measures and detection strategies:

- Input validation and HTML escaping in attachment rendering
- Rate limiting on chat.postMessage API
- Log and scan API payloads for JS/HTML patterns
- Update to patched Rocket.Chat versions

## Objectives

1. Deliver stored XSS to target channel
2. Trigger execution on admin views for cookie theft
3. Enable further attacks like privilege escalation or RCE

## Instructions

### Step 1: Prepare Headers and Endpoint

**Context**: Set up authentication for the API call.

Gather: Token, User ID, Server URL (e.g., https://chat.example.com).

### Step 2: Execute API Post

**Context**: Send the payload using curl to inject the message.

Execute [[commands/curl-post-malicious-message-to-rocket-chat]]:

```bash
curl -H "X-Auth-Token: <Token>" -H "X-User-Id: <user Id>" -H "Content-type:application/json" https://<server>/api/v1/chat.postMessage -d @cookiesplz.json
```

> Expected output: {"success": true, "message": {...}}. The message appears in '#cookies'; viewing triggers alert(document.cookie).

### Step 3: Verify Execution

**Context**: Confirm XSS fires on view.

Have an admin (or self in test) view the channel; check for alert popup with cookies.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-post-malicious-message-to-rocket-chat]]

## Tools Used

- [[tools/curl]]

## Tags

- [[api-post]]
- [[xss-injection]]
- [[message-delivery]]
