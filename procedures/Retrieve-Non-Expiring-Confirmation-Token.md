---
tags:
  - token-retrieval
  - auth-bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: a3ab868c-ff1b-48c0-ad35-a175b07c6755
created_at: '2025-12-14T17:24:45.496Z'
updated_at: '2025-12-14T17:24:45.496Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Retrieve-Non-Expiring-Confirmation-Token

## Summary

This procedure involves extracting the confirmation token from a login.gov activation email, exploiting the fact that these tokens do not expire after the advertised 24 hours, allowing indefinite reuse for auth bypass.

## Description

Once email access is gained, the attacker locates the sign-up confirmation email and parses the token from the URL. In login.gov's staging environment, tokens like those in https://idp.staging.login.gov/sign_up/email/confirm?confirmation_token=1wzjBaAyfcVnS5iWgmxq remain valid beyond 48 hours. This enables direct access to sensitive flows without time-based expiration checks. Prerequisites: Email compromise. Expected outcome: Token ready for use in password reset.

## Requirements

1. Access to victim's email inbox
2. Ability to parse URLs (browser or text editor)
3. Knowledge of token format (query parameter in email link)

## Defense

Defensive measures and detection strategies:

- Implement true token expiration with server-side checks
- Log and alert on token reuse after extended periods
- Use short-lived, single-use tokens for confirmations

## Objectives

1. Obtain the confirmation token string
2. Verify token validity by testing reuse
3. Prepare for 2FA bypass

## Instructions

### Step 1: Locate Confirmation Email

**Context**: Identify the email sent during account sign-up.

**Instructions**: Search inbox for emails from noreply@login.gov with subjects related to email confirmation.

> Expected output: Email body with clickable link or raw URL.

### Step 2: Extract Token

**Context**: Parse the token from the confirmation URL.

**Instructions**: Copy the full URL from the email, e.g., https://idp.staging.login.gov/sign_up/email/confirm?confirmation_token=1wzjBaAyfcVnS5iWgmxq, and isolate the confirmation_token value.

> Expected output: Token string like 1wzjBaAyfcVnS5iWgmxq; test by accessing the URL after 24+ hours to confirm non-expiration.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[token-retrieval]]
- [[auth-bypass]]
