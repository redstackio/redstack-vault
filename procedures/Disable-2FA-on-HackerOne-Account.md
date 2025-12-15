---
id: proc-001
tags:
  - 2fa-bypass
  - preparation
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
updated_at: '2025-12-14T17:24:48.541Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Disable-2FA-on-HackerOne-Account

## Summary

This procedure disables two-factor authentication on a HackerOne account to test submission restrictions and prepare for authorization bypass exploitation in the embedded form.

## Description

In the context of testing HackerOne's vulnerability reporting system, disabling 2FA allows observation of enforcement during normal submissions while setting up conditions for the bypass via the embedded form. This step requires authenticated access to account settings and is a prerequisite for verifying the 2FA block in standard workflows. Expected outcome: Account operates without 2FA prompts, enabling clear testing of bypass success.

## Requirements

1. Valid HackerOne account credentials with 2FA enabled
2. Web browser access to https://hackerone.com
3. No additional tools needed beyond standard browser navigation

## Defense

Defensive measures and detection strategies:

- Enforce mandatory 2FA for all accounts via policy settings
- Monitor account setting changes (e.g., 2FA disable events) with alerts to users
- Log all authentication configuration modifications for audit

## Objectives

1. Remove 2FA to simulate or test enforcement gaps
2. Prepare account for normal submission failure observation
3. Ensure clean state for embedded form bypass validation

## Instructions

### Step 1: Log In to HackerOne

**Context**: Access your account to reach settings.

Log in at https://hackerone.com using your credentials.

> Successful login redirects to the dashboard without 2FA if already disabled, or prompts for it if enabled.

### Step 2: Navigate to Account Settings

**Context**: Locate the security or authentication section.

Click on your profile icon, then select 'Settings' > 'Security' or 'Two-Factor Authentication'.

> The settings page loads, showing current 2FA status.

### Step 3: Disable 2FA

**Context**: Toggle off the 2FA requirement.

If 2FA is enabled, enter your current 2FA code and confirm disable. Save changes.

> Confirmation message appears: 'Two-factor authentication has been disabled.'

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- 2fa-bypass
- preparation
