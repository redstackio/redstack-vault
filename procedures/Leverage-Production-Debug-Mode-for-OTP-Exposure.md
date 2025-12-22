---
id: p2b3c4d5-e6f7-8901-bcde-f2345678901
tags:
  - debug-mode
  - otp-exposure
  - configuration-error
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/curl-trigger-otp-debug]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:24:39.827Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Leverage-Production-Debug-Mode-for-OTP-Exposure

## Summary

This procedure takes advantage of debug mode left enabled in production, allowing direct exposure of OTPs sent to mobile numbers without standard obfuscation or logging protections.

## Description

The application was configured with debug mode active for testing but not disabled, resulting in verbose responses that include plaintext OTPs when requesting mobile verification. Attackers can trigger OTP generation via API and receive the value directly, enabling immediate use for account verification or takeover. This was discovered by appending debug flags to requests after gaining initial access.

## Requirements

1. Valid session or token from prior auth bypass
2. Knowledge of OTP endpoint (e.g., /otp/send)
3. Ability to monitor API responses for debug output
4. Phone number for testing OTP triggers

## Defense

Defensive measures and detection strategies:

- Automate disabling debug flags in production deployments
- Implement environment-specific configurations (e.g., via CI/CD)
- Monitor logs for debug-enabled responses or unusual OTP exposures
- Use WAF rules to block requests with debug parameters

## Objectives

1. Retrieve plaintext OTP for mobile verification
2. Bypass multi-factor protections
3. Chain to full account access

## Instructions

### Step 1: Trigger OTP Generation

**Context**: Send a request to the OTP service with a target mobile number.

Use the API endpoint to initiate OTP send.

**Command** ([[commands/curl-trigger-otp-debug]]):
```bash
curl -X POST https://api.kartpay.com/otp/send -H "Authorization: Bearer access_token" -d '{"phone":"+1234567890"}'
```

> In a debug-enabled environment, the response may include hints; if not, proceed to add debug flag.

### Step 2: Enable Debug and Retrieve OTP

**Context**: Append debug parameter to expose the OTP in the response.

Resubmit with explicit debug flag, as the mode persists.

**Command** ([[commands/curl-trigger-otp-debug]]):
```bash
curl -X POST https://api.kartpay.com/otp/send -H "Authorization: Bearer access_token" -d '{"phone":"+1234567890", "debug":true}'
```

> Expected output: JSON response with field like {"otp": "123456", "debug_info": "..."}, confirming exposure.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Unsecured Credentials]] Unprotected Service

### Sub-Techniques

-

## Commands Used

- [[commands/curl-trigger-otp-debug]]

## Tools Used

-

## Tags

- [[debug-mode]]
- [[otp-exposure]]
- [[configuration-error]]
