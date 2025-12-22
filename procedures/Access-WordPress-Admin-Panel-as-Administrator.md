---
tags:
  - wordpress
  - admin-access
  - authentication
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
id: 02726984-6331-48c5-9fde-475cb19655c2
created_at: '2025-12-14T03:15:26.771Z'
updated_at: '2025-12-14T03:15:26.771Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-WordPress-Admin-Panel-as-Administrator

## Summary

This procedure outlines logging into the WordPress admin panel using valid administrator credentials, establishing a session required to access plugin configuration pages vulnerable to exploitation.

## Description

In a WordPress environment, administrative access is necessary to reach backend pages like plugin options. This step assumes possession of valid credentials and focuses on authenticating to the `/wp-admin/` area. It sets the stage for navigating to vulnerable admin pages, such as those in the Huge IT Image Gallery plugin, where DOM-based XSS can be triggered. Expected outcomes include a persistent admin session allowing unrestricted access to configuration interfaces.

## Requirements

1. Valid WordPress administrator username and password
2. Network connectivity to the target WordPress site
3. Web browser with cookies enabled for session management

## Defense

Defensive measures and detection strategies:

- Enforce multi-factor authentication (MFA) for admin logins
- Monitor login attempts for brute-force or unusual IP origins
- Use plugins like Wordfence or Sucuri for login protection and anomaly detection

## Objectives

1. Establish an authenticated admin session
2. Verify administrator privileges
3. Prepare for access to plugin admin pages

## Instructions

### Step 1: Navigate to Login Page

**Context**: Direct the browser to the WordPress login endpoint to initiate authentication.

No specific command; manually enter `https://target.com/wp-admin/` in the browser address bar.

> The login form should appear, prompting for username/email and password.

### Step 2: Authenticate with Credentials

**Context**: Submit administrator credentials to obtain a session cookie.

Enter username and password into the form fields and click 'Log In'.

> Upon success, redirect to the dashboard at `/wp-admin/index.php`. Check the user menu in the top-right to confirm 'Administrator' role.

### Step 3: Verify Session

**Context**: Ensure the session is active and privileges are sufficient.

Navigate to any admin page, such as Settings > General, to confirm unrestricted access.

> Successful verification shows editable admin options without permission errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[wordpress]]
- [[admin-access]]
- [[authentication]]
