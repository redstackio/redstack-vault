---
tags:
  - nextcloud
  - api-replay
  - email-flood
  - devtools
type: procedure
tools:
  - '[[tools/Chrome-Developer-Tools]]'
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:01.511Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 5d1e972b-77be-461c-865b-b28f41065f3a
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
---
# Replay-API-Request-for-Email-Flood-Using-Browser-DevTools

## Summary

This procedure uses browser developer tools to capture and replay the Nextcloud mailtest API request multiple times, enabling continuous email sends to flood the victim's inbox and cause a DoS.

## Description

After sending an initial test email, the XHR request to /settings/admin/mailtest can be intercepted in the browser's network panel and replayed indefinitely due to no rate limiting. This scales the attack to thousands of emails. Requires admin session and dev tools; outcome is overwhelmed victim email service.

## Requirements

1. Active admin session in Nextcloud
2. Browser with developer tools (e.g., Chrome)
3. Prior successful test email to capture the request

## Defense

Defensive measures and detection strategies:

- Implement API rate limiting and session-based throttling on mailtest
- Detect repeated identical requests from the same IP/session
- Block or alert on high-volume email sends from internal APIs

## Objectives

1. Capture and automate replay of mailtest API
2. Flood target inbox with repeated emails
3. Achieve denial-of-service on email delivery

## Instructions

### Step 1: Capture API Request

**Context**: Perform a test send while monitoring network traffic.

Open Chrome Developer Tools (F12), go to Network tab, then click 'Send test mail' from admin settings.

> The panel captures the POST request to /settings/admin/mailtest with status 200.

### Step 2: Replay Request Multiple Times

**Context**: Use the replay feature to send repeated emails.

Right-click the captured XHR request in the network panel and select 'Replay XHR' or copy as cURL and execute in console multiple times.

> Each replay triggers another email send; repeat 100+ times for flood effect.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Chrome-Developer-Tools]]

## Tags

- [[nextcloud]]
- [[dos]]
- [[browser-devtools]]
