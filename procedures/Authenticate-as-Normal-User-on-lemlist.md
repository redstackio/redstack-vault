---
id: proc-uuid-1
tags:
  - authentication
  - initial-access
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
updated_at: '2025-12-14T17:28:51.739Z'
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
# Authenticate-as-Normal-User-on-lemlist

## Summary

This procedure establishes an authenticated session on app.lemlist.com using standard user credentials, serving as the entry point for exploiting improper access controls.

## Description

The attack begins with logging into the application as a regular user. This step is crucial because the subsequent vulnerability relies on an active authenticated session without proper role-based authorization checks on admin endpoints. The target environment is a web-based email outreach platform, and this procedure assumes the attacker has obtained valid credentials through prior means (e.g., phishing or purchase). Expected outcomes include a valid session cookie, enabling navigation to protected areas.

## Requirements

1. Valid email and password for a standard lemlist user account
2. Web browser with JavaScript enabled
3. Internet connectivity to app.lemlist.com

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) for all logins to prevent credential-based access
- Monitor login attempts from unusual IP addresses or locations
- Use session management with short expiration times and IP binding

## Objectives

1. Obtain an active user session
2. Verify standard user permissions are applied
3. Prepare for escalation to unauthorized admin views

## Instructions

### Step 1: Navigate to Login Page

**Context**: Access the authentication endpoint to initiate the login process.

Open a web browser and go to https://app.lemlist.com/login.

> This loads the login form where credentials can be entered.

### Step 2: Enter Credentials and Submit

**Context**: Provide standard user details to authenticate and establish a session.

Fill in the email and password fields with valid standard user credentials, then click 'Log In'.

> Upon success, the browser redirects to the user dashboard, and session cookies (e.g., auth tokens) are set. Failure results in an error message.

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
