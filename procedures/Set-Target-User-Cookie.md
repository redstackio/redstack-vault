---
tags:
  - cookie-injection
  - account-takeover
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: a4ff1ba3-c821-48c6-996e-71db21fd4028
created_at: '2025-12-14T17:33:11.944Z'
updated_at: '2025-12-14T17:33:11.944Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Set-Target-User-Cookie

## Summary

This procedure injects a session cookie with a target user's ID into the modified login response, enabling full unauthorized access to their account.

## Description

Following response modification, adding a Set-Cookie header with the target user's ID (obtained via enumeration or known value) tricks the client into assuming the target's session. This exploits cookie-based auth without server validation, common in web apps like Mars. The result is complete account takeover, allowing data access and actions as the victim.

## Requirements

1. Modified success response from prior procedure
2. Target user ID (e.g., from public sources or prior recon)
3. Proxy tool for header injection

## Defense

Defensive measures and detection strategies:

- Validate cookies server-side against session state
- Use secure, HttpOnly, SameSite cookies to limit manipulation
- Implement rate limiting and anomaly detection on session creations

## Objectives

1. Bind session to target account
2. Gain persistent unauthorized access
3. Confirm takeover via account actions

## Instructions

### Step 1: Identify Cookie Format

**Context**: Determine the auth cookie structure from app behavior.

Inspect prior legitimate sessions (e.g., via dev tools) to note cookie name (e.g., session_id) and format (e.g., user_id:123).

> Assume base64 or plain ID; test with known account if possible.

### Step 2: Inject Set-Cookie Header

**Context**: Add the header to the modified response.

In Burp Suite, insert: Set-Cookie: session_id=target_user_456; Path=/; Secure

> Replace 456 with actual target ID; ensure expiration and flags match legit cookies.

### Step 3: Validate Access

**Context**: Forward and test the session.

Release response; navigate to protected areas (e.g., profile).

> Expected: Access granted as target user, confirming takeover.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[cookie-injection]]
- [[account-takeover]]
- [[web]]
