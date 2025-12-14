---
tags:
  - cookie-replay
  - session-hijacking
  - auth-bypass
type: procedure
tools:
  - '[[tools/Burp-Proxy]]'
  - '[[tools/Burp-Repeater]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Pass the Hash]]'
updated_at: '2025-12-14T17:31:30.800Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 8d979407-03e5-4bab-ac0e-37dceb542fb9
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Pass the Hash]]'
---
# Replay-Cookies-to-Bypass-Authentication

## Summary

This procedure replays captured session cookies in a new unauthenticated session to bypass logout protections and regain access to the victim's account.

## Description

Using tools like Burp, the original cookies are manually inserted into a fresh request to a protected endpoint. Due to lack of invalidation, the server treats it as valid, allowing impersonation. This exploits OWASP A2 broken authentication in web apps.

## Requirements

1. Captured cookie values from prior session
2. Burp Suite configured for interception and replay
3. Target admin endpoint URL

## Defense

Defensive measures and detection strategies:

- Invalidate sessions on logout by changing token values
- Implement CSRF token rotation per request
- Detect cookie reuse via IP/user-agent mismatch logging

## Objectives

1. Inject stolen cookies into new request
2. Bypass authentication checks
3. Restore full session privileges

## Instructions

### Step 1: Intercept New Request

**Context**: In the unauthenticated session, trigger a request to the admin page for interception.

Navigate to the admin edit page in the new session and refresh to intercept with Burp Proxy.

### Step 2: Modify Cookies in Repeater

**Context**: Replace the empty or invalid cookies with originals.

Forward to Burp Repeater, paste the captured cookies (__cfduid, csrf_token, session) into the Cookie header, and update the request.

**Expected Output**: Modified request with original auth tokens.

### Step 3: Forward and Verify

**Context**: Send the tampered request to the server.

Click Forward in Repeater to replay the request.

**Expected Output**: Server responds with successful access, no login required.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Pass the Hash]] Pass the Ticket

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Proxy]]
- [[tools/Burp-Repeater]]

## Tags

- cookie-replay
- session-hijacking
