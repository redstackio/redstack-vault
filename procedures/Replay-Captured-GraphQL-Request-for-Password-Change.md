---
tags:
  - replay
  - bypass
  - account-takeover
type: procedure
tools:
  - '[[tools/Charles-Proxy]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:25:52.972Z'
sub_techniques: []
id: 72b99b82-b25c-4c18-b395-0927a729df84
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Replay-Captured-GraphQL-Request-for-Password-Change

## Summary

This procedure replays a captured GraphQL mutation request after sign-out to unauthorizedly change a HackerOne user's password, exploiting the delay in session and token invalidation for account takeover.

## Description

Post-password change and sign-out, the x-auth-token and __Host-session remain valid for 5-20 minutes. By replaying the captured mutation with modified new password values via proxy, an attacker bypasses re-authentication. This targets the GraphQL endpoint handling password updates, demonstrating a critical authentication flaw if requests are obtained via MiTM or logs.

## Requirements

1. Captured GraphQL request from prior step (including tokens and payload)
2. Active Charles Proxy session
3. Replay within token expiration window (monitor timestamps)

## Defense

Defensive measures and detection strategies:

- Immediately invalidate all sessions/tokens on password changes
- Rate-limit and validate mutations against current session state
- Detect replay attempts via request fingerprinting or timing anomalies

## Objectives

1. Successfully update password without re-authentication
2. Validate token reuse post-sign-out
3. Achieve control over the target account

## Instructions

### Step 1: Modify Captured Request

**Context**: Adjust the payload for the desired new password while retaining auth headers.

In Charles Proxy, open the captured request, edit the GraphQL variables section to change the new password value (e.g., update 'newPassword' field), but keep x-auth-token and __Host-session unchanged.

> Modified request ready; ensure mutation structure (e.g., updateUser mutation) is intact.

### Step 2: Replay the Request

**Context**: Send the altered request to the GraphQL endpoint post-sign-out.

Execute the replay immediately after sign-out, targeting the same backend endpoint (inferred from capture, e.g., /graphql). Monitor for success response.

> Server accepts the request, returns success (e.g., { "data": { "updateUser": { "user": { ... } } } }); no auth error if within window.

### Step 3: Validate Takeover

**Context**: Confirm the password change by attempting login.

Navigate to https://hackerone.com/users/sign_in and log in with the original username and newly set password.

> Successful login indicates takeover; original password no longer works.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Charles-Proxy]]

## Tags

- replay
- bypass
- account-takeover
