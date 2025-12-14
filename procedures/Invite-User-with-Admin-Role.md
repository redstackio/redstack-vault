---
id: proc-invite-admin
tags:
  - access-grant
  - team-management
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
  - '[[External Remote Services]]'
updated_at: '2025-12-14T17:28:51.673Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[External Remote Services]]'
---
# Invite-User-with-Admin-Role

## Summary

This procedure outlines inviting a user to an Omise team with admin privileges, enabling them to perform elevated actions in the dashboard for subsequent testing of access controls.

## Description

In the context of testing role-based access controls in Omise's dashboard, an owner uses the team management interface to invite a secondary user and assign admin roles. This grants the user access to sensitive features like editing or adding payment links. The procedure assumes owner credentials and targets the test environment at https://dashboard.omise.co/team. Expected outcome is successful invitation and role assignment without errors.

## Requirements

1. Owner-level credentials for Omise dashboard
2. Access to https://dashboard.omise.co/team
3. Valid email for the invitee user

## Defense

Defensive measures and detection strategies:

- Implement invitation logging and approval workflows
- Monitor for unusual role assignments in audit logs
- Enforce multi-factor authentication for role changes

## Objectives

1. Grant temporary admin access to test user
2. Establish baseline for privilege escalation testing
3. Verify invitation process integrity

## Instructions

### Step 1: Access Team Management

**Context**: Log in as owner and navigate to the team invitation page.

No specific command; use browser to visit https://dashboard.omise.co/team.

> Enter owner credentials and locate the 'Invite Member' section.

### Step 2: Send Invitation with Admin Role

**Context**: Specify invitee details and assign admin privileges.

No specific command; fill form with email and select 'Admin' role, then submit.

> Invitation email sent; user accepts to gain admin access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[External Remote Services]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- access-grant
- team-management
