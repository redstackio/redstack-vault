---
tags:
  - privilege-escalation
  - shopify
  - staff-management
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:29:10.054Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: fdf4b389-3414-4fd8-a8a9-9bc6c80df05f
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Create Staff with Full Permissions

## Summary

This procedure creates a new staff account in Shopify admin with unrestricted permissions across all store functions, setting up a vector for later privilege escalation in the POS application.

## Description

In the context of exploiting UI access control flaws in Shopify POS, this step prepares a high-privilege account that can be manipulated via limited interfaces. It requires initial admin access and targets the staff management section of the Shopify admin dashboard. The outcome is a fully empowered staff member whose permissions can be inherited through PIN-based session switching in POS.

## Requirements

1. Valid Shopify store owner or admin login credentials
2. Access to the Shopify admin dashboard via web browser
3. Enabled staff management feature in store settings

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls (RBAC) with granular permission auditing
- Monitor staff creation events for unusual permission assignments
- Use multi-factor authentication (MFA) for all admin actions

## Objectives

1. Establish a full-privilege staff account for escalation chaining
2. Ensure the account is assignable to POS roles
3. Prepare for PIN manipulation in subsequent steps

## Instructions

### Step 1: Access Staff Management

**Context**: Log in to the admin interface to reach user permissions.

Navigate to Settings > Users and permissions > Staff in the Shopify admin.

> This loads the staff listing page where new accounts can be added.

### Step 2: Add New Staff

**Context**: Create and configure the account with maximum permissions.

Click 'Add staff'. Enter details for the new staff member. Under permissions, select all checkboxes for full access, including admin, orders, products, and retail sections. Assign a temporary PIN if prompted and save.

> Successful save shows a confirmation and adds the staff to the list with full permissions indicated.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[privilege-escalation]]
- [[shopify]]
- [[staff-management]]
