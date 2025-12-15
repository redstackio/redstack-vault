---
id: uuid-placeholder-3
tags:
  - role-promotion
  - buddypress
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
  - WordPress
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:51.922Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Promote-User-to-Group-Moderator

## Summary

This procedure legitimately promotes a user to moderator role in a BuddyPress group using admin privileges, setting the stage for subsequent unauthorized escalation.

## Description

As part of the privilege escalation chain, log in as the group admin (account A) to elevate the attacker (account B) to moderator in group 'abc'. This uses the standard BuddyPress admin interface but highlights the need for the vulnerability in the REST API. Prerequisites include existing group and user setup. Outcome: Attacker gains limited elevated access for request capture.

## Requirements

1. Logged-in access as group admin (account A)
2. Group 'abc' with B as member
3. BuddyPress group management enabled

## Defense

Defensive measures and detection strategies:

- Log all role changes with admin notifications
- Restrict moderator promotions to site-wide admins
- Audit group admin actions periodically

## Objectives

1. Grant moderator privileges to attacker for API access
2. Establish baseline for escalation testing
3. Verify legitimate role change works

## Instructions

### Step 1: Access Group Admin Interface

**Context**: Navigate to manage members as admin.

Log in as A, go to /groups/abc/admin/manage-members/.

### Step 2: Select and Promote User

**Context**: Perform the role elevation.

Select account B from the members list, choose 'Promote to Moderator', and confirm the action.

**Expected Output**: B's role updated to moderator in the interface.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- role-promotion
- buddypress
