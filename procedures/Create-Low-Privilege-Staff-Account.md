---
id: proc-shopify-create-staff-report-only
tags:
  - shopify
  - staff-account
  - access-control
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:26.798Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-Low-Privilege-Staff-Account

## Summary

This procedure creates a Shopify staff account with only 'report' permissions, limiting access to basic reporting features while excluding billing and subscription management, setting up for testing unauthorized access to privileged functions like trial extension.

## Description

In Shopify's admin panel, staff accounts can be configured with granular permissions. This procedure focuses on creating an account with the minimal 'report' permission to simulate a low-privilege user. The target environment is a Shopify store admin interface during the trial period. Prerequisites include admin access to the store. Expected outcome is a functional staff account that can log in but is denied access to sensitive areas, highlighting potential misconfigurations in permission enforcement.

## Requirements

1. Admin credentials for the Shopify store
2. Web browser access to the admin panel (e.g., https://store.myshopify.com/admin)
3. Valid email address for the new staff user

## Defense

Defensive measures and detection strategies:

- Enforce least-privilege principle by auditing staff permissions regularly
- Monitor staff account creations via Shopify audit logs for unusual patterns
- Implement role-based access control (RBAC) with strict mutation-level checks in GraphQL resolvers

## Objectives

1. Establish a controlled low-privilege account for exploitation testing
2. Verify permission isolation before attempting bypass
3. Prepare session for unauthorized actions

## Instructions

### Step 1: Access Staff Management

**Context**: Log in as admin and navigate to create a new staff user.

**Instructions**: Go to Settings > Users and permissions > Add staff. Enter email, name, and select only 'Reports' permission. Uncheck all others like 'Billing' or 'Subscriptions'.

> No command executed; this is UI-based. Expected output: Staff invite sent via email.

### Step 2: Staff Account Activation

**Context**: Have the staff user accept the invite and log in to confirm permissions.

**Instructions**: Use the provided email to accept invite, set password, and log in to admin panel.

> Expected output: Successful login with restricted dashboard view.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- shopify
- staff-creation
- permissions
