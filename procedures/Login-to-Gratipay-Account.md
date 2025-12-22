---
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
updated_at: '2025-12-14T03:16:31.121Z'
sub_techniques: []
id: 6b4b9ea9-7f53-4c4b-9b3d-fef92f0c0cb4
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-to-Gratipay-Account

## Summary

This procedure authenticates a user to the Gratipay platform, enabling access to profile editing features required for injecting XSS payloads.

## Description

In the context of exploiting Stored XSS on Gratipay, logging in establishes a valid session. This is a prerequisite for accessing user-specific features like editing the profile statement. The target environment is the Gratipay web application, and success grants authenticated access without elevated privileges.

## Requirements

1. Valid username and password for a Gratipay account
2. Web browser with internet access
3. No prior session cookies (for clean login)

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on login attempts to prevent brute-force
- Monitor for anomalous login patterns from new IPs
- Enforce multi-factor authentication (MFA) for all accounts

## Objectives

1. Establish authenticated session
2. Gain access to profile management
3. Prepare for payload injection

## Instructions

### Step 1: Navigate to Login Page

**Context**: Access the authentication endpoint to begin login.

Open a web browser and go to https://gratipay.com/login/ or the main site which redirects to login if unauthenticated.

### Step 2: Enter Credentials

**Context**: Provide valid user details to authenticate.

Fill in the username/email and password fields, then submit the form.

### Step 3: Verify Session

**Context**: Confirm successful authentication.

Check for redirect to dashboard or profile; inspect browser dev tools for session cookies.

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
- [[web]]
