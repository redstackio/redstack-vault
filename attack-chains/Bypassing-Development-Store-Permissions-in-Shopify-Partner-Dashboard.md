---
id: ac-shopify-dev-store-bypass-1167453
tags:
  - shopify
  - access-control
  - authorization-bypass
  - development-store
  - partner-dashboard
type: attack_chain
tools: []
tactics:
  - '[[Privilege Escalation]]'
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Grant-Temporary-Permissions-to-Staff-Member]]'
  - '[[procedures/Initiate-Development-Store-Creation]]'
  - '[[procedures/Revoke-Development-Store-Permissions]]'
  - '[[procedures/Complete-Development-Store-Creation-via-UI-or-API]]'
step_count: 4
techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[T1078.004]]'
updated_at: '2025-12-14T17:30:35.784Z'
description: >-
  An improper access control vulnerability in Shopify's partner dashboard allows
  staff with only managed store permissions to create unauthorized development
  stores by exploiting missing permission checks during the creation process.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[T1078.004]]'
---
# Bypassing Development Store Permissions in Shopify Partner Dashboard

Multi-stage attack chain demonstrating how staff members with limited permissions can exploit improper access controls in Shopify's partner dashboard to create and access development stores, enabling unauthorized resource creation and elevated actions within the organization.

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
    A[Grant Temporary Permissions] --> B[Initiate Store Creation]
    B --> C[Revoke Permissions]
    C --> D[Complete Creation and Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser for UI interactions
- [[tools/curl]] for API alternative

### Target Environment

- Shopify Partner Dashboard (web application)
- Access to organization owner account
- Staff account with managed store permissions

### Initial Access Requirements

- Valid organization owner credentials
- Valid staff member credentials (e.g., Doe account)
- Network access to partners.shopify.com

## Detailed Attack Procedures

### Step 1: Grant Temporary Permissions
procedure: [[procedures/Grant-Temporary-Permissions-to-Staff-Member]]

**Objective**: Temporarily elevate staff permissions to initiate the development store creation process.

**Instructions**: As the organization owner, log in to the Shopify Partner Dashboard and grant the staff member both development store and managed store permissions.

**Expected Output**: Staff member (Doe) now has temporary access to development store creation features.

**Success Indicators**:
- Permissions updated in the dashboard
- Staff can access the stores/new page

### Step 2: Initiate Development Store Creation
procedure: [[procedures/Initiate-Development-Store-Creation]]

**Objective**: Start the development store signup process to obtain necessary session state before permission revocation.

**Instructions**: Have the staff member log in and navigate to https://partners.shopify.com/organizationID/stores/new, then select the development store option to begin creation.

**Expected Output**: Signup process initiated, with UI elements for continuing creation visible.

**Success Indicators**:
- Development store option selectable
- No immediate permission denial

### Step 3: Revoke Development Store Permissions
procedure: [[procedures/Revoke-Development-Store-Permissions]]

**Objective**: Remove elevated permissions to demonstrate the bypass, ensuring the staff only has managed store access.

**Instructions**: As the owner, edit the staff member's permissions in the dashboard to revoke development store access, leaving only add/remove managed stores.

**Expected Output**: Staff permissions updated to exclude development stores.

**Success Indicators**:
- Permission edit confirmation
- Staff can no longer access development store features directly

### Step 4: Complete Development Store Creation via UI or API
procedure: [[procedures/Complete-Development-Store-Creation-via-UI-or-API]]

**Objective**: Finalize the store creation despite revoked permissions, gaining unauthorized access to the new development store.

**Instructions**: Staff continues through the UI to complete creation and auto-login, or alternatively uses API calls: first execute [[commands/get-shopify-dev-store-token]] to obtain the token, then [[commands/post-shopify-create-dev-store]] to create the store with form data.

For UI:
```bash
# No command; interact via browser UI
```

For API (using curl):
```bash
# See linked commands for details
curl -X GET "https://partners.shopify.com/organizationID/stores/signup_object/dev_store" \
  -H "Cookie: ..." # Include session cookies

curl -X POST "https://app.shopify.com/services/signup/create" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "signup[shop_name]=newiez2&signup[email]=example@gmail.com&..." # Full form data
```

**Expected Output**: New development store created; automatic login to the store admin.

**Success Indicators**:
- Store accessible via provided URL
- Staff can perform elevated actions in the store
- No permission errors during completion

## Attack Chain Summary

### Key Achievements

1. Successful creation of development store without ongoing permissions
2. Automatic login and access to unauthorized resources
3. Demonstration of missing checks on signup endpoints, allowing broader organization impact

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation
- [[T1078.004]] Cloud Accounts

### MITRE ATT&CK Tactics

- [[Privilege Escalation]] Privilege Escalation
- [[Initial Access]] Initial Access

---
*Last updated: 2023-10-01T00:00:00Z*
