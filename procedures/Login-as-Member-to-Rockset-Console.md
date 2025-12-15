---
tags:
  - authentication
  - rockset
  - member-login
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:51.656Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 11f595ea-1381-4671-87fb-501c302f204b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-as-Member-to-Rockset-Console

## Summary

This procedure describes authenticating into the Rockset console using a member account credentials obtained from an invitation email, establishing a session with limited UI privileges for further access testing.

## Description

After receiving an invitation, the member uses the provided email and temporary password to log in at https://console.rockset.com/. This grants access to the member dashboard, where admin features like billing are hidden from the menu. The procedure targets the login endpoint and expects a redirect to a restricted view, setting up the environment for direct URL bypass. No special tools are needed beyond a browser.

## Requirements

1. Invitation email with member credentials (email and temp password)
2. Web browser access to https://console.rockset.com/
3. Stable internet connection

## Defense

Defensive measures and detection strategies:

- Enforce multi-factor authentication (MFA) on all logins
- Monitor login logs for unusual IP addresses or failed attempts
- Implement session timeouts and IP binding for console access

## Objectives

1. Establish a valid member session
2. Confirm limited privilege view loads
3. Prepare for menu verification and URL bypass

## Instructions

### Step 1: Navigate to Login Page

**Context**: Reach the authentication endpoint.

Open a browser and go to https://console.rockset.com/.

> The login form should appear, prompting for email and password.

### Step 2: Authenticate as Member

**Context**: Use invitation details to sign in.

Enter the member email (e.g., himanshujoshitest2019@gmail.com) and temporary password from the email. Click 'Login' or submit.

> Successful login redirects to the member dashboard; change password if prompted.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- authentication
- rockset
- member-login
