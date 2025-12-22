---
id: proc-create-staff-no-perm-001
name: Create-No-Permission-Staff-Account
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:59.754Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
tags:
  - shopify
  - staff-account
  - authorization
platforms:
  - Web
tools: []
commands: []
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---

# Create-No-Permission-Staff-Account

## Summary

This procedure creates a staff member account in Shopify with no explicit permissions assigned, simulating a low-privilege user for testing authorization controls in the admin interface.

## Description

In Shopify stores, staff accounts can be created by owners or admins via the admin UI. By unchecking all permission options, the account gains authentication but no access to features, allowing testers to probe for backend API bypasses. This is a prerequisite for exploiting authorization flaws in GraphQL endpoints, where UI restrictions may not propagate to API responses.

## Requirements

1. Valid owner or admin credentials for the target Shopify store
2. Access to the Shopify admin dashboard (https://store.myshopify.com/admin)
3. No additional tools required; uses built-in UI

## Defense

Defensive measures and detection strategies:

- Implement role-based access control (RBAC) audits to ensure no zero-permission accounts are created unnecessarily
- Monitor staff account creations via Shopify audit logs for anomalous permission assignments
- Enforce multi-factor authentication (MFA) on all staff accounts to prevent unauthorized use

## Objectives

1. Establish a authenticated but unauthorized staff identity
2. Prepare for API-level testing without UI interference
3. Validate initial access using valid but low-privilege credentials

## Instructions

### Step 1: Navigate to Staff Management

**Context**: Access the staff creation interface in the Shopify admin.

Log in as owner/admin and go to Settings > Users and permissions > Add staff.

### Step 2: Configure Zero Permissions

**Context**: Create the account without assigning any roles or permissions.

Enter staff details (e.g., email, first/last name), then uncheck all permission checkboxes (e.g., settings, orders, products). Send invitation.

**Expected Output**: Invitation email sent; staff appears in list with "No access" status.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[shopify]]
- [[staff-account]]
- [[authorization]]
