---
tags:
  - shopify
  - checkout-settings
  - privilege-escalation
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploitation for Privilege Escalation]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 0ba0c910-9fd1-4e46-8291-9469760e4cbc
created_at: '2025-12-14T17:29:57.125Z'
updated_at: '2025-12-14T17:29:57.125Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Access-Checkout-Settings-as-Staff

## Summary

Authenticate as a limited staff member and navigate to the checkout settings page to test permission scopes.

## Description

Using the newly created staff account, this procedure logs in and accesses the checkout configuration, which should be allowed under 'Settings' permission. This sets up for further configuration changes. Target is Shopify admin UI; outcome is successful page load confirming access.

## Requirements

1. Staff invitation email and setup link
2. Store admin URL access
3. Basic web browser

## Defense

Defensive measures and detection strategies:

- Log all staff logins and page accesses
- Restrict settings sub-pages by finer permissions
- Alert on unusual navigation patterns from low-priv accounts

## Objectives

1. Validate login with limited permissions
2. Reach sensitive configuration areas
3. Confirm no blocks on settings navigation

## Instructions

### Step 1: Complete Password Setup

**Context**: Use the invitation to initialize the account.

Click the email link and create a secure password.

### Step 2: Login and Navigate

**Context**: Access the admin and go to checkout.

Log in at the store URL, then visit /admin/settings/checkout.

> Expected output: Checkout settings page displays fully.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[shopify]]
- [[staff-login]]
- [[settings-access]]
