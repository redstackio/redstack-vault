---
tags:
  - setup
  - shopify
  - staff-account
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
updated_at: '2025-12-14T17:29:44.807Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: ed67b449-eea0-47df-a389-9cacd1d7ef69
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-Staff-Account-and-Install-Flow-App

## Summary

This procedure sets up a staff account with limited 'Apps' permission in Shopify and installs the Flow app, preparing the environment for testing authorization bypass in connectors.

## Description

In a Shopify shop, log in as the owner to create a staff member with only 'Apps' permission. Then, install the Flow automation app from the Shopify app store. Switch to the staff account to access the Flow connectors interface. This simulates an insider threat scenario where a staff member gains access to app integrations before removal. Prerequisites include owner-level access to the shop admin.

## Requirements

1. Valid Shopify shop owner credentials
2. Access to Shopify admin panel (https://admin.shopify.com)
3. Internet connectivity for app installation

## Defense

Defensive measures and detection strategies:

- Regularly audit and revoke staff permissions promptly
- Monitor app installations and connector changes via Shopify logs
- Implement role-based access controls (RBAC) with least privilege

## Objectives

1. Create a testable staff account with minimal permissions
2. Install Flow app to enable connector interactions
3. Verify staff access to apps without broader admin rights

## Instructions

### Step 1: Create Staff Account

**Context**: Access the Shopify admin to add a new staff member with 'Apps' permission only.

No specific command; manual UI navigation:

Navigate to Shopify admin > Settings > Users and permissions > Add staff > Select 'Apps' permission only > Save.

> This creates a staff account limited to app management, excluding other admin functions.

### Step 2: Install Flow App

**Context**: As owner, install the Flow app to integrate automation workflows.

No specific command; manual UI navigation:

Go to https://apps.shopify.com/flow > Click 'Add app' > Install on the shop.

> Flow app is now available; confirm installation in Apps section.

### Step 3: Access as Staff

**Context**: Log in with staff credentials to verify access to Flow.

No specific command; manual login:

Log in at https://[Your-Shop].myshopify.com/admin with staff details > Navigate to Apps > Flow.

> Staff should see Flow but not other restricted areas.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[setup]]
- [[shopify]]
- [[staff-account]]
