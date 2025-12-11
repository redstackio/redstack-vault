---
tags:
  - auth-bypass
  - sso-takeover
  - email-confirmation
  - privilege-escalation
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Privilege Escalation]]'
commands: []
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Shopify-Free-Trial-Signup]]'
  - '[[procedures/Access-and-Edit-User-Profile-in-Shopify]]'
  - '[[procedures/Change-Email-to-Target-and-Trigger-Confirmation]]'
  - '[[procedures/Receive-and-Use-Misrouted-Confirmation-Email]]'
  - '[[procedures/Verify-Target-Email-via-Confirmation-Link]]'
  - '[[procedures/Integrate-SSO-and-Set-Master-Password-for-Takeover]]'
step_count: 6
techniques:
  - '[[Valid Accounts]]'
  - '[[Use Alternate Authentication Material]]'
description: >-
  Multi-stage attack exploiting an email confirmation bypass in Shopify to
  confirm arbitrary emails and achieve full privilege escalation via SSO
  integration, enabling takeover of shop owner accounts.
skill_level: intermediate
impact_level: high
id: 57e928fd-da52-45af-bc0c-bfc9d9141c55
created_at: '2025-12-11T06:10:40.594Z'
updated_at: '2025-12-11T06:10:40.594Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0004]]'
mitre_techniques:
  - '[[T1078]]'
  - '[[T1550]]'
---
# Shopify Email Confirmation Bypass Leading to SSO Account Takeover

## Overview

This attack chain exploits a vulnerability in Shopify's email confirmation system during profile edits, allowing an attacker to confirm arbitrary email addresses without access to them. By signing up with an attacker-controlled email, changing it to the target's email, and receiving the confirmation link at the original email, the attacker can verify the target's email on their account. This enables SSO integration with the target's existing Shopify stores, leading to full account takeover by setting a master password. The attack was discovered through testing signup and profile processes on Shopify's free trial and impacts shop owners by granting control over their stores, though mitigated for single-login accounts.

## Attack Flow Visualization

```mermaid
graph LR
    A[Signup with Attacker Email] --> B[Access Profile]
    B --> C[Change to Target Email]
    C --> D[Receive Confirmation Email]
    D --> E[Click Verification Link]
    E --> F[Integrate SSO and Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
    style E fill:#e74c3c
    style F fill:#f39c12
```

## Prerequisites & Requirements

### Required Tools

- None (browser and email client sufficient)

### Target Environment

- Web-based platform: Shopify (*.myshopify.com)
- Required services: Shopify SSO, Email system
- Network access: Public internet access to Shopify site and attacker-controlled email

### Initial Access Requirements

- Attacker-controlled email address that can receive emails
- Knowledge of target email address associated with Shopify stores
- No prior credentials needed

## Detailed Attack Procedures

## Step 1: Signup with Attacker Email - [[procedures/Shopify-Free-Trial-Signup]]

### Objective

Create a new Shopify account using an attacker-controlled email to establish a base for the bypass.

### Instructions

Visit the Shopify pricing page and sign up for a free trial using an email like attacker@gmail.com.

### Expected Output

Successful account creation and access to the Shopify dashboard.

### Success Indicators

- Receipt of welcome email
- Ability to log in to the new store

## Step 2: Access Profile - [[procedures/Access-and-Edit-User-Profile-in-Shopify]]

### Objective

Navigate to the user profile section to prepare for email modification.

### Instructions

After entering the store, click on the name in the top right corner and select 'Your Profile'.

### Expected Output

Access to the profile editing page.

### Success Indicators

- Profile details are displayed and editable

## Step 3: Change to Target Email - [[procedures/Change-Email-to-Target-and-Trigger-Confirmation]]

### Objective

Modify the email to the target's address, triggering the flawed confirmation process.

### Instructions

Update the email field to the target email (e.g., yaworsk@hackerone.com) and click save.

### Expected Output

System triggers email confirmation, but link is sent to original email.

### Success Indicators

- No immediate error; confirmation process initiates

## Step 4: Receive Confirmation Email - [[procedures/Receive-and-Use-Misrouted-Confirmation-Email]]

### Objective

Obtain the confirmation link sent erroneously to the attacker's original email.

### Instructions

Check the attacker-controlled email (e.g., attacker@gmail.com) for the confirmation message from mailer@shopify.com.

### Expected Output

Email containing the verification link for the target email.

### Success Indicators

- Email received with valid link

## Step 5: Verify Target Email - [[procedures/Verify-Target-Email-via-Confirmation-Link]]

### Objective

Confirm the target's email on the attacker's Shopify instance using the link.

### Instructions

Click the link in the email to verify the target email.

### Expected Output

Target email is confirmed on the attacker's account.

### Success Indicators

- Confirmation success message
- Target email now associated with attacker's profile

## Step 6: Integrate SSO and Takeover - [[procedures/Integrate-SSO-and-Set-Master-Password-for-Takeover]]

### Objective

Use SSO to integrate and gain control over the target's stores by setting a master password.

### Instructions

In the profile, select to integrate accounts sharing the same email and follow prompts to set a master password.

### Expected Output

Access to all stores under the target email.

### Success Indicators

- Successful integration
- Ability to manage target's stores

## Attack Chain Summary

### Key Achievements

1. Arbitrary email confirmation without access to target inbox
2. SSO-based privilege escalation to shop owner accounts
3. Control over multiple stores via master password setup

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]
- [[Use Alternate Authentication Material]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Privilege Escalation]]

*Last updated: 2023-10-01*
