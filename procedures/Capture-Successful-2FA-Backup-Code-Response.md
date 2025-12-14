---
tags:
  - traffic-interception
  - 2fa
  - response-capture
type: procedure
tools:
  - '[[tools/HTTP-Proxy-Interceptor]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:31:30.619Z'
sub_techniques:
  - '[[Credentials In Files]]'
id: c6e849b8-e4f8-43f1-a46d-ed57a8e8a679
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Capture-Successful-2FA-Backup-Code-Response

## Summary

This procedure logs into the Basecamp account using the old password and a 2FA backup code while using a proxy to intercept and save the successful authentication response for later replay in the account takeover.

## Description

With 2FA enabled, the attacker attempts login, provides the backup code at the prompt, and uses an HTTP proxy to capture the response from the 2FA validation endpoint (likely POST to /sessions or similar). This response contains session artifacts that remain valid post-password change due to the vulnerability. Prerequisites include proxy setup and backup code. Expected outcome: Saved response enabling replay.

## Requirements

1. HTTP proxy tool configured (e.g., Burp Suite) to intercept browser traffic
2. Known old password and one backup code
3. Browser session routed through proxy

## Defense

Defensive measures and detection strategies:

- Invalidate all sessions/tokens on password change
- Use short-lived tokens and bind them to password hash
- Detect proxy interception via TLS fingerprinting or HSTS

## Objectives

1. Authenticate via 2FA backup code
2. Intercept the full success response
3. Store response for replay without alerting

## Instructions

### Step 1: Configure Proxy and Initiate Login

**Context**: Set up interception for the login flow.

**Instructions**: Launch proxy tool, configure browser to use it (e.g., set proxy to 127.0.0.1:8080), navigate to sign-in page, submit email and old password.

> Expected output: Proxy shows POST request to login endpoint; response prompts for 2FA.

### Step 2: Submit Backup Code

**Context**: Complete 2FA to trigger success response.

**Instructions**: Enter the backup code in the 2FA prompt form and submit.

> Expected output: Proxy intercepts 200 OK response from 2FA endpoint; save full response (headers, body, cookies).

### Step 3: Verify and Log Out

**Context**: Confirm access and clean up.

**Instructions**: Access dashboard briefly, then log out.

> Expected output: Session active; logout successful.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials

### Sub-Techniques

- [[Credentials In Files]] Credentials In Files (adapted for web responses)

## Commands Used


## Tools Used

- [[tools/HTTP-Proxy-Interceptor]]

## Tags

- [[traffic-interception]]
- [[2fa]]
- [[response-capture]]
