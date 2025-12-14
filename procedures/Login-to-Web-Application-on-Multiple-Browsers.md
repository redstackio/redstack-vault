---
tags:
  - authentication
  - session-establishment
type: procedure
tools:
  - '[[tools/Mozilla-Firefox]]'
  - '[[tools/Google-Chrome]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:11.349Z'
sub_techniques: []
id: 9ad04088-93ae-4b5a-b4c9-f9157a2b438c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-to-Web-Application-on-Multiple-Browsers

## Summary

This procedure establishes authenticated sessions on multiple browsers using the same credentials, setting up the conditions to test session invalidation upon password changes in web applications with broken authentication mechanisms.

## Description

In vulnerable web applications like the one at https://bridge.cspr.ng/, users can log in simultaneously on different browsers without session conflicts. This is exploited to demonstrate that password changes do not propagate session termination to all active logins, allowing potential unauthorized access on shared or unattended devices. The procedure targets PHP-based platforms such as Airship CMS, where session management is not robustly implemented.

## Requirements

1. Valid username and password for the target account
2. Access to multiple web browsers (e.g., Firefox and Chrome)
3. Internet connectivity to reach https://bridge.cspr.ng/

## Defense

Defensive measures and detection strategies:

- Implement server-side session invalidation on password changes by revoking all session tokens
- Use short session timeouts and multi-factor authentication (MFA) to limit lingering access
- Monitor for multiple concurrent logins from the same account and alert users

## Objectives

1. Create concurrent active sessions for testing persistence
2. Verify no immediate session conflicts during multi-browser login
3. Prepare for password change exploitation

## Instructions

### Step 1: Open Primary Browser and Navigate to Login

**Context**: Launch the first browser to initiate authentication, simulating a legitimate user session.

No command required; use the browser's address bar:

Navigate to `https://bridge.cspr.ng/` and enter credentials in the login form.

> Submits POST request to authentication endpoint; on success, sets session cookie (e.g., PHPSESSID).

### Step 2: Authenticate in Primary Browser

**Context**: Complete login to establish the session.

Enter username and password, then submit the form.

> Expected: Redirect to dashboard; inspect network tab for session cookie persistence.

### Step 3: Repeat in Secondary Browser

**Context**: Establish a parallel session to enable independent actions like password changes.

Open second browser, navigate to `https://bridge.cspr.ng/`, and log in with identical credentials.

> Both sessions should be active; check developer tools for separate cookie instances.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Mozilla-Firefox]]
- [[tools/Google-Chrome]]

## Tags

- authentication
- session-establishment
