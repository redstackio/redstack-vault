---
tags:
  - setup
  - authentication
  - concrete-cms
type: procedure
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Chrome]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: d2905810-403b-44b0-9f73-31dc27d5ac74
created_at: '2025-12-14T03:16:20.412Z'
updated_at: '2025-12-14T03:16:20.412Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Prepare-Test-Environment-in-Concrete-CMS

## Summary

This procedure sets up a test environment in Concrete CMS by creating admin and secondary user accounts, enabling simulation of a multi-user stored XSS attack scenario.

## Description

In a Concrete CMS instance (version 8.3.1), log in as an administrator to create a secondary user with admin privileges for calendar access. Use separate browser sessions to mimic distinct authenticated users, ensuring the environment is ready for injecting and triggering XSS payloads without interference.

## Requirements

1. Access to a running Concrete CMS instance with admin credentials
2. Updated web browser (Firefox or Chrome) for multiple sessions
3. Permissions to manage users in the dashboard

## Defense

Defensive measures and detection strategies:

- Implement role-based access control to limit user creation to trusted admins
- Monitor user account creations via audit logs in CMS
- Use multi-factor authentication for admin logins

## Objectives

1. Establish isolated sessions for attacker and victim simulation
2. Ensure secondary user has necessary permissions for event creation
3. Validate environment setup without triggering alerts

## Instructions

### Step 1: Log In as Admin

**Context**: Gain initial access to the dashboard for user management.

Open Firefox or Chrome and navigate to the Concrete CMS login page. Enter admin credentials to authenticate.

**Expected Output**: Dashboard accessible.

### Step 2: Create Secondary User

**Context**: Add a test user with admin privileges to simulate an attacker.

Navigate to System & Settings > Users & Groups in the dashboard. Create a new user named 'user2' and assign to the Administrators group for calendar access.

**Expected Output**: User2 account created successfully.

### Step 3: Prepare Separate Session

**Context**: Simulate a distinct user session using incognito mode.

Open a new incognito/private window in Chrome or Firefox, log in as user2.

**Expected Output**: User2 session active without sharing cookies with admin session.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]
- [[tools/Chrome]]

## Tags

- [[setup]]
- [[concrete-cms]]
