---
tags:
  - invitation
  - admin-role
  - streamlabs
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
updated_at: '2025-12-14T17:29:57.358Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 63cd68c8-64cc-4ff4-9080-652d3975a32c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-Administrator-Invitation-in-Streamlabs

## Summary

This procedure creates an invitation link in Streamlabs with administrator privileges, allowing a collaborator to gain elevated access to the owner's account settings.

## Description

In the Streamlabs dashboard, the owner can generate invitations for team members with roles like Administrator. This step exploits the feature to set up the initial access vector for privilege escalation. The invitation grants the admin the ability to manage aspects of the owner's account, but subsequent steps reveal insufficient controls. Prerequisites include valid owner credentials and access to the web dashboard. Expected outcomes: A functional invitation link that, when accepted, provides admin-level impersonation.

## Requirements

1. Valid Streamlabs owner account credentials
2. Web browser with login capabilities
3. Internet access to streamlabs.com

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls (RBAC) to limit invitation scopes
- Monitor invitation creations and acceptances via audit logs
- Require multi-factor authentication (MFA) for all account actions

## Objectives

1. Establish admin-level access to the target account
2. Prepare for impersonation and escalation
3. Enable unauthorized navigation to restricted endpoints

## Instructions

### Step 1: Log In and Navigate to Settings

**Context**: Access the owner's dashboard and locate the shared access section to initiate invitation creation.

Navigate to https://streamlabs.com/dashboard#/settings/shared-access in your web browser while logged in as the owner.

> This loads the shared access management page where invitations can be generated.

### Step 2: Generate Admin Invitation

**Context**: Create and configure the invitation with Administrator role to grant elevated privileges.

Click the 'Generate Invitation' or similar button, select 'Administrator' role, and copy the generated link.

> The link will allow the recipient to accept and gain admin access, including potential impersonation of the owner's view.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- invitation-creation
- admin-privileges
