---
tags:
  - broken-authentication
  - account-takeover
  - password-reset
  - email-change
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Secret-Account]]'
  - '[[procedures/Request-Password-Reset-Link]]'
  - '[[procedures/Change-Account-Email-Address]]'
  - '[[procedures/Use-Old-Password-Reset-Link]]'
  - '[[procedures/Complete-Password-Reset]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:11.448Z'
description: >-
  Exploits a broken authentication mechanism where password reset tokens remain
  valid after an email address change, enabling unauthorized password resets and
  account takeover.
skill_level: intermediate
impact_level: high
id: 317c3eec-e97e-4779-8d06-c0271eafd5bf
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
---
# Account Takeover via Persistent Password Reset Token After Email Change

Multi-stage attack chain demonstrating a complete attack workflow exploiting a flaw in the Secret application's password reset process.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Account] --> B[Request Reset Link]
    B --> C[Change Email]
    C --> D[Logout and Use Old Link]
    D --> E[Reset Password]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome or Firefox)
- Access to two email accounts (one for initial registration, one for the changed email)

### Target Environment

- Secret web application
- Email service for receiving reset links
- No special ports or services beyond standard HTTPS (port 443)

### Initial Access Requirements

- No prior credentials needed; starts with account creation
- Network access to the Secret app and email provider
- Ability to receive and store email links

## Detailed Attack Procedures

### Step 1: Create Account
procedure: [[procedures/Create-Secret-Account]]

**Objective**: Establish an initial foothold by creating a test account on the target application.

**Instructions**: Navigate to the Secret application's registration page and complete the signup process using a controlled email address.

**Expected Output**: Successful account creation with confirmation email sent to the provided address.

**Success Indicators**:
- Account dashboard accessible after login
- Confirmation email received

### Step 2: Request Password Reset Link
procedure: [[procedures/Request-Password-Reset-Link]]

**Objective**: Generate a password reset token without immediately using it, to test token persistence.

**Instructions**: Log out of the account, then initiate a password reset request via the login page, providing the registered email.

**Expected Output**: Password reset link emailed to the original address; do not click it yet.

**Success Indicators**:
- Email containing reset link received and saved
- No password change attempted

### Step 3: Change Email Address
procedure: [[procedures/Change-Account-Email-Address]]

**Objective**: Modify the account's contact email while the reset token remains active, exploiting the lack of token invalidation.

**Instructions**: Log back in with the original credentials, navigate to account settings, update the email to a new address, and complete any verification process for the new email.

**Expected Output**: Email successfully updated in the account profile; verification email sent to and confirmed from the new address.

**Success Indicators**:
- Account settings reflect the new email
- Login still functional with old credentials

### Step 4: Use Old Password Reset Link
procedure: [[procedures/Use-Old-Password-Reset-Link]]

**Objective**: Access the still-valid reset link from the original email to bypass the updated email verification.

**Instructions**: Log out of the account, then open and click the saved password reset link from the original email.

**Expected Output**: Reset form loads without errors, allowing entry of a new password despite the email change.

**Success Indicators**:
- Reset page accessible via old link
- No invalid token error displayed

### Step 5: Complete Password Reset
procedure: [[procedures/Complete-Password-Reset]]

**Objective**: Finalize the unauthorized password change to achieve account takeover.

**Instructions**: On the reset form, enter and confirm a new password, then submit to update the account credentials.

**Expected Output**: Password successfully changed; login with new password grants access to the account.

**Success Indicators**:
- Confirmation message for password update
- Ability to log in with new password, excluding old one

## Attack Chain Summary

### Key Achievements

1. Demonstrated persistence of reset tokens post-email change
2. Achieved unauthorized password reset without new email access
3. Enabled full account takeover for the target user

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Valid Accounts]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Credential Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
