---
id: proc-twitter-login-remember-me-37822
tags:
  - authentication
  - login
  - web
type: procedure
tools:
  - '[[tools/FireBug]]'
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
updated_at: '2025-12-14T17:28:20.591Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-with-Remember-Me-Enabled

## Summary

This procedure authenticates a user to Twitter's web application while enabling the 'Remember Me' checkbox, which sets authentication cookies with an extended expiration period, facilitating the demonstration of persistence risks.

## Description

In the context of vulnerability assessment, this step simulates legitimate user login to trigger the vulnerable 'Remember Me' functionality on Twitter's login page (https://twitter.com/login). The feature is intended for user convenience but results in cookies like 'auth_token' and 'remember_checked_on' being set with a nearly 10-year lifespan (approximately 3651 days), far exceeding secure practices. This misconfiguration allows stolen cookies to provide attackers with long-term account access, especially on shared or compromised devices. Prerequisites include valid Twitter credentials and browser access; no advanced setup is needed.

## Requirements

1. Valid Twitter username and password
2. Web browser (e.g., Firefox) with network access to https://twitter.com
3. Optional: Browser extension like FireBug for immediate inspection

## Defense

Defensive measures and detection strategies:

- Enforce shorter cookie expiration (e.g., 30 days max) for 'Remember Me'
- Implement cookie security flags (HttpOnly, Secure) and monitor for anomalous long-lived sessions
- Warn users about risks on shared devices and require explicit opt-in for persistence

## Objectives

1. Trigger the setting of persistent authentication cookies
2. Establish a baseline authenticated session for further analysis
3. Highlight the security implications of extended cookie lifetimes

## Instructions

### Step 1: Navigate to Login Page

**Context**: Access the target login endpoint to begin the authentication process.

Open a web browser and go to https://twitter.com/login.

### Step 2: Enter Credentials and Enable Remember Me

**Context**: Provide authentication details while activating the persistence feature to set vulnerable cookies.

Enter your Twitter username and password in the respective fields. Check the 'Remember Me' checkbox below the password field. Click the 'Log in' button to submit.

> Upon successful authentication, the browser will set the 'auth_token' (session identifier) and 'remember_checked_on' (flag for persistence) cookies with expiration dates approximately 10 years in the future.

### Step 3: Verify Authentication

**Context**: Confirm login success to ensure cookies are applied.

Check for redirection to the Twitter dashboard (e.g., https://twitter.com/home). If prompted for additional verification, complete it without disabling 'Remember Me'.

**Expected Output**: Access to the user's timeline and profile, with cookies stored in the browser's cookie jar.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/FireBug]]

## Tags

- [[authentication]]
- [[login]]
- [[web]]
