---
tags:
  - initial-access
  - account-creation
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
updated_at: '2025-12-14T17:28:51.693Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 1f3f58fa-2fe1-46af-8e5d-c012c7cc51c0
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-Verified-Account-and-Access-Dashboard

## Summary

This procedure establishes initial access to the vulnerable DoD web application by creating a standard user account, verifying it, and navigating to the dashboard, exploiting the ease of registration to bypass higher privilege requirements.

## Description

In the context of the DoD application's improper access controls, attackers can register without special credentials and immediately access features intended for privileged users. This step requires only a web browser and internet access, leading to the dashboard where further exploitation occurs. Expected outcomes include a verified account and dashboard visibility, setting the stage for PII exposure.

## Requirements

1. Web browser with JavaScript enabled
2. Valid email for verification
3. Access to the redacted application URL `███████/`

## Defense

Defensive measures and detection strategies:

- Implement CAPTCHA or additional verification during registration to deter automated account creation.
- Monitor for unusual registration spikes and dashboard access patterns from new accounts.
- Enforce role-based access control (RBAC) immediately post-registration.

## Objectives

1. Gain a foothold as a verified standard user.
2. Reach the dashboard interface without elevated privileges.
3. Validate access to widget features.

## Instructions

### Step 1: Register New Account

**Context**: Begin by creating a basic user account on the application.

Navigate to `███████/` and fill out the registration form with minimal details (e.g., username, email, password). Submit the form.

> Upon submission, an email verification link is sent. No code block needed as this is UI-based.

### Step 2: Verify Account

**Context**: Complete verification to activate the account.

Check your email and click the verification link provided.

> Successful verification redirects to login; log in with the new credentials.

### Step 3: Access Dashboard

**Context**: Navigate to the vulnerable dashboard page.

After login, go to `███████` in the application menu or URL bar.

> The dashboard loads, potentially prompting for initial setup if new.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[initial-access]]
- [[account-creation]]
