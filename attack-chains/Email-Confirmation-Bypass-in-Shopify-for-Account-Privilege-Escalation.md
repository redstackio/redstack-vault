---
tags:
  - authentication-bypass
  - privilege-escalation
  - shopify
  - email-verification
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
  - '[[procedures/Retest-Email-Confirmation-Fix]]'
  - '[[procedures/Exploit-Email-Change-Before-Verification]]'
step_count: 2
techniques:
  - '[[Valid Accounts]]'
description: >-
  Multi-stage attack chain exploiting an email confirmation bypass in Shopify to
  achieve privilege escalation and access unowned user accounts.
skill_level: intermediate
impact_level: high
id: 89e78dc0-afe7-4914-a463-6cf7abe958e9
created_at: '2025-12-11T06:10:40.131Z'
updated_at: '2025-12-11T06:10:40.131Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0004]]'
mitre_techniques:
  - '[[T1078]]'
---
# Email Confirmation Bypass in Shopify for Account Privilege Escalation

## Overview

This attack chain demonstrates an authentication bypass vulnerability in Shopify's email confirmation process, discovered during retesting of a previous fix. By changing the email address before receiving the verification on the original email, an attacker can verify an unowned email, leading to full privilege escalation and access to a subset of Shopify user accounts not on the single login system. The chain focuses on verifying the bypass and exploiting it for unauthorized access.

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Retest] --> B[Email Change Exploit]
    B --> C[Privilege Escalation]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- None specified; web browser for interacting with Shopify interface.

### Target Environment

- Platform: Web (Shopify platform)
- Required services: Shopify user accounts, Email confirmation system
- Network access: Standard internet access to myshop.myshopify.com

### Initial Access Requirements

- Existing Shopify account for testing
- Access to the email change functionality
- No special credentials beyond a standard user account

## Detailed Attack Procedures

### Step 1: Retest Previous Vulnerability Fix - [[procedures/Retest-Email-Confirmation-Fix]]

**Objective**: Verify if the previous email confirmation bypass fix is effective, checking that confirmation emails cannot be received and integrations are blocked.

**Instructions**:

Navigate to the email settings in your Shopify account on myshop.myshopify.com. Attempt to initiate an email change and observe if the system prevents confirmation receipt or blocks cross-store integrations as per the fix for report #791775.

Look for indicators that the fix is in place, such as inability to complete changes without verification.

**Expected Output**: Confirmation that the initial fix blocks certain actions, but identifies potential gaps for further exploitation.

**Success Indicators**:
- System blocks integration across stores/partners
- No verification email received on attempted changes

### Step 2: Exploit Email Change Before Verification - [[procedures/Exploit-Email-Change-Before-Verification]]

**Objective**: Change the email address prior to receiving the verification message on the original email, bypassing ownership checks to verify an unowned email.

**Instructions**:

Using the same technique from the previous report, initiate an email change in the Shopify account settings. Before the verification email arrives at the original address, submit a new email address change. This allows the system to verify the new email without proper ownership validation, granting access to accounts not owned by the attacker.

Monitor for successful verification and test access to affected accounts.

**Expected Output**: Successful email verification without ownership, enabling privilege escalation to access a small subset of Shopify user accounts.

**Success Indicators**:
- Email change completes without original verification
- Access granted to unowned accounts not on single login system

## Attack Chain Summary

### Key Achievements

1. Verified gaps in the email confirmation fix
2. Bypassed email ownership checks for unauthorized verification
3. Achieved full privilege escalation to access other user accounts

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Privilege Escalation]]

*Last updated: 2023-10-01*
