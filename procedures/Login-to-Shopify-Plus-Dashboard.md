---
tags:
  - authentication
  - shopify
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:24:56.686Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
id: 75aeb512-baba-4315-b781-db0213757f4a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-to-Shopify-Plus-Dashboard

## Summary

This procedure authenticates a user to the Shopify Plus admin dashboard using valid credentials with User management permissions, establishing initial access for subsequent enumeration activities.

## Description

The login process involves standard web authentication to the Shopify admin portal. It requires credentials tied to a Shopify Plus account that includes permissions for managing users. This step is a prerequisite for accessing the vulnerable 'Add users' functionality and sets the stage for information disclosure by ensuring the attacker operates within an authorized session.

## Requirements

1. Valid Shopify Plus account credentials (email and password)
2. User management permissions enabled on the account
3. Web browser with JavaScript enabled for the admin interface
4. Direct internet access to shopify.com

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) to prevent credential-based access
- Monitor login attempts from unusual IP addresses or locations
- Use session timeouts and IP whitelisting for admin access

## Objectives

1. Establish an authenticated session in the Shopify Plus dashboard
2. Verify access to user management features
3. Prepare for navigation to invitation tools without alerting defenses

## Instructions

### Step 1: Access Login Page and Authenticate

**Context**: Navigate to the entry point and submit credentials to gain dashboard access.

No specific command required; perform via browser UI:

- Open a web browser (e.g., Chrome or Firefox).
- Go to `https://accounts.shopify.com/login` or directly to your store's admin login.
- Enter the email and password associated with the Shopify Plus account.
- Click 'Log in' or press Enter.

> Upon success, you will be redirected to the dashboard at `https://admin.shopify.com/store/[id]`. Verify by checking for the 'Users' menu item in the sidebar.

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
