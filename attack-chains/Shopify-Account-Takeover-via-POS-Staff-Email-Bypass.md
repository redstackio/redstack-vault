---
id: bc2a28a2-6dee-4ffd-b6d1-6b4741b49d33
name: Shopify Account Takeover via POS Staff Email Bypass
type: attack_chain
description: >-
  Multi-stage attack exploiting Shopify's POS staff endpoint to bypass email
  verification and takeover accounts without Shopify IDs
verified: false
submitted: true
step_count: 9
created_at: '2025-12-11T06:10:40.646Z'
updated_at: '2025-12-11T06:10:40.646Z'
procedures:
  - '[[procedures/Create-Development-Store-with-Modified-Email]]'
  - '[[procedures/Enable-POS-and-Update-Staff-Email]]'
  - '[[procedures/Merge-Accounts-and-Create-Shopify-ID]]'
techniques:
  - '[[Valid Accounts]]'
  - '[[Modify Authentication Process]]'
tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
tags:
  - shopify
  - account-takeover
  - authentication-bypass
  - email-bypass
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Browser-Console]]'
  - '[[tools/Browser-Dev-Tools]]'
commands:
  - '[[commands/update-organization-email]]'
  - '[[commands/update-user-email]]'
complexity: medium
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0003]]'
mitre_techniques:
  - '[[T1078]]'
  - '[[T1556]]'
---

# Shopify Account Takeover via POS Staff Email Bypass

Multi-stage attack chain demonstrating a complete workflow to exploit a vulnerability in Shopify's POS staff endpoint, allowing bypass of email verification for accounts without Shopify IDs. This enables merging accounts and taking over victim shops by updating staff emails without confirmation.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 9 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Identify Victim Shop] --> B[Create Dev Store]
    B --> C[Modify Email]
    C --> D[Validate Email]
    D --> E[Enable POS]
    E --> F[Access POS Staff]
    F --> G[Modify CURL Request]
    G --> H[Refresh and Merge]
    H --> I[Create Shopify ID]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#f39c12
    style E fill:#3498db
    style F fill:#3498db
    style G fill:#3498db
    style H fill:#27ae60
    style I fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]
- [[tools/Browser-Console]]
- [[tools/Browser-Dev-Tools]]

### Target Environment

- Platform: Web
- Required services: Shopify Partners Dashboard, Point of Sale (POS), GraphQL Proxy, Shopify Accounts
- Tech stack: Ruby on Rails

### Initial Access Requirements

- Access to Shopify partner dashboard
- Control over an email address for validation
- Knowledge of victim shop without Shopify ID

## Detailed Attack Procedures

### Step 1: Identify Victim Shop - [[procedures/Create-Development-Store-with-Modified-Email]]

**Procedure**: [[procedures/Create-Development-Store-with-Modified-Email]]

**Objective**: Target a shop without a Shopify ID to prepare for account merging.

**Expected Output**: Identification of vulnerable shop.

**Success Indicators**:
- Shop confirmed to lack Shopify ID
- No existing account merge

### Step 2: Create Development Store - [[procedures/Create-Development-Store-with-Modified-Email]]

**Procedure**: [[procedures/Create-Development-Store-with-Modified-Email]]

**Objective**: Initiate a new development store via the partner dashboard.

**Expected Output**: New development store created.

**Success Indicators**:
- Store accessible in dashboard

Access https://partners.shopify.com and initiate store creation.

### Step 3: Update Shop Email - [[procedures/Create-Development-Store-with-Modified-Email]]

**Procedure**: [[procedures/Create-Development-Store-with-Modified-Email]]

**Objective**: Modify the email to a controlled non-existing address.

**Expected Output**: Email field updated without validation.

**Success Indicators**:
- Email changed in form data

Use [[tools/Browser-Console]] to execute [[commands/update-organization-email]]:

```javascript
window.RailsData.current_organization.business_email = "nonexistingemail@shopify.com";
```

And [[commands/update-user-email]]:

```javascript
window.RailsData.user.email = "nonexistingemail@shopify.com";
```

Alternatively, intercept with [[tools/Burp-Suite]] to alter the request.

### Step 4: Validate Controlled Email - [[procedures/Create-Development-Store-with-Modified-Email]]

**Procedure**: [[procedures/Create-Development-Store-with-Modified-Email]]

**Objective**: Confirm the modified email.

**Expected Output**: Email validated.

**Success Indicators**:
- Validation link clicked and confirmed

Click the validation link sent to the controlled email.

### Step 5: Add POS to Sales Channels - [[procedures/Enable-POS-and-Update-Staff-Email]]

**Procedure**: [[procedures/Enable-POS-and-Update-Staff-Email]]

**Objective**: Enable Point of Sale in the shop.

**Expected Output**: POS activated.

**Success Indicators**:
- POS visible in admin interface

Enable POS in the shop's admin interface.

### Step 6: Access POS Staff Page - [[procedures/Enable-POS-and-Update-Staff-Email]]

**Procedure**: [[procedures/Enable-POS-and-Update-Staff-Email]]

**Objective**: Navigate to staff management.

**Expected Output**: Staff page loaded.

**Success Indicators**:
- Access to POS > Staff section

Navigate to POS > Staff in the shop admin.

### Step 7: Capture and Modify CURL Request - [[procedures/Enable-POS-and-Update-Staff-Email]]

**Procedure**: [[procedures/Enable-POS-and-Update-Staff-Email]]

**Objective**: Update staff email to victim's without verification.

**Expected Output**: Staff email updated.

**Success Indicators**:
- Modified request sent successfully

Use [[tools/Browser-Dev-Tools]] to copy CURL request, replace email with victim's, and send.

### Step 8: Refresh Profile and Combine Accounts - [[procedures/Merge-Accounts-and-Create-Shopify-ID]]

**Procedure**: [[procedures/Merge-Accounts-and-Create-Shopify-ID]]

**Objective**: Trigger account merge without validation.

**Expected Output**: Merge prompt appears.

**Success Indicators**:
- Accounts combined

Refresh shop profile page.

### Step 9: Create Shopify ID and Takeover - [[procedures/Merge-Accounts-and-Create-Shopify-ID]]

**Procedure**: [[procedures/Merge-Accounts-and-Create-Shopify-ID]]

**Objective**: Finalize takeover by creating ID and optionally changing email.

**Expected Output**: Full account control.

**Success Indicators**:
- Shopify ID created
- Access to victim shop

Proceed with ID creation and change email if desired.

## Attack Chain Summary

### Key Achievements

1. Bypassed email verification for staff updates
2. Merged accounts without confirmation
3. Achieved unauthorized shop ownership transfer

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]
- [[Modify Authentication Process]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Persistence]]

---

*Last updated: [TIMESTAMP]*
