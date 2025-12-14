---
tags:
  - 2fa
  - login
  - session
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:48.363Z'
skill_level: intermediate
impact_level: low
sub_techniques: []
id: c6fe576e-5905-4de4-8fe9-84576c397495
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Initiate-2FA-Login-Session

## Summary

This procedure starts a standard login process on an account with 2FA enabled, reaching the confirmation stage to enable request capture for subsequent manipulation.

## Description

In the context of exploiting CS Money's 2FA endpoints, this step involves performing a normal login to generate a session with the steamid cookie. It requires an account with 2FA activated and sets the stage for intercepting the /login/confirm request. The outcome is a valid session token and cookie, which will be modified to target victims.

## Requirements

1. Access to a test account with 2FA enabled via Steam integration
2. Browser or proxy tool for session management
3. Knowledge of the target's login endpoint (e.g., CS Money web app)

## Defense

Defensive measures and detection strategies:

- Implement session binding to prevent cookie tampering
- Monitor for unusual login patterns from known IPs
- Rate limit login attempts at the IP level

## Objectives

1. Establish a 2FA confirmation session
2. Generate steamid cookie for capture
3. Prepare for request interception

## Instructions

### Step 1: Perform Initial Login

**Context**: Enter credentials to reach the 2FA prompt, initiating the session.

No specific command; use the web form to submit username and password.

> Browser navigates to the 2FA code entry page upon success.

### Step 2: Enter Valid 2FA Code to Trigger Request

**Context**: Submit a correct 2FA code to generate the capturable POST request.

Use the form to input the code from your authenticator app.

> The /login/confirm request is prepared but intercepted before submission.

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

- [[2fa]]
- [[login]]
- [[session]]
