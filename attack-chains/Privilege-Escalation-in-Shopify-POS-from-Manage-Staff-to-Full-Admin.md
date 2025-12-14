---
tags:
  - privilege-escalation
  - shopify
  - pos
  - ui-bypass
  - auth-bypass
type: attack_chain
tools: []
tactics:
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Staff-with-Full-Permissions]]'
  - '[[procedures/Create-POS-User-with-Manage-Staff-Permissions]]'
  - '[[procedures/Login-to-POS-with-Admin-then-Switch-to-Limited-User]]'
  - '[[procedures/Change-PIN-of-Full-Permissions-Staff-in-POS]]'
  - '[[procedures/Lock-and-Re-login-to-POS-with-New-PIN]]'
  - '[[procedures/Navigate-to-Edit-Staff-POS-Access-and-Manage-POS-Roles]]'
  - '[[procedures/Open-Full-Permissions-Role-and-Click-on-Assigned-Staff]]'
  - '[[procedures/Click-Manage-Shopify-Admin-Access-from-Roles-Page]]'
  - '[[procedures/Click-Breadcrumb-to-Plan-and-Permissions-Admin-Page]]'
step_count: 9
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:29:10.060Z'
description: >-
  A multi-stage privilege escalation attack in Shopify's Point of Sale
  application, allowing a user with limited 'Manage Staff' permissions to bypass
  UI controls and access full store owner-level admin privileges via nested
  navigation paths.
skill_level: intermediate
impact_level: high
id: b727e324-33c4-4d4a-a495-461a956e2c4c
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Privilege Escalation in Shopify POS from Manage Staff to Full Admin

Multi-stage attack chain demonstrating a complete privilege escalation workflow in Shopify's Point of Sale (POS) application, exploiting improper access controls in the UI to elevate a limited 'Manage Staff' role to full store owner-level admin access.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 9 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Full Access Staff] --> B[Create Limited POS User]
    B --> C[Login and Switch in POS]
    C --> D[Modify PIN for Escalation]
    D --> E[Re-login with Elevated PIN]
    E --> F[Navigate to Staff Edit]
    F --> G[Access Roles and Staff]
    G --> H[Trigger Admin Access Link]
    H --> I[Reach Full Admin Page]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#f39c12
    style E fill:#3498db
    style F fill:#3498db
    style G fill:#3498db
    style H fill:#3498db
    style I fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser for accessing Shopify admin and POS app
- Physical or emulated access to POS terminal

### Target Environment

- Shopify store with POS application enabled
- Admin access to create staff accounts
- POS app launched on a device (e.g., iPad or desktop)

### Initial Access Requirements

- Valid store owner or admin credentials for initial login
- Ability to create and manage staff in Shopify admin
- No additional network access beyond standard Shopify login

## Detailed Attack Procedures

### Step 1: Setup Full Access Staff
procedure: [[procedures/Create-Staff-with-Full-Permissions]]

**Objective**: Prepare a staff account with unrestricted permissions to facilitate later escalation.

**Instructions**: Log in to the Shopify admin dashboard. Navigate to Settings > Users and permissions > Staff. Click 'Add staff' and assign full permissions to all sections, including admin access. Save the new staff account.

**Expected Output**: A new staff member with complete store access created.

**Success Indicators**:
- Staff account listed with full permissions badge
- Account can perform any admin action if tested

### Step 2: Create Limited POS User
procedure: [[procedures/Create-POS-User-with-Manage-Staff-Permissions]]

**Objective**: Establish a low-privilege POS-specific user role limited to staff management.

**Instructions**: In Shopify admin, go to Settings > Users and permissions > Staff. Edit or create a new staff account. Under 'Retail' permissions, enable only 'Manage staff' and disable all others. Assign a PIN for POS access and save.

**Expected Output**: Staff account with restricted POS role confirmed in retail settings.

**Success Indicators**:
- Permission list shows only 'Manage staff' checked
- User can log in to POS but lacks broader access

### Step 3: Initial POS Login and User Switch
procedure: [[procedures/Login-to-POS-with-Admin-then-Switch-to-Limited-User]]

