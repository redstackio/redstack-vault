---
tags:
  - account-takeover
  - authentication-bypass
  - shopify
  - sso
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
commands: []
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Bypass-Shopify-Email-Confirmation]]'
  - '[[procedures/Initiate-Shopify-Account-Review]]'
  - '[[procedures/Authenticate-with-Attacker-Store-Password]]'
  - '[[procedures/Bypass-Master-Password-via-URL-Manipulation]]'
  - '[[procedures/Set-New-Password-for-Victim-Account]]'
  - '[[procedures/Confirm-Shopify-Account-Merger]]'
step_count: 6
techniques:
  - '[[Valid Accounts]]'
  - '[[Modify Authentication Process]]'
description: >-
  Multi-stage attack exploiting email confirmation bypass and account merging
  flaws in Shopify to achieve full merchant account takeover with SSO enabled.
skill_level: intermediate
impact_level: high
id: 25478162-8d57-4bd6-b6da-debc374b2f2b
created_at: '2025-12-13T09:01:26.826Z'
updated_at: '2025-12-13T09:01:26.826Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Modify Authentication Process]]'
---
# Shopify Account Takeover via Email Confirmation Bypass and Account Merging

Multi-stage attack chain demonstrating a complete workflow to bypass email confirmation, exploit an account merging flaw in Shopify, and achieve full takeover of merchant accounts with SSO enabled, without knowing the master password.

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
    A[Email Confirmation Bypass] --> B[Initiate Account Review]
    B --> C[Authenticate with Attacker Password]
    C --> D[Bypass Master Password]
    D --> E[Set New Password]
    E --> F[Confirm Merger and Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#e74c3c
    style E fill:#f39c12
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (web browser only)

### Target Environment

- Web platform
- Shopify services: SSO and Accounts
- Network access to Shopify domains

### Initial Access Requirements

- Victim's email address
- Victim must have SSO enabled but no 2FA
- Ability to create new Shopify stores

## Detailed Attack Procedures

### Step 1: Bypass Email Confirmation
procedure: [[procedures/Bypass-Shopify-Email-Confirmation]]

**Objective**: Create a new store associated with the victim's email by bypassing confirmation.

**Instructions**: Sign up for a new Shopify store (e.g., h48ngalog.myshopify.com) using a similar email to the victim's (e.g., ngalog+1@wearehackeorne.com). Bypass the email confirmation process as detailed in previous report #791775.

**Expected Output**: Successful creation and access to the new store without email verification.

**Success Indicators**:
- New store created
- Email associated without confirmation

### Step 2: Initiate Account Review
procedure: [[procedures/Initiate-Shopify-Account-Review]]

**Objective**: Start the account merging process in the Shopify interface.

**Instructions**: In the newly created store's interface, click the 'Review accounts' button to initiate the merging process.

**Expected Output**: Navigation to the account review page.

**Success Indicators**:
- Account review process started
- Prompt for authentication appears

### Step 3: Authenticate with Attacker Store Password
procedure: [[procedures/Authenticate-with-Attacker-Store-Password]]

**Objective**: Proceed in the merging process using the attacker's own store credentials.

**Instructions**: Enter the password for the newly created attacker-controlled store to authenticate.

**Expected Output**: Successful authentication and progression to the next merging step.

**Success Indicators**:
- Authentication succeeds
- Access to further merging options

### Step 4: Bypass Master Password via URL Manipulation
procedure: [[procedures/Bypass-Master-Password-via-URL-Manipulation]]

**Objective**: Avoid the master password prompt by directly navigating to the password reset endpoint.

**Instructions**: At the /login path with existing query parameters, manually change the URL path to /accounts_merge/new-password while keeping the query string intact.

**Expected Output**: Direct access to the new password setting page without master password requirement.

**Success Indicators**:
- Navigation to new-password page
- No master password prompt

### Step 5: Set New Password for Victim Account
procedure: [[procedures/Set-New-Password-for-Victim-Account]]

**Objective**: Set a new password for the victim's account during merging.

**Instructions**: On the new-password page, enter a new password of choice, choose not to enable 2FA, and submit the form.

**Expected Output**: Password successfully set for the victim's account.

**Success Indicators**:
- Password change confirmation
- Progression to merger confirmation

### Step 6: Confirm Account Merger
procedure: [[procedures/Confirm-Shopify-Account-Merger]]

**Objective**: Finalize the account merger to gain full access to the victim's store.

**Instructions**: On the confirmation page, click the confirm button to complete the merger.

**Expected Output**: Accounts merged, granting access to the victim's store.

**Success Indicators**:
- Full access to victim's merchant account
- Control over store features

## Attack Chain Summary

### Key Achievements

1. Bypassed email confirmation to associate attacker store with victim email
2. Exploited URL manipulation to bypass master password
3. Achieved full account takeover via merging

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]
- [[Modify Authentication Process]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Persistence]]

*Last updated: 2023-10-01*
