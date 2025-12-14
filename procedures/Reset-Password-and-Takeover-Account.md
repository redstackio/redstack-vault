---
id: proc-uuid-003
tags:
  - account-takeover
  - password-reset
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:33:06.399Z'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Account Manipulation]]'
---
# Reset-Password-and-Takeover-Account

## Summary

This procedure uses an extracted password reset token to access the reset form, change the admin password, and log in to achieve full account takeover.

## Description

With the token in hand from blind injection, the /admin/sp/{token} route allows unauthenticated password updates via POST. Submitting a new password overwrites the target's credentials. Logging in grants admin privileges, enabling site control, data deletion, or content manipulation in FlintCMS.

## Requirements

1. Valid extracted reset token
2. Access to localhost:4000
3. Browser or HTTP client for form submission

## Defense

Defensive measures and detection strategies:

- Expire reset tokens quickly (e.g., 15 minutes)
- Require additional verification (e.g., CAPTCHA) on reset
- Audit logs for token usage and password changes

## Objectives

1. Overwrite target account password
2. Gain authenticated admin access
3. Demonstrate full compromise impact

## Instructions

### Step 1: Access Reset Page

**Context**: Use token to reach the form.

Visit http://localhost:4000/admin/sp/{extracted_token} in a browser.

**Expected Output**: Password reset form loads without authentication.

### Step 2: Submit New Password

**Context**: Update credentials.

Enter and confirm a new password (e.g., newadminpass) and submit the form.

**Expected Output**: Success message or redirect to login.

### Step 3: Log In with New Credentials

**Context**: Verify takeover.

Go to /admin/login, enter email admin@localhost.com and new password to access dashboard.

**Expected Output**: Admin panel with full controls.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Valid Accounts]]
- [[Account Manipulation]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-takeover]]
- [[password-reset]]
