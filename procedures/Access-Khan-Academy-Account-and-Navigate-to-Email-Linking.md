---
id: proc-khan-access-nav
tags:
  - authentication
  - web-access
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
updated_at: '2025-12-14T17:24:18.879Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Khan-Academy-Account-and-Navigate-to-Email-Linking

## Summary

This procedure authenticates a user to a Khan Academy account and navigates to the linked accounts section to initiate the email linking process, setting up the environment for exploiting the race condition vulnerability.

## Description

In the context of the Khan Academy race condition attack, this step establishes a valid session on www.khanacademy.org and positions the attacker at the vulnerable email confirmation flow. It requires valid credentials and simulates normal user behavior to reach the /api/internal/graphql/requestAuthEmail endpoint without raising suspicion. Expected outcomes include access to the email input form after identity verification.

## Requirements

1. Valid Khan Academy account credentials (username/email and password)
2. Web browser with internet access to www.khanacademy.org
3. No proxy interference initially (Burp Suite configured later)

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) for account logins to prevent unauthorized access
- Monitor login attempts from unusual IP addresses or locations
- Rate-limit login and navigation actions to detect automated reconnaissance

## Objectives

1. Establish an authenticated session on the target platform
2. Reach the email linking interface without errors
3. Prepare for request interception in subsequent steps

## Instructions

### Step 1: Log In to Khan Academy

**Context**: Connect to the site and authenticate using provided credentials to gain a valid session.

No specific command; use a web browser to navigate to www.khanacademy.org and enter credentials in the login form.

> Successful login redirects to the user dashboard. Expected output: Profile name visible in the top navigation.

### Step 2: Navigate to Linked Accounts

**Context**: Access the settings to reach the email linking section.

No specific command; click Profile name > Settings > Account tab > Linked accounts > Connect another email.

> Expected output: Email input form appears.

### Step 3: Confirm Identity

**Context**: Verify ownership by providing the account password before proceeding.

No specific command; enter the account password when prompted.

> Expected output: Password verification succeeds, unlocking the email send button.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- authentication
- web-access
