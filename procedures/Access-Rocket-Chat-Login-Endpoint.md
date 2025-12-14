---
tags:
  - auth-bypass
  - rocket-chat
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:30.850Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 66dd7ad9-05a0-4579-8b19-074be0770372
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Rocket-Chat-Login-Endpoint

## Summary

This procedure establishes initial unauthenticated access to a Rocket.Chat instance by navigating to the login endpoint, ensuring no session exists to prepare for exploitation.

## Description

In the context of exploiting the login-token vulnerability, this step involves accessing the Rocket.Chat web application at the target URL (e.g., http://127.0.0.1:3000) while logged out. The goal is to confirm the instance is reachable and the login interface is presented without any active authentication, setting the stage for injecting payloads into the /api/v1/login endpoint. This targets web-based Rocket.Chat deployments using Node.js and Meteor with MongoDB backend.

## Requirements

1. Network access to the Rocket.Chat server on port 3000
2. Web browser or curl for HTTP requests
3. No existing session cookies

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on login endpoints to detect anomalous access patterns
- Monitor for repeated unauthenticated requests to /api/v1/login

## Objectives

1. Confirm reachability of the unauthenticated login page
2. Ensure clean session state for subsequent exploitation
3. Identify the base URL for targeted requests

## Instructions

### Step 1: Navigate to Target URL

**Context**: Open the Rocket.Chat instance to verify accessibility and login state.

**Command** (using browser or [[tools/curl]] for verification):
```bash
curl -I http://127.0.0.1:3000
```

> This HEAD request checks if the server responds with 200 OK, indicating the instance is live. Expected output includes HTTP/1.1 200 OK and server headers confirming Rocket.Chat.

### Step 2: Confirm No Session

**Context**: Ensure no authentication tokens are present to simulate an external attacker.

**Instructions**: Clear browser cookies or use incognito mode. Attempt to access the dashboard; it should redirect to login.

**Expected Output**: Redirect to /login or similar unauthenticated page.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/curl]]

## Tags

- [[auth-bypass]]
- [[rocket-chat]]
