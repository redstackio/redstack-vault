---
tags:
  - setup
  - team-invite
type: procedure
tools:
  - '[[tools/Browser]]'
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
updated_at: '2025-12-14T17:25:29.259Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: b5dc5b41-aca5-491d-87b7-31d4f3bb2118
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Setup-Team-and-Users

## Summary

This procedure establishes a testing environment by creating a team with an admin victim and a low-privilege attacker user, enabling subsequent IDOR exploitation within team contexts.

## Description

In the target web application, log in as an admin to invite a new user with 'USER' role. This simulates a real team setup where UUIDs are exposed in shared features like conversation assignments. Prerequisites include valid admin credentials and access to the invitation UI. Expected outcome: Attacker (user2) joins the team without elevated privileges.

## Requirements

1. Admin credentials for initial login
2. Access to team invitation features in the web app
3. Valid email for new user registration

## Defense

Defensive measures and detection strategies:

- Restrict team invitations to verified admins only
- Log all user invitations and monitor for anomalous patterns
- Implement rate limiting on invite functions

## Objectives

1. Create controlled environment for privilege escalation testing
2. Ensure attacker has team membership for UUID discovery
3. Validate low-privilege role assignment

## Instructions

### Step 1: Admin Login and Invite

**Context**: Gain initial access as admin to perform team setup.

**Command** (Browser Navigation):

No CLI command; use browser to log in at https://app.outpost.co/sign-in and navigate to team settings.

> Log in with user1 credentials, go to team management, and invite user2 via email with 'USER' role. Expected: Invitation sent.

### Step 2: Accept Invitation

**Context**: Complete user2 onboarding to join the team.

**Command** (Browser Navigation):

Use email link to register user2 and confirm team join.

> Expected: user2 dashboard accessible with 'USER' role.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser]]

## Tags

- [[setup]]
- [[team-invite]]
