---
tags:
  - password-reset
  - initial-access
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
updated_at: '2025-12-14T17:33:24.568Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 6ddc975c-e8ee-43b2-bc32-a52eb04103a5
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Request-and-Copy-Password-Reset-Link

## Summary

This procedure outlines how to request a password reset link for an Imgur account and copy it without activation, setting up for exploitation of non-expiring links in subsequent steps.

## Description

In the context of Imgur's vulnerability, an attacker with initial account access requests a password reset to obtain a token-based link sent via email. By copying the link URL directly from the email (e.g., inspecting the HTML or viewing source), the attacker avoids clicking it, which would consume the token. This preserves the link's validity for use after email changes. The target environment is Imgur's web platform, requiring only a username or email to initiate. Prerequisites include knowledge of the target account details. Expected outcome: A reusable reset URL stored securely.

## Requirements

1. Access to the target's email or username for reset initiation
2. Web browser for navigating Imgur's site
3. Text editor or note-taking app to store the link

## Defense

Defensive measures and detection strategies:

- Implement server-side token invalidation on email changes
- Monitor for unusual reset requests followed by email updates
- Rate-limit password reset attempts per account

## Objectives

1. Obtain a valid password reset token without consuming it
2. Store the link for delayed exploitation
3. Enable account manipulation in a multi-step attack

## Instructions

### Step 1: Initiate Password Reset

**Context**: Start the reset process to trigger email delivery of the link.

Navigate to https://imgur.com/signin and click 'Forgot Password?'. Enter the target username or email and submit.

> The system sends an email containing the reset link to the current account email.

### Step 2: Extract and Copy Link

**Context**: Retrieve the link from the email without activating it to keep the token intact.

Open the email inbox associated with the account. Locate the reset email from Imgur, view the message source or right-click the link to copy its URL (e.g., https://imgur.com/reset?token=exampletoken123). Paste into a secure text file.

> Expected output: Full URL copied, ready for later use. Avoid clicking to prevent token expiration.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[password-reset]]
- [[initial-access]]
