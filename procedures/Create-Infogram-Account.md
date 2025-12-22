---
tags:
  - account-creation
  - initial-access
  - infogram
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T12:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T03:16:14.298Z'
sub_techniques: []
id: 239f6548-4240-4c0f-bec9-222d77be98ed
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-Infogram-Account

## Summary

This procedure outlines the standard registration process to create a free account on Infogram, providing access to project creation and sharing features necessary for exploiting vulnerabilities in the platform.

## Description

Infogram allows users to sign up via email and password, with optional social login. Upon registration, users gain a dashboard for creating infographics and projects. This step is a prerequisite for any project-based attacks, such as injecting malicious content into titles. The process typically takes under 2 minutes and requires email verification. Expected outcome: authenticated session enabling project management.

## Requirements

1. Web browser with JavaScript enabled
2. Valid email address for registration and verification
3. Internet connection to https://infogram.com

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on registrations to prevent abuse
- Monitor for suspicious email patterns in new accounts
- Require CAPTCHA on signup to deter automated registrations

## Objectives

1. Establish legitimate user access to Infogram features
2. Obtain session for project creation
3. Enable subsequent steps in the attack chain

## Instructions

### Step 1: Navigate to Registration

**Context**: Access the Infogram signup page to begin account creation.

Browse to https://infogram.com and click the 'Sign Up' or 'Create Account' button. Fill in the required fields: email, password, and any optional details.

### Step 2: Verify Email

**Context**: Complete verification to activate the account.

Check your email inbox for the verification link from Infogram and click it to confirm. Log in with the new credentials.

> Upon success, you will be redirected to the dashboard.

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
- [[initial-access]]
