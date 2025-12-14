---
tags:
  - user-creation
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
  - '[[External Remote Services]]'
updated_at: '2025-12-14T17:26:22.513Z'
sub_techniques: []
id: 209c248c-6c78-438c-8e41-239fd3496028
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[External Remote Services]]'
---
# Create-Low-Privilege-User

## Summary

Create a standard user account in Nextcloud without group privileges to gain initial foothold for file upload and exploitation.

## Description

As an admin, create a new user via the web interface. This user has no special privileges, simulating an unprivileged attacker. Log in as this user to proceed with payload upload, ensuring the attack remains stealthy.

## Requirements

1. Admin access to Nextcloud
2. Web browser
3. No additional tools needed

## Defense

Defensive measures and detection strategies:

- Limit user creation to admins only
- Monitor new user accounts via logs
- Implement approval workflows for new users

## Objectives

1. Gain authenticated access as low-priv user
2. Avoid detection by using standard accounts
3. Prepare for file operations

## Instructions

### Step 1: Admin Login and User Creation

**Context**: Use admin credentials to add a new user.

Log in as admin, go to Settings > Users, click 'New user'. Enter details (e.g., username: normaluser, no groups), set password, and create.

### Step 2: Login as New User

**Context**: Switch to the low-priv account.

Log out, then log in with the new user's credentials.

**Expected Output**: Dashboard for new user loads.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[External Remote Services]] External Remote Services

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- user-creation
- initial-access
