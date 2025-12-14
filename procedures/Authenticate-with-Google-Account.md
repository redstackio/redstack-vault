---
tags:
  - auth-bypass
  - google-oauth
  - jenkins
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
  - '[[Domain Accounts]]'
updated_at: '2025-12-14T17:31:52.712Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: d63de105-30a1-4e7b-81b4-664c72de8c84
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Domain Accounts]]'
---
# Authenticate-with-Google-Account

## Summary

This procedure exploits a flawed Google OAuth flow in Jenkins to authenticate using any valid Google account, bypassing intended restrictions.

## Description

The vulnerability stems from improper authentication configuration, allowing generic Google logins to grant full access. In the attack scenario, this provides initial foothold in the test Jenkins environment without custom credentials.

## Requirements

1. Valid Google account credentials
2. Access to the Jenkins login page
3. Web browser supporting OAuth

## Defense

Defensive measures and detection strategies:

- Enforce strict OAuth scopes and domain restrictions
- Require additional MFA or IP whitelisting post-OAuth
- Audit authentication logs for anomalous logins

## Objectives

1. Achieve unauthorized session
2. Gain access to Jenkins dashboard
3. Validate lack of production access

## Instructions

### Step 1: Initiate Login

**Context**: Start the authentication process via the Jenkins UI.

Navigate to the Jenkins login page and click the Google sign-in button to redirect to OAuth flow.

**Expected Output**: Google login prompt appears.

### Step 2: Complete Authentication

**Context**: Use arbitrary Google credentials to complete the flow.

Enter any valid Google email and password; the flawed flow accepts it without further checks.

**Expected Output**: Redirect back to Jenkins dashboard as logged-in user.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Domain Accounts]] Domain Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[auth-bypass]]
- [[google-oauth]]
