---
tags:
  - information-disclosure
  - shopify
  - user-enumeration
  - privacy-breach
type: attack_chain
tools: []
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2024-10-01T00:00:00Z'
procedures:
  - '[[procedures/Login-to-Shopify-Plus-Dashboard]]'
  - '[[procedures/Navigate-to-Add-Users-Page]]'
  - '[[procedures/Enter-Existing-Email-for-Lookup]]'
  - '[[procedures/Submit-Invite-Form-to-Disclose-Name]]'
step_count: 4
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:24:56.690Z'
description: >-
  Multi-stage attack chain exploiting the Shopify Plus user invitation process
  to disclose full names of existing Shopify account holders through email
  enumeration.
skill_level: basic
impact_level: medium
id: bf642f2e-ec46-49a8-831d-538d561fa1f7
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Shopify Plus Information Disclosure via Add Users Email Lookup

Multi-stage attack chain demonstrating a complete attack workflow to enumerate personal information from existing Shopify accounts using the Plus 'Add users' feature.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Basic |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Login to Dashboard] --> B[Navigate to Add Users]
    B --> C[Enter Target Email]
    C --> D[Submit Invite and Disclose Name]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (browser-based interaction)

### Target Environment

- Web platform
- Shopify Plus store with User management permissions
- No specific services or ports required beyond standard HTTPS access

### Initial Access Requirements

- Valid Shopify Plus credentials with User management access
- Direct network access to the Shopify admin dashboard
- No prior compromise needed

## Detailed Attack Procedures

### Step 1: Login to Dashboard
procedure: [[procedures/Login-to-Shopify-Plus-Dashboard]]

**Objective**: Gain access to the Shopify Plus admin panel to enable user management actions.

**Instructions**: Open a web browser and navigate to the Shopify login page. Enter your valid credentials associated with a Shopify Plus account that has User management permissions.

**Expected Output**: Successful redirection to the Shopify Plus dashboard.

**Success Indicators**:
- Dashboard loads without errors
- User management section is visible in the navigation menu

### Step 2: Navigate to Add Users Page
procedure: [[procedures/Navigate-to-Add-Users-Page]]

**Objective**: Reach the user invitation interface where the disclosure vulnerability can be exploited.

**Instructions**: From the dashboard, click on 'Users' in the left sidebar, then select 'Add users'. Alternatively, directly access the URL `https://shopify.plus/[id]/users/invite` where `[id]` is your shop identifier.

**Expected Output**: The 'Add users' form loads, displaying fields for email input and role selection along with a 'Send invite' button.

**Success Indicators**:
- Invite form is visible
- Email input field is present and functional

### Step 3: Enter Existing Email for Lookup
procedure: [[procedures/Enter-Existing-Email-for-Lookup]]

**Objective**: Input an email address linked to an existing Shopify account to trigger the premature disclosure check.

**Instructions**: In the email field of the invite form, enter an email address known or suspected to be associated with an existing Shopify ID, such as `francisbeaudoin+h1-2101@wearehackerone.com`.

**Expected Output**: The form accepts the input without immediate error, preparing for submission.

**Success Indicators**:
- Email field populates correctly
- No validation error for invalid format

### Step 4: Submit Invite Form to Disclose Name
procedure: [[procedures/Submit-Invite-Form-to-Disclose-Name]]

**Objective**: Submit the form to force the system to reveal the full name of the account holder if the email matches an existing Shopify ID.

**Instructions**: Select any available role from the dropdown (e.g., 'Viewer'), then click 'Send invite'. Observe the response on the user page.

**Expected Output**: If the email matches an existing account, the full name (first and last) of the account holder is displayed prematurely, before any invitation acceptance.

**Success Indicators**:
- Full name appears in the interface
- Confirmation of user details without invitation completion

## Attack Chain Summary

### Key Achievements

1. Secure access to Shopify Plus admin with necessary permissions
2. Navigation to the vulnerable invitation endpoint
3. Successful email input triggering backend lookup
4. Disclosure of sensitive personal information (full names) for enumeration

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Account Discovery]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---
*Last updated: 2024-10-01T00:00:00Z*
