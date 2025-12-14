---
id: proc-uuid-2
tags:
  - postmessage
  - xss
  - cross-origin
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:20.880Z'
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
# Send-Malicious-postMessage-from-XSS-Context

## Summary

This procedure uses the XSS context on widgets.wp.com to send a crafted postMessage to a target Jetpack-enabled site, tampering with the 'liker.avatar_URL' to inject an unencoded payload that triggers XSS on the receiver.

## Description

From the exploited preview page, JavaScript sends a postMessage event to an open window or iframe of the target site. The Jetpack plugin's listener accepts messages from widgets.wp.com but fails to encode the avatar_URL before innerHTML insertion. This chains the initial XSS to the target domain. Requires the target site to have Jetpack Likes enabled; outcomes include JS execution on the victim's domain.

## Requirements

1. Successful Step 1 XSS execution
2. Target URL with Jetpack Likes (e.g., wordpress.com post)
3. Browser supporting postMessage API

## Defense

Defensive measures and detection strategies:

- Validate and encode all postMessage data before DOM insertion
- Enforce strict origin checks beyond just widgets.wp.com
- Log cross-origin messages for anomaly detection

## Objectives

1. Deliver tampered payload via postMessage
2. Bypass origin validation in Jetpack listener
3. Propagate XSS to target domain

## Instructions

### Step 1: Embed postMessage in XSS Payload

**Context**: Modify the initial XSS payload to include postMessage sending logic targeting the victim site.

Inject this JS in the onerror or direct script: `var target = window.open('https://target.wordpress.com/post'); target.postMessage({action: 'showOtherGravatars', liker: {avatar_URL: '"%3E%3Cimg%20src=x%20onerror=alert(document.domain)%3E'}}, '*');`

> This opens the target and sends the message. Expected output: Message transmitted, verifiable in dev tools console.

### Step 2: Confirm Message Receipt

**Context**: On the target window, check if the listener processes the payload.

Monitor the target's console for errors or use a proxy to inspect messages.

> Success: No rejection due to origin; payload ready for insertion on interaction (e.g., likes display).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- postmessage
- xss
