---
id: proc-004
tags:
  - response-replay
  - bypass
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:11.392Z'
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
# Replay-Authentication-Response

## Summary

This procedure manipulates the HTTP response in a proxy to replay a captured successful authentication payload during the victim's account linking, deceiving the client-side code into completing the unauthorized link.

## Description

After intercepting the victim's invalid password submission, replace the response with the previously captured success response from the attacker. This bypasses the client-side check since Khan Academy performs confirmation only via JavaScript parsing of the response, without additional server verification. Target: Password confirmation endpoint; outcome: Successful linking of attacker's external account to victim, enabling takeover via password reset.

## Requirements

1. Captured successful response from attacker session
2. Intercepted invalid request from victim in Burp Suite
3. Matching request parameters (e.g., same CSRF token if present)

## Defense

Defensive measures and detection strategies:

- Move all authentication to server-side with session-bound tokens
- Implement response integrity checks (e.g., digital signatures)
- Detect proxy usage via inconsistent headers or timing anomalies

## Objectives

1. Alter response to simulate successful validation
2. Trick client into proceeding with linking
3. Achieve unauthorized account association

## Instructions

### Step 1: Intercept Victim Request

**Context**: Capture the outgoing password submission.

In Burp Proxy, set to intercept client requests. Submit invalid password in victim session; catch the POST request.

> Expected: Request details (body, headers) visible in Intercept tab.

### Step 2: Modify and Forward Response

**Context**: Replace with successful payload.

Forward the request to server if needed, but drop and edit the response: Paste attacker's success JSON/headers. Adjust status to 200 OK. Forward to browser.

> Client-side JS parses as success; linking UI updates accordingly.

### Step 3: Verify Bypass

**Context**: Confirm unauthorized linking completed.

Observe victim's interface: Linking should succeed without error. Test by attempting password reset via linked Gmail.

> Success: External account now tied to victim; attacker can lock out original user.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[response-replay]]
- [[bypass]]
