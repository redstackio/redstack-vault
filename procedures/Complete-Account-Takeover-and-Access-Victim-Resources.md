---
tags:
  - account-takeover
  - privilege-escalation
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Privilege Escalation]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: b9ed785d-cfaa-4faa-9bb3-03fae8779089
created_at: '2025-12-11T06:10:22.793Z'
updated_at: '2025-12-11T06:10:22.793Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0004]]'
mitre_techniques:
  - '[[T1078]]'
---
# Complete Account Takeover and Access Victim Resources

## Summary

This procedure finalizes the account takeover by setting up Shopify ID, entering passwords, and accessing victim resources.

## Description

After bypassing confirmation, attackers review accounts, set up Shopify ID, and establish a new password, gaining full access to the victim's store and partner account. This exploits the escalated privileges from the bypass, targeting non-SSO legacy accounts, with the outcome being unauthorized control over victim assets.

## Requirements

1. Successful confirmation bypass
2. Store password knowledge
3. Access to review accounts section

## Defense

Defensive measures and detection strategies:

- Deploy fixes to remove legacy verification
- Monitor for unauthorized account setups and logins

## Objectives

1. Set up Shopify ID
2. Establish new password
3. Access victim store and accounts

## Instructions

### Step 1: Review Accounts

**Context**: Navigate to review section.

Click on Review accounts.

### Step 2: Enter Store Password

**Context**: Input password for access.

Enter the store's password to proceed.

### Step 3: Set Up Shopify ID and Password

**Context**: Complete setup and set password.

Click Set up Shopify ID, complete the process, click continue, and set a new password.

### Step 4: Access Resources

**Context**: Login and verify access.

Access the victim's store and partner account without restrictions.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- account-takeover
- privilege-escalation
