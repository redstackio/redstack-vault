---
tags:
  - shopify
  - authorization-bypass
  - account-takeover
  - web
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Multiple-Shopify-Partner-Accounts-with-Shared-Email]]'
  - '[[procedures/Submit-Collaborator-Access-Request-to-Target-Store]]'
  - >-
    [[procedures/Trigger-Automatic-Account-Conversion-with-Second-Partner-Account]]
  - '[[procedures/Access-Target-Store-as-Active-Collaborator]]'
step_count: 4
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:01.294Z'
description: >-
  Multi-stage attack exploiting improper authorization in Shopify's partner
  system to gain unauthorized collaborator access to any target store by
  manipulating account conversion logic with shared emails.
skill_level: intermediate
impact_level: high
id: 66076da9-5624-47b7-b8dd-4e2a4bdec29c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
---

# Shopify Admin Authentication Bypass via Partner Account Conversion

Multi-stage attack chain demonstrating a complete attack workflow exploiting an improper authorization vulnerability in Shopify's partner account system.

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
    A[Create Shared Email Accounts] --> B[Submit Access Request]
    B --> C[Trigger Conversion]
    C --> D[Gain Store Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome)
- Valid business email address

### Target Environment

- Shopify Partners platform (partners.shopify.com)
- Target Shopify store
- No specific ports required; web-based access

### Initial Access Requirements

- Internet access
- Ability to register free Shopify partner accounts
- No prior credentials on target store needed

## Detailed Attack Procedures

### Step 1: Create Multiple Partner Accounts
procedure: [[procedures/Create-Multiple-Shopify-Partner-Accounts-with-Shared-Email]]

**Objective**: Establish two partner accounts using the same business email to exploit conversion logic.

**Instructions**: Navigate to partners.shopify.com and register the first partner account using a business email (e.g., attacker@business.com). Immediately register a second partner account using the exact same business email without completing verification on the first.

**Expected Output**: Two pending or active partner accounts linked to the shared email.

**Success Indicators**:
- Dashboard access for both accounts
- Email confirmation received for registrations

### Step 2: Submit Collaborator Access Request
procedure: [[procedures/Submit-Collaborator-Access-Request-to-Target-Store]]

**Objective**: Initiate a pending collaborator request on the target store using the first account.

**Instructions**: From the first partner account's dashboard, search for the target store and submit a collaborator access request, providing details like role (e.g., full access).

**Expected Output**: Pending request status visible in the dashboard.

**Success Indicators**:
- Request submitted successfully
- Pending notification in partner dashboard

### Step 3: Trigger Automatic Conversion
procedure: [[procedures/Trigger-Automatic-Account-Conversion-with-Second-Partner-Account]]

**Objective**: Use the second account to force automatic conversion of the pending request due to shared email detection.

**Instructions**: Log in to the second partner account. The system detects the shared email and existing pending request, applying conversion logic that activates the collaborator status without merchant approval.

**Expected Output**: Request status changes from pending to active.

**Success Indicators**:
- Active collaborator badge appears
- No merchant approval prompt

### Step 4: Gain Store Access
procedure: [[procedures/Access-Target-Store-as-Active-Collaborator]]

**Objective**: Log in to the target store's admin panel with full permissions.

**Instructions**: From the partner dashboard, navigate to the target store and select login. Use the collaborator credentials to access the admin interface.

**Expected Output**: Full admin access to the store dashboard.

**Success Indicators**:
- Successful login without additional authentication
- Ability to perform admin actions (e.g., view orders, edit products)

## Attack Chain Summary

### Key Achievements

1. Bypassed merchant approval for collaborator access
2. Gained unauthorized full permissions on any Shopify store
3. Exploited account conversion flaw using shared emails

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access

---

*Last updated: 2023-10-01T00:00:00Z*
