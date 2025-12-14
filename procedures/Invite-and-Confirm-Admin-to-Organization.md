---
id: proc-bitwarden-invite-admin
tags:
  - bitwarden
  - organization-invite
  - admin-grant
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:29:36.674Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Invite-and-Confirm-Admin-to-Organization

## Summary

This procedure sets up a Bitwarden organization under one account and invites a second account as an admin, establishing the preconditions for role escalation. It leverages Bitwarden's organization invitation feature to grant elevated access.

## Description

Using the owner account (accountA), create a new organization via the web dashboard. Then, invite the admin account (accountB) with admin privileges. The invitee accepts, and the owner confirms, adding the admin to the organization. This simulates a legitimate admin addition but sets up the self-escalation vector. The target environment is Bitwarden's web app; outcomes include a multi-user organization ready for manipulation.

## Requirements

1. Logged-in session for accountA
2. Logged-in session for accountB
3. Organization creation permissions (default for new accounts)

## Defense

Defensive measures and detection strategies:

- Require owner approval for all role changes
- Audit logs for invitation patterns
- Limit invites to verified emails

## Objectives

1. Create organization under accountA
2. Grant and confirm admin access to accountB
3. Verify dual-member organization structure

## Instructions

### Step 1: Create Organization with AccountA

**Context**: Establish the organization that will be targeted for takeover.

Log in to Bitwarden with accountA. Click 'New Organization' in the dashboard, provide a name (e.g., 'TestOrg'), and confirm creation. Note the organization ID if visible.

### Step 2: Invite AccountB as Admin

**Context**: Send admin invitation to set up escalation target.

In the organization settings (gear icon > Manage > Members), select 'Invite User'. Enter accountB's email, select 'Admin' role, and send the invite.

### Step 3: Accept and Confirm Invitation

**Context**: Complete the addition to make accountB an active admin.

Log out of accountA, log in with accountB, and check for the invitation email or in-app notification. Accept the invite. Switch back to accountA, go to pending invites in organization settings, and confirm accountB's membership.

Log out and back in with accountB to ensure access.

**Expected Output**: accountB visible as admin in organization members list.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[bitwarden]]
- [[organization-invite]]
- [[admin-grant]]
