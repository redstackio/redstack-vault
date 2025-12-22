---
id: proc-gitlab-initiate-session
tags:
  - auth
  - session
  - gitlab
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:30.880Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Initiate Attacker Login Session

## Summary

This procedure establishes a valid session for the attacker on the GitLab login page, setting the session[:otp_user_id] to the attacker's ID, which is a prerequisite for manipulating subsequent 2FA requests.

## Description

In the context of the GitLab 2FA bypass, the attacker uses their own credentials to initiate a login flow. This creates a backend session that stores the user's ID for OTP verification. The procedure targets the /users/sign_in endpoint and assumes the attacker has valid username/password credentials. Expected outcome is progression to the 2FA prompt without errors.

## Requirements

1. Valid attacker GitLab credentials (username and password)
2. Network access to GitLab instance
3. Browser or proxy tool like Burp Suite for traffic monitoring

## Defense

Defensive measures and detection strategies:

- Enforce strict session validation and bind OTP to exact user ID without parameter overrides
- Monitor for unusual login patterns from known user sessions
- Use rate limiting on login attempts

## Objectives

1. Create authenticated session for attacker
2. Set session[:otp_user_id] for manipulation
3. Reach 2FA prompt stage

## Instructions

### Step 1: Access Sign-In Page

**Context**: Navigate to the GitLab login interface to begin the authentication flow.

No command required; use browser to go to https://target-gitlab.com/users/sign_in and enter attacker's username and password.

> Submits POST to /users/sign_in with user[login] and user[password], setting session.

### Step 2: Proceed to 2FA

**Context**: Upon successful password validation, the system prompts for 2FA, confirming session establishment.

Submit any OTP (to be intercepted later); do not complete yet.

> Expected: Redirect to 2FA form with session active.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[auth]]
- [[session]]
- [[gitlab]]
