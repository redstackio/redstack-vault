---
id: proc-login-default-remedy-sso-creds
tags:
  - default-credentials
  - auth-bypass
  - sso
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
  - '[[Default Accounts]]'
updated_at: '2025-12-14T17:28:51.546Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Default Accounts]]'
---
# Login-with-Default-Remedy-SSO-Credentials

## Summary

This procedure demonstrates authenticating to a Remedy SSO admin interface using unchanged default credentials, exploiting weak initial configuration to achieve unauthorized administrative access and control over the SSO system.

## Description

Remedy SSO installations often ship with default admin credentials (Username: Admin, Password: RSSO#Admin#) that must be changed post-deployment. If overlooked, attackers can log in directly after accessing the admin page, gaining privileges to modify SSO configurations, view user sessions, and extract infrastructure details. This targets CWE-521 (Weak Password Requirements) and is common in public exposures. The attack assumes no multi-factor authentication or lockouts. Successful login provides full admin dashboard access, enabling high-impact actions like adding rogue users or altering authentication policies for organizations like MTN Group.

## Requirements

1. Access to the Remedy SSO admin login page (from prior procedure)
2. Knowledge of default credentials for BMC Remedy SSO
3. No rate-limiting or CAPTCHA on the login form

## Defense

Defensive measures and detection strategies:

- Enforce mandatory credential changes during initial setup via deployment scripts
- Enable account lockouts after failed login attempts and monitor for brute-force patterns
- Use centralized logging to alert on default credential usage or unusual admin logins from external IPs

## Objectives

1. Bypass authentication using default admin account
2. Gain administrative control over SSO configuration
3. Retrieve sensitive user and infrastructure data

## Instructions

### Step 1: Enter Default Credentials

**Context**: Input the known default username and password into the login form to attempt authentication.

No specific command; manual form submission.

```plaintext
Username: Admin
Password: RSSO#Admin#
```

> Locate the login fields on the page, enter the credentials, and click the submit button (e.g., "Login" or "Sign In").

**Expected Output**: No error message; page redirects to the admin dashboard.

### Step 2: Validate Admin Access

**Context**: Confirm elevated privileges by interacting with admin features.

No specific command; explore the dashboard.

> Navigate to sections like "Users," "Configuration," or "Realm Management" to verify access to sensitive functions.

**Expected Output**: Full admin interface with options to view/edit SSO settings, user data, and infrastructure integrations.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Default Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[default-credentials]]
- [[auth-bypass]]
- [[sso]]
