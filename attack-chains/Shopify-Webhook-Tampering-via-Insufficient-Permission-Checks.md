---
id: ac-shopify-webhook-tampering-001
tags:
  - shopify
  - webhook
  - access-control
  - permission-bypass
  - tampering
type: attack_chain
tools:
  - '[[tools/Burp-Proxy]]'
tactics:
  - '[[Initial Access]]'
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Assign-Limited-Settings-Permission-to-Staff]]'
  - '[[procedures/Create-Order-Creation-Webhook-as-Owner]]'
  - '[[procedures/View-Webhook-as-Low-Privilege-Staff]]'
  - '[[procedures/Edit-Order-Creation-Webhook-as-Staff]]'
  - '[[procedures/Delete-Order-Creation-Webhook-as-Staff]]'
step_count: 5
techniques:
  - '[[Valid Accounts]]'
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:29:36.322Z'
description: >-
  Demonstrates how low-privilege staff users in Shopify can edit and delete
  critical Order Creation webhooks despite lacking Orders permission, leading to
  potential disruption of order notifications.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Account Manipulation]]'
---
# Shopify Webhook Tampering via Insufficient Permission Checks

Multi-stage attack chain demonstrating improper access control in Shopify's admin panel, allowing staff with only 'Settings' permission to edit and delete 'Order Creation' webhooks that require 'Orders' permission.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Permissions] --> B[Create Webhook]
    B --> C[View as Staff]
    C --> D[Edit Webhook]
    D --> E[Delete Webhook]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Proxy]] (for testing creation restrictions)

### Target Environment

- Shopify Store Admin Panel (web-based SaaS platform)
- Required services/ports: HTTPS on standard web ports (443)
- Network access requirements: Valid Shopify owner and staff account credentials

### Initial Access Requirements

- Owner-level credentials for permission assignment and webhook creation
- Staff credentials with only 'Settings' permission
- Direct access to Shopify admin dashboard

## Detailed Attack Procedures

### Step 1: Assign Limited Permissions
procedure: [[procedures/Assign-Limited-Settings-Permission-to-Staff]]

**Objective**: Limit staff access to only 'Settings' to simulate low-privilege scenario.

**Instructions**: Log in as the store owner and navigate to the staff management section to assign permissions.

**Expected Output**: Staff user now has 'Settings' permission only, confirmed in the permissions list.

**Success Indicators**:
- Staff permission updated to 'Settings' only
- No 'Orders' permission granted

### Step 2: Create Order Creation Webhook
procedure: [[procedures/Create-Order-Creation-Webhook-as-Owner]]

**Objective**: Establish a critical webhook for order notifications that staff should not be able to modify.

**Instructions**: As owner, go to Settings > Notifications and set up the webhook for the orders/create event.

**Expected Output**: Webhook listed in Notifications with active status.

**Success Indicators**:
- Webhook successfully created and visible in the list
- Endpoint URL configured for order events

### Step 3: View Webhook as Low-Privilege Staff
procedure: [[procedures/View-Webhook-as-Low-Privilege-Staff]]

**Objective**: Verify that staff can access the webhook list despite permission mismatch.

**Instructions**: Log in as staff and navigate to Settings > Notifications to view existing webhooks.

**Expected Output**: 'Order Creation' webhook appears in the list without errors.

**Success Indicators**:
- Staff can see owner-created webhooks
- No access denied message for viewing

### Step 4: Edit Order Creation Webhook
procedure: [[procedures/Edit-Order-Creation-Webhook-as-Staff]]

**Objective**: Demonstrate unauthorized modification of webhook configuration.

**Instructions**: As staff, select the webhook, open the edit modal, change the URL, and save.

**Expected Output**: Webhook URL updated successfully without permission errors.

**Success Indicators**:
- Changes saved and reflected in the webhook details
- No 403 or permission check triggered

### Step 5: Delete Order Creation Webhook
procedure: [[procedures/Delete-Order-Creation-Webhook-as-Staff]]

**Objective**: Show ability to remove critical webhook, disrupting notifications.

**Instructions**: As staff, select the webhook and confirm deletion in the UI.

**Expected Output**: Webhook removed from the list.

**Success Indicators**:
- Webhook no longer visible
- Deletion succeeds without elevated permissions

## Attack Chain Summary

### Key Achievements

1. Bypassed permission checks for webhook management
2. Enabled low-privilege tampering with order notifications
3. Potential for business disruption via altered or removed webhooks

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Account Manipulation]] Account Manipulation

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Privilege Escalation]] Privilege Escalation

---
*Last updated: 2023-10-01T00:00:00Z*
