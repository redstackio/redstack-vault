---
tags:
  - idor
  - shopify
  - unauthorized-access
  - privacy-violation
  - web
type: attack_chain
tools: []
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Shopify-Partner-Account-and-Add-Business]]'
  - '[[procedures/Invite-Member-with-Manage-Apps-Permission]]'
  - '[[procedures/Create-Development-Store]]'
  - '[[procedures/Add-Staff-Member-to-Store]]'
  - '[[procedures/Activate-Limited-Permission-Member-Account]]'
  - '[[procedures/Access-Shop-Details-via-Predictable-IDOR-URL]]'
  - '[[procedures/View-Unauthorized-Shop-Information]]'
  - '[[procedures/Access-Staff-List-via-Transfer-Feature]]'
step_count: 8
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:29:44.890Z'
description: >-
  Multi-stage attack exploiting an Insecure Direct Object Reference (IDOR) in
  Shopify's partners.shopify.com, allowing users with only 'Manage apps'
  permission to access sensitive shop information and staff account names via
  predictable incremental IDs.
id: 11331c14-fbf7-410a-9514-29fc45761ec9
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Shopify Partners IDOR: Unauthorized Access to Shop Details and Staff Accounts

Multi-stage attack chain demonstrating a complete attack workflow exploiting IDOR in Shopify's partner dashboard to gain unauthorized access to shop data and staff accounts.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 8 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Account Setup] --> B[Invite Limited User]
    B --> C[Create Test Store]
    C --> D[Add Staff]
    D --> E[Activate Limited User]
    E --> F[IDOR Exploitation]
    F --> G[View Shop Data]
    G --> H[View Staff List]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#f39c12
    style E fill:#3498db
    style F fill:#e67e22
    style G fill:#27ae60
    style H fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome or Firefox)

### Target Environment

- Shopify Partners platform (partners.shopify.com)
- Web-based access

### Initial Access Requirements

- Ability to create a Shopify Partner account
- No special network access beyond internet connectivity
- Basic understanding of web URL manipulation

## Detailed Attack Procedures

### Step 1: Account Setup
procedure: [[procedures/Create-Shopify-Partner-Account-and-Add-Business]]

**Objective**: Establish a test environment by creating a partner account and associating a business.

**Instructions**: Register a new account on partners.shopify.com and add a business entity to serve as the base for testing.

**Expected Output**: Active partner account with linked business.

**Success Indicators**:
- Partner dashboard accessible
- Business entity listed

### Step 2: Invite Limited User
procedure: [[procedures/Invite-Member-with-Manage-Apps-Permission]]

**Objective**: Add a member with minimal permissions to test authorization bypass.

**Instructions**: Navigate to the memberships section and invite a new member, assigning only the 'Manage apps' role.

**Expected Output**: Invitation sent and member account created.

**Success Indicators**:
- Member invitation email received
- Limited role confirmed

### Step 3: Create Test Store
procedure: [[procedures/Create-Development-Store]]

**Objective**: Generate a development store for exploitation testing.

**Instructions**: Use the partner dashboard to create a new development store under the associated business.

**Expected Output**: New store created with assigned ID.

**Success Indicators**:
- Store appears in dashboard
- Store ID noted for later use

### Step 4: Add Staff to Store
procedure: [[procedures/Add-Staff-Member-to-Store]]

**Objective**: Populate the store with staff accounts to demonstrate data exposure.

**Instructions**: Access the store settings, initiate a transfer process, and add a staff account.

**Expected Output**: Staff account added to the store.

**Success Indicators**:
- Staff listed in store details
- Transfer option available

### Step 5: Activate Limited User
procedure: [[procedures/Activate-Limited-Permission-Member-Account]]

**Objective**: Log in as the limited user to simulate unauthorized access.

**Instructions**: In a separate browser session, accept the invitation and log in with the limited permissions.

**Expected Output**: Limited user session active.

**Success Indicators**:
- Dashboard loads with restricted views
- No admin features accessible

### Step 6: IDOR URL Access
procedure: [[procedures/Access-Shop-Details-via-Predictable-IDOR-URL]]

**Objective**: Exploit predictable IDs to directly access shop details without authorization.

**Instructions**: Construct and navigate to the shop detail URL using the business and store IDs.

**Expected Output**: Shop detail page loads.

**Success Indicators**:
- Unauthorized page accessible
- No permission error

### Step 7: View Shop Data
procedure: [[procedures/View-Unauthorized-Shop-Information]]

**Objective**: Extract sensitive shop information via the IDOR endpoint.

**Instructions**: Observe the loaded shop details, which persist even after ownership changes.

**Expected Output**: Internal shop data displayed.

**Success Indicators**:
- Shop info visible
- Data remains post-transfer

### Step 8: View Staff List
procedure: [[procedures/Access-Staff-List-via-Transfer-Feature]]

**Objective**: Access staff account names through the transfer interface.

**Instructions**: Click the transfer option to reveal the staff dropdown.

**Expected Output**: List of staff accounts shown.

**Success Indicators**:
- Staff names exposed
- No auth required

## Attack Chain Summary

### Key Achievements

1. Bypassed permission checks with minimal role
2. Enumerated sensitive shop data via IDOR
3. Exposed staff account details leading to privacy risks

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Account Discovery]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*
