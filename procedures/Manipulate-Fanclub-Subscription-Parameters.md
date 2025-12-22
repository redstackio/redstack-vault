---
tags:
  - parameter-tampering
  - improper-authorization
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:33:24.455Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: d0b301e2-50ff-433a-82bd-1058575a62d8
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Manipulate Fanclub Subscription Parameters

## Summary

This procedure exploits improper authorization in Chaturbate's fanclub subscription process by tampering with request parameters to subscribe to a target user's account instead of the attacker's own, setting the stage for further manipulation.

## Description

In the fanclub subscription flow, the backend fails to validate that the subscription target matches the authenticated user, allowing parameter modification to specify any username. This is tested by intercepting the POST request to the subscription endpoint and altering the 'username' field. Prerequisites include an active attacker session and knowledge of the target's username. Successful manipulation allows the subscription to proceed unauthorized, enabling email setting in the next stage.

## Requirements

1. Registered Chaturbate account for the attacker
2. Proxy tool like Burp Suite for request interception
3. Target user's exact username
4. Valid session cookies from login

## Defense

Defensive measures and detection strategies:

- Implement strict authorization checks to ensure subscription targets match the authenticated user
- Validate all user-input parameters against session data on the server side
- Log and monitor subscription requests for parameter mismatches or unusual targets
- Rate-limit subscription attempts per user

## Objectives

1. Bypass authorization to target arbitrary accounts in the subscription flow
2. Enable unauthorized modifications to the target account
3. Prepare for email injection without triggering alerts

## Instructions

### Step 1: Intercept Subscription Request

**Context**: Start the fanclub subscription process for a test or the attacker's own account to capture the baseline request, then modify it for the target.

Use Burp Suite to proxy traffic and intercept the POST request to the subscription endpoint (typically /subscribe or similar).

**Command** (Manual via Proxy):
Intercept and edit the request body to change the 'username' parameter from your own to the target's, e.g.:

```http
POST /api/subscribe HTTP/1.1
Host: chaturbate.com
Cookie: session=your_session
Content-Type: application/json

{"username": "target_username", "plan": "monthly", "email": "attacker@example.com"}
```

> This modifies the target without server-side rejection due to missing checks. Expected response: 200 OK with subscription initiation.

### Step 2: Forward and Verify

**Context**: Send the tampered request and confirm it processes as if legitimate.

Forward the request in Burp and check the response for success indicators like a payment redirect.

> No specific command; monitor for errors. Success: No 403 Forbidden or auth failure.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Account Manipulation]] Account Manipulation

### Sub-Techniques


## Commands Used


## Tools Used

- [[Burp Suite]]

## Tags

- [[parameter-tampering]]
- [[improper-authorization]]
