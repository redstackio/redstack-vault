---
tags:
  - auth-bypass
  - web
  - captcha
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:58.263Z'
sub_techniques: []
id: e0f48a31-aad5-4520-a305-69800da0c1e3
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Submit Email for Reset

## Summary

This procedure submits the victim's email address along with CAPTCHA verification to request a password reset link from Weblate.

## Description

Entering the victim's email and solving the CAPTCHA sends a reset request to the server, which emails a link. This step requires access to the reset form and knowledge of the email. The vulnerability lies in the link's behavior, not this submission.

## Requirements

1. Victim's email address
2. Ability to solve CAPTCHA (human or solver service)
3. Active session on reset form

## Defense

Defensive measures and detection strategies:

- Enhance CAPTCHA with advanced challenges (e.g., reCAPTCHA v3)
- Rate limit email submissions per IP
- Verify email domains against known users

## Objectives

1. Trigger email dispatch
2. Receive confirmation of request
3. Prepare for link retrieval

## Instructions

### Step 1: Enter Email and Solve CAPTCHA

**Context**: Provide target email to initiate link generation.

In the reset form, input the victim's email (e.g., victim@example.com) and complete the CAPTCHA by following on-screen instructions (e.g., select images). Click submit.

> Expected output: Message like 'We've emailed you instructions for setting your password.'

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[auth-bypass]]
- [[web]]
- [[captcha]]
