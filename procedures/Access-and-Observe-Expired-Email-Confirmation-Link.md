---
tags:
  - auth-bypass
  - discovery
type: procedure
tools:
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: ab77e824-09fd-4a39-be2f-dae786915f9f
created_at: '2025-12-14T17:33:24.373Z'
updated_at: '2025-12-14T17:33:24.373Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access and Observe Expired Email Confirmation Link

## Summary

This procedure accesses an expired email confirmation link to observe the error response, revealing token structure for manipulation and confirming single-use enforcement.

## Description

Loading a previously confirmed or timed-out email link triggers an error, but exposes the token's predictable format (e.g., segments with underscores and digits). This aids in identifying manipulation points for bypass. The issue arises from client-side or weak server-side checks that don't fully invalidate altered tokens.

## Requirements

1. Leaked email confirmation URL (e.g., from dorking)
2. Logged-out browser session
3. [[tools/Web-Browser]]

## Defense

Defensive measures and detection strategies:

- Hash and salt tokens to prevent pattern guessing
- Implement rate limiting on confirmation endpoints
- Use one-time pads or HMAC for token integrity

## Objectives

1. Confirm expiration behavior
2. Analyze token for vulnerabilities
3. Prepare for manipulation

## Instructions

### Step 1: Ensure Logged-Out State

**Context**: Prevent interference from active sessions.

Clear browser cookies for sorare.com and log out if signed in.

> Expected output: No active session; ready for anonymous access.

### Step 2: Load the Expired Link

**Context**: Trigger the confirmation attempt to see the failure mode.

In [[tools/Web-Browser]], load: https://sorare.com/confirm_email?token=Jt7S7WS_4EphEyiDn6z_&redirectUrl=https%3A%2F%2Fsorare.com%2F

> Expected output: Error message "Errors: was already confirmed, please try signing in." Token remains in address bar for inspection.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Web-Browser]]

## Tags

- [[token-manipulation]]
- [[information-disclosure]]
