---
tags:
  - initial-access
  - authentication
type: procedure
tools:
  - '[[tools/HTTP-Proxy-Interceptor]]'
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
updated_at: '2025-12-14T17:31:30.627Z'
sub_techniques: []
id: a35b4990-2c57-4aff-b4c7-0678298b5546
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-to-Victim-Account-with-Old-Password

## Summary

This procedure establishes initial access to the victim's Basecamp account using the known old password, serving as the entry point for subsequent 2FA manipulation in the account takeover attack.

## Description

In the context of exploiting Basecamp's improper authentication, the attacker uses the victim's email and old password to log in via the web sign-in page. This grants access to the dashboard and settings, allowing further steps like enabling 2FA. The procedure assumes the attacker has obtained the credentials through prior means (e.g., phishing or leak). Expected outcome is full session establishment without 2FA initially enabled.

## Requirements

1. Knowledge of victim's email and old password
2. Direct network access to Basecamp's sign-in page (https://basecamp.com/sign_in)
3. Web browser or HTTP client for form submission

## Defense

Defensive measures and detection strategies:

- Enforce strong, unique passwords and monitor for credential leaks
- Implement rate limiting on login attempts to detect brute-force or repeated access
- Log all successful logins with IP and user-agent for anomaly detection

## Objectives

1. Gain authenticated access to the victim's account dashboard
2. Verify old password validity
3. Prepare for account settings modifications

## Instructions

### Step 1: Navigate to Sign-In Page

**Context**: Access the Basecamp login endpoint to submit credentials.

**Instructions**: Open a web browser and go to the Basecamp sign-in page. No specific command needed; use the HTML form.

> Submit the form with victim's email and old password. Expected output: Redirect to dashboard if successful.

### Step 2: Verify Access

**Context**: Confirm session is active and settings are reachable.

**Instructions**: Once logged in, navigate to the account dashboard and attempt to access settings.

> Expected output: Dashboard loads, profile/settings menu visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/HTTP-Proxy-Interceptor]]

## Tags

- [[initial-access]]
- [[authentication]]
