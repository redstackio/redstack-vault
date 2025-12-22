---
tags:
  - email-bypass
  - sso-takeover
  - account-takeover
  - shopify
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Sign-Up-for-Shopify-Free-Trial]]'
  - '[[procedures/Access-Shopify-User-Profile]]'
  - '[[procedures/Change-Profile-Email-to-Target]]'
  - '[[procedures/Receive-Confirmation-Email-on-Original-Account]]'
  - '[[procedures/Confirm-Target-Email-via-Bypass]]'
  - '[[procedures/Initiate-SSO-Integration-for-Linked-Accounts]]'
  - '[[procedures/Set-Master-Password-for-Account-Takeover]]'
step_count: 7
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:30:58.676Z'
description: >-
  A multi-stage attack exploiting an email confirmation bypass in Shopify's
  signup process to hijack arbitrary email addresses and takeover linked stores
  through SSO integration.
skill_level: intermediate
impact_level: high
id: 0effe091-23c0-4eff-893d-3fd7b8400cdc
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
  - '[[Account Manipulation]]'
---
# Shopify Email Confirmation Bypass Leading to Multi-Store Account Takeover via SSO

Multi-stage attack chain demonstrating a complete attack workflow exploiting a logic flaw in Shopify's email confirmation during signup and profile updates, enabling unauthorized confirmation of target emails and subsequent takeover of all linked Shopify stores and partner accounts via SSO.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 7 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Sign Up for Trial] --> B[Access Profile]
    B --> C[Change Email to Target]
    C --> D[Receive Confirmation on Attacker Email]
    D --> E[Confirm Target Email]
    E --> F[Initiate SSO Integration]
    F --> G[Set Master Password for Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#3498db
    style F fill:#27ae60
    style G fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome)
- Attacker-controlled email account capable of receiving emails

### Target Environment

- Shopify platform (myshop.myshopify.com)
- Access to internet and email service
- No specific ports required; operates over HTTPS

### Initial Access Requirements

- No prior credentials needed
- Attacker must control an email address
- Target email must be associated with existing Shopify stores or partner accounts

## Detailed Attack Procedures

### Step 1: Sign Up for Free Trial
procedure: [[procedures/Sign-Up-for-Shopify-Free-Trial]]

**Objective**: Create a new Shopify account using an attacker-controlled email to establish a base for the bypass.

**Instructions**: Navigate to the Shopify pricing page and enter signup details with the attacker email. Complete the store setup fields to proceed to the dashboard.

**Expected Output**: Successful creation of a new trial store (e.g., you-shop.myshopify.com) with the attacker email associated.

**Success Indicators**:
- Dashboard access granted
- Confirmation email received at attacker email (if any initial one is sent)

### Step 2: Access User Profile
procedure: [[procedures/Access-Shopify-User-Profile]]

**Objective**: Reach the profile management section to prepare for email modification.

**Instructions**: From the dashboard, click the user avatar in the top-right corner and select 'Your Profile' from the dropdown menu.

**Expected Output**: Profile page loads, displaying current email and other details.

**Success Indicators**:
- Profile page accessible
- Current email shown as attacker-controlled address

### Step 3: Change Email to Target
procedure: [[procedures/Change-Profile-Email-to-Target]]

**Objective**: Update the profile email to the target's address before any confirmation is processed.

**Instructions**: In the email field, enter the target email (e.g., target@example.com) and click 'Save'. The system will queue a confirmation without immediately sending it to the target.

**Expected Output**: Profile saves with the new email pending confirmation; no error on save.

**Success Indicators**:
- Email field updates to target address
- Pending confirmation status implied (no immediate block)

### Step 4: Receive Confirmation Email on Original Account
procedure: [[procedures/Receive-Confirmation-Email-on-Original-Account]]

**Objective**: Intercept the misdirected confirmation email sent to the original signup email due to the logic flaw.

**Instructions**: Check the attacker-controlled email inbox for a message from mailer@shopify.com containing a confirmation link for the email change.

**Expected Output**: Email arrives with a link like 'Confirm your email at myshop.myshopify.com/confirm?token=...' intended for the target but sent to attacker.

**Success Indicators**:
- Email received within seconds to minutes
- Link present in email body

### Step 5: Confirm Target Email via Bypass
procedure: [[procedures/Confirm-Target-Email-via-Bypass]]

**Objective**: Use the intercepted link to confirm the target email without target interaction, hijacking the address.

**Instructions**: Click the confirmation link in the email. This action binds the target email to the attacker's Shopify account.

**Expected Output**: Confirmation success message; profile now shows target email as verified.

**Success Indicators**:
- Account email updated to target
- No further confirmation required from target

### Step 6: Initiate SSO Integration for Linked Accounts
procedure: [[procedures/Initiate-SSO-Integration-for-Linked-Accounts]]

**Objective**: Leverage the hijacked email to discover and integrate other Shopify accounts sharing the same email.

**Instructions**: Return to the profile page; a prompt will appear indicating linked accounts. Click to view and initiate integration for stores or partner accounts.

**Expected Output**: List of linked stores/partners displayed; option to integrate via SSO.

**Success Indicators**:
- Linked accounts detected
- Integration prompt appears

### Step 7: Set Master Password for Account Takeover
procedure: [[procedures/Set-Master-Password-for-Account-Takeover]]

**Objective**: Establish control over all integrated accounts by setting a shared master password.

**Instructions**: Follow the SSO integration flow to create a master password. This grants access to all stores and partners under the email without additional verification.

**Expected Output**: Successful integration; login to target stores using the new master password.

**Success Indicators**:
- Access to target dashboards
- Full owner privileges on multiple stores

## Attack Chain Summary

### Key Achievements

1. Bypassed email confirmation to hijack arbitrary emails
2. Discovered and integrated multiple linked Shopify accounts via SSO
3. Achieved full privilege escalation to owner level across stores and partners

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Valid Accounts]] Valid Accounts
- [[Account Manipulation]] Account Manipulation

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Privilege Escalation]] Privilege Escalation

---
*Last updated: 2023-10-01T12:00:00Z*
