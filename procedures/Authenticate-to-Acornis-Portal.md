---
id: auth-acronis-portal
tags:
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
updated_at: '2025-12-13T23:52:49.849Z'
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
# Authenticate-to-Acornis-Portal

## Summary

This procedure establishes an authenticated session to the Acronis learning portal, a prerequisite for exploiting session-context vulnerabilities like XSS in authenticated endpoints.

## Description

In the context of testing the Acronis portal at https://learn.acronis.com/, authentication is required to access features like the licensing-check endpoint. This step uses standard login functionality with valid credentials, setting session cookies that the subsequent XSS can exploit to steal sensitive data such as tokens. The procedure assumes the tester has legitimate access or is performing authorized security testing.

## Requirements

1. Valid username and password for an Acronis account
2. Web browser with cookies enabled
3. Network access to https://learn.acronis.com/

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) to protect login
- Monitor for unusual login attempts from unfamiliar IPs
- Use session timeout and cookie security flags (HttpOnly, Secure)

## Objectives

1. Gain authenticated access to the portal
2. Establish session context for vulnerability exploitation
3. Verify session establishment without errors

## Instructions

### Step 1: Navigate to Login Page

**Context**: Access the authentication endpoint to begin the login process.

Navigate to https://learn.acronis.com/ in your web browser.

> The login form should appear, prompting for credentials.

### Step 2: Submit Credentials

**Context**: Provide valid credentials to authenticate and set session cookies.

Enter your username and password, then submit the form.

> Upon success, the browser redirects to the dashboard, and developer tools (F12 > Application > Cookies) show session tokens.

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
- [[web-login]]
