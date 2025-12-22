---
tags:
  - authentication
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
updated_at: '2025-12-14T03:47:18.407Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 5fd222e4-454c-4339-88a4-9312bd4f449d
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Authenticate-as-Administrator

## Summary

This procedure describes logging into the target web application using administrative credentials to gain elevated privileges for subsequent actions like client creation in the Ubiquiti UCRM demo.

## Description

Authentication as an administrator provides the necessary permissions to access sensitive forms and features. In this scenario, valid admin credentials are used to log into https://dev-ucrm-billing-demo.ubnt.com/, bypassing any guest restrictions and enabling the creation of clients with custom attributes vulnerable to XSS.

## Requirements

1. Valid admin username and password for the application.
2. Network access to the login endpoint.
3. Modern web browser for form submission.

## Defense

Defensive measures and detection strategies:

- Enforce multi-factor authentication (MFA) for admin accounts.
- Monitor login attempts for brute-force or unusual IP origins.
- Use session timeouts and IP whitelisting for admin access.

## Objectives

1. Establish a privileged session in the application.
2. Access admin-only features like client management.
3. Avoid detection during initial access.

## Instructions

### Step 1: Navigate to Login

**Context**: Access the authentication endpoint to begin the login process.

No command; use browser to visit https://dev-ucrm-billing-demo.ubnt.com/.

> Enter the URL in the browser address bar. Expected output: Login form appears.

### Step 2: Submit Credentials

**Context**: Provide admin credentials to authenticate.

Fill in username and password fields, then submit the form.

> Click login button after entering credentials. Expected output: Redirect to admin dashboard with session cookie set.

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
