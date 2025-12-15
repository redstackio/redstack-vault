---
tags:
  - authentication
  - web
type: procedure
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:29:10.199Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
id: 99a2c170-d838-4fc5-bbb4-576af09e9e60
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-as-Secondary-Admin-Account

## Summary

This procedure outlines logging into Revive Adserver using a secondary admin account to simulate a victim user who will trigger the stored XSS payload.

## Description

To exploit stored XSS, the attacker needs to view the injected data from another admin's perspective. This involves authenticating with a different admin account, ensuring the session is isolated. It assumes multiple admin accounts exist and uses standard web login mechanisms without any exploitation at this stage.

## Requirements

1. Secondary admin credentials (e.g., admin2 username and password)
2. Browser access to the Revive Adserver login page
3. No prior session cookies from other accounts

## Defense

Defensive measures and detection strategies:

- Enforce multi-factor authentication (MFA) for admin logins
- Log all admin authentication attempts and review for anomalies
- Use session isolation and IP binding to detect account sharing

## Objectives

1. Establish an independent admin session
2. Prepare for navigation to the vulnerable page
3. Avoid triggering the payload prematurely

## Instructions

### Step 1: Clear Browser Session

**Context**: Ensure no existing cookies interfere with the new login.

In Firefox, clear cookies for the Revive Adserver domain or use incognito mode.

**Expected Output**: Clean browser state.

### Step 2: Access Login Page and Authenticate

**Context**: Enter credentials for the secondary admin.

Navigate to the login page and input admin2's username and password. Submit the form.

**Expected Output**: Successful redirect to the admin dashboard.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- login
- admin-access
