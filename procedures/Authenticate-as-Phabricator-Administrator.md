---
tags:
  - authentication
  - phabricator
  - admin-access
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
updated_at: '2025-12-14T04:08:46.192Z'
sub_techniques: []
id: 1b2ee69b-f8d9-4d46-b69d-00cf709c8aba
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Authenticate-as-Phabricator-Administrator

## Summary

This procedure outlines logging into Phabricator as an administrator to access privileged configuration interfaces, a prerequisite for exploiting vulnerabilities like SSRF in admin settings.

## Description

Phabricator is a PHP-based collaboration platform where administrative users can modify server configurations. This step ensures the attacker has the necessary privileges to reach the notifications.server settings. Without admin access, the configuration cannot be altered. The procedure assumes valid credentials are available, either through prior compromise or legitimate access.

## Requirements

1. Valid Phabricator administrator username and password
2. Network access to the Phabricator web interface (typically HTTPS on port 443)
3. Modern web browser for session management

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) for admin accounts
- Monitor login attempts and session creations in Phabricator logs
- Use role-based access controls to limit configuration changes

## Objectives

1. Establish an authenticated admin session
2. Verify access to configuration menus
3. Prepare for subsequent privilege exploitation

## Instructions

### Step 1: Access Phabricator Login Page

**Context**: Open the Phabricator installation URL in a browser to initiate authentication.

No specific command; navigate to https://phabricator.mycompany.com/ and enter admin credentials.

> Successful login redirects to the dashboard with admin indicators.

### Step 2: Verify Administrative Privileges

**Context**: Confirm the session grants access to admin features.

Check the user menu or dashboard for 'Config' or 'Settings' options.

> Expected output: Admin-only menus visible, confirming elevated access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[authentication]]
- [[phabricator]]
- [[admin-access]]
