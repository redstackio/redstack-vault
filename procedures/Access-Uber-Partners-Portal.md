---
tags:
  - authentication
  - web-access
  - uber
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T03:15:26.681Z'
sub_techniques: []
id: 0e67546c-d54f-4e7b-bcf8-386174aa5c50
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Uber-Partners-Portal

## Summary

This procedure outlines logging into the Uber Partners Portal using valid credentials to gain access to the dashboard and subsequent profile editing features.

## Description

In the context of exploiting web vulnerabilities like self-XSS, initial access to the authenticated portal is required. This involves navigating to the login page and authenticating with partner credentials. The procedure assumes the attacker has legitimate access to an Uber partner account. Expected outcome is a session established in the browser, allowing navigation to protected areas like the profile page.

## Requirements

1. Valid Uber Partners credentials (email and password)
2. Web browser with cookies enabled
3. Internet connection to https://partners.uber.com

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) to prevent credential compromise
- Monitor login attempts for anomalies, such as unusual IP addresses or failed logins

## Objectives

1. Establish an authenticated session in the Uber Partners Portal
2. Access the main dashboard for further navigation
3. Prepare for profile manipulation without session expiration

## Instructions

### Step 1: Navigate to Login Page

**Context**: Open the Uber Partners website to begin the authentication process.

No command required; manually enter https://partners.uber.com in the browser address bar and press Enter.

> The login form should load, prompting for email and password.

### Step 2: Enter Credentials and Submit

**Context**: Provide authentication details to log in.

No command required; fill in the email and password fields, then click the 'Log In' button.

> Upon success, the browser redirects to the dashboard. Failure results in an error message.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- authentication
- web-access
