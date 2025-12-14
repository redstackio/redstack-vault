---
id: ac-shopify-pos-email-hijack-001
tags:
  - shopify
  - broken-access-control
  - account-takeover
  - graphql
  - google-apps
type: attack_chain
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Access-Shopify-POS-Staff-Management]]'
  - '[[procedures/Capture-GraphQL-StaffMemberUpdate-Mutation]]'
  - '[[procedures/Modify-Email-in-GraphQL-Payload]]'
  - '[[procedures/Link-Google-Account-and-Authenticate]]'
step_count: 4
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:46.865Z'
description: >-
  Multi-stage attack exploiting broken access control in Shopify Point of Sale
  to update another staff member's email and link the attacker's Google account,
  enabling account takeover.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
---
id: ac-shopify-pos-email-hijack-001
name: Shopify POS Staff Email Update for Google Account Takeover
type: attack_chain
description: Multi-stage attack exploiting broken access control in Shopify Point of Sale to update another staff member's email and link the attacker's Google account, enabling account takeover.
verified: false
submitted: false
step_count: 4
created_at: 2023-10-01T00:00:00Z
updated_at: 2023-10-01T00:00:00Z
procedures: [[procedures/Access-Shopify-POS-Staff-Management]], [[procedures/Capture-GraphQL-StaffMemberUpdate-Mutation]], [[procedures/Modify-Email-in-GraphQL-Payload]], [[procedures/Link-Google-Account-and-Authenticate]]
techniques: [[Valid Accounts]], [[Exploit Public-Facing Application]]
tactics: [[Initial Access]]
tags: shopify, broken-access-control, account-takeover, graphql, google-apps
platforms: Web
tools: [[tools/Browser-Developer-Tools]]
complexity: medium
skill_level: intermediate
impact_level: high
---

# Shopify POS Staff Email Update for Google Account Takeover

Multi-stage attack chain demonstrating a complete attack workflow exploiting insufficient authorization in Shopify's Point of Sale staff management to hijack staff or owner accounts via Google Apps linkage.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Staff Management] --> B[Capture GraphQL Mutation]
    B --> C[Modify Email Payload]
    C --> D[Link Google Account and Login]
    D --> E[Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Browser-Developer-Tools]]

### Target Environment

- Shopify store configured for Google Apps login
- Target staff or owner account with Shopify ID but no linked Google account
- Attacker has staff member access with Point of Sale permissions

### Initial Access Requirements

- Valid staff credentials for the target Shopify store
- Network access to Shopify POS interface
- Attacker's Google Apps email from the store's configured domain

## Detailed Attack Procedures

### Step 1: Access Staff Management

procedure: [[procedures/Access-Shopify-POS-Staff-Management]]

**Objective**: Navigate to the Point of Sale staff management interface and select the target account to prepare for email modification.

**Instructions**: Log in to the Shopify admin with staff credentials, then access the POS staff page and select the victim's profile.

**Expected Output**: Target staff member's profile loaded in the interface, ready for updates.

**Success Indicators**:
- Staff management page accessible
- Target account selected without errors

### Step 2: Capture GraphQL Mutation

procedure: [[procedures/Capture-GraphQL-StaffMemberUpdate-Mutation]]

**Objective**: Intercept the StaffMemberUpdate GraphQL mutation request to obtain the payload structure for modification.

**Instructions**: Use browser developer tools to monitor network traffic while attempting to save the staff profile, capturing the CURL export of the request.

**Expected Output**: CURL command copied, showing the GraphQL mutation to https://pos-channel.shopifycloud.com/graphql-proxy/admin.

**Success Indicators**:
- Network request captured successfully
- Payload includes StaffMemberUpdate mutation details

### Step 3: Modify Email Payload

procedure: [[procedures/Modify-Email-in-GraphQL-Payload]]

**Objective**: Alter the email field in the captured GraphQL payload to the attacker's Google Apps email, enabling unauthorized linkage.

**Instructions**: Edit the CURL payload's 'email' variable to the attacker's email, then execute the modified request via terminal or tool.

**Expected Output**: Server response confirming the email update without errors.

**Success Indicators**:
- Modified request executes successfully
- Email field updated in the victim's account

### Step 4: Link and Authenticate

procedure: [[procedures/Link-Google-Account-and-Authenticate]]

**Objective**: Log out and re-authenticate using the attacker's Google account to link it to the victim's staff permissions.

**Instructions**: Log out of the current session, then log in using the modified Google Apps email to complete the linkage.

**Expected Output**: Successful login with access to the victim's staff or owner permissions.

**Success Indicators**:
- Google authentication succeeds
- Access granted to victim's account features

## Attack Chain Summary

### Key Achievements

1. Unauthorized email update on staff/owner accounts via GraphQL
2. Linkage of attacker's Google account for persistent access
3. Potential chaining with XSS for full owner takeover without privileges

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
