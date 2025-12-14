---
id: proc-setup-low-priv-pos-001
tags:
  - shopify
  - pos
  - setup
  - broken-access-control
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:17.922Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Setup-Low-Privilege-User-with-POS-Access

## Summary

This procedure creates a low-privilege staff user in Shopify Plus, enables POS access with an Associate role, and revokes all admin permissions to test persistent access controls, highlighting broken authorization in the POS system.

## Description

In a Shopify Plus environment, an org owner can create staff users with minimal permissions. By enabling POS access via the app's staff page and then revoking admin perms, the procedure demonstrates that POS authentication remains active, allowing token issuance. This targets the admin panel at URLs like https://*.myshopify.com/admin/apps/pos/staff/<user_id>. Prerequisites include org owner access and the POS app installed.

## Requirements

1. Shopify Plus org owner credentials
2. Installed Shopify POS app
3. Access to Shopify admin panel

## Defense

Defensive measures and detection strategies:

- Implement strict permission syncing between admin and POS roles
- Monitor for permission revocation warnings and audit POS access logs
- Enforce role-based access control (RBAC) validation on all endpoints

## Objectives

1. Create and configure a low-privilege user for POS testing
2. Verify persistence of POS access after admin revocation
3. Prepare for token-based API exploitation

## Instructions

### Step 1: Create Minimal Privilege User

**Context**: Log in as org owner and create a new staff user with lowest permissions.

Navigate to Shopify Plus admin > Settings > Users and permissions > Add staff. Set minimal role (e.g., no permissions selected).

**Expected Output**: New user created with email like ramsexy+h1-2102-3@wearehackerone.com and user ID (e.g., 61357948984).

### Step 2: Enable POS Access

**Context**: Assign POS Associate role to the user.

Visit https://h1-2102-ramsexy.myshopify.com/admin/apps/pos/staff/61357948984, check 'Give Point of Sale access', select Associate role, and save.

**Expected Output**: POS access enabled for the user.

### Step 3: Revoke Admin Permissions

**Context**: Remove all admin access to isolate POS functionality.

Return to user permissions page, uncheck all permissions, and save. Note the warning: "POS access remains active".

**Expected Output**: All admin permissions revoked, but POS access persists.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- shopify
- pos
- setup
