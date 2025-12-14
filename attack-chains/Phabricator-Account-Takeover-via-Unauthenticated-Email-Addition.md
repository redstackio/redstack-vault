---
tags:
  - account-takeover
  - auth-bypass
  - phabricator
  - email-manipulation
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Defense Evasion]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Gain-Access-to-Valid-User-Session]]'
  - '[[procedures/Initiate-Email-Addition-in-Account-Settings]]'
  - '[[procedures/Submit-New-Email-Address]]'
  - '[[procedures/Validate-New-Email-Address]]'
  - '[[procedures/Request-Password-Reset-to-New-Email]]'
  - '[[procedures/Use-One-Time-Login-to-Change-Password]]'
step_count: 6
techniques:
  - '[[Valid Accounts]]'
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:30:58.997Z'
description: >-
  Multi-stage attack exploiting Phabricator's lack of re-authentication when
  adding emails, allowing session hijackers to add a controlled email, validate
  it, and perform a password reset for full account takeover.
skill_level: intermediate
impact_level: high
id: bba3617f-992f-46c1-b623-e7ee4b634772
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Account Manipulation]]'
---
# Phabricator Account Takeover via Unauthenticated Email Addition

Multi-stage attack chain demonstrating a complete attack workflow exploiting the Phabricator vulnerability where users with a valid session can add emails without re-authentication, bypassing 2FA and enabling account takeover.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Gain Session Access] --> B[Add New Email]
    B --> C[Validate Email]
    C --> D[Request Password Reset]
    D --> E[Login via One-Time Link]
    E --> F[Change Password and Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#3498db
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser with developer tools for session manipulation

### Target Environment

- Phabricator web application
- Valid user session (e.g., via cookie)
- Control over an arbitrary email address

### Initial Access Requirements

- Valid user session cookie (obtained via hijacking, phishing, or shared access)
- Network access to the Phabricator instance
- No prior password or 2FA knowledge needed beyond session

## Detailed Attack Procedures

### Step 1: Gain Access to a Valid User Session
procedure: [[procedures/Gain-Access-to-Valid-User-Session]]

**Objective**: Obtain a valid session to the target Phabricator account to perform authenticated actions without credentials.

**Instructions**: Use session hijacking techniques such as intercepting cookies via MITM, physical access to a logged-in device, or exploiting long session timeouts. Import the session cookie into your browser's developer tools.

**Expected Output**: Active session allowing access to account settings without login prompts.

**Success Indicators**:
- Successful navigation to dashboard or settings without authentication
- Session cookie validated in browser

### Step 2: Initiate Email Addition in Account Settings
procedure: [[procedures/Initiate-Email-Addition-in-Account-Settings]]

**Objective**: Access the email management interface to begin adding a new address without triggering re-authentication.

**Instructions**: Navigate to the account settings page in Phabricator, typically at `/settings/panel/emails/` or similar, and locate the 'Add Email' form. No password or 2FA is prompted due to the existing session.

**Expected Output**: Form fields for entering a new email address appear.

**Success Indicators**:
- Email addition interface loads
- No authentication challenge issued

### Step 3: Submit New Email Address
procedure: [[procedures/Submit-New-Email-Address]]

**Objective**: Add an attacker-controlled email to the account without additional verification.

**Instructions**: Enter the controlled email address (e.g., attacker@example.com) into the form and submit. The system accepts it without requiring password or 2FA confirmation.

**Expected Output**: Confirmation message that the email has been added and a validation link sent.

**Success Indicators**:
- Email listed in account settings
- Validation email received in controlled inbox

### Step 4: Validate New Email Address
procedure: [[procedures/Validate-New-Email-Address]]

**Objective**: Confirm ownership of the new email to enable its use for resets.

**Instructions**: Access the controlled email inbox and click the validation link sent by Phabricator. This activates the email for the account.

**Expected Output**: Success message confirming email validation in Phabricator settings.

**Success Indicators**:
- Email marked as primary or verified in settings
- No further validation required

### Step 5: Request Password Reset to New Email
procedure: [[procedures/Request-Password-Reset-to-New-Email]]

**Objective**: Trigger a one-time login link to the newly validated email for unauthorized access.

**Instructions**: From the Phabricator login or password reset page (e.g., `/auth/`), initiate a password reset for the target account, selecting the new email as the recovery address.

**Expected Output**: One-time login link emailed to the controlled address.

**Success Indicators**:
- Reset request processed
- Link received in attacker-controlled email

### Step 6: Use One-Time Login to Change Password
procedure: [[procedures/Use-One-Time-Login-to-Change-Password]]

**Objective**: Gain full control by logging in and updating credentials.

**Instructions**: Click the one-time login link to access the account dashboard, then navigate to settings to change the password to an attacker-controlled value.

**Expected Output**: Successful login and password update confirmation.

**Success Indicators**:
- Access to account features
- Old password invalidated

## Attack Chain Summary

### Key Achievements

1. Bypassed 2FA and re-authentication to add a controlled email
2. Validated the email without victim interaction
3. Performed password reset leading to full takeover

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]
- [[Account Manipulation]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Defense Evasion]]

---
*Last updated: 2023-10-01T00:00:00Z*
