---
tags:
  - user-invite
  - shopify-plus
  - low-priv
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
  - Shopify Plus
techniques:
  - '[[Valid Accounts]]'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
id: c440cc74-1898-4e7b-9ab0-e6877d885dfa
created_at: '2025-12-14T17:29:20.194Z'
updated_at: '2025-12-14T17:29:20.194Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Invite-Low-Privileged-User-with-Store-Management

## Summary

This procedure involves an organization admin inviting a new user with only Store Management permissions, setting up a low-privileged account for subsequent exploitation of authorization flaws in Shopify Plus.

## Description

In the context of testing improper authorization in Shopify Plus, this step creates a user who can access the GraphQL API at /stores/api but lacks User Management permissions. The procedure uses the admin dashboard to send an invitation, granting limited store access. Prerequisites include admin credentials and access to the organization ID.

## Requirements

1. Valid Shopify Plus organization admin account
2. Browser access to https://shopify.plus/:org_id
3. Email for the new user to receive invitation

## Defense

Defensive measures and detection strategies:

- Enforce strict role-based access control (RBAC) during user invitations
- Log all user creation events and review for anomalous permissions
- Use multi-factor authentication (MFA) for admin actions

## Objectives

1. Establish a low-privileged account for testing API access
2. Simulate insider or compromised low-priv user scenarios
3. Prepare for GraphQL queries with restricted permissions

## Instructions

### Step 1: Navigate to Invitation Page

**Context**: Access the user management section to invite a new user.

**Command** (Browser Navigation):

Visit https://shopify.plus/:org_plus_id/users/invite in your browser as admin.

> Fill in user details, select 'Store Management' permission only, and send invitation. Expected output: Confirmation message and email sent to the user.

### Step 2: Verify Invitation

**Context**: Ensure the user receives and can use the invitation.

**Command** (No CLI; manual):

Have the user check email and complete registration.

> Expected output: User logged in with Store Management access to https://shopify.plus/:plus_org_id/stores/api.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[user-invite]]
- [[shopify-plus]]
