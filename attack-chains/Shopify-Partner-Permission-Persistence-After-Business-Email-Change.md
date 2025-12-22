---
tags:
  - shopify
  - authorization-bypass
  - privilege-escalation
  - information-disclosure
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
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Shopify-Partner-Account-and-Grant-Collaboration]]'
  - '[[procedures/Change-Partner-Business-Email]]'
  - '[[procedures/Access-Store-with-Old-Email-via-Persistent-Permissions]]'
step_count: 3
techniques:
  - '[[Account Manipulation]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:58.574Z'
description: >-
  Multi-stage attack exploiting Shopify's failure to revoke partner
  collaboration permissions when the business email is changed, leading to
  unauthorized persistent access to stores.
skill_level: intermediate
impact_level: high
id: 390ce3bd-e860-47ec-8b65-7384c858a14b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Account Manipulation]]'
  - '[[Valid Accounts]]'
---
# Shopify Partner Permission Persistence After Business Email Change

Multi-stage attack chain demonstrating unauthorized access persistence in Shopify partner accounts due to unrevoked collaboration permissions after email changes.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Partner Account and Collaboration] --> B[Change Business Email]
    B --> C[Exploit Persistent Permissions for Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome)

### Target Environment

- Shopify Partners platform (partners.shopify.com)
- Shopify Accounts (accounts.shopify.com)
- Target Shopify store with owner collaboration approval

### Initial Access Requirements

- Valid business email for initial partner account creation
- Owner approval for store collaboration
- No prior access to target store required beyond collaboration grant

## Detailed Attack Procedures

### Step 1: Setup Partner Account and Collaboration
procedure: [[procedures/Create-Shopify-Partner-Account-and-Grant-Collaboration]]

**Objective**: Establish a partner account linked to a target store via collaboration permissions.

**Instructions**: Register a new Shopify partner account using a controlled business email, then request and obtain collaboration access to the target store from the owner.

Access the Shopify Partners dashboard at https://partners.shopify.com and complete registration. Once confirmed, navigate to the collaborations section and request access to the target store. Await and accept the permission grant from the store owner.

**Expected Output**: Successful login to partner dashboard and visibility of the collaborated store.

**Success Indicators**:
- Partner account confirmed via email
- Collaboration request approved and store accessible in dashboard

### Step 2: Change Business Email
procedure: [[procedures/Change-Partner-Business-Email]]

**Objective**: Modify the partner account's business email to simulate deletion or change, without revoking existing permissions.

**Instructions**: From the partner dashboard settings, update the business email to a new controlled address and confirm the change.

Navigate to account settings in https://partners.shopify.com, locate the business email field, enter the new email, and save. Confirm the update via the verification process.

**Expected Output**: Business email updated successfully in partner profile.

**Success Indicators**:
- New email receives confirmation
- Old email no longer listed as primary in settings

### Step 3: Exploit Persistent Permissions for Access
procedure: [[procedures/Access-Store-with-Old-Email-via-Persistent-Permissions]]

**Objective**: Use the old email to regain unauthorized access to the collaborated store, demonstrating permission persistence.

**Instructions**: Attempt login with the old business email to accounts.shopify.com, then access the previously collaborated store, which grants entry under the original partner name.

First, try direct store login with old email (expect failure). Then, log in to https://accounts.shopify.com using the old email. From the dashboard, navigate to and enter the target store.

**Expected Output**: Successful login to Shopify account and access to the store dashboard as the original partner.

**Success Indicators**:
- Login to accounts.shopify.com succeeds with old email
- Target store accessible despite email change, showing partner name

## Attack Chain Summary

### Key Achievements

1. Persistent unauthorized access to collaboration stores post-email change
2. Potential privilege escalation to developer store ownership
3. Disclosure of store names from separated partner accounts

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Account Manipulation]] Account Manipulation
- [[Valid Accounts]] Valid Accounts

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Privilege Escalation]] Privilege Escalation

---
*Last updated: 2023-10-01T00:00:00Z*
