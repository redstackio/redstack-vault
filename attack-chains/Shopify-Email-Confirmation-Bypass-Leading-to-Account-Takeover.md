---
tags:
  - auth-bypass
  - email-bypass
  - privilege-escalation
  - shopify
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
  - '[[procedures/Retest-Email-Change-Fix-in-Shopify]]'
  - '[[procedures/Exploit-Email-Confirmation-Bypass-in-Shopify]]'
step_count: 2
techniques:
  - '[[Modify Authentication Process]]'
  - '[[Valid Accounts]]'
description: >-
  A race condition in Shopify's email change process allows bypassing
  verification to take over unowned accounts and escalate to shop owner
  privileges.
skill_level: intermediate
impact_level: high
id: 135587d8-1278-487a-9b8c-65fa5690d329
created_at: '2025-12-14T17:30:58.652Z'
updated_at: '2025-12-14T17:30:58.652Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Modify Authentication Process]]'
  - '[[Valid Accounts]]'
---
# Shopify Email Confirmation Bypass Leading to Account Takeover

## Overview

This attack chain exploits a vulnerability in Shopify's account management system where an attacker can change their email address before the verification message arrives on the original email. Discovered during retesting of a prior fix on February 14, 2020, this bypass allows verification of an unowned email, leading to full control over affected shop owner accounts that have not migrated to the single login system. The impact includes privilege escalation, potentially compromising a subset of legacy Shopify users.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Retest Prior Fix] --> B[Exploit Email Bypass]
    B --> C[Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome with developer tools for timing)

### Target Environment

- Shopify account management portal (myshop.myshopify.com/admin)
- Web platform with access to account settings

### Initial Access Requirements

- Valid Shopify login credentials for a test or target account
- Ability to receive emails on the original account
- No special network access beyond internet connectivity

## Detailed Attack Procedures

### Step 1: Retest Email Change Fix
procedure: [[procedures/Retest-Email-Change-Fix-in-Shopify]]

**Objective**: Verify the status of a previous email confirmation fix and identify if the email change process still allows premature modifications.

**Instructions**: Log in to the Shopify admin panel at myshop.myshopify.com/admin. Navigate to account settings and attempt to initiate an email change. Monitor the verification process to check if changes can be made before the original email verification completes. Use browser developer tools to inspect network requests and time the email delivery.

**Expected Output**: Confirmation that the system sends a verification email to the original address but permits immediate email updates in settings.

**Success Indicators**:
- Email change option available without completing prior verification
- No blocking mechanism observed during retest

### Step 2: Exploit Email Confirmation Bypass
procedure: [[procedures/Exploit-Email-Confirmation-Bypass-in-Shopify]]

**Objective**: Change the email to an unowned address and verify it before the original verification email arrives, enabling account takeover.

**Instructions**: In the account settings, update the email field to a new, attacker-controlled address. Quickly verify the new email using the confirmation link sent to it, racing against the delivery to the original email. Once verified, the account binds to the new email, granting full access including shop owner privileges.

**Expected Output**: Successful login and control using the new email, with access to admin functions.

**Success Indicators**:
- New email verified without original email confirmation
- Ability to perform privileged actions like managing shop settings

## Attack Chain Summary

### Key Achievements

1. Bypassed email verification through timing manipulation
2. Achieved privilege escalation to shop owner on legacy accounts
3. Demonstrated full account takeover without owning the original email

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Modify Authentication Process]]
- [[Valid Accounts]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Privilege Escalation]]

---
*Last updated: 2023-10-01T00:00:00Z*
