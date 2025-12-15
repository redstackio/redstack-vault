---
tags:
  - nextcloud
  - authentication
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
updated_at: '2025-12-14T17:29:57.045Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
id: 16975c55-d228-4b47-8241-602c953218a4
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-as-Group-Admin

## Summary

Authenticate into Nextcloud using the newly created group admin account to access user management functionalities required for the exploit.

## Description

This procedure involves standard login to switch to the group admin context. It ensures the session has the necessary permissions to create and delete users, which interact with the filesystem. Target environment is the Nextcloud web interface; prerequisites include valid credentials from the prior user creation step.

## Requirements

1. Credentials for the group admin user (username/password)
2. Network access to Nextcloud login page
3. Web browser with cookies enabled

## Defense

Defensive measures and detection strategies:

- Enforce multi-factor authentication (MFA) for admin accounts
- Log all login events and alert on logins from unusual IPs
- Session timeout and IP binding to prevent unauthorized access

## Objectives

1. Gain active session as group admin
2. Verify access to admin features
3. Set stage for user creation/deletion

## Instructions

### Step 1: Navigate to Login Page

**Context**: Access the Nextcloud instance login.

No specific command; use browser:

- Enter URL: https://nextcloud.example.com/login

> Page loads with username/password fields.

### Step 2: Authenticate

**Context**: Enter credentials and submit.

No specific command; in the form:

- Username: [group-admin-username]
- Password: [password]
- Click 'Log in'

> Dashboard loads if successful, with admin menu available.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[nextcloud]]
- [[login]]
