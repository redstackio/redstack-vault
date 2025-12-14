---
id: proc-register-new-account
tags:
  - account-creation
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
updated_at: '2025-12-14T03:46:38.069Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Register-New-Account

## Summary

This procedure outlines creating a new user account on a web application to gain initial access for further exploitation, such as injecting payloads in subsequent steps.

## Description

In the context of exploiting web vulnerabilities like stored XSS, registering an account provides the attacker with a controlled environment to modify profile data. This targets applications with self-service registration, assuming no CAPTCHA or strict validation blocks basic sign-ups. Expected outcome is an active account ready for login and profile editing.

## Requirements

1. Access to a valid email address for registration and verification
2. Knowledge of the target's registration endpoint (e.g., /register)
3. Web browser for form submission

## Defense

Defensive measures and detection strategies:

- Implement CAPTCHA or rate limiting on registration to prevent abuse
- Monitor for bulk account creations from suspicious IPs

## Objectives

1. Establish attacker presence in the application
2. Enable access to user-specific features like profile editing
3. Prepare for payload injection without alerting defenses

## Instructions

### Step 1: Navigate to Registration

**Context**: Locate and access the account creation form to begin setup.

No specific command; use browser to visit the registration URL (e.g., https://target.com/register) and fill in fields: email (attacker-controlled), password, and any required details like username.

> Submit the form. Expected output: Success message or email sent for verification.

### Step 2: Submit Registration Form

**Context**: Complete the form submission to trigger account creation.

Provide details such as email: test@attacker.com, password: SecurePass123. Click 'Register'.

> Expected output: Redirect or confirmation page indicating account pending verification.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-creation]]
- [[web-registration]]
