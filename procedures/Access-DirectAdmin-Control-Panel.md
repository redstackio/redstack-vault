---
id: proc-uuid-1
tags:
  - directadmin
  - authentication
  - web-login
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
updated_at: '2025-12-14T17:28:28.482Z'
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
# Access-DirectAdmin-Control-Panel

## Summary

This procedure outlines how to log into the DirectAdmin web-based control panel using valid credentials, providing access to user management features including password changes.

## Description

DirectAdmin is a web hosting control panel that exposes administrative functions over HTTPS on port 2222. This procedure assumes the attacker or tester has legitimate credentials, which could be obtained via phishing, prior compromise, or social engineering. Upon successful login, the panel allows navigation to sensitive endpoints like password modification without additional authentication checks beyond the initial login. The target environment is a standard DirectAdmin installation, and the outcome is authenticated access enabling further exploitation of misconfigurations such as weak password policies.

## Requirements

1. Valid username and password for a DirectAdmin user account
2. Network connectivity to the target host on port 2222 (HTTPS)
3. A modern web browser to handle the login form

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) for all DirectAdmin logins to prevent unauthorized access
- Monitor login attempts and failed authentications via server logs (e.g., /var/log/directadmin/error.log) for anomalies
- Use web application firewalls (WAF) to detect and block suspicious access patterns to the login endpoint

## Objectives

1. Establish authenticated session in the DirectAdmin panel
2. Gain visibility into user controls for subsequent actions
3. Validate credential validity without triggering alerts

## Instructions

### Step 1: Navigate to Login Endpoint

**Context**: Locate and access the DirectAdmin login page to initiate authentication.

Open a web browser and enter the URL: https://da.theendlessweb.com:2222/ (replace with target hostname). The login form will load, prompting for username and password.

### Step 2: Authenticate with Credentials

**Context**: Submit valid credentials to establish a session.

Enter the username and current password in the respective fields. Click the login button. If credentials are valid, the dashboard will load.

> Upon success, you should see the DirectAdmin user interface with options like 'Password' under the user menu. Failed attempts will display an error without locking the account.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[directadmin]]
- [[web-login]]
- [[authentication]]
