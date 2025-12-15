---
tags:
  - authentication
  - shopify
  - staff-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
  - Shopify
techniques:
  - '[[Valid Accounts]]'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
id: 77759a69-3fd5-4616-bc93-6e620585dce3
created_at: '2025-12-14T17:29:29.027Z'
updated_at: '2025-12-14T17:29:29.027Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-to-Shopify-Admin-as-Low-Privilege-Staff

## Summary

This procedure authenticates to the Shopify admin panel using a staff account restricted to 'Settings' permission, establishing a session for testing authorization boundaries in the GraphQL API.

## Description

In the context of exploiting improper authorization in Shopify, logging in as a low-privilege staff member allows testing of API mutations that should be restricted. The target environment is the Shopify admin web interface, requiring valid credentials. Expected outcome is a session token usable for subsequent API calls, with no direct impact but enabling unauthorized actions.

## Requirements

1. Valid staff account credentials with only 'Settings' permission
2. Web browser or HTTP client for authentication
3. Access to the store's admin URL (e.g., https://yoursubdomain.myshopify.com/admin)

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) for staff accounts
- Monitor login attempts and session usage for unusual API calls from low-priv accounts
- Enforce strict permission checks in GraphQL resolvers

## Objectives

1. Establish authenticated session with minimal privileges
2. Verify permission restrictions in the admin dashboard
3. Prepare for API exploitation without triggering alerts

## Instructions

### Step 1: Access Admin Login

**Context**: Navigate to the Shopify admin login to initiate authentication.

**Command** (Browser Navigation):

Open https://yoursubdomain.myshopify.com/admin/login in a web browser.

> Enter staff email and password. Upon success, the dashboard loads with restricted menu options.

### Step 2: Verify Permissions

**Context**: Confirm the account's permission level to ensure it's low-privilege.

**Command** (Account Settings Check):

Navigate to Settings > Users and permissions.

> Review the staff role; it should show only 'Settings' enabled, excluding 'Order'.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- authentication
- shopify
