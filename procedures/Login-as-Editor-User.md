---
tags:
  - wordpress
  - editor-role
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
updated_at: '2025-12-14T17:29:44.825Z'
sub_techniques: []
id: c5d3ea6a-5cb2-4a25-8323-8c79610a61c3
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-as-Editor-User

## Summary

This procedure authenticates the attacker as the elevated Editor user to access WordPress with enhanced capabilities for content injection.

## Description

Using the newly set credentials, log in to switch sessions from Shop Manager to Editor. Editors in WordPress have broad permissions, including post creation with unfiltered HTML/JS. This step transitions control to the compromised account. Expected outcome: Editor dashboard session.

## Requirements

1. Updated Editor user credentials
2. Access to the login endpoint
3. Logout from previous session if necessary

## Defense

Defensive measures and detection strategies:

- Implement session timeout and IP binding for admin logins
- Monitor for multiple logins from the same user account
- Use role-based login auditing

## Objectives

1. Establish Editor session
2. Verify elevated capabilities
3. Set up for XSS payload deployment

## Instructions

### Step 1: Initiate Login

**Context**: Start a new authentication session.

Navigate to https://target.com/wp-login.php and enter the Editor username.

> The form prompts for password.

### Step 2: Submit Credentials

**Context**: Complete authentication.

Enter the new password and log in.

> Redirects to /wp-admin/ with Editor menus visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- wordpress
- login
