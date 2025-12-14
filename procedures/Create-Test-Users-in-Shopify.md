---
id: proc-uuid-1
tags:
  - shopify
  - user-creation
type: procedure
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
updated_at: '2025-12-14T17:28:52.137Z'
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
# Create-Test-Users-in-Shopify

## Summary

This procedure sets up test users in a Shopify shop to simulate admin and limited access scenarios for testing access controls.

## Description

In a Shopify test environment, create an admin user with full permissions and a limited user with only 'Sales Channels Overviews' access. This allows verification of permission enforcement on admin features like the Activity Feed. Prerequisites include owning a Shopify shop and having admin access.

## Requirements

1. Shopify account owner credentials
2. Access to Shopify admin panel
3. Test shop environment

## Defense

Defensive measures and detection strategies:

- Enforce strict role-based access control (RBAC) in user management
- Monitor user creation events for anomalies

## Objectives

1. Establish baseline users for permission testing
2. Simulate real-world limited access scenarios
3. Prepare for access control validation

## Instructions

### Step 1: Log In as Shop Owner

**Context**: Access the admin panel to manage users.

Navigate to https://yourshop.myshopify.com/admin/users and log in with owner credentials.

> Expected: Admin dashboard loads.

### Step 2: Create Admin User X

**Context**: Set up full permission user.

Click 'Add staff' and assign 'Account Owner' role with full permissions.

> Expected: User X created with complete access.

### Step 3: Create Limited User Y

**Context**: Restrict to Overviews only.

Click 'Add staff' again, select limited permissions for 'Sales Channels Overviews' only.

> Expected: User Y created with restricted access.

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
- user-management
