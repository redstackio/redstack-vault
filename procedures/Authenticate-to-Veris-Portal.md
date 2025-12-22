---
id: 123e4567-e89b-12d3-a456-426614174001
name: Authenticate-to-Veris-Portal
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:26.717Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - authentication
  - web
commands: []
platforms:
  - Web
tools: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---

# Authenticate-to-Veris-Portal

## Summary

This procedure authenticates a user to the Veris sandbox portal using valid credentials, establishing a session necessary for accessing protected features like the Member Book.

## Description

In the context of exploiting web vulnerabilities, initial authentication is required to reach authenticated endpoints. This procedure involves logging into the Veris portal at https://sandbox.veris.in/portal/, which uses standard form-based authentication. Successful login grants a session cookie for subsequent interactions. Prerequisites include possessing valid account credentials; without them, the attack cannot proceed to injection phases.

## Requirements

1. Valid Veris account username and password
2. Web browser with cookies enabled
3. Direct internet access to https://sandbox.veris.in/

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) to prevent credential-based access
- Monitor login attempts for anomalies, such as unusual IP addresses or failed logins
- Use web application firewalls (WAF) to detect brute-force or suspicious login patterns

## Objectives

1. Establish an authenticated session to the Veris portal
2. Gain access to member management features
3. Enable subsequent payload injection without re-authentication

## Instructions

### Step 1: Navigate to Login Page

**Context**: Access the authentication endpoint to begin the login process.

Open a web browser and go to https://sandbox.veris.in/portal/login (or the default login path).

> The login form should load, prompting for username and password.

### Step 2: Submit Credentials

**Context**: Provide valid credentials to authenticate and obtain a session.

Enter the username and password in the respective fields and click 'Sign In' or submit the form.

> Upon success, the browser redirects to the dashboard, and session cookies are set. Check browser developer tools (Network tab) for 200 OK on login endpoint and Set-Cookie headers.

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
- [[web]]
