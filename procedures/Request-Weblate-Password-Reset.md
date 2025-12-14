---
tags:
  - password-reset
  - token-generation
  - weblate
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
  - '[[Account Manipulation]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:19.718Z'
skill_level: low
impact_level: low
detection_risk: low
sub_techniques: []
id: f0b4dee7-131b-47e4-927a-21905fa73b04
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Account Manipulation]]'
  - '[[Exploit Public-Facing Application]]'
---
# Request-Weblate-Password-Reset

## Summary

This procedure initiates a password reset request on Weblate to generate a session token, which is captured but not immediately used, setting up the conditions for token reuse exploitation.

## Description

Targeting the password reset functionality in Weblate (Django-based), this step involves submitting a reset request for the verified account, resulting in an email containing a time-limited link with an embedded token. The token is intended for one-time use but, due to the vulnerability, persists beyond password changes. This procedure assumes account access and focuses on email delivery of the token for later reuse. Outcomes include possession of a valid reset URL without altering the account yet.

## Requirements

1. Verified Weblate account
2. Access to the account's email inbox
3. Web browser for form submission

## Defense

Defensive measures and detection strategies:

- Rate-limit password reset requests per IP/email
- Invalidate tokens immediately upon generation if unused within a short window
- Log reset requests and monitor for patterns indicating abuse

## Objectives

1. Generate a password reset token
2. Capture the token without consumption
3. Prepare for testing token persistence

## Instructions

### Step 1: Initiate Reset Request

**Context**: Trigger the reset mechanism to send the token via email.

Navigate to the password reset page on Weblate (typically under accounts/login or a dedicated reset form). Enter the registered email address and submit the request.

> An email will be sent containing a reset link like `https://demo.weblate.org/accounts/password/reset/key/.../`. Do not click it yet.

### Step 2: Capture the Token Link

**Context**: Secure the link for later use without activating the reset.

Open the email and copy the full reset URL, including the token parameter.

> Store the link safely; it should remain valid for the demo.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Account Manipulation]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- password-reset
- token-generation
- weblate
