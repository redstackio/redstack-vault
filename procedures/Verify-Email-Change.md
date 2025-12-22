---
tags:
  - account-takeover
  - verification
type: procedure
tools:
  - '[[tools/CloudFlare]]'
tactics:
  - '[[Persistence]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Steal Web Session Cookie]]'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 8dc7e1d7-a019-4d1b-9ca6-625928422137
created_at: '2025-12-13T09:00:34.474Z'
updated_at: '2025-12-13T09:00:34.474Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# Verify Email Change

## Summary

This procedure completes the account takeover by clicking the verification link in the email sent to the attacker's address.

## Description

After the email change request, Discourse sends a verification email to the new address. The attacker confirms it, finalizing the takeover, while the victim receives a notification.

## Requirements

1. Access to the attacker's email inbox
2. Successful email change request from previous step

## Defense

Defensive measures and detection strategies:

- Require additional verification for email changes
- Notify users of changes and allow rollback

## Objectives

1. Confirm email change
2. Gain full control of victim's account
3. Complete takeover

## Instructions

### Step 1: Check Email and Verify

**Context**: Receive and act on the verification email.

No specific command; manually click the verification link in the email sent to the attacker's address.

> This confirms the change, and the victim's original email receives a notification, but the change is already effective.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Steal Web Session Cookie]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/CloudFlare]]

## Tags

- account-takeover
- verification
