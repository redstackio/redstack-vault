---
id: proc-uuid-1
name: Initiate Password Reset and Capture Tokens
tags:
  - auth-bypass
  - password-reset
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/OWASP-ZAP]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:34.299Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Initiate Password Reset and Capture Tokens

## Summary

This procedure initiates the password reset flow for victim and attacker accounts on Remitly, capturing leaked session parameters and JWT tokens via proxy interception to prepare for token swapping.

## Description

In Remitly's password reset, the /orchestrator/v1/password_reset/start endpoint fails to properly validate session data, leaking sensitive tokens. By intercepting requests for both accounts, the attacker obtains the victim's AMP_d0cf3ed24c (containing deviceId, userId, sessionId) and JWT (with email and other info). This sets up the swap for account takeover. Prerequisites include a proxy tool configured for the browser and access to both emails.

## Requirements

1. Proxy tool (e.g., Burp Suite) running and browser traffic routed through it
2. Attacker's Remitly account with email/phone access
3. Victim's email address
4. Network access to remitly.com

## Defense

Defensive measures and detection strategies:

- Implement strict token binding to user sessions and device IDs with server-side validation
- Rate-limit password reset initiations per IP/email and monitor for proxy-like request patterns
- Log and alert on mismatched session parameters in reset requests

## Objectives

1. Generate and capture session tokens for victim without alerting
2. Obtain attacker's reset flow for OTP integration
3. Identify the correct endpoint leaking JWT (may require testing multiple similar endpoints)

## Instructions

### Step 1: Navigate to Reset Page

**Context**: Access the password reset entry point to begin the flow.

Intercept traffic using [[tools/Burp-Suite]]. No specific command; manual browser navigation.

> Navigate to https://www.remitly.com and click 'Forgot Password'. Expected: Form for email entry.

### Step 2: Initiate for Victim

**Context**: Start reset for victim to capture their tokens.

Submit POST to /orchestrator/v1/password_reset/start with victim's email in the proxy.

> Intercepted request body includes email; response leaks AMP_d0cf3ed24c and JWT. Save these values.

### Step 3: Initiate for Attacker

**Context**: Repeat for attacker to get their flow ready for OTP.

Submit similar POST with attacker's email.

> Capture attacker's response tokens, but prepare to overwrite with victim's.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[auth-bypass]]
- [[password-reset]]
