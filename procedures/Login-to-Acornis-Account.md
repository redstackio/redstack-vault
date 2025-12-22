---
tags:
  - authentication
  - web
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
techniques: []
updated_at: '2025-12-14T00:11:09.540Z'
sub_techniques: []
id: 7de38f17-fcfa-4052-81bf-9483299e652b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
---
# Login-to-Acornis-Account

## Summary

This procedure authenticates a user to the Acronis account portal, providing access to support features where the self-XSS vulnerability can be exploited.

## Description

The Acronis support system requires user authentication to submit requests and upload attachments. This step uses standard web login mechanics to establish a session. The target environment is the web-based account portal at account.acronis.com. Expected outcome is a valid session allowing navigation to support sections. Prerequisites include valid credentials.

## Requirements

1. Valid Acronis account email and password
2. Web browser with JavaScript enabled
3. Internet access to account.acronis.com

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) to prevent unauthorized logins
- Monitor login attempts for anomalies, such as unusual IP addresses or failed attempts

## Objectives

1. Establish authenticated session
2. Access support request interface
3. Prepare for vulnerability exploitation

## Instructions

### Step 1: Navigate to Login Page

**Context**: Access the authentication endpoint to begin the login process.

No command required; open a web browser and go to https://account.acronis.com.

> Enter the URL in the browser address bar. The login form should load.

### Step 2: Authenticate

**Context**: Submit credentials to create a session.

No command required; fill in the email and password fields and click 'Login'.

> Upon success, you will be redirected to the account dashboard. Check for any session cookies set in browser developer tools.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- authentication
- web
