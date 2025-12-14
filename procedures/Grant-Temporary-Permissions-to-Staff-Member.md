---
id: proc-shopify-grant-temp-permissions
tags:
  - shopify
  - permissions
  - staff-management
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1078.004]]'
updated_at: '2025-12-14T17:30:35.781Z'
skill_level: low
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1078.004]]'
---
# Grant-Temporary-Permissions-to-Staff-Member

## Summary

This procedure involves temporarily granting a staff member elevated permissions in the Shopify Partner Dashboard to enable initiation of sensitive actions like development store creation, setting up the conditions for a permission bypass exploit.

## Description

In the context of exploiting improper access controls, the organization owner uses the dashboard to add both development store and managed store permissions to a limited staff account (e.g., Doe). This step is crucial as it allows the staff to start the creation process before permissions are revoked, highlighting the lack of ongoing checks in subsequent steps. The target environment is the Shopify Partner Dashboard web application, requiring owner-level access. Expected outcomes include the staff gaining temporary access to restricted features without triggering alerts.

## Requirements

1. Organization owner credentials for Shopify Partner Dashboard
2. Existing staff member account with basic access
3. Web browser access to https://partners.shopify.com

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls (RBAC) with granular permissions and audit logs for changes
- Monitor permission modifications via Shopify's audit logs and alert on temporary grants
- Enforce just-in-time (JIT) access for elevated roles to limit exposure windows

## Objectives

1. Enable staff to access development store creation features temporarily
2. Set up session state for bypass exploitation
3. Prepare for permission revocation without disrupting ongoing processes

## Instructions

### Step 1: Log In as Organization Owner

**Context**: Access the admin interface to manage staff permissions.

**Command** (Browser Navigation):
```bash
# No CLI command; use web browser
# Navigate to: https://partners.shopify.com/sign_in
# Log in with owner credentials
```

> Log in to the Partner Dashboard using owner account. Expected output: Dashboard homepage loaded.

### Step 2: Edit Staff Permissions

**Context**: Locate and modify the target staff member's role to include development store access.

**Command** (Browser UI Interaction):
```bash
# No CLI; UI steps:
# 1. Go to Settings > Users & permissions
# 2. Select staff member (Doe)
# 3. Add 'Development stores' and 'Managed stores' permissions
# 4. Save changes
```

> Update permissions and confirm. Expected output: Success message confirming permission grant; staff can now see development options.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[T1078.004]] Cloud Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[shopify]]
- [[permissions]]
- [[staff-management]]
