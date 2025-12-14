---
id: proc-765679-attacker-login
tags:
  - authentication
  - valid-accounts
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-13T23:52:49.711Z'
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
# Authenticate-as-Attacker-in-Outpost

## Summary

This procedure logs in to the Outpost application using the attacker's credentials to access the Inbox for payload upload.

## Description

Authentication grants access to the web interface where conversations and file uploads occur. Target the sign-in endpoint at https://app.outpost.co/sign-in. Prerequisites include a registered account; outcomes include session establishment for subsequent steps.

## Requirements

1. Registered attacker account (e.g., seq@seq.teamoutpost.com)
2. Valid password
3. Web browser with cookies enabled

## Defense

Defensive measures and detection strategies:

- Enforce multi-factor authentication (MFA)
- Log failed login attempts and alert on anomalies
- Use session timeouts and IP binding

## Objectives

1. Secure attacker session
2. Access Inbox features
3. Prepare for conversation creation

## Instructions

### Step 1: Access Sign-In Page

**Context**: Open the login interface.

Navigate to https://app.outpost.co/sign-in in a web browser.

> Page loads with email and password fields.

### Step 2: Enter Credentials and Submit

**Context**: Authenticate to gain access.

Enter seq@seq.teamoutpost.com as email, provide the password, and click sign in.

> Successful login redirects to the dashboard; session cookie set.

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
- [[valid-accounts]]
