---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - session-hijacking
  - authentication
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:12.006Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Establish Valid Session Access

## Summary

This procedure outlines how to obtain a valid authenticated session on a web application using legitimate or compromised credentials, setting the stage for further unauthorized actions like account manipulation.

## Description

In web applications, sessions are typically managed via cookies or tokens issued upon successful login. This procedure assumes access to valid credentials (e.g., via phishing, shared access, or prior compromise) and focuses on establishing the session to mimic a legitimate user. The target environment is a standard web app like FantasyTote, where login endpoints are public-facing. Expected outcomes include session establishment without triggering anomalies, enabling escalation to vulnerable features.

## Requirements

1. Valid username and password or session token/cookie
2. Web browser with developer tools for inspecting sessions
3. Network connectivity to the target site (HTTPS)

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) for login
- Monitor for anomalous login locations or devices
- Use session binding to IP/user-agent and short expiration times

## Objectives

1. Secure a persistent authenticated session
2. Verify session validity for subsequent steps
3. Avoid detection during initial access

## Instructions

### Step 1: Access Login Page

**Context**: Begin by reaching the authentication endpoint to input credentials.

Navigate to the main website, such as https://www.fantasytote.com/, and locate the sign-in form.

### Step 2: Submit Credentials

**Context**: Authenticate using provided or stolen credentials to receive session tokens.

Enter the username and password in the respective fields and submit the form. Monitor the browser's network tab for session cookie issuance (e.g., 'session_id' or 'auth_token').

> Upon success, the application redirects to a protected page, confirming session establishment.

### Step 3: Verify Session

**Context**: Ensure the session allows access to authenticated resources.

Attempt to access a protected endpoint, like the user dashboard, to confirm the session is active.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[session-access]]
- [[web-auth]]
