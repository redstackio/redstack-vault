---
tags:
  - authentication-bypass
  - oauth
  - jenkins
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
  - Jenkins
techniques:
  - '[[Valid Accounts]]'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques:
  - '[[Default Accounts]]'
id: 03889eed-f665-475f-b498-28bb204185c6
created_at: '2025-12-11T06:10:15.840Z'
updated_at: '2025-12-11T06:10:15.840Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1078]]'
---
# Authenticate via Google OAuth

## Summary

This procedure exploits misconfigured Google OAuth in Jenkins to gain authenticated access using any valid Google account.

## Description

Due to the lack of whitelisting, the Jenkins instance treats any Google-authenticated user as valid, granting dashboard access. This is a critical authentication flaw enabling initial foothold.

## Requirements

1. Valid Google account credentials.
2. URL of the misconfigured Jenkins instance.
3. Web browser supporting OAuth flows.

## Defense

Defensive measures and detection strategies:

- Configure OAuth to restrict to specific domains or users.
- Enable multi-factor authentication and logging for logins.

## Objectives

1. Successfully log in to Jenkins.
2. Access the main dashboard.
3. Establish session for further actions.

## Instructions

### Step 1: Initiate Login

**Context**: Access the login endpoint and select Google option.

Navigate to Jenkins /login and click Google sign-in.

> Expected: Redirect to Google authentication page.

### Step 2: Complete Authentication

**Context**: Provide Google credentials.

Enter valid Google username and password.

> Expected: Redirect back to Jenkins dashboard.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques

- [[Default Accounts]]

## Commands Used

None

## Tools Used

None

## Tags

- authentication-bypass
- oauth
- jenkins
