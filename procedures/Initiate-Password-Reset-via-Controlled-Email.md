---
tags:
  - password-reset
  - account-takeover
  - weblate
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-reset-password-weblate]]'
verified: false
platforms:
  - Web
  - Django
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:58.296Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 92b90b1d-9e83-4cbf-8a9c-4b07c554eaa5
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Initiate-Password-Reset-via-Controlled-Email

## Summary

This procedure triggers a password reset using the now-primary controlled email on Weblate's /accounts/reset/ endpoint, allowing the attacker to receive the reset link and complete the account takeover.

## Description

With the controlled email as primary, a POST to /accounts/reset/ sends the reset link to the attacker's inbox. This bypasses the need for the original password, leveraging the prior email manipulation for full access.

## Requirements

1. Controlled email set as primary
2. CSRF token from the reset form
3. Access to the forgot password page

## Defense

Defensive measures and detection strategies:

- Require secondary verification for resets (e.g., MFA)
- Delay reset links or notify original email
- Monitor reset requests post-email changes

## Objectives

1. Send reset link to controlled email
2. Enable new password setting
3. Achieve persistent account control

## Instructions

### Step 1: Access Reset Form

**Context**: Navigate to /accounts/password/reset/ to get CSRF.

Extract token from the form.

### Step 2: Submit Reset Request

**Context**: POST the controlled email to initiate reset.

**Command** ([[commands/curl-reset-password-weblate]]):
```bash
curl -X POST 'https://target.weblate.org/accounts/reset/' \
  -H 'X-CSRFToken: your_csrf_token' \
  -d 'csrfmiddlewaretoken=your_csrf_token&email=user1%2Bhackerone%40example.com'
```

> Expected output: Message indicating reset email sent.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/curl-reset-password-weblate]]

## Tools Used


## Tags

- password-reset
- account-takeover
- weblate
