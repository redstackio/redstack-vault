---
tags:
  - improper-authorization
  - shopify
  - signed-urls
  - third-party-integration
  - authorization-bypass
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
  - Shopify
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Add-Staff-Member-with-Apps-Permission]]'
  - '[[procedures/Install-Shopify-Flow-App]]'
  - '[[procedures/Access-Flow-Connectors-as-Staff]]'
  - '[[procedures/Generate-and-Save-Signed-URLs]]'
  - '[[procedures/Revoke-Staff-Permissions]]'
  - '[[procedures/Reuse-Signed-URLs-to-Modify-Connections]]'
step_count: 6
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:07.365Z'
description: >-
  Attack chain exploiting non-expiring signed URLs in Shopify Flow app to allow
  revoked staff members to modify third-party service connections like Google
  Sheets, Trello, and Asana, leading to unauthorized data access.
skill_level: intermediate
impact_level: high
id: 6f4a2d9b-8f5b-403b-a3d0-f6780bba6eae
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Improper Authorization in Shopify Flow Signed URLs Allowing Unauthorized Third-Party Connections

Multi-stage attack chain demonstrating a complete attack workflow exploiting improper authorization in Shopify Flow's signed URLs for third-party connectors.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Add Staff with Apps Permission] --> B[Install Flow App]
    B --> C[Access Connectors as Staff]
    C --> D[Generate Signed URLs]
    D --> E[Revoke Staff Permissions]
    E --> F[Reuse URLs to Modify Connections]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#9b59b6
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome)
- Access to Shopify admin panel

### Target Environment

- Shopify store with admin access
- Shopify Flow app installed
- Third-party services: Google Sheets, Trello, Asana

### Initial Access Requirements

- Valid Shopify store owner credentials
- Ability to create and manage staff accounts
- No prior network restrictions assumed

## Detailed Attack Procedures

### Step 1: Add Staff Member with Apps Permission
procedure: [[procedures/Add-Staff-Member-with-Apps-Permission]]

**Objective**: Create a staff account with limited 'Apps' permission to simulate an insider or temporary access scenario.

**Instructions**: Log in to the Shopify admin as the owner and navigate to the staff management section to add a new user with only 'Apps' permission enabled.

**Expected Output**: New staff account created and confirmed via email or admin panel.

**Success Indicators**:
- Staff account visible in the admin panel
- Login successful with the new account

### Step 2: Install Shopify Flow App
procedure: [[procedures/Install-Shopify-Flow-App]]

**Objective**: Install the Flow app on the Shopify store to enable workflow and connector functionality.

**Instructions**: From the Shopify admin, search for and install the Flow app from the app store.

**Expected Output**: Flow app installed and accessible in the apps section.

**Success Indicators**:
- App listed in installed apps
- No installation errors

### Step 3: Access Flow Connectors as Staff
procedure: [[procedures/Access-Flow-Connectors-as-Staff]]

**Objective**: Log in as the staff member to access the Flow connectors page for third-party services.

**Instructions**: Log in with staff credentials and navigate to the Flow app's connectors section.

**Expected Output**: Connectors page loaded, showing options for Google Sheets, Trello, Asana.

**Success Indicators**:
- Page accessible without permission errors
- Connector settings visible

### Step 4: Generate and Save Signed URLs
procedure: [[procedures/Generate-and-Save-Signed-URLs]]

**Objective**: Interact with connector settings to generate non-expiring signed URLs containing the path_hmac parameter.

**Instructions**: Click on settings links for Google Sheets, Trello, and Asana, then copy and save the generated URLs, which include parameters like shop_domain, shop_id, and path_hmac.

**Expected Output**: URLs saved, e.g., https://flow-connectors.shopifycloud.com/gsheet/connect?shop_domain=[shop].myshopify.com&shop_id=[shop-id]&path_hmac=[hmac].

**Success Indicators**:
- URLs contain valid path_hmac
- URLs can be opened in browser

### Step 5: Revoke Staff Permissions
procedure: [[procedures/Revoke-Staff-Permissions]]

**Objective**: Remove the staff member's access to simulate a departed employee or permission revocation.

**Instructions**: Log back in as owner and delete or deactivate the staff account via the admin panel.

**Expected Output**: Staff account removed from the list.

**Success Indicators**:
- Account no longer logs in
- Permissions revoked confirmed

### Step 6: Reuse Signed URLs to Modify Connections
procedure: [[procedures/Reuse-Signed-URLs-to-Modify-Connections]]

**Objective**: Use the saved signed URLs to connect or modify third-party accounts despite revoked permissions, gaining unauthorized access to store data.

**Instructions**: Open the saved URLs in a browser and perform actions like connecting personal accounts to workflows.

**Expected Output**: Successful modification of connectors, e.g., linking a personal Google Sheets account.

**Success Indicators**:
- Changes applied without authentication prompts
- Unauthorized access to customer data via workflows

## Attack Chain Summary

### Key Achievements

1. Bypassed authorization by exploiting non-expiring signed URLs with shared path_hmac.
2. Allowed revoked staff to maintain control over third-party integrations.
3. Enabled potential data exfiltration or manipulation through connected services like Google Sheets.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Persistence]] Persistence

---
*Last updated: 2023-10-01T00:00:00Z*
