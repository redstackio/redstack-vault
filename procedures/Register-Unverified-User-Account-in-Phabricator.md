---
tags:
  - account-creation
  - phabricator
  - email-abuse
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[External Remote Services]]'
updated_at: '2025-12-14T17:32:20.241Z'
sub_techniques: []
id: 403cc2b1-dcc9-4aad-9176-27f1fb784478
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[External Remote Services]]'
---
---

# Register-Unverified-User-Account-in-Phabricator

## Summary

This procedure registers a new user account in Phabricator using an arbitrary email address, bypassing immediate verification requirements to enable subsequent API abuse for email bombing.

## Description

Phabricator allows user registration without mandatory email verification for login if configured with auth.require-email-verification=false. By providing a target's email during signup, an initial verification email is sent, and the account can be used to trigger unlimited resends via the email API, leading to mailbox overload. This targets web-based Phabricator instances and exploits improper access controls on email functions.

## Requirements

1. Access to Phabricator registration page (e.g., https://target.phabricator.com/account/begin/)
2. Target email address for bombing
3. Web browser for form submission

## Defense

Defensive measures and detection strategies:

- Enable rate limiting on email resend endpoints (e.g., via PHP throttling in PhabricatorUserEmail.php)
- Require CAPTCHA on registration and resend requests
- Monitor email server logs for high-volume sends from single sources

## Objectives

1. Create an unverified account tied to target email
2. Trigger initial verification email
3. Prepare for repeated API calls without restrictions

## Instructions

### Step 1: Access Registration Page

**Context**: Navigate to the Phabricator signup form to begin account creation.

No command required; use browser to visit https://target.phabricator.com/account/begin/ and fill in username, password, and the target email address.

> Submit the form. If auth.require-email-verification is false, login proceeds without verification; otherwise, the account is created but unverified.

### Step 2: Confirm Initial Email Send

**Context**: Verify the registration triggers the first verification email, confirming the setup.

Check the target mailbox for the verification email containing the token.

> Expected: Email arrives with subject like "Verify Your Email Address" and a verification link/token.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[External Remote Services]] External Remote Services

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-creation]]
- [[phabricator]]
- [[email-abuse]]
