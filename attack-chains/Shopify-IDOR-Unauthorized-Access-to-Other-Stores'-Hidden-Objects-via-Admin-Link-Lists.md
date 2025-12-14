---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - idor
  - shopify
  - unauthorized-access
  - admin-panel
  - improper-authentication
type: attack_chain
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Shopify-Link-List-IDOR]]'
step_count: 6
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:28:58.408Z'
description: >-
  An IDOR vulnerability in Shopify's admin panel allows authenticated users to
  access hidden collections, products, pages, and blogs from other stores by
  manipulating the subject_id parameter during link list creation.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
name: Shopify IDOR: Unauthorized Access to Other Stores' Hidden Objects via Admin Link Lists
type: attack_chain
description: An IDOR vulnerability in Shopify's admin panel allows authenticated users to access hidden collections, products, pages, and blogs from other stores by manipulating the subject_id parameter during link list creation.
verified: false
submitted: false
step_count: 6
created_at: 2023-10-01T00:00:00Z
updated_at: 2023-10-01T00:00:00Z
procedures: [[procedures/Exploit-Shopify-Link-List-IDOR]]
techniques: [[Exploit Public-Facing Application]], [[Account Discovery]]
tactics: [[Initial Access]], [[Discovery]]
tags: idor, shopify, unauthorized-access, admin-panel, improper-authentication
platforms: Web
tools: [[tools/Browser-Developer-Tools]]
complexity: medium
skill_level: intermediate
impact_level: high
---

# Shopify IDOR: Unauthorized Access to Other Stores' Hidden Objects via Admin Link Lists

Multi-stage attack chain demonstrating a complete attack workflow exploiting an IDOR in Shopify's admin interface to gain unauthorized read access to other stores' hidden objects.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Navigate to Admin Panel] --> B[Initiate Link List Creation]
    B --> C[Select Object Type]
    C --> D[Inspect and Modify subject_id]
    D --> E[Submit and Observe]
    E --> F[Unauthorized Access Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#3498db
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Browser-Developer-Tools]]

### Target Environment

- Shopify admin panel (web-based)
- Required services/ports: HTTPS on port 443
- Network access requirements: Authenticated access to a Shopify store admin

### Initial Access Requirements

- Valid Shopify admin credentials for any store
- Network position: Direct internet access to Shopify's admin domain
- Prior access needed: None beyond authentication

## Detailed Attack Procedures

### Step 1: Navigate to Link Lists Admin Page
procedure: [[procedures/Exploit-Shopify-Link-List-IDOR]]

**Objective**: Access the link lists management interface in the Shopify admin panel to begin the exploitation process.

**Instructions**: Log in to the Shopify admin panel and directly navigate to the link lists section.

**Expected Output**: The link lists admin page loads, displaying existing link lists or options to create new ones.

**Success Indicators**:
- Admin panel accessible
- URL shows /admin/link_lists

### Step 2: Initiate Link List Creation
procedure: [[procedures/Exploit-Shopify-Link-List-IDOR]]

**Objective**: Start the process of creating a new link list to expose the vulnerable form elements.

**Instructions**: Click the 'Add link list' button in the interface.

**Expected Output**: A form for creating a new link list appears, including fields for links and object selection.

**Success Indicators**:
- New link list form is visible
- Interface ready for object linking

### Step 3: Select Object Type
procedure: [[procedures/Exploit-Shopify-Link-List-IDOR]]

**Objective**: Choose the type of object (e.g., collection) to link, setting up the context for ID manipulation.

**Instructions**: From the dropdown or list, select an object type such as 'collection', 'product', 'page', or 'blog'.

**Expected Output**: The form updates to allow selection or input of the specific object via ID.

**Success Indicators**:
- Object type selected
- Form field for subject_id becomes relevant

### Step 4: Inspect HTML Elements
procedure: [[procedures/Exploit-Shopify-Link-List-IDOR]]

**Objective**: Use browser tools to examine the form structure and identify the vulnerable parameter.

**Instructions**: Right-click on the form and select 'Inspect Element' or open developer tools (F12) to view the HTML source, focusing on input fields.

**Expected Output**: HTML reveals the input field named 'link_list[links][][subject_id]'.

**Success Indicators**:
- Developer tools open
- Vulnerable input field identified

### Step 5: Modify subject_id Parameter
procedure: [[procedures/Exploit-Shopify-Link-List-IDOR]]

**Objective**: Alter the subject_id to reference an object from another store, bypassing access controls.

**Instructions**: In the developer tools, locate and edit the value attribute of the 'link_list[links][][subject_id]' input to an arbitrary ID from another Shopify store (e.g., obtained from public sources or prior recon).

**Expected Output**: The input field now contains the manipulated ID.

**Success Indicators**:
- ID changed successfully
- No immediate errors in the form

### Step 6: Submit Form and Observe Results
procedure: [[procedures/Exploit-Shopify-Link-List-IDOR]]

**Objective**: Save the link list to trigger the server-side validation bypass and reveal unauthorized data.

**Instructions**: Click the 'Save' button to submit the form; wait for the page to reload.

**Expected Output**: Upon reload, the interface displays the name of the hidden object (e.g., collection name) from the other store.

**Success Indicators**:
- Page reloads without errors
- Unauthorized object name visible in the link list

## Attack Chain Summary

### Key Achievements

1. Bypassed store-specific access controls via IDOR in link list creation.
2. Achieved unauthorized read access to hidden objects like collections and products from other stores.
3. Demonstrated improper authentication allowing cross-store data leakage without identifying the source store.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Account Discovery]] Account Discovery

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Discovery]] Discovery

---
*Last updated: 2023-10-01T00:00:00Z*
