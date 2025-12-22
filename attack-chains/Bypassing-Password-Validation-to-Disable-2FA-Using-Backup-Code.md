---
id: ac-2fa-bypass-hackerone
tags:
  - auth-bypass
  - 2fa
  - graphql
  - hackerone
type: attack_chain
tools: []
tactics:
  - '[[Defense Evasion]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Disable-2FA-Without-Password-Verification]]'
step_count: 4
techniques:
  - '[[Reversible Encryption]]'
updated_at: '2025-12-14T17:24:48.421Z'
description: >-
  An attack chain exploiting a vulnerability in HackerOne's 2FA disable process,
  allowing authenticated users to remove two-factor authentication without
  verifying their password, only using a valid backup code, thereby weakening
  account security.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Reversible Encryption]]'
---
# Bypassing Password Validation to Disable 2FA Using Backup Code

Multi-stage attack chain demonstrating how an authenticated user can disable two-factor authentication (2FA) on HackerOne without providing a valid password, relying solely on a valid backup code. This vulnerability was discovered during report submission to a 2FA-mandated program, where entering a random password with a valid backup code successfully disables 2FA. The impact includes reduced account security, making compromise easier if backup codes are obtained by attackers.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~2 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Enable 2FA on Account] --> B[Initiate 2FA Disable] --> C[Submit Invalid Password with Valid Backup Code]
    C --> D[2FA Disabled Without Password Check]

    style A fill:#3498db
    style B fill:#f39c12
    style C fill:#e74c3c
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome with developer tools for GraphQL inspection)

### Target Environment

- HackerOne platform (/settings/auth endpoint)
- GraphQL API backend
- Authenticated user session with 2FA enabled and backup codes generated

### Initial Access Requirements

- Valid authenticated session on HackerOne
- Access to a valid 2FA backup code (generated during 2FA setup)
- No prior compromise needed, but assumes user has enabled 2FA

## Detailed Attack Procedures

### Step 1: Enable 2FA on Account
procedure: [[procedures/Disable-2FA-Without-Password-Verification]]

**Objective**: Set up 2FA to generate backup codes and establish the vulnerable state.

**Instructions**: Log in to HackerOne and navigate to the authentication settings to enable 2FA. This generates backup codes, one of which will be used later.

**Expected Output**: 2FA enabled, backup codes displayed and saved.

**Success Indicators**:
- 2FA status shows as enabled in /settings/auth
- Backup codes are available for use

### Step 2: Initiate 2FA Disable
procedure: [[procedures/Disable-2FA-Without-Password-Verification]]

**Objective**: Trigger the disable confirmation dialog to access the input fields for password and backup code.

**Instructions**: In the /settings/auth page, click the disable icon next to 'Two-factor authentication'. This opens a confirmation window requiring authentication (backup code) and password.

**Expected Output**: Confirmation modal appears with fields for OTP code and password.

**Success Indicators**:
- Modal opens without errors
- Fields for code and password are visible

### Step 3: Submit Invalid Password with Valid Backup Code
procedure: [[procedures/Disable-2FA-Without-Password-Verification]]

**Objective**: Exploit the lack of password validation by submitting a random password alongside a valid backup code.

**Instructions**: In the confirmation window, enter a valid backup code in the OTP field and any random string (e.g., 'wrongpass') in the password field. Click 'Save' to submit the GraphQL mutation [[commands/destroy-two-factor-auth-mutation]].

```json
{"query":"mutation Destroy_two_factor_authentication_credentials_mutation($input_0:DestroyTwoFactorAuthenticationCredentialsInput!,$first_1:Int!,$throttle_time_2:Int!,$first_4:Int!,$size_3:ProfilePictureSizes!) {destroyTwoFactorAuthenticationCredentials(input:$input_0) {clientMutationId,...F1,...F2}} fragment F0 on User {id,totp_supported,totp_enabled,remaining_otp_backup_code_count,account_recovery_phone_number,username,name,_profile_picturePkPpF:profile_picture(size:$size_3)} fragment F1 on DestroyTwoFactorAuthenticationCredentialsPayload {me {id,user_type,_program_health_acknowledgements2aGZgn:program_health_acknowledgements(first:$first_1,throttle_time:$throttle_time_2) {edges {node {id,reason,team_member {user {id},id,team {handle,name,sla_failed_count,id}}},cursor},pageInfo {hasNextPage,hasPreviousPage}},new_feature_notification {name,description,url,id},...F0}} fragment F2 on DestroyTwoFactorAuthenticationCredentialsPayload {me {totp_enabled,remaining_otp_backup_code_count,id},was_successful,_errors3exXYb:errors(first:$first_4) {edges {node {type,field,message,id},cursor},pageInfo {hasNextPage,hasPreviousPage}}}","variables":{"input_0":{"password":"wrongpass","otp_code":"123456","clientMutationId":"9"},"first_1":1,"throttle_time_2":3600,"first_4":100,"size_3":"small"}}
```

**Expected Output**: The mutation executes without password check, returning was_successful: true.

**Success Indicators**:
- No error on password field
- Backup code is consumed (remaining count decreases)

### Step 4: Verify 2FA Disabled
procedure: [[procedures/Disable-2FA-Without-Password-Verification]]

**Objective**: Confirm that 2FA has been successfully disabled, reducing account security.

**Instructions**: Refresh the /settings/auth page or check the 2FA status. The system processes the request via the GraphQL mutation without validating the password.

**Expected Output**: 2FA status shows as disabled; no further 2FA prompts on login.

**Success Indicators**:
- totp_enabled: false in user profile
- Account now accessible with password only

## Attack Chain Summary

### Key Achievements

1. Enabled 2FA and obtained backup codes
2. Bypassed password requirement in disable process
3. Successfully disabled 2FA using only backup code
4. Weakened account security for potential future compromise

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Reversible Encryption]]

### MITRE ATT&CK Tactics

- [[Defense Evasion]]

---
*Last updated: 2023-10-01T00:00:00Z*
