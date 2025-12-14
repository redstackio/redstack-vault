---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
tags:
  - web
  - authentication
  - initial-access
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:23.681Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Register-and-Login-to-DoD-Web-App

## Summary

This procedure establishes initial access to the DoD web application by registering a test account and authenticating, setting up a legitimate session for further exploitation.

## Description

In the context of testing for IDOR vulnerabilities, creating a test account allows the attacker to interact with the application and obtain a session cookie. The target is a PHP-based web app with open registration at https://██████████/register.php. Successful login provides access to user-specific endpoints like the profile page, where the UID2 cookie is set with the user's ID.

## Requirements

1. Network access to the DoD web app URLs (e.g., https://███████/login.php)
2. Valid username and password format (e.g., alphanumeric with special characters)
3. Browser or proxy tool like Burp Suite for traffic inspection

## Defense

Defensive measures and detection strategies:

- Implement CAPTCHA or email verification on registration to prevent automated account creation
- Monitor for unusual login patterns from new accounts accessing sensitive areas

## Objectives

1. Create a test user account
2. Authenticate and establish a session
3. Access the profile functionality to trigger cookie setting

## Instructions

### Step 1: Navigate to Registration

**Context**: Access the registration page to create a test account.

Use a browser to visit https://██████████/register.php and fill in the form with username: testuser and password: TEst.123.!.

> Submit the form to create the account. Expected output: Confirmation message or redirect to login.

### Step 2: Login with Test Credentials

**Context**: Authenticate to set the session and UID2 cookie.

Navigate to https://███████/login.php, enter the test credentials, and submit.

> Expected output: Successful login, redirect to dashboard, and UID2 cookie set in browser (inspect via developer tools).

### Step 3: Verify Session

**Context**: Confirm access to protected areas.

After login, navigate to the 'My Profile Page' to ensure the session is active.

> Expected output: Profile page loads with test user data.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[web]]
- [[authentication]]
