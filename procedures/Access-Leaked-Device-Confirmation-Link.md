---
tags:
  - auth-bypass
  - initial-access
type: procedure
tools:
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 489ef89a-eda0-4f20-a032-2e559f7b50b9
created_at: '2025-12-14T17:33:24.375Z'
updated_at: '2025-12-14T17:33:24.375Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access Leaked Device Confirmation Link

## Summary

This procedure tests access to a leaked device confirmation link, resulting in unauthorized redirection to a user's profile settings due to insufficient validation.

## Description

By directly loading an indexed device confirmation URL, attackers bypass normal auth flows and gain partial access to another user's account settings. The vulnerability stems from tokens that redirect without verifying expiration or ownership, allowing profile viewing and potential modifications. This step confirms the disclosure impact and sets up further exploitation.

## Requirements

1. A leaked URL from prior reconnaissance (e.g., via Google dorking)
2. Standard web browser like Chrome or Firefox
3. No authentication required

## Defense

Defensive measures and detection strategies:

- Enforce token expiration checks on all confirm_device requests
- Require session cookies or additional auth factors for redirects
- Log and alert on direct token access without referer

## Objectives

1. Gain unauthorized entry to user profile
2. Expose settings for observation or alteration
3. Validate token reusability

## Instructions

### Step 1: Load the Leaked URL

**Context**: Directly access the device confirmation endpoint to trigger the redirect.

In [[tools/Web-Browser]], enter and load: https://sorare.com/confirm_device?token=N04J3Zczv1GaFrniJisN1QgsisoJHQ

> Expected output: Automatic redirect to /settings/profile for user JACK3422, indicating access despite invalid appearance.

### Step 2: Observe Profile Access

**Context**: Verify the extent of unauthorized access gained.

Navigate within the redirected page to check editable fields like name or email.

> Expected output: Full view of profile settings without login prompt. Success if PII like username is visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Web-Browser]]

## Tags

- [[auth-bypass]]
- [[account-takeover]]
