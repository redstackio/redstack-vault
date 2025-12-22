---
id: proc-uuid-3
name: Enter Attacker OTP and Swap Tokens
tags:
  - otp
  - token-swap
type: procedure
tools:
  - '[[tools/Burp-JSON-Web-Token-Extension]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Use Alternate Authentication Material]]'
updated_at: '2025-12-14T17:33:34.294Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Use Alternate Authentication Material]]'
---
# Enter Attacker OTP and Swap Tokens

## Summary

This procedure uses the attacker's OTP from their reset flow and swaps in the victim's captured tokens to prepare the malicious reset request.

## Description

After initiating resets, the attacker receives an OTP via email/phone. The victim's tokens (AMP_d0cf3ed24c, JWT, state_token) are swapped into the attacker's request payload. The Burp JWT extension helps identify and validate tokens. This exploits the lack of binding checks.

## Requirements

1. Captured victim tokens from prior steps
2. Attacker's OTP received
3. Proxy with JWT extension loaded

## Defense

Defensive measures and detection strategies:

- Bind OTP to specific session IDs and validate against them
- Use short-lived tokens with HMAC signing tied to user identity
- Detect token mismatches via anomaly detection in request logs

## Objectives

1. Authenticate attacker's OTP legitimately
2. Integrate victim's session data seamlessly
3. Avoid detection through unmodified OTP flow

## Instructions

### Step 1: Receive and Note OTP

**Context**: Get the one-time password for attacker.

Check attacker's email/phone for OTP sent during their reset.

> OTP is a 6-digit code, valid briefly.

### Step 2: Prepare Swap in Proxy

**Context**: Load attacker's request and identify tokens.

Use [[tools/Burp-JSON-Web-Token-Extension]] to highlight JWT in green.

> Edit AMP_d0cf3ed24c and JWT fields to victim's values.

### Step 3: Insert OTP

**Context**: Add OTP to payload.

Include OTP in the request body as per form fields.

> Payload now has victim's tokens + attacker's OTP.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Use Alternate Authentication Material]] Use Alternate Authentication Material

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-JSON-Web-Token-Extension]]

## Tags

- [[otp]]
- [[token-swap]]
