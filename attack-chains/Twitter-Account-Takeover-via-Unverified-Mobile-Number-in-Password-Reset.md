---
tags:
  - broken-authentication
  - account-takeover
  - mobile-verification
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Add-Unverified-Mobile-Number-to-Account]]'
  - '[[procedures/Log-Out-After-Mobile-Number-Addition]]'
  - '[[procedures/Reset-Password-Using-Unverified-Mobile-Number]]'
step_count: 3
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:58.810Z'
description: >-
  Multi-stage attack exploiting broken authentication in Twitter's mobile
  verification to associate an unverified mobile number with an account,
  enabling password reset and account takeover.
skill_level: intermediate
impact_level: high
id: 3f47dce9-61ac-4670-b848-4d64268cfc6f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Twitter-Account-Takeover-via-Unverified-Mobile-Number-in-Password-Reset

Multi-stage attack chain demonstrating a complete attack workflow exploiting broken authentication in Twitter's (now X) mobile verification process to enable unauthorized password resets and account takeover.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Add Unverified Mobile Number] --> B[Log Out] --> C[Password Reset with Unverified Number] --> D[Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome or Firefox with developer tools for inspection)

### Target Environment

- Twitter web platform
- Access to a target Twitter account (e.g., via credentials or session)
- Control over a mobile number (attacker's own or random for testing)

### Initial Access Requirements

- Valid session or credentials for the target Twitter account
- No special network access beyond standard internet
- No prior access to the mobile number verification service needed beyond web interface

## Detailed Attack Procedures

### Step 1: Add Unverified Mobile Number
procedure: [[procedures/Add-Unverified-Mobile-Number-to-Account]]

**Objective**: Associate an unverified or random mobile number with the target account without completing verification, priming it for password reset abuse.

**Instructions**: Log in to the target Twitter account using a web browser. Navigate to the account settings, specifically the mobile section. Select the country code, enter a random or controlled mobile number (e.g., your own number that you can receive SMS on), and submit the request. The system will indicate that a verification code has been sent but will not enforce entering the code to associate the number loosely with the account.

**Expected Output**: Confirmation message stating a code was sent to the mobile number, but the flow proceeds without verification input, allowing the number to be linked for reset purposes.

**Success Indicators**:
- Mobile number input accepted without code entry
- Account settings reflect the number as added (even if unverified)

### Step 2: Log Out After Mobile Number Addition
procedure: [[procedures/Log-Out-After-Mobile-Number-Addition]]

**Objective**: Terminate the current session to simulate a lost access scenario, forcing reliance on the password reset flow.

**Instructions**: From the account settings or main dashboard, select the logout option. Confirm the logout to end the session completely.

**Expected Output**: Redirect to the Twitter login page, confirming the session is terminated.

**Success Indicators**:
- Successful logout with no active session
- Inability to access account features without re-authentication

### Step 3: Reset Password Using Unverified Mobile Number
procedure: [[procedures/Reset-Password-Using-Unverified-Mobile-Number]]

**Objective**: Exploit the unverified number association to receive and use a password reset code, completing the account takeover.

**Instructions**: Navigate to the Twitter forgot password page. Enter the target account's username or email, then select the option to reset via mobile number. Input the previously added unverified mobile number. The system will send a reset code to that number without verifying its prior association. Receive the SMS code on the controlled number, enter it to proceed, and set a new password.

**Expected Output**: Successful password reset confirmation, allowing login with the new credentials.

**Success Indicators**:
- Reset code received on the controlled mobile number
- New password set and account access gained

## Attack Chain Summary

### Key Achievements

1. Bypassed mobile verification during number addition
2. Enabled unauthorized password reset using a controlled number
3. Achieved full account takeover without legitimate credentials

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
