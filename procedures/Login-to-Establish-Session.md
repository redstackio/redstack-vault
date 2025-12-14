---
tags:
  - auth
  - session
type: procedure
tools:
  - '[[tools/EditThisCookie-Extension]]'
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
updated_at: '2025-12-14T17:31:42.653Z'
sub_techniques: []
id: b4c6e014-d231-4a95-b71e-a13cfc3923a3
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-to-Establish-Session

## Summary

This procedure authenticates a user to the HackerOne web application to create an active session, setting the stage for cookie extraction and testing session persistence.

## Description

In the context of testing broken session management, logging in establishes valid session cookies that should be invalidated on logout but are not. This targets web applications like HackerOne where standard authentication flows are used. Prerequisites include a valid account; outcomes include an authenticated session ready for cookie manipulation.

## Requirements

1. Valid HackerOne account credentials (username/email and password)
2. Modern web browser (e.g., Chrome)
3. Network access to https://www.hackerone.com/

## Defense

Defensive measures and detection strategies:

- Implement proper session invalidation on logout by server-side token revocation
- Monitor for anomalous session reuse from different IPs or after inactivity
- Use HttpOnly and Secure flags on cookies to limit theft via XSS or network sniffing

## Objectives

1. Gain authenticated access to protected application areas
2. Generate session cookies for persistence testing
3. Verify session establishment before logout simulation

## Instructions

### Step 1: Navigate and Authenticate

**Context**: Access the login page and submit credentials to initiate session creation.

No command required; perform manually:

1. Open browser and go to https://www.hackerone.com/login
2. Enter credentials and submit the form

> Successful login redirects to the dashboard, and session cookies (e.g., _h1_session) are set in the browser.

### Step 2: Verify Session

**Context**: Confirm authentication by accessing a protected resource.

Navigate to a dashboard or account page post-login.

> Expected: Access granted without re-prompt for credentials.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/EditThisCookie-Extension]]

## Tags

- [[auth]]
- [[session]]
