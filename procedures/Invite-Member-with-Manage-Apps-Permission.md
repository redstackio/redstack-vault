---
tags:
  - invitation
  - permissions
  - shopify
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:29:44.883Z'
sub_techniques: []
id: 138c371d-83b5-4fa0-96eb-bff11e92e780
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Invite-Member-with-Manage-Apps-Permission

## Summary

This procedure invites a new member to the Shopify Partner organization with only 'Manage apps' permission, setting up a low-privilege account for IDOR testing.

## Description

To demonstrate authorization bypass, a member is invited via the memberships page with restricted roles. This allows testing access to sensitive endpoints without full admin rights. The technical approach relies on Shopify's permission model, where 'Manage apps' should not grant shop detail visibility, but IDOR enables it.

## Requirements

1. Active partner account with admin access
2. Email address for the invitee
3. Access to memberships dashboard

## Defense

Defensive measures and detection strategies:

- Enforce strict role-based access control (RBAC)
- Log and alert on permission assignments

## Objectives

1. Create low-privilege test user
2. Limit scope to 'Manage apps' only
3. Enable isolated session testing

## Instructions

### Step 1: Navigate to Memberships

**Context**: Access the invitation interface.

Log in as admin and go to https://partners.shopify.com/[YOUR_ID]/memberships.

> Page loads with option to invite members.

### Step 2: Send Invitation

**Context**: Assign minimal permissions during invite.

Click 'Invite member', enter email, and select only 'Manage apps' role, then submit.

> Invitation email sent; member can activate upon receipt.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[invitation]]
- [[permissions]]
- [[shopify]]
