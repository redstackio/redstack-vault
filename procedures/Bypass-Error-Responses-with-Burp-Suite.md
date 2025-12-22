---
tags:
  - response-manipulation
  - bypass
  - logic-flaw
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 2a6357bd-b29e-405f-832a-5b42d668f144
created_at: '2025-12-14T17:33:12.393Z'
updated_at: '2025-12-14T17:33:12.393Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass-Error-Responses-with-Burp-Suite

## Summary

This procedure intercepts and modifies HTTP responses from the API to bypass AngularJS frontend error checks, allowing the flow to proceed with invalid data.

## Description

The API returns 400 Bad Request with {"status":"error"} for issues like invalid usernames or tokens, but the frontend relies on status codes and body. Using Burp Suite, change to 200 OK and {"status":"ok"} to trick the client. This aids bruteforce and initiation steps. ReCAPTCHA is not enforced server-side.

## Requirements

1. Burp Suite proxy intercept enabled
2. Traffic routed through Burp
3. Ongoing API interactions

## Defense

Defensive measures and detection strategies:

- Server-side validation with no client reliance
- Use HTTPS and validate integrity
- Monitor for anomalous response patterns

## Objectives

1. Override error responses
2. Advance the reset flow
3. Facilitate takeover

## Instructions

### Step 1: Intercept Response

**Context**: During any API call (e.g., initiation or verification), Burp captures the response.

**Instructions**: In Burp Repeater or Proxy, edit the response: Set status to 200 OK, body to {"status":"ok"}. Forward to browser.

> Applies to errors in steps 1-3. Frontend proceeds as if successful.

### Step 2: Verify Bypass

**Context**: Confirm the AngularJS app advances (e.g., next form loads).

> No command; visual confirmation in browser.

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

- [[response-manipulation]]
- [[bypass]]
- [[logic-flaw]]
