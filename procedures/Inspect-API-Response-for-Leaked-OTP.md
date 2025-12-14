---
id: proc-uuid-2
tags:
  - otp-leak
  - response-inspection
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
updated_at: '2025-12-14T17:32:48.485Z'
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
# Inspect-API-Response-for-Leaked-OTP

## Summary

This procedure involves parsing and extracting the OTP code from the API response obtained after submitting a phone number, confirming the leakage vulnerability.

## Description

Following the OTP request, the API returns a JSON object containing sensitive data like the OTP, which should be restricted to SMS delivery. Attackers inspect this using tools like curl output or browser developer tools to retrieve the code. This step is crucial for verifying the vulnerability and obtaining the code for authentication. It applies to web-based authentication flows and assumes prior API interaction.

## Requirements

1. Captured API response from the OTP request step
2. Basic JSON parsing knowledge or tools like jq for extraction
3. Access to command line or browser console

## Defense

Defensive measures and detection strategies:

- Remove OTP from API responses and audit response schemas
- Use response encryption or tokenization for sensitive data
- Implement WAF rules to detect inspection attempts or unusual request patterns

## Objectives

1. Extract the leaked OTP code accurately
2. Validate the vulnerability presence
3. Enable seamless transition to authentication

## Instructions

### Step 1: Parse Response Output

**Context**: Review the raw API response to locate and note the OTP value, typically in a field like "otp" or "code".

**Command** (Manual inspection or with jq):
```bash
curl -X POST https://target.com/api/auth/otp -H "Content-Type: application/json" -d '{"phone": "+1234567890"}' | jq '.otp'
```

> If using jq (optional), this extracts the OTP directly (e.g., outputs "123456"). Otherwise, manually inspect the JSON for the code. Success is extracting a valid 4-6 digit OTP without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- otp-leak
- response-inspection
