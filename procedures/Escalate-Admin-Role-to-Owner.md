---
id: proc-bitwarden-escalate-owner
tags:
  - bitwarden
  - privilege-escalation
  - role-manipulation
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:29:36.671Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Escalate-Admin-Role-to-Owner

## Summary

This procedure exploits a business logic flaw in Bitwarden's role editing, allowing an admin to self-promote to owner without authorization checks, gaining full control over the organization.

## Description

Logged in as the admin (accountB), access the organization settings and navigate to the members or invite users section. Locate the entry for accountB and edit the role dropdown from 'Admin' to 'Owner'. The change applies immediately due to missing validation preventing self-escalation. This technique relies on the web UI's lack of restrictions on editing one's own role. Post-escalation, the attacker has owner privileges, including member management.

## Requirements

1. Active admin membership in the target organization
2. Logged-in session for the admin account
3. No two-factor authentication blocking UI actions

## Defense

Defensive measures and detection strategies:

- Implement server-side checks to prevent self-role elevation
- Log and alert on role changes, especially self-edits
- Require owner confirmation for promotions to owner

## Objectives

1. Change admin role to owner via UI
2. Verify escalated privileges
3. Enable subsequent takeover actions

## Instructions

### Step 1: Access Organization Settings

**Context**: Prepare to edit roles from the admin perspective.

Log in to Bitwarden with accountB. Select the organization from the dashboard and click the settings gear icon.

### Step 2: Edit Own Role to Owner

**Context**: Exploit the UI to perform unauthorized escalation.

Navigate to 'Members' or 'Invite Users' section. Find accountB's entry in the list. Click the edit icon (pencil), change the role from 'Admin' to 'Owner', and save the changes.

No confirmation prompt should appear due to the flaw.

### Step 3: Verify Escalation

**Context**: Confirm the role update and new privileges.

Refresh the members list or log out/in. Check that accountB is now listed as 'Owner'. Test by attempting owner-only actions, like viewing billing if applicable.

**Expected Output**: Role updated to owner; full access granted.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Account Manipulation]] Account Manipulation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[bitwarden]]
- [[privilege-escalation]]
- [[role-manipulation]]
