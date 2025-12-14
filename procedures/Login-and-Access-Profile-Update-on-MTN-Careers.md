---
tags:
  - login
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
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:23:27.937Z'
sub_techniques: []
id: d92fb11b-8719-4a33-939d-961867b8c293
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-and-Access-Profile-Update-on-MTN-Careers

## Summary

This procedure describes logging into the newly created account on the MTN Careers website and navigating to the profile update section to prepare for file upload exploitation.

## Description

After registration, authentication is required to access user profile features. The login process uses standard form-based authentication on the PHP web app. Once logged in, users can reach the profile edit area where the vulnerable upload feature resides, setting the stage for RCE via file upload.

## Requirements

1. Registered account credentials (email/password)
2. Web browser session
3. No additional privileges needed

## Defense

Defensive measures and detection strategies:

- Enforce multi-factor authentication (MFA) for logins
- Log and monitor login attempts for brute-force or anomalous patterns
- Session timeout and IP binding to prevent session hijacking

## Objectives

1. Establish authenticated session
2. Reach the profile photo upload interface
3. Confirm access to vulnerable feature

## Instructions

### Step 1: Navigate to Login Page

**Context**: Locate the authentication entry point.

Go to https://careers.mtn.cm/ and click the 'Login' button.

### Step 2: Enter Credentials

**Context**: Authenticate using registered details.

Input email and password, then submit the form.

### Step 3: Navigate to Profile Update

**Context**: Access the edit profile section post-login.

In the user dashboard, find and select 'Update Profile' or similar option to load the photo upload area.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- login
- authentication
