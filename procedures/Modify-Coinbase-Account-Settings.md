---
id: proc-coinbase-modify-settings-001
tags:
  - account-takeover
  - web
  - ios
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
  - iOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:28:52.115Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Modify-Coinbase-Account-Settings

## Summary

This procedure enables unauthorized editing of Coinbase account details, such as changing passwords or deleting the account, directly from the settings page without further verification.

## Description

Leveraging the persistent unauthorized session, attackers can alter critical account settings. This includes password resets, profile updates, or full account deletion, resulting in complete takeover or denial of service for the victim. The root cause is the absence of re-authentication on sensitive endpoints post-bypass.

## Requirements

1. Access to settings page via unauthorized session
2. iOS browser with loaded settings
3. Knowledge of desired modifications

## Defense

Defensive measures and detection strategies:

- Require re-authentication (e.g., MFA) for all account changes
- Monitor and alert on rapid setting modifications from new sessions
- Implement change confirmation emails for high-risk actions

## Objectives

1. Alter account credentials or details
2. Achieve full takeover or disruption
3. Confirm vulnerability exploitation

## Instructions

### Step 1: Select Modification Option

**Context**: Choose the setting to edit, such as password change.

No command required; click on password or account deletion section.

> Form fields load for input without verification.

### Step 2: Submit Changes

**Context**: Enter new details and apply.

No command required; fill form (e.g., new password) and submit.

> Changes apply immediately with success message, no email confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Account Manipulation]] Account Manipulation

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- account-takeover
- web
- ios
