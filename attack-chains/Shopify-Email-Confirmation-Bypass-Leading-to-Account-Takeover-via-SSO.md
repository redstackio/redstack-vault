---
tags:
  - authentication-bypass
  - account-takeover
  - sso
  - shopify
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Privilege Escalation]]'
commands: []
platforms:
  - Web
  - Cloud
complexity: low
procedures:
  - '[[procedures/Sign-Up-for-Shopify-Free-Trial-with-Controlled-Email]]'
  - '[[procedures/Access-Shopify-User-Profile]]'
  - '[[procedures/Change-Email-to-Target-in-Shopify-Profile]]'
  - '[[procedures/Receive-Shopify-Confirmation-Email-at-Original-Address]]'
  - '[[procedures/Click-Misdirected-Confirmation-Link-for-Target-Email]]'
  - '[[procedures/Integrate-Other-Accounts-via-Shopify-SSO]]'
  - '[[procedures/Set-Master-Password-for-Integrated-Shopify-Stores]]'
step_count: 7
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
description: >-
  Exploits a vulnerability in Shopify's email confirmation process during free
  trial signups to bypass confirmation and escalate privileges to any shop
  owner's account via SSO integration.
skill_level: beginner
impact_level: high
id: d811fa69-5e83-4223-8a6a-a88436dd67d4
created_at: '2025-12-13T09:01:26.853Z'
updated_at: '2025-12-13T09:01:26.853Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Shopify Email Confirmation Bypass Leading to Account Takeover via SSO

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 7 |
| Execution Time | ~10 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Step 1: Signup] --> B[Step 2: Access Profile] --> C[Step 3: Change Email] --> D[Step 4: Receive Email] --> E[Step 5: Confirm Link] --> F[Step 6: Integrate SSO] --> G[Step 7: Set Password]
    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#e74c3c
    style E fill:#f39c12
    style F fill:#3498db
    style G fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None

### Target Environment

- Web-based Shopify platform
- Services: Shopify SSO, Shopify Email System
- Network access requirements: Internet access to Shopify websites and email inbox

### Initial Access Requirements

- Ability to access an email account controlled by the attacker
- No prior credentials needed; starts with free trial signup
- Web browser for interacting with Shopify interface

## Detailed Attack Procedures

### Step 1: Sign Up for Free Trial
procedure: [[procedures/Sign-Up-for-Shopify-Free-Trial-with-Controlled-Email]]

**Objective**: Create a new Shopify account using a controlled email to initiate the attack.

**Instructions**: Visit https://www.shopify.com/pricing and complete the signup process for a free trial using an email address like attacker@gmail.com that you can access.

**Expected Output**: Successful creation of a Shopify free trial account.

**Success Indicators**:
- Account created
- Access to the new store dashboard

### Step 2: Access User Profile
procedure: [[procedures/Access-Shopify-User-Profile]]

**Objective**: Navigate to the profile section to prepare for email change.

**Instructions**: After entering the store, click on the name in the top right corner and navigate to 'Your Profile'.

**Expected Output**: User profile page loaded.

**Success Indicators**:
- Profile settings accessible

### Step 3: Change Email to Target
procedure: [[procedures/Change-Email-to-Target-in-Shopify-Profile]]

**Objective**: Update the account email to the target's email address.

**Instructions**: In the profile, update the email field to the target's email (e.g., yaworsk@hackerone.com) and submit the changes.

**Expected Output**: Email change request processed, triggering confirmation email.

**Success Indicators**:
- Email update saved without immediate confirmation

### Step 4: Receive Confirmation Email
procedure: [[procedures/Receive-Shopify-Confirmation-Email-at-Original-Address]]

**Objective**: Obtain the misdirected confirmation link sent to the original email.

**Instructions**: Check the original email inbox (attacker@gmail.com) for the confirmation email from mailer@shopify.com containing the link intended for the new email.

**Expected Output**: Email received with confirmation link.

**Success Indicators**:
- Confirmation link available in controlled inbox

### Step 5: Click Confirmation Link
procedure: [[procedures/Click-Misdirected-Confirmation-Link-for-Target-Email]]

**Objective**: Verify the target's email using the misdirected link.

**Instructions**: Click the link in the received email to confirm and update the account to the target's email.

**Expected Output**: Email confirmation successful, account now associated with target's email.

**Success Indicators**:
- Account email updated to target

### Step 6: Integrate with Other Accounts via SSO
procedure: [[procedures/Integrate-Other-Accounts-via-Shopify-SSO]]

**Objective**: Link other Shopify accounts associated with the confirmed email.

**Instructions**: In the profile, select the option to integrate other Shopify accounts linked to the now-confirmed target email.

**Expected Output**: Accounts integrated via SSO.

**Success Indicators**:
- Access to additional stores granted

### Step 7: Set Master Password
procedure: [[procedures/Set-Master-Password-for-Integrated-Shopify-Stores]]

**Objective**: Gain full control by setting a new password for all integrated stores.

**Instructions**: Follow the on-screen instructions to change the password for all stores under the target email.

**Expected Output**: Master password set, full access achieved.

**Success Indicators**:
- Password reset successful
- Control over all associated stores

## Attack Chain Summary

### Key Achievements

1. Bypassed email confirmation by exploiting misdirected link
2. Confirmed arbitrary target email without access
3. Escalated privileges to take over multiple Shopify stores via SSO

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Privilege Escalation]]

*Last updated: 2023-10-01*
