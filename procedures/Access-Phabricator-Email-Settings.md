---
id: access-email-settings-uuid
name: Access-Phabricator-Email-Settings
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.842Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - email-settings
  - phabricator
commands: []
platforms:
  - Web
tools:
  - '[[tools/Lightning-Browser]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---

# Access-Phabricator-Email-Settings

## Summary

This procedure details navigating to the email settings page in Phabricator using an authenticated session, setting the stage for intercepting sensitive requests during email addition.

## Description

Once logged in, the email settings page allows users to manage associated emails, which is vulnerable to request replay due to weak validation. Use a mobile browser to mimic victim behavior and capture traffic. The endpoint is `/settings/user/(username)/page/email/`. Prerequisites include valid session cookies from login.

## Requirements

1. Active Phabricator session with victim's credentials
2. Mobile browser for traffic interception compatibility
3. Knowledge of victim's username

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) for settings changes
- Log and alert on access to sensitive settings pages from unusual user agents

## Objectives

1. Reach the email management interface
2. Prepare for form submission interception
3. Validate session integrity

## Instructions

### Step 1: Log In

**Context**: Ensure authenticated access.

Use the browser to log in at the Phabricator login page.

> Expected output: Session cookies set.

### Step 2: Navigate to Settings

**Context**: Direct to email page.

Enter URL: `https://admin.phacility.com/settings/user/(username)/page/email/`.

> Expected output: Page loads with email list and add form.

### Step 3: Verify Access

**Context**: Confirm permissions.

Check if add email button is present.

> Expected output: Form fields for new email visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

None

## Commands Used

None

## Tools Used

- [[tools/Lightning-Browser]]

## Tags

- [[email-settings]]
- [[phabricator]]
