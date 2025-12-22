---
id: proc-uuid-create-auth
tags:
  - authentication
  - initial-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T04:08:48.179Z'
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
# Create-Account-and-Authenticate

## Summary

This procedure establishes initial authenticated access to the target web application by creating a test user account and logging in, enabling navigation to vulnerable features like the profile editor.

## Description

In the context of exploiting web vulnerabilities such as SSRF, authenticated access is often required to interact with user-specific features. This procedure targets self-registration-enabled applications like Moodle, where no prior credentials are needed. It sets the stage for reaching the image upload URL downloader in the profile edit page, from which SSRF can be triggered.

## Requirements

1. External network access to the target web application
2. Web browser (e.g., Firefox or Chrome)
3. No special tools required for this step

## Defense

Defensive measures and detection strategies:

- Disable self-registration or require admin approval for new accounts
- Monitor for unusual registration patterns or rapid account creations
- Implement rate limiting on login endpoints

## Objectives

1. Gain legitimate user access to the application
2. Reach the profile editing interface
3. Prepare for vulnerability exploitation without raising alerts

## Instructions

### Step 1: Register New Account

**Context**: Create a test user to simulate legitimate access.

Navigate to the registration page (typically `/login/signup.php` or similar) and fill in details like username, email, and password. Submit the form.

**Expected Output**: Confirmation email or direct dashboard access upon successful registration.

### Step 2: Authenticate

**Context**: Log in to access protected areas.

Go to the login page (e.g., `/login/index.php`), enter the created credentials, and submit.

**Expected Output**: Redirect to user dashboard.

### Step 3: Navigate to Profile Edit

**Context**: Locate the vulnerable feature.

From the dashboard, go to `/user/edit.php` and scroll to the user picture/image upload section, which opens the URL downloader interface.

**Expected Output**: URL downloader field visible for remote image fetching.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[authentication]]
- [[initial-access]]