**Objective**: Gain entry to the POS app using owner credentials and switch to the limited user context.

**Instructions**: Launch the Shopify POS application on the terminal. Log in with store owner admin credentials. Once inside, enter the PIN of the limited POS user from Step 2 to switch sessions.

**Expected Output**: POS interface loads under the limited user's permissions.

**Success Indicators**:
- UI shows limited options, e.g., only staff management visible
- No errors on PIN entry

### Step 4: Modify PIN of Elevated Staff
procedure: [[procedures/Change-PIN-of-Full-Permissions-Staff-in-POS]]

**Objective**: Update the PIN of the full-permissions staff to enable controlled re-authentication.

**Instructions**: In the POS app (under limited user), navigate to the Staff section. Select the full-permissions staff from Step 1. Edit the account and set the POS PIN to '1234'. Save changes.

**Expected Output**: PIN updated successfully for the target staff.

**Success Indicators**:
- Confirmation message on save
- Staff list reflects the change

### Step 5: Re-authenticate with Elevated Context
procedure: [[procedures/Lock-and-Re-login-to-POS-with-New-PIN]]

**Objective**: Lock the session and re-enter using the modified PIN to inherit full permissions.

**Instructions**: Lock the POS application screen. Re-authenticate by entering the new PIN '1234' associated with the full-permissions staff.

**Expected Output**: POS unlocks with expanded UI options reflecting full permissions.

**Success Indicators**:
- Broader menu items now accessible
- No permission denial errors

### Step 6: Access Staff POS Settings
procedure: [[procedures/Navigate-to-Edit-Staff-POS-Access-and-Manage-POS-Roles]]

**Objective**: Enter the staff management interface to initiate the escalation path.

**Instructions**: In POS Staff section, select any staff member. Edit their POS app access settings. Click the 'Manage POS Roles' link to proceed to the roles listing.

**Expected Output**: Roles management page loads within POS context.

**Success Indicators**:
- Page transitions without errors
- Roles list visible

### Step 7: Inspect Full Role Assignment
procedure: [[procedures/Open-Full-Permissions-Role-and-Click-on-Assigned-Staff]]

**Objective**: Navigate deeper into the role details to expose hidden admin links.

**Instructions**: On the roles page, open the full-permissions role from Step 1. Scroll to the bottom to the 'Assigned Staff' section. Click on any assigned staff member.

**Expected Output**: Staff details panel opens within the role context.

**Success Indicators**:
- Assigned staff clickable and expands
- No access denied messages

### Step 8: Trigger Admin Access Navigation
procedure: [[procedures/Click-Manage-Shopify-Admin-Access-from-Roles-Page]]

**Objective**: Exploit the UI link to bridge POS and full admin interfaces.

**Instructions**: Scroll to the bottom of the staff details and click 'Manage Shopify admin access'. This loads the Plan & Permissions staff page from the admin.

**Expected Output**: Shopify admin Plan & Permissions page appears, bypassing POS limits.

**Success Indicators**:
- URL shifts to admin domain path
- Full staff management options visible

### Step 9: Reach Core Admin Settings
procedure: [[procedures/Click-Breadcrumb-to-Plan-and-Permissions-Admin-Page]]

**Objective**: Complete escalation by accessing owner-level account settings.

**Instructions**: At the top of the Plan & Permissions page, click the breadcrumb navigation for 'Plan and Permissions'. This directs to https://shop.myshopify.com/admin/settings/account.

**Expected Output**: Full admin account settings page loads, granting owner features like ownership transfer.

**Success Indicators**:
- Access to sensitive actions (e.g., add staff, transfer ownership)
- No permission prompts or blocks

## Attack Chain Summary

### Key Achievements

1. Elevated limited POS user to full admin without direct credentials
2. Bypassed permission checks via UI navigation chaining
3. Enabled potential store takeover through owner settings access

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### MITRE ATT&CK Tactics

- [[Privilege Escalation]] Privilege Escalation

---
*Last updated: 2023-10-01T00:00:00Z*
