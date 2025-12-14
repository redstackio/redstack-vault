---
tags:
  - broken-access-control
  - discovery
  - authorization
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Account Discovery]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 76cbfcd5-307f-4749-9126-96b43cc3a3ef
created_at: '2025-12-14T17:33:06.691Z'
updated_at: '2025-12-14T17:33:06.691Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Discover-Tenant-Admin-Authorization-Flaw-in-User-Management

## Summary

This procedure identifies an authorization vulnerability in Lemlist's user management system, where tenant admins can access and potentially modify credentials of other users, including invited agency accounts, due to insufficient access controls.

## Description

In the Lemlist web application, tenant admins have elevated privileges that inadvertently allow them to view and interact with other users' profiles without proper permission checks. This flaw is exploitable after a user accepts an invitation to the tenant, exposing shared environments to risks like unauthorized modifications. The procedure involves testing UI elements and API endpoints to confirm the lack of enforcement, typically using browser tools for inspection.

## Requirements

1. Valid tenant admin login credentials for app.lemlist.com
2. Access to a tenant with multiple users, including at least one invited account that has been accepted
3. Web browser with developer tools enabled

## Defense

Defensive measures and detection strategies:

- Implement role-based access control (RBAC) to restrict admin actions to their own accounts
- Log all user management access attempts and alert on cross-user modifications
- Enforce MFA on all accounts to mitigate post-reset login risks

## Objectives

1. Confirm unauthorized access to other users' credential management
2. Document the scope of the flaw for reporting
3. Validate impact on invited agency accounts

## Instructions

### Step 1: Login and Navigate to User Management

**Context**: Gain initial access as a tenant admin to reach the vulnerable interface.

Log in to app.lemlist.com using admin credentials and navigate to the user management or admin dashboard section.

> Expected: Dashboard loads with user list visible.

### Step 2: Test Access to Other Users

**Context**: Probe for authorization flaws by attempting to view non-owned user profiles.

Select a non-admin user account from the list, including an invited one that has accepted the invitation. Attempt to view detailed profile information, focusing on credential-related fields.

> Expected: Full access to user details without permission prompts.

### Step 3: Inspect for Password Reset Access

**Context**: Verify if credential modification is possible.

Within the selected user's profile, check for password reset or edit options. Use browser developer tools (F12) to inspect network requests for any authorization headers or checks.

> Expected: Password reset interface available; API responses lack user-specific permission validation.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[broken-access-control]]
- [[Discovery]]
- [[authorization]]
