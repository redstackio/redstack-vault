---
tags:
  - nextcloud
  - user-management
  - privilege-escalation
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:29:57.050Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 706d9f0f-b677-4b36-a60d-f51b9d594baf
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-and-Assign-Group-Admin-User

## Summary

This procedure creates a new user in Nextcloud and assigns them as an admin to an arbitrary group, setting up a controlled account for further exploitation of user management features.

## Description

In the context of Nextcloud's admin interface, group admins can create users and assign roles. This step assumes initial access as a group admin and uses the web UI to prepare an exploit account. The lack of validation in user creation allows subsequent steps to target filesystem directories. Expected outcome: A new group admin user ready for login and malicious actions.

## Requirements

1. Valid group admin credentials in Nextcloud
2. Access to the admin settings via web browser
3. Active Nextcloud session

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls to limit group admin user creation
- Monitor user creation logs for unusual patterns (e.g., rapid admin assignments)
- Use filesystem auditing to detect unexpected directory interactions

## Objectives

1. Establish a secondary admin account for isolation in exploitation
2. Verify group admin permissions for user management
3. Prepare for targeted user creation matching filesystem paths

## Instructions

### Step 1: Access User Management

**Context**: Log in as the initial group admin and navigate to the users section to initiate creation.

No specific command; use the Nextcloud web interface:

- Go to Settings > Administration > Users
- Click 'Add user' button

> This opens the user creation form. Fill in basic details like username and password.

### Step 2: Assign Group Admin Role

**Context**: During or after creation, assign the new user to a group and set as group admin.

No specific command; in the UI:

- Select an existing group or create one
- Edit group settings to add the new user as admin

> Confirmation appears in the group members list. Successful if the user shows admin privileges.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[nextcloud]]
- [[user-creation]]
