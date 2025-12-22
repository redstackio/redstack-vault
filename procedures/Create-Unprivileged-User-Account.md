---
tags:
  - wordpress
  - user-creation
  - account
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
  - WordPress
techniques:
  - '[[External Remote Services]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques:
  - '[[T1133.001]]'
id: f3c29c48-3885-4a0e-a3ab-84ad24dee1a9
created_at: '2025-12-13T23:55:20.653Z'
updated_at: '2025-12-13T23:55:20.653Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[External Remote Services]]'
---
# Create-Unprivileged-User-Account

## Summary

This procedure registers a standard, unprivileged user account on a WordPress site, providing a vector for injecting payloads into profile fields without requiring special permissions.

## Description

WordPress sites often allow open registration. This step creates a basic user account that can edit its own profile, targeting the bio field vulnerable to stored XSS via wp_targeted_link_rel. The account has no administrative privileges, simulating a legitimate user action.

## Requirements

1. User registration enabled on the WordPress site
2. Access to the registration form (typically `/wp-login.php?action=register`)
3. Valid email address for verification

## Defense

Defensive measures and detection strategies:

- Disable open registration or require approval
- Implement CAPTCHA on registration forms
- Log and review new account creations

## Objectives

1. Obtain a foothold as a low-privilege user
2. Enable profile editing for payload insertion
3. Avoid detection by mimicking normal user behavior

## Instructions

### Step 1: Navigate to Registration

**Context**: Access the site's user creation interface.

Visit the WordPress registration page.

> URL: `https://target-site.com/wp-login.php?action=register`

### Step 2: Fill Registration Form

**Context**: Provide minimal details to create the account.

Enter username, email, and password; submit the form.

> Use a non-suspicious username and valid email to avoid blocks.

### Step 3: Confirm Account

**Context**: Activate if email verification is required.

Check email for activation link and click to complete registration.

> Log in with the new credentials to verify access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[External Remote Services]]

### Sub-Techniques

- [[T1133.001]]

## Commands Used


## Tools Used


## Tags

- [[wordpress]]
- [[registration]]
- [[user-account]]
