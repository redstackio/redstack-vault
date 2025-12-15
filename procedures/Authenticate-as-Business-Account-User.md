---
tags:
  - authentication
  - web
  - csrf
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:29.878Z'
sub_techniques: []
id: 934862e2-7755-4dfd-8a2c-085b6a96ea4c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Authenticate as Business Account User

## Summary

This procedure establishes an authenticated session in Infogram using business account credentials, enabling access to team management features necessary for exploiting the CSRF vulnerability.

## Description

In the context of testing Infogram's team management, authentication as a business account user is required to interact with invitation features. This step sets up the session that the CSRF attack will exploit, as the vulnerability relies on valid session cookies without additional protections. Expected outcome is a logged-in state with team admin privileges.

## Requirements

1. Valid Infogram business account credentials (email and password)
2. Web browser with proxy support for Burp Suite
3. Network access to infogram.com

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) for business accounts
- Monitor login attempts and session anomalies
- Use web application firewalls (WAF) to detect unusual access patterns

## Objectives

1. Establish authenticated session for team management access
2. Verify admin privileges for invitation handling
3. Prepare environment for vulnerability testing

## Instructions

### Step 1: Access Login Page

**Context**: Navigate to the Infogram login interface to begin authentication.

Open a web browser and go to https://infogram.com/login.

> Enter business account email and password, then submit the form. Successful login redirects to the dashboard.

### Step 2: Verify Session

**Context**: Confirm access to team features post-login.

Navigate to the team management section in the dashboard.

> Look for options like 'Manage Teams' to ensure session is active and privileges are sufficient.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- authentication
- web
- csrf
