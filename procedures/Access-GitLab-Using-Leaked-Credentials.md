---
id: proc-uuid-4
name: Access-GitLab-Using-Leaked-Credentials
tags:
  - initial-access
  - valid-accounts
  - default-creds
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
updated_at: '2025-12-14T17:28:44.323Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[Default Accounts]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access GitLab Using Leaked Credentials

## Summary

This procedure authenticates to a GitLab EE instance using leaked default root credentials obtained from a public source, granting full administrative access for potential data exfiltration or manipulation.

## Description

Default or reused credentials like 'root' with exposed passwords allow bypassing authentication on private instances. Once logged in, admins can access source code, secrets, and user data. This targets GitLab EE via web interface on HTTPS.

## Requirements

1. Leaked username and password
2. Target GitLab URL
3. Web browser

## Defense

Defensive measures and detection strategies:

- Change default credentials immediately upon deployment
- Enable MFA for all admin accounts
- Monitor login attempts and failed authentications in GitLab logs

## Objectives

1. Gain authenticated access to GitLab
2. Verify administrative privileges
3. Avoid further exploitation to maintain stealth

## Instructions

### Step 1: Navigate to Login Page

**Context**: Access the sign-in endpoint.

Visit in browser:

https://[target-hostname]/users/sign_in

> Standard GitLab login form appears.

### Step 2: Submit Credentials

**Context**: Enter and authenticate with leaked details.

Input username: root
Password: [leaked-password]
Click sign in.

> Successful login redirects to dashboard with admin menu options.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques

- [[Default Accounts]]

## Commands Used


## Tools Used


## Tags

- [[initial-access]]
- [[valid-accounts]]
- [[default-creds]]
