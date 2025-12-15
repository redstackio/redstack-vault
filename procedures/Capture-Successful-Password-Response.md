---
id: proc-002
tags:
  - response-interception
  - proxy
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
updated_at: '2025-12-14T17:31:11.397Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Capture-Successful-Password-Response

## Summary

This procedure uses a web proxy to intercept and store a legitimate HTTP response from Khan Academy's password confirmation endpoint during account linking, which can later be replayed to bypass validation on another session.

## Description

During the account linking process on Khan Academy, the client-side JavaScript prompts for a password and sends it to the server via an AJAX request (e.g., POST to /api/account/verify-password). The server responds with a success indicator if valid. By proxying this traffic, the attacker captures the exact response payload. This exploits the absence of server-side replay protection or unique nonces. The target is the web-based linking flow, with outcomes including a reusable response artifact for manipulation.

## Requirements

1. Active attacker session on Khan Academy
2. Proxy tool (Burp Suite) installed and browser configured to route traffic through it (e.g., 127.0.0.1:8080)
3. Knowledge of external service credentials (e.g., Gmail password)
4. Access to account linking feature

## Defense

Defensive measures and detection strategies:

- Add server-side CSRF tokens or timestamps to responses to prevent replay
- Implement response signing with HMAC to detect tampering
- Log and alert on proxy-like traffic patterns or unusual response sizes

## Objectives

1. Trigger and complete a valid password confirmation
2. Intercept the unaltered server response
3. Store response for later reuse in bypass

## Instructions

### Step 1: Configure Proxy

**Context**: Route browser traffic through Burp Suite to enable interception.

Launch Burp Suite, start the proxy listener on port 8080. In browser settings, set HTTP proxy to 127.0.0.1:8080. Test by navigating to khanacademy.org.

> Expected: All traffic visible in Burp's Proxy > HTTP history tab.

### Step 2: Perform Legitimate Linking

**Context**: Initiate linking to prompt password and submit correctly.

In attacker session, go to account settings > Link Gmail. Enter correct Gmail password when prompted and submit.

> Burp intercepts the POST request; forward it to receive the 200 OK response with success JSON.

### Step 3: Copy Response

**Context**: Extract the full response for replay.

In Burp Repeater or Inspector, copy the response headers and body (e.g., {"success": true, "token": "abc123"}). Save to a text file or note the exact format.

> Verify: Response status 200, no error fields.

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

- [[response-interception]]
- [[proxy]]
