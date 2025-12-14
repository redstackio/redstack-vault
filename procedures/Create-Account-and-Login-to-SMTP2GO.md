---
tags:
  - initial-access
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
updated_at: '2025-12-13T23:52:25.355Z'
sub_techniques: []
id: e3e9332c-7e35-474a-981f-29390f91229a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-Account-and-Login-to-SMTP2GO

## Summary

This procedure establishes authenticated access to the SMTP2GO web application by creating a new account and logging in, serving as the entry point for exploiting vulnerabilities in user management features.

## Description

The SMTP2GO application allows public registration at https://app.smtp2go.com. An attacker uses this to gain a legitimate session, enabling navigation to sensitive settings like SMTP user creation where the XSS vulnerability resides. Expected outcomes include a valid session cookie for subsequent actions, with no technical barriers beyond basic email verification.

## Requirements

1. Valid email address for registration
2. Web browser with JavaScript enabled
3. Internet access to https://app.smtp2go.com

## Defense

Defensive measures and detection strategies:

- Implement CAPTCHA or rate limiting on registration endpoints
- Monitor for anomalous account creation patterns from new IPs
- Log all login attempts and flag rapid successive registrations

## Objectives

1. Obtain a valid user session for dashboard access
2. Verify application accessibility without restrictions
3. Prepare for internal navigation to vulnerable features

## Instructions

### Step 1: Access Registration Page

**Context**: Reach the public-facing registration interface to create a new account.

Navigate to https://app.smtp2go.com and click the registration link if not already on the login page.

### Step 2: Enter Credentials and Register

**Context**: Provide minimal required details to complete account creation.

Fill in email, password, and any other fields (e.g., name), then submit the form. Confirm via email if prompted.

### Step 3: Login to Dashboard

**Context**: Authenticate to gain access to the main application interface.

Enter the newly created credentials on the login form and submit to redirect to the dashboard.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[initial-access]]
- [[web]]

