---
tags:
  - email-primary
  - auth-bypass
  - weblate
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-set-primary-email-weblate]]'
verified: false
platforms:
  - Web
  - Django
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:32:58.298Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 7636510a-b5ef-43de-87bb-33d864ad796b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Set-New-Email-as-Primary-in-Weblate

## Summary

This procedure changes the primary email in a Weblate account to the verified controlled email via the /accounts/profile/ endpoint, without requiring the current password, escalating the attack toward takeover.

## Description

The profile update form allows setting the email field to the new verified address via POST, including other profile data and CSRF. Unlike password changes, no current password is needed, allowing demotion of the original email and prioritization of the attacker's.

## Requirements

1. Verified controlled email in the account
2. Session cookie and CSRF token
3. Profile form parameters (username, first_name, etc.)

## Defense

Defensive measures and detection strategies:

- Enforce password confirmation for primary email changes
- Rate-limit profile updates
- Alert on primary email switches

## Objectives

1. Make controlled email the primary contact
2. Demote original email
3. Enable password reset to controlled email

## Instructions

### Step 1: Gather Profile Data

**Context**: Extract current profile fields from /accounts/profile/ GET.

Note fields like username, first_name, activetab, language.

### Step 2: Update Profile with New Primary

**Context**: POST the form data setting email to controlled.

**Command** ([[commands/curl-set-primary-email-weblate]]):
```bash
curl -X POST 'https://target.weblate.org/accounts/profile/' \
  -H 'Cookie: sessionid=your_session_cookie' \
  -H 'X-CSRFToken: your_csrf_token' \
  -d 'email=user1%2Bhackerone%40example.com&username=victim_user&first_name=Victim&activetab=%23account&language=it&secondary_in_zen=on&csrfmiddlewaretoken=your_csrf_token'
```

> Expected output: Updated profile confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Account Manipulation]] Account Manipulation

### Sub-Techniques


## Commands Used

- [[commands/curl-set-primary-email-weblate]]

## Tools Used


## Tags

- email-primary
- auth-bypass
- weblate
