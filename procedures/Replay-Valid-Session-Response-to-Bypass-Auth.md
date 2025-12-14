---
id: proc-wakatime-replay-session
tags:
  - session-replay
  - auth-bypass
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:42.996Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Replay Valid Session Response to Bypass Auth

## Summary

This procedure modifies an intercepted invalid login response in Burp Suite by replacing it with a captured valid one, allowing session hijacking in WakaTime to bypass authentication and rate limits for unauthorized access.

## Description

Exploiting the root cause of no token invalidation or replay protection, the attacker swaps the entire HTTP response (status, headers, cookies) from a failed login attempt with the legitimate one. This results in the browser accepting the valid session despite wrong credentials, enabling access to /dashboard and persistent interactions like data theft or modification. Impact includes indefinite token persistence.

## Requirements

1. Captured valid login response from Step 1
2. Intercepted invalid response from Step 2
3. Burp Suite Repeater or Inspector for response editing
4. Ongoing proxy session

## Defense

Defensive measures and detection strategies:

- Use CSRF tokens, nonces, or timestamps in responses to prevent replay
- Implement server-side session binding and revocation on errors
- Detect proxy tampering via TLS fingerprinting or behavioral anomalies

## Objectives

1. Hijack session for unauthorized access
2. Bypass 429 rate limits on failed logins
3. Maintain persistence for data exfiltration

## Instructions

### Step 1: Modify Intercepted Response

**Context**: Replace invalid response contents with valid ones to simulate success.

In Burp Intercept, edit the response: Set status to 302, Location: /dashboard, paste valid Set-Cookie headers and body.

> Ensure all session tokens are included; remove any error indicators.

### Step 2: Forward Modified Response

**Context**: Deliver the replayed response to the browser to establish the session.

Click "Forward" in Burp to send the altered response.

> Browser should redirect to /dashboard as if login succeeded.

### Step 3: Verify and Maintain Session

**Context**: Confirm access and use the session for further actions.

Send follow-up requests (e.g., GET /dashboard) using the replayed cookies.

> Expected: Full account access, including sensitive data like API keys and coding activity.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- session-replay
- auth-bypass
