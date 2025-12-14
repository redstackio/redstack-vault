---
tags:
  - authentication
  - admin-access
  - concrete-cms
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
updated_at: '2025-12-14T03:16:02.522Z'
skill_level: basic
impact_level: medium
detection_risk: low
sub_techniques: []
id: c7461bff-0369-47a2-967f-08f1c84388ab
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-as-Admin-to-Concrete-CMS

## Summary

This procedure describes authenticating as an administrator in Concrete CMS to gain access to privileged features like Express entity management, a prerequisite for exploiting the stored XSS vulnerability.

## Description

Access the login interface of the Concrete CMS instance and use valid admin credentials to authenticate. This grants access to the dashboard where system settings, including Express entities, can be modified. The procedure assumes the CMS is already installed and running. Expected outcome is a session with admin privileges, enabling further actions without restrictions.

## Requirements

1. Running Concrete CMS instance
2. Valid admin username and password
3. Web browser with cookies enabled
4. No two-factor authentication enabled (if present, handle accordingly)

## Defense

Defensive measures and detection strategies:

- Enforce strong password policies and multi-factor authentication (MFA)
- Log and monitor failed login attempts
- Use session timeouts and IP restrictions for admin access

## Objectives

1. Establish an authenticated admin session
2. Access the dashboard for entity manipulation
3. Prepare for vulnerability exploitation

## Instructions

### Step 1: Navigate to Login Page

**Context**: Locate the authentication endpoint.

**Action**:

- Open the web browser and go to http://your-cms-url/index.php/login.

> The login form should appear with fields for username/email and password.

### Step 2: Enter Credentials

**Context**: Provide admin details to authenticate.

**Action**:

- Input the admin username and password.
- Click 'Login' or submit the form.

> Successful authentication redirects to the dashboard.

### Step 3: Verify Admin Access

**Context**: Confirm privileges are granted.

**Action**:

- Check for admin menu items like 'Dashboard' and 'System & Settings'.

> If access is denied, credentials are invalid; retry or reset.

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
- [[admin-access]]
- [[concrete-cms]]
