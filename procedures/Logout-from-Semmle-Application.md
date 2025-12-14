---
tags:
  - logout
  - session-management
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
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
id: 9fcc4dbd-2cc7-41d7-9728-d4e98d5e93aa
created_at: '2025-12-13T23:55:20.682Z'
updated_at: '2025-12-13T23:55:20.682Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Logout-from-Semmle-Application

## Summary

This procedure forces or ensures a user session is terminated in the Semmle web application, setting up the conditions for the vulnerable redirect to trigger during a subsequent login.

## Description

In the context of exploiting DOM-based XSS via the redirect parameter, logging out is essential to simulate a logged-out user's interaction with the malicious URL. The Semmle application processes the redirect only upon login, so an active session would bypass this flow. This step prepares the victim for payload delivery without alerting them to any anomaly.

## Requirements

1. Access to the Semmle application URL (https://lgtm-com.pentesting.semmle.net/)
2. Valid user session (to log out)
3. Browser with JavaScript enabled

## Defense

Defensive measures and detection strategies:

- Implement session timeout and auto-logout after inactivity
- Monitor for unusual logout patterns or rapid login/logout cycles
- Use CSP headers to restrict script execution post-redirect

## Objectives

1. Terminate the current authenticated session
2. Redirect user to login page
3. Prepare for malicious URL interaction

## Instructions

### Step 1: Access Logout Endpoint

**Context**: Navigate to the application's logout functionality to invalidate the session.

No specific command; manually click the logout button or visit the logout URL (typically /logout or similar in Semmle).

> Upon execution, the browser clears session cookies, and the user is redirected to the login page. Expected output: Login prompt appears, confirming logout.

### Step 2: Verify Logged-Out State

**Context**: Confirm no active session persists to ensure redirect vulnerability is exploitable.

Attempt to access a protected resource; should redirect to login.

> Browser shows login form without authentication. Success if no dashboard or protected content loads.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[logout]]
- [[session-termination]]
