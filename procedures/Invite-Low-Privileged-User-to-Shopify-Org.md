---
tags:
  - shopify
  - user-invitation
  - privilege-management
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:29:36.335Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 8bc6f7b9-8344-4263-ac9c-bf30f1fad9ef
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Invite-Low-Privileged-User-to-Shopify-Org

## Summary

This procedure involves inviting a new user to a Shopify Plus organization with only Store Management permissions, enabling simulation of low-privileged access to test for privilege escalation vulnerabilities in API endpoints.

## Description

In Shopify Plus, organization admins can invite users via the web interface, assigning roles like Store Management, which provides access to stores API but should not allow user management functions. This step sets up the attacker-controlled low-privileged account used in subsequent steps to query and mutate organization data without proper authorization checks.

## Requirements

1. Admin access to Shopify Plus organization dashboard
2. Valid email for the new user account
3. Network access to https://shopify.plus/:org_id

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls (RBAC) with strict API permission checks
- Monitor user invitations and role assignments for anomalies
- Audit GraphQL queries/mutations for unauthorized access patterns

## Objectives

1. Create a low-privileged user account with Store Management role
2. Grant API access without User Management privileges
3. Prepare for testing unauthorized mutation execution

## Instructions

### Step 1: Navigate to Invitation Page

**Context**: Access the user management section as an Org Plus admin to initiate invitation.

Log in to https://shopify.plus/:org_id/users/invite and fill in the user details, selecting 'Store Management' permissions.

> No command needed; this is a web UI action. Expected output: Invitation sent via email.

### Step 2: Verify User Access

**Context**: Confirm the new user can log in and access the stores API.

Have the user log in at https://shopify.plus/:org_id and attempt to access /stores/api endpoint.

> Expected output: Successful login with limited UI options; API accessible but no User Management features.

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
- rbac-bypass
