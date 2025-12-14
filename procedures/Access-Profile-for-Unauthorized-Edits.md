---
id: proc-streamlabs-profile-edit-001
tags:
  - unauthorized-edit
  - billing-exposure
  - profile-access
type: procedure
tools: []
tactics:
  - '[[Collection]]'
  - '[[Command and Control]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:20.825Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
  - '[[Command and Control]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
---
# Access-Profile-for-Unauthorized-Edits

## Summary

This procedure allows a moderator to access and modify the parent account's profile, including billing and app management, exploiting inadequate role checks for Prime subscribers.

## Description

The app-store profile page at https://platform.streamlabs.com/app-store/profile lacks enforcement for moderators in shared context, exposing credit card details, CVV, subscriptions, and enabling edits. Also, /api/v1/s/user/me may leak billing info. Expected outcome: Full read/write access to sensitive features.

## Requirements

1. Parent context as moderator
2. Parent account is Prime subscriber for full impact
3. Web browser

## Defense

Defensive measures and detection strategies:

- Enforce owner-only access to billing and profile edits
- Token-based auth with role validation on every profile action
- Alert on modifications from shared access sessions

## Objectives

1. View billing information including credit card and CVV
2. Edit subscriptions, account details, and installed apps
3. Potentially compromise financial data or account integrity

## Instructions

### Step 1: Navigate to Profile Page

**Context**: Access the app-store profile while in parent context.

Go to https://platform.streamlabs.com/app-store/profile in the browser.

**Expected Output**: Profile loads with sections for billing, subscriptions, account info, and apps.

### Step 2: Interact with Sensitive Features

**Context**: View and attempt edits on exposed data.

Inspect billing section for credit card details and CVV; try editing a subscription or installing an app.

**Expected Output**: Data visible and changes apply without restrictions; API may return prime_subscription details.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection
- [[Command and Control]] Command and Control

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[unauthorized-edit]]
- [[billing-exposure]]
- [[profile-access]]
