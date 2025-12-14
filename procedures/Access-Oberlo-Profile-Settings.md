---
id: proc-access-oberlo-profile
tags:
  - navigation
  - profile-access
  - oberlo
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
updated_at: '2025-12-14T03:47:18.238Z'
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
# Access-Oberlo-Profile-Settings

## Summary

This procedure details how to navigate to the user profile settings in Oberlo after authentication, positioning the attacker to reach the vulnerable name field for XSS injection.

## Description

Once logged in, the profile settings page at https://app.oberlo.com/settings/account/profile contains the editable name field lacking proper sanitization. This step involves standard UI navigation within the authenticated session. It sets the stage for payload injection and assumes the account creation procedure has been completed. Outcomes include access to the form where exploitation occurs.

## Requirements

1. Active authenticated session in Oberlo
2. Web browser
3. Dashboard access from prior login

## Defense

Defensive measures and detection strategies:

- Log and monitor access to sensitive settings pages
- Implement role-based access controls for profile edits
- Alert on unusual navigation patterns post-login

## Objectives

1. Reach the profile editing interface
2. Expose the vulnerable name input field
3. Prepare for payload submission

## Instructions

### Step 1: Log In to Dashboard

**Context**: Ensure an active session before navigating.

If not already logged in, access https://app.oberlo.com/auth/login and authenticate.

> Dashboard loads upon successful login.

### Step 2: Navigate to Settings

**Context**: Locate the profile management section.

From the dashboard, click on the user menu (typically top-right) and select "Settings" or "Account".

> This opens the account settings overview.

### Step 3: Select Profile Tab

**Context**: Target the specific profile editing page.

Within settings, choose "Profile" to load https://app.oberlo.com/settings/account/profile.

> The page displays editable fields including the vulnerable Name input.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[navigation]]
- [[profile-access]]
- [[oberlo]]
