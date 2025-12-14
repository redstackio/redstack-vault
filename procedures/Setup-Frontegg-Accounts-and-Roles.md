---
id: proc-frontegg-setup-001
tags:
  - account-setup
  - frontegg
  - initial-access
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
updated_at: '2025-12-14T17:32:29.180Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Setup-Frontegg-Accounts-and-Roles

## Summary

This procedure establishes the necessary Owner and Admin accounts in Frontegg to test access control boundaries, simulating a multi-user tenant environment for vulnerability exploitation.

## Description

In the context of testing Frontegg's API access controls, create two user accounts: one as Owner and one as Admin. The Owner invites the Admin to the tenant, assigning the Admin role. This setup allows demonstration of how lower-privileged users can access higher-privileged resources. Prerequisites include access to the Frontegg registration page and email for invitations. Expected outcome: Admin has limited UI access but can exploit API endpoints.

## Requirements

1. Internet access to Frontegg signup page
2. Valid email addresses for two accounts
3. Browser for UI navigation

## Defense

Defensive measures and detection strategies:

- Enforce strict role-based access control (RBAC) in API endpoints
- Log all account invitations and role assignments for auditing
- Use multi-factor authentication (MFA) for account creation

## Objectives

1. Create foundational accounts for privilege testing
2. Assign roles to mimic real tenant hierarchies
3. Establish baseline for access control validation

## Instructions

### Step 1: Register Owner Account

**Context**: Create the primary Owner account to control the tenant.

Navigate to the Frontegg registration page and sign up with a new email.

**Expected Output**: Owner account dashboard accessible.

### Step 2: Register Admin Account

**Context**: Prepare the secondary account for invitation.

Sign up with a different email to create the Admin account.

**Expected Output**: Separate login for Admin account.

### Step 3: Invite Admin from Owner Panel

**Context**: Grant Admin role to enable targeted actions.

Log in as Owner, go to tenant users section, and send invitation with Admin role.

**Expected Output**: Invitation sent; Admin accepts via email.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-setup]]
- [[frontegg]]
- [[initial-access]]
