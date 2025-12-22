---
id: 8f634c8e-f032-43c8-a5e8-ad5793a7cf09
name: uber-passwordless-signup-postfix-test
type: command
executor: bash
data: >-
  curl -X POST https://cn-geo1.uber.com/rt/users/passwordless-signup -H
  "User-Agent: client/iphone/2.137.1" -H "Connection: close" -H "Content-Type:
  application/json" -d
  '{"phoneNumberE164":"+xxxxx","userWorkflow":"PASSWORDLESS_SIGNUP","userRole":"client","mobileCountryISO2":"XX","state":"CREATE_NEW_PASSWORD","newPasswordData":{"newPassword":"12345678911a!"}}'
output: >-
  {"errorCode":"INVALID_REQUEST","errorMessage":"Jumping state, client side bug
  (or an
  attack)!","phoneNumberE164":"+xxxxx","serverState":"FAILED","tripVerifyStateData":{},"userMessage":"Sorry,
  your request does not match our record. Please wait a few minutes and start
  again.","userRole":"client","userWorkflow":"PASSWORDLESS_SIGNUP"}
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:34.386Z'
platforms:
  - Web
tags:
  - validation
  - remediation-test
verified: false
validated: true
submitted: true
---

# uber-passwordless-signup-postfix-test

## Command

```bash
curl -X POST https://cn-geo1.uber.com/rt/users/passwordless-signup -H "User-Agent: client/iphone/2.137.1" -H "Connection: close" -H "Content-Type: application/json" -d '{"phoneNumberE164":"+xxxxx","userWorkflow":"PASSWORDLESS_SIGNUP","userRole":"client","mobileCountryISO2":"XX","state":"CREATE_NEW_PASSWORD","newPasswordData":{"newPassword":"12345678911a!"}}'
```

## Description

This command tests the Uber passwordless signup endpoint after remediation to confirm it rejects unauthorized state jumps, validating the fix for the authentication bypass vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| phoneNumberE164 | Phone in E.164 format | Yes |
| userWorkflow | PASSWORDLESS_SIGNUP | Yes |
| userRole | 'client' | Yes |
| mobileCountryISO2 | Country code (e.g., 'XX') | Yes |
| state | CREATE_NEW_PASSWORD | Yes |
| newPasswordData.newPassword | Test password | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://cn-geo1.uber.com/rt/users/passwordless-signup -H "User-Agent: client/iphone/2.137.1" -H "Content-Type: application/json" -d '{"phoneNumberE164":"+15551234567","userWorkflow":"PASSWORDLESS_SIGNUP","userRole":"client","mobileCountryISO2":"US","state":"CREATE_NEW_PASSWORD","newPasswordData":{"newPassword":"TestPass123!"}}'
```

### Advanced Usage

Use with verbose output:
```bash
curl -v -X POST ... # (add -v for details)
```

## Expected Output

JSON with serverState: FAILED, errorCode: INVALID_REQUEST, and message indicating state jump rejection.

## Related

- [[Related Procedure: Replay-Uber-Passwordless-Signup-for-Password-Reset]]
