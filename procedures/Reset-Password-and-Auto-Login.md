---
tags:
  - account-takeover
  - auto-login
  - improper-auth
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 2fe902e4-8998-4f41-9bf1-bfc953ace7ae
created_at: '2025-12-14T17:28:58.782Z'
updated_at: '2025-12-14T17:28:58.782Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Reset-Password-and-Auto-Login

## Summary

This procedure uses a compromised password reset link to change the account password and automatically log in, bypassing any additional authentication due to missing access controls.

## Description

Exploiting the Legal Robot flaw, submitting a new password via the reset endpoint grants immediate session access, leading to account takeover. This violates OWASP guidelines for forgot password flows. Expected outcome is full unauthorized access to the account's data and functions. Requires a valid reset link from previous steps.

## Requirements

1. Compromised reset link
2. Web browser for form submission
3. New password meeting application policies

## Defense

Defensive measures and detection strategies:

- Require re-authentication or CAPTCHA after reset
- Implement multi-factor authentication (MFA) prompts post-reset
- Log password changes and alert users via secondary channels

## Objectives

1. Change the target account's password
2. Establish an authenticated session
3. Achieve complete account control

## Instructions

### Step 1: Access Reset Form

**Context**: Load the compromised link to reach the password change interface.

Paste the reset link into a browser and navigate to it.

> The page should display a form for entering a new password without prompting for login credentials.

### Step 2: Submit New Password

**Context**: Update the password and trigger the auto-login.

Enter the new password twice (if required) and submit the form.

> Upon submission, the application processes the change and redirects to the dashboard with an active session, confirming the vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-takeover]]
- [[access-control]]
