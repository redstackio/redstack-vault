---
tags:
  - authentication
  - web-login
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
updated_at: '2025-12-14T03:15:47.146Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 22c95a64-46cb-4872-adcb-c3065d79801b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Log-into-Informatica-Marketplace-Account

## Summary

This procedure authenticates a user to the Informatica Marketplace web application, granting access to profile management features necessary for subsequent exploitation steps.

## Description

The procedure involves using valid credentials to log into marketplace.informatica.com, targeting the login functionality which uses standard web forms. This establishes a session for editing user profiles. Expected outcomes include a valid session cookie and access to protected pages. Prerequisites include having a registered account.

## Requirements

1. Valid email and password for an Informatica Marketplace account.
2. Web browser with internet access.
3. No VPN or proxy restrictions blocking the site.

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) to prevent unauthorized logins.
- Monitor login attempts for anomalies like unusual IP addresses.

## Objectives

1. Establish an authenticated session.
2. Gain access to user profile editing.
3. Prepare for payload injection without session expiration.

## Instructions

### Step 1: Navigate to Login Page

**Context**: Access the authentication endpoint to begin the login process.

Navigate to `https://marketplace.informatica.com` and click on the login link, or directly go to the login form.

> Upon loading, the form should display fields for email and password.

### Step 2: Submit Credentials

**Context**: Provide authentication details to obtain a session.

Enter the email address and password in the respective fields, then submit the form.

> Successful login redirects to the user dashboard, with session cookies set in the browser.

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
- [[web-login]]
