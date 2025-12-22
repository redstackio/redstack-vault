---
tags:
  - password-reset
  - initial-access
type: procedure
tools:
  - '[[tools/Firefox-Browser]]'
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
updated_at: '2025-12-14T17:25:12.915Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: fd75a187-c97c-46b7-a716-07f00a5d0720
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Password-Reset-Page-with-Token

## Summary

This procedure simulates or facilitates access to a web application's password reset page, where a sensitive reset token is exposed in the URL query parameter, setting the stage for subsequent leakage exploitation.

## Description

In the context of a vulnerability like the one in HackerOne's platform, users receive an email with a recovery link pointing to `/users/password/edit?reset_password_token=TOKEN`. Accessing this page without immediately submitting a new password allows for potential leakage if the user navigates away. This step is crucial as it positions the token in the browser's current URL, which can be included in referer headers during cross-domain requests. Prerequisites include having triggered a password reset (e.g., via forgot password form) and controlling the email delivery or simulating the user.

## Requirements

1. Valid email address registered on the target platform to receive reset link
2. Access to a web browser like Firefox for simulation
3. Network connectivity to the target web application

## Defense

Defensive measures and detection strategies:

- Implement strict referer policies (e.g., Referrer-Policy: no-referrer) on sensitive pages
- Strip query parameters from referer headers using server-side configurations
- Monitor for anomalous access to reset pages from non-standard user agents

## Objectives

1. Load the password reset page with the token in the URL
2. Prepare for cross-domain navigation without form submission
3. Ensure the token remains valid (typically time-limited)

## Instructions

### Step 1: Trigger Password Reset

**Context**: Initiate the reset process to generate and receive the token via email.

No specific command; use the web form on `/users/password/new` to enter email and submit.

> Expected: Email arrives with link like `https://target.com/users/password/edit?reset_password_token=TOKEN`.

### Step 2: Navigate to Reset Page

**Context**: Open the link in a browser to load the page.

Use [[tools/Firefox-Browser]] to visit the URL from the email.

> Expected: Page loads with form fields for new password confirmation; URL bar shows token.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox-Browser]]

## Tags

- [[password-reset]]
- [[token-access]]
