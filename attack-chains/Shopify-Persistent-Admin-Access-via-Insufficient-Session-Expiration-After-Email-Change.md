---
tags:
  - shopify
  - session-expiration
  - auth-bypass
  - persistent-access
type: attack_chain
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Chrome-Beta]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Change-Shopify-Account-Email-Address]]'
  - '[[procedures/Verify-Shopify-Email-Change]]'
  - '[[procedures/Login-to-Shopify-with-Old-Email-in-Separate-Browser]]'
  - '[[procedures/Access-Shopify-Store-with-Old-Session]]'
step_count: 4
techniques:
  - '[[Valid Accounts]]'
  - '[[Use Alternate Authentication Material]]'
updated_at: '2025-12-14T17:28:58.535Z'
description: >-
  Demonstrates how changing a Shopify account email does not invalidate existing
  admin sessions, allowing unauthorized persistent access to stores using old
  credentials for up to two hours.
skill_level: intermediate
impact_level: high
id: b992ec28-1c02-4624-bdeb-ff416c37228c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Use Alternate Authentication Material]]'
---
# Shopify Persistent Admin Access via Insufficient Session Expiration After Email Change

Multi-stage attack chain demonstrating how Shopify's authentication system fails to invalidate admin web sessions upon email changes, enabling unauthorized access to stores and admin panels using outdated credentials.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Change Email] --> B[Verify Change]
    B --> C[Login with Old Email]
    C --> D[Access Store]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Firefox]]
- [[tools/Chrome-Beta]]

### Target Environment

- Web platform
- Shopify Admin and Stores services
- Access to a Shopify account managing multiple stores

### Initial Access Requirements

- Valid Shopify account credentials (email and password)
- Two separate browsers for isolated sessions
- Network access to Shopify's web interface

## Detailed Attack Procedures

### Step 1: Change Account Email
procedure: [[procedures/Change-Shopify-Account-Email-Address]]

**Objective**: Update the primary email address associated with the Shopify account to simulate a credential change scenario.

**Instructions**: Open [[tools/Firefox]] and navigate to the Shopify account settings. Update the email address to a new one and save the changes. This action should trigger a verification process but does not invalidate existing sessions.

**Expected Output**: Confirmation that the new email is set as primary.

**Success Indicators**:
- Email update successful in account settings
- No immediate session termination observed

### Step 2: Verify Email Change
procedure: [[procedures/Verify-Shopify-Email-Change]]

**Objective**: Confirm the email change has taken effect without affecting ongoing sessions.

**Instructions**: In the same browser session ([[tools/Firefox]]), check the account profile to ensure the new email is now listed as the primary contact method.

**Expected Output**: Account profile displays the updated email address.

**Success Indicators**:
- New email verified as active
- Original session remains authenticated

### Step 3: Login with Old Email
procedure: [[procedures/Login-to-Shopify-with-Old-Email-in-Separate-Browser]]

**Objective**: Attempt authentication using the previous email to exploit session persistence.

**Instructions**: Switch to [[tools/Chrome-Beta]] and navigate to the Shopify login page. Enter the old email and password, then input the verification code sent to the old email inbox to complete login.

**Expected Output**: Successful authentication and access to the account dashboard.

**Success Indicators**:
- Login completes without errors
- Access to account features granted despite email change

### Step 4: Access Store with Old Session
procedure: [[procedures/Access-Shopify-Store-with-Old-Session]]

**Objective**: Gain unauthorized entry to managed stores using the persistent session from old credentials.

**Instructions**: From the logged-in session in [[tools/Chrome-Beta]], navigate to a store URL (e.g., https://example.myshopify.com/admin) and perform administrative actions.

**Expected Output**: Full access to store management tools and data.

**Success Indicators**:
- Admin panel loads without re-authentication
- Sensitive store data visible and editable

## Attack Chain Summary

### Key Achievements

1. Email change does not invalidate admin sessions
2. Persistent access to multiple stores using old credentials
3. Potential for data exposure or unauthorized modifications

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Use Alternate Authentication Material]] Use Alternate Authentication Material

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access

---

*Last updated: 2023-10-01T00:00:00Z*
