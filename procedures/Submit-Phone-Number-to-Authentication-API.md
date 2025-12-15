---
id: proc-uuid-1
tags:
  - otp-leak
  - api-request
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-submit-phone]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:48.489Z'
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
# Submit-Phone-Number-to-Authentication-API

## Summary

This procedure submits a phone number to the target authentication API endpoint, triggering OTP generation and leaking the code in the response, exploiting improper API response handling.

## Description

In vulnerable web applications using phone-based OTP for authentication, the API endpoint for requesting OTPs inadvertently includes the generated code in the JSON response body. This allows attackers to obtain the OTP without receiving the SMS, facilitating unauthorized access. The procedure targets public-facing web APIs and requires only HTTP access. Expected outcomes include receiving a response with the OTP, enabling subsequent authentication steps.

## Requirements

1. Network access to the target web application's API (HTTPS)
2. Knowledge of the OTP request endpoint (e.g., /api/auth/otp)
3. A fabricated or target phone number in international format (e.g., +1XXXXXXXXX)

## Defense

Defensive measures and detection strategies:

- Ensure OTP codes are never included in API responses; transmit only via secure SMS
- Implement rate limiting on OTP requests per IP or phone number
- Log and monitor API responses for anomalous access patterns

## Objectives

1. Trigger OTP generation without legitimate user intent
2. Leak the OTP for immediate exploitation
3. Prepare for authentication bypass

## Instructions

### Step 1: Prepare and Send OTP Request

**Context**: Craft a JSON payload with the phone number and submit it via POST to the authentication endpoint to initiate the leak.

**Command** ([[commands/curl-submit-phone]]):
```bash
curl -X POST https://target.com/api/auth/otp -H "Content-Type: application/json" -d '{"phone": "+1234567890"}'
```

> This command sends the phone number to the API, which generates and leaks the OTP in the response (e.g., {"success": true, "otp": "123456"}). Success is indicated by a 200 OK status and visible OTP.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-submit-phone]]

## Tools Used


## Tags

- otp-leak
- api-request
