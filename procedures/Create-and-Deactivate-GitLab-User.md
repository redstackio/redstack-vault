---
tags:
  - gitlab
  - user-management
  - deactivation
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Create Account]]'
updated_at: '2025-12-14T17:25:59.536Z'
sub_techniques: []
id: 31e9c169-57af-445a-bbd9-bbf86109b70d
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Create Account]]'
---
# Create-and-Deactivate-GitLab-User

## Summary

This procedure creates a new user account in GitLab using admin privileges and immediately deactivates it to simulate a restricted account for testing API bypasses.

## Description

In the context of GitLab's authorization bypass vulnerability, this sets up a deactivated user that can still authenticate via personal access tokens to the GraphQL API. The process uses the GitLab admin panel, as direct API creation is possible but panel is simpler for initial setup. Expected outcome is a user with no activity, allowing clean deactivation without warnings.

## Requirements

1. Admin access to GitLab instance
2. Web browser access to GitLab admin panel
3. No existing user conflicts

## Defense

Defensive measures and detection strategies:

- Monitor admin user creation logs for unusual patterns
- Enforce two-factor authentication for admin accounts
- Audit deactivated users periodically

## Objectives

1. Establish a test deactivated user
2. Ensure no activity to avoid reactivation prompts
3. Prepare for token generation

## Instructions

### Step 1: Login as Admin

**Context**: Gain admin privileges to access user management.

Log in to GitLab with admin credentials and navigate to Admin Area > Users.

### Step 2: Create New User

**Context**: Add a new user account via the admin panel.

Click 'New User', fill in details (e.g., username, email, name), and create the account. Do not send invitation email.

> This creates the user without requiring password setup.

### Step 3: Deactivate User

**Context**: Immediately deactivate to apply restrictions.

Edit the new user and toggle 'Active' to false, then save.

> Deactivation prevents web login but not API token use in GraphQL.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Create Account]] Create Account

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/curl]]

## Tags

- gitlab
- admin
- user-creation
