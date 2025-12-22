---
tags:
  - race-condition
  - email-verification-bypass
  - shopify
  - account-takeover
type: attack_chain
tools:
  - '[[tools/HTTP-Proxy-(e.g.,-Burp-Suite)]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Setup-Shopify-Store-and-Employee-Invitation]]'
  - '[[procedures/Create-Shopify-Partner-Account]]'
  - '[[procedures/Change-Partner-Email-and-Capture-Confirmation-Link]]'
  - '[[procedures/Intercept-and-Time-Email-Change-Request-for-Race-Condition]]'
  - '[[procedures/Confirm-Arbitrary-Email-and-Add-Managed-Store]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
description: >-
  Exploits a race condition in Shopify's Partners Dashboard to bypass email
  verification, confirm arbitrary emails, and gain unauthorized access to stores
  by converting staff accounts to collaborator accounts.
skill_level: intermediate
impact_level: high
id: b96d38f0-7c9a-4514-924f-be72b295cccd
created_at: '2025-12-11T03:47:56.706Z'
updated_at: '2025-12-11T03:47:56.706Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Shopify Partners Dashboard Race Condition for Arbitrary Email Confirmation and Store Takeover

Multi-stage attack chain demonstrating a race condition exploit in Shopify's Partners Dashboard to bypass email verification, confirm arbitrary email addresses, and gain unauthorized access to any associated store by converting a staff account to a collaborator account.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Store] --> B[Setup Partner Account]
    B --> C[Prepare Confirmation Link]
    C --> D[Exploit Race Condition]
    D --> E[Access Store]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/HTTP-Proxy-(e.g.,-Burp-Suite)]]

### Target Environment

- Web platform
- Shopify Partners Dashboard and Shopify Stores services
- Network access to Shopify web interfaces

### Initial Access Requirements

- Attacker-controlled email address
- Access to a Shopify store for testing (or target store details)
- Victim's email address associated with a Shopify store staff account

## Detailed Attack Procedures

### Step 1: Setup Store and Invite Employee - [[procedures/Setup-Shopify-Store-and-Employee-Invitation]]

**Procedure**: [[procedures/Setup-Shopify-Store-and-Employee-Invitation]]

**Objective**: Create a Shopify store and invite an employee to establish a staff account that can later be converted.

**Expected Output**: A staff invitation sent to the employee's email, optionally accepted.

**Success Indicators**:
- Store created successfully
- Invitation email received and optionally accepted

### Step 2: Setup Partner Account - [[procedures/Create-Shopify-Partner-Account]]

**Procedure**: [[procedures/Create-Shopify-Partner-Account]]

**Objective**: Establish or access a Shopify Partners account as the attacker to initiate email changes.

**Expected Output**: Logged into or newly created Partners account.

**Success Indicators**:
- Access to Partners Dashboard at https://partners.shopify.com/[ID]

### Step 3: Change Email and Capture Link - [[procedures/Change-Partner-Email-and-Capture-Confirmation-Link]]

**Procedure**: [[procedures/Change-Partner-Email-and-Capture-Confirmation-Link]]

**Objective**: Change the partner email to an attacker-owned address and capture the confirmation link without visiting it.

**Expected Output**: Confirmation link retrieved from email.

**Success Indicators**:
- Email change initiated
- Confirmation link available for later use

### Step 4: Exploit Race Condition - [[procedures/Intercept-and-Time-Email-Change-Request-for-Race-Condition]]

**Procedure**: [[procedures/Intercept-and-Time-Email-Change-Request-for-Race-Condition]]

**Objective**: Intercept the email change request to the victim's address, release it after a delay, and immediately confirm using the previous link to exploit the race condition.

**Expected Output**: Arbitrary email confirmed due to race condition.

**Success Indicators**:
- Request delayed 1,100-2,500 ms
- Confirmation link visited successfully during the window
- Email confirmation success message

### Step 5: Add Managed Store - [[procedures/Confirm-Arbitrary-Email-and-Add-Managed-Store]]

**Procedure**: [[procedures/Confirm-Arbitrary-Email-and-Add-Managed-Store]]

**Objective**: Add the target store as a managed store, converting the staff account to a collaborator and gaining access.

**Expected Output**: Unauthorized access to the store.

**Success Indicators**:
- Store added to managed stores
- Collaborator access granted

## Attack Chain Summary

### Key Achievements

1. Bypassed email verification via race condition
2. Confirmed arbitrary email address
3. Gained unauthorized access to Shopify store

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

*Last updated: 2023-10-01*
