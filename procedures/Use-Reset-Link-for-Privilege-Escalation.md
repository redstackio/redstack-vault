---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
name: Use-Reset-Link-for-Privilege-Escalation
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:28:36.691Z'
tactics:
  - '[[Privilege Escalation]]'
techniques:
  - '[[Account Manipulation]]'
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - privilege-escalation
  - account-takeover
  - phabricator
commands: []
platforms:
  - Web
tools: []
skill_level: low
impact_level: high
detection_risk: high
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Account Manipulation]]'
  - '[[Valid Accounts]]'
---

# Use-Reset-Link-for-Privilege-Escalation

## Summary

This procedure utilizes the exposed admin password reset link from daemon logs to change the admin password and gain elevated privileges in Phabricator.

## Description

With the reset link in hand, the attacker can directly access the admin account's reset form, set a new password, and log in as admin. This completes the privilege escalation chain, granting control over Phabricator's administrative functions, such as user management and configuration changes. The link is typically valid for a short time (e.g., 1 hour), so prompt use is essential.

## Requirements

1. Valid password reset URL/token from logs
2. Web browser to access the link
3. No expiration of the token (act within validity period)

## Defense

Defensive measures and detection strategies:

- Shorten reset token lifetimes and require additional verification (e.g., security questions)
- Monitor for unusual password changes on admin accounts and alert immediately
- Enable audit logs for privilege changes and integrate with SIEM

## Objectives

1. Reset the admin password using the exposed link
2. Authenticate as admin to confirm escalation
3. Access restricted admin features

## Instructions

### Step 1: Access Reset Link

**Context**: Open the copied URL to initiate the password change.

No command required; paste the full reset URL (e.g., https://phabricator.example.com/reset?token=abc123) into a browser.

> The page loads a form for new password entry. Expected output: No errors, form visible.

### Step 2: Complete Reset and Login

**Context**: Set new credentials and verify admin access.

No command required; enter a strong new password twice, submit, then log out and log in with admin email and new password.

> Success: Redirect to admin dashboard with elevated options (e.g., manage users). Failure: Token expired or invalid.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Account Manipulation]] Account Manipulation
- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[privilege-escalation]]
- [[account-takeover]]
- [[phabricator]]
