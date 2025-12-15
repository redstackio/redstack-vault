---
tags:
  - phabricator
  - account-takeover
  - password-reset
  - broken-authentication
  - email-change
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
  - '[[procedures/Create-Phabricator-Account]]'
  - '[[procedures/Request-Phabricator-Password-Reset-Link]]'
  - '[[procedures/Change-Phabricator-Email-Address]]'
  - '[[procedures/Use-Old-Reset-Link-for-Account-Takeover]]'
step_count: 4
techniques:
  - '[[Valid Accounts]]'
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:31:30.995Z'
description: >-
  Multi-stage attack exploiting Phabricator's failure to invalidate password
  reset tokens upon email changes, enabling account takeover using compromised
  old email access.
skill_level: intermediate
impact_level: high
id: 0f196111-37f5-4a04-b03f-b550a75089cc
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Account Manipulation]]'
---
# Phabricator Account Takeover via Non-Expiring Password Reset Tokens After Email Change

Multi-stage attack chain demonstrating a complete attack workflow exploiting a broken authentication mechanism in Phabricator.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Account] --> B[Request Reset Link]
    B --> C[Change Email]
    C --> D[Use Old Reset Link]
    D --> E[Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (manual web interactions)

### Target Environment

- Phabricator web application
- Required services/ports: HTTP/HTTPS on standard web ports (80/443)
- Network access requirements: Direct access to the Phabricator instance and email services

### Initial Access Requirements

- No prior credentials needed for initial account creation
- Access to email inboxes (a@x.com and b@x.com for testing)
- Ability to interact with the web interface

## Detailed Attack Procedures

### Step 1: Create Account
procedure: [[procedures/Create-Phabricator-Account]]

**Objective**: Establish a test account to demonstrate the vulnerability.

**Instructions**: Navigate to the Phabricator registration page and create a new account using the email a@x.com.

**Expected Output**: Successful account creation with confirmation email sent to a@x.com.

**Success Indicators**:
- Account registered and login possible
- Confirmation email received

### Step 2: Request Password Reset
procedure: [[procedures/Request-Phabricator-Password-Reset-Link]]

**Objective**: Generate a password reset token without consuming it.

**Instructions**: Log out of the account, then initiate a password reset request via the login page, providing the email a@x.com. Do not click the link in the received email.

**Expected Output**: Email containing a one-time reset link sent to a@x.com.

**Success Indicators**:
- Reset email received with a valid link
- Link not yet used

### Step 3: Change Email Address
procedure: [[procedures/Change-Phabricator-Email-Address]]

**Objective**: Modify the account's email to invalidate any email-based security assumptions, but leave the old reset token active.

**Instructions**: Log back in using the original credentials, navigate to account settings, update the email to b@x.com, verify the new email, and remove the old email a@x.com.

**Expected Output**: Email successfully changed and verified.

**Success Indicators**:
- New email b@x.com confirmed
- Old email a@x.com removed from account
- Login still functional with original password

### Step 4: Exploit Old Reset Link
procedure: [[procedures/Use-Old-Reset-Link-for-Account-Takeover]]

**Objective**: Use the previously generated reset link to takeover the account despite the email change.

**Instructions**: Access the old reset link from the email sent to a@x.com and use it to set a new password.

**Expected Output**: Password successfully reset, allowing login with the new password.

**Success Indicators**:
- Old link remains valid
- Account password changed
- Full account access achieved

## Attack Chain Summary

### Key Achievements

1. Demonstrated persistence of reset tokens post-email change
2. Enabled account takeover using compromised old email access
3. Highlighted broken authentication in Phabricator's reset mechanism

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Account Manipulation]] Account Manipulation

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access

---

*Last updated: 2023-10-01T00:00:00Z*
