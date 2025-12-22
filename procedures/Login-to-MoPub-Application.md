---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
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
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-13T23:55:06.330Z'
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
# Login-to-MoPub-Application

## Summary

This procedure authenticates a user to the MoPub web application, providing access to the dashboard and subsequent vulnerable settings pages.

## Description

In the context of exploiting stored XSS in MoPub, logging in is the initial step to gain authenticated access. The target environment is the web-based MoPub platform at https://app.mopub.com. Prerequisites include valid credentials for a company account. Expected outcomes include a valid session that allows navigation to account settings where payloads can be injected.

## Requirements

1. Valid MoPub username and password for a company account
2. Web browser with JavaScript enabled
3. Network access to https://app.mopub.com

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) to prevent unauthorized logins
- Monitor login attempts for anomalies like unusual IP addresses

## Objectives

1. Establish an authenticated session
2. Access the main dashboard
3. Prepare for navigation to vulnerable areas

## Instructions

### Step 1: Access Login Page

**Context**: Navigate to the MoPub login endpoint to begin authentication.

Open a web browser and go to https://app.mopub.com/account/login/.

**Expected Output**: Login form appears with fields for email and password.

### Step 2: Enter Credentials

**Context**: Provide valid authentication details to log in.

Enter the username/email and password, then submit the form.

**Expected Output**: Successful login redirects to the dashboard.

**Success Indicators**:
- No error messages
- Session cookie is set

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
- web-login
