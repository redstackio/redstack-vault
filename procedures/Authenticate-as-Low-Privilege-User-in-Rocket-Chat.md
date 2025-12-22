---
id: proc-rocket-auth-low-priv
tags:
  - authentication
  - initial-access
  - rocket-chat
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
updated_at: '2025-12-14T17:32:58.336Z'
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
# Authenticate-as-Low-Privilege-User-in-Rocket-Chat

## Summary

This procedure establishes an authenticated session in Rocket.Chat using low-privilege user credentials, providing the foundation for subsequent exploitation steps without requiring admin access.

## Description

In the context of exploiting the Rocket.Chat regex vulnerability, authentication as a standard user allows access to endpoints vulnerable to blind regex searches. The target environment is a Rocket.Chat web application, and the outcome is a valid session for API interactions. Prerequisites include valid low-privilege credentials.

## Requirements

1. Valid low-privilege user account in Rocket.Chat
2. Web browser or API client for login
3. Network access to the Rocket.Chat instance

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) for all users
- Monitor login attempts from unusual IPs or user agents
- Use session timeout and IP binding to prevent token reuse

## Objectives

1. Gain authenticated access to the application
2. Establish session for token extraction
3. Avoid triggering admin-level alerts

## Instructions

### Step 1: Access Login Page

**Context**: Navigate to the Rocket.Chat login interface to begin authentication.

Open a web browser and go to the Rocket.Chat URL (e.g., https://target.rocket.chat).

### Step 2: Enter Credentials

**Context**: Submit low-privilege credentials to authenticate.

Enter username/email and password, then click login. No specific command; use the web form.

> Upon success, the dashboard loads, and session cookies (including rc_token) are set.

### Step 3: Verify Access

**Context**: Confirm low-privilege status.

Check user settings or profile; ensure no admin features are visible.

> Expected: Standard user interface without elevated permissions.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[authentication]]
- [[initial-access]]
