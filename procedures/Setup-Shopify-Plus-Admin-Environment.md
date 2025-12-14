---
tags:
  - shopify
  - admin-setup
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:29:44.855Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: bcd3fc80-dad0-4188-84ec-87efd94532fe
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Setup-Shopify-Plus-Admin-Environment

## Summary

This procedure sets up a Shopify Plus admin environment by logging in, creating a test role and user, and navigating to the user page to prepare for exploiting the role change mutation.

## Description

In the context of testing improper access control in Shopify Plus, this procedure establishes legitimate admin access and creates artifacts needed to trigger the vulnerable GraphQL mutation. It assumes valid credentials and focuses on internal navigation without external dependencies. Expected outcome is readiness to initiate role changes on a controlled user.

## Requirements

1. Valid Shopify Plus admin credentials
2. Web browser with proxy support (e.g., for Burp Suite integration)
3. Access to https://shopify.plus domain

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) for admin logins
- Monitor for unusual user and role creation patterns in admin logs

## Objectives

1. Gain admin access to Shopify Plus organization
2. Create test role and user for mutation testing
3. Position at user detail page for request interception

## Instructions

### Step 1: Log In to Shopify Plus

**Context**: Authenticate as an admin to access the management interface.

Navigate to https://shopify.plus/login and enter credentials.

> Successful login redirects to the admin dashboard.

### Step 2: Create a New Role

**Context**: Generate a role to use in the subsequent mutation.

Navigate to Administration > Users > Roles > Create role, fill in details, and save.

> Role created with a GraphQL ID like gid://organization/Role/[id].

### Step 3: Create a New User

**Context**: Add a test user within your organization.

Go to Administration > Users > All users > Add users, provide details, and assign the new role.

> User created with ID like gid://organization/OrganizationUser/[id].

### Step 4: Navigate to the New User's Page

**Context**: Access the user detail page to enable role change initiation.

In Administration > Users > All users, click the new user to reach https://shopify.plus/[org-id]/users/[user-id].

> Page loads with Access and permissions section visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[shopify]]
- [[admin-setup]]
