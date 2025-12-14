---
id: proc-uuid-3
tags:
  - api-abuse
  - app-activation
  - rocket-chat
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/activate-rocket-chat-app-via-api]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:09.733Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Activate-Installed-App-via-API

## Summary

This procedure activates a previously uploaded app in Rocket.Chat by sending an unauthorized POST request to the API endpoint exploiting broken access control to enable the malicious app without admin privileges.

## Description

After uploading an app the `/api/apps/<id>/status` endpoint lacks proper checks allowing non-admins to set the app status to 'manually_enabled'. The attacker uses the app ID from app.json in the request body. This can lead to execution of harmful functionality like RCE. Prerequisites: Installed app and valid session; outcome: Active malicious app compromising the instance.

## Requirements

1. Installed app ID from previous upload step
2. Valid non-admin session
3. HTTP client like curl for API requests

## Defense

Defensive measures and detection strategies:

- Enforce admin-only access to app status APIs
- Audit and validate all app activations with logging
- Disable or restrict app marketplace for untrusted users

## Objectives

1. Enable the installed malicious app
2. Trigger potential compromise actions
3. Confirm activation without admin intervention

## Instructions

### Step 1: Prepare API Request

**Context**: Identify the app ID and construct the JSON payload.

**Command** (Manual):

Use the ID from app.json e.g. "malicious-app".

> Expected output: Payload `{"status":"manually_enabled"}`.

### Step 2: Send Activation Request

**Context**: Execute the POST to activate the app.

**Command** ([[commands/activate-rocket-chat-app-via-api]]):
```bash
curl -X POST http://<rocket-chat-url>/api/apps/<app-id>/status -H "Content-Type: application/json" -d '{"status":"manually_enabled"}'
```

> This sends the request using the session cookie if needed. Expected output: 200 OK response confirming activation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/activate-rocket-chat-app-via-api]]

## Tools Used


## Tags

- api-abuse
- app-activation
- rocket-chat
