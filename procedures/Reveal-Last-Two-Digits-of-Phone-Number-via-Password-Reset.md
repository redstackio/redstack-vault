---
tags:
  - information-disclosure
  - twitter
  - password-reset
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Identity Information]]'
updated_at: '2025-12-14T17:24:42.881Z'
sub_techniques: []
id: 63b5218c-248c-41e0-bf38-cd2851cc7a62
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Identity Information]]'
---
# Reveal-Last-Two-Digits-of-Phone-Number-via-Password-Reset

## Summary

This procedure exploits Twitter's password reset flow to disclose the last two digits of a user's associated mobile phone number by initiating a reset request, which reveals partial phone information in the response message.

## Description

In Twitter's password reset process, entering a username triggers a response that specifies sending an SMS to a phone number ending in certain digits if the account has mobile verification enabled. This information disclosure allows attackers to partially identify the phone number without authentication, setting up further enumeration. The target environment is Twitter's web platform, and the outcome is the revelation of the last two digits (e.g., '15'), reducing the search space for brute forcing.

## Requirements

1. Access to Twitter's public password reset endpoint (no login required).
2. Known target username.
3. Web browser for manual interaction or scripting capability for automation.

## Defense

Defensive measures and detection strategies:

- Implement consistent error messages that do not reveal phone details (e.g., generic 'recovery option selected' without digits).
- Rate limit reset requests per IP and username to prevent exhaustion.
- Monitor for repeated reset attempts on usernames and alert on anomalies.

## Objectives

1. Disclose partial phone number to enable targeted brute forcing.
2. Confirm mobile verification is enabled on the target account.
3. Gather reconnaissance data for privacy compromise.

## Instructions

### Step 1: Initiate Password Reset

**Context**: Access the password reset flow to trigger the phone disclosure.

Navigate to the Twitter password reset URL (e.g., https://twitter.com/i/flow/password_reset) and enter the target username in the search field.

> Click 'Search' to submit. The response will display a message like 'We'll text a code to the phone number ending in 15' if mobile is associated.

### Step 2: Capture Response

**Context**: Observe and record the partial phone information.

Inspect the page or network response for the exact message containing the last two digits.

> Successful output: Partial digits revealed, e.g., ending in '15'. If no phone, it may prompt for email instead.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Identity Information]] Gather Victim Identity Information

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[information-disclosure]]
- [[twitter]]
- [[password-reset]]
