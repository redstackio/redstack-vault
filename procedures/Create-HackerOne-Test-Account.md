---
tags:
  - account-creation
  - hackerone
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
updated_at: '2025-12-14T17:32:48.477Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 4f740558-4696-40fe-b0bd-11e29a05c886
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-HackerOne-Test-Account

## Summary

This procedure outlines the creation of a test user account on the HackerOne platform to set up the environment for testing API access control vulnerabilities.

## Description

In the context of demonstrating improper access control, a new test account is registered on HackerOne using standard registration flows. This account will later be banned to test token persistence. The target environment is the HackerOne web platform, and the outcome is a functional user account with credentials for further steps.

## Requirements

1. Valid email address for registration
2. Internet access to hackerone.com
3. No prior HackerOne account with the same email

## Defense

Defensive measures and detection strategies:

- Monitor for bulk or suspicious account creations via rate limiting
- Implement CAPTCHA on registration to prevent automation

## Objectives

1. Obtain valid credentials for a HackerOne user account
2. Verify account functionality for API token generation
3. Set up for subsequent banning and exploitation

## Instructions

### Step 1: Register New Account

**Context**: Navigate to the HackerOne registration page and provide details to create a new hacker account.

No specific command required; use web browser to visit https://hackerone.com/signup and enter username (e.g., 'mrtst'), email, and password.

> Upon submission, expect an email verification link. Click to activate the account.

### Step 2: Verify Account Login

**Context**: Log in to confirm the account is active.

Use the web interface to log in with the new credentials.

> Successful login redirects to the user dashboard, indicating the account is ready.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- account-creation
- hackerone
