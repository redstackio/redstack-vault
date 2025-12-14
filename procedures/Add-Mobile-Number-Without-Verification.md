---
id: proc-add-mobile-no-verif-207552
tags:
  - business-logic
  - sms-spam
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:32:58.255Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Add-Mobile-Number-Without-Verification

## Summary

This procedure exploits the lack of SMS or call verification when adding or changing a mobile number on Khan Academy, allowing redirection of notifications or spam to arbitrary phones.

## Description

The account settings permit updating mobile numbers without confirmation, rooted in a business logic flaw. Though Khan Academy noted mobile numbers were not actively used for SMS at the time, the feature enables potential abuse like spamming notifications. Manual testing confirmed no OTP is sent, making it viable for attackers to target non-users or control comms post-takeover.

## Requirements

1. Access to the account settings page
2. Arbitrary phone number to input (e.g., for spam testing)
3. Account with mobile field available

## Defense

Defensive measures and detection strategies:

- Require SMS OTP for mobile additions/changes
- Limit notification sends and monitor for bulk updates
- Disable or deprecate unused mobile features with warnings

## Objectives

1. Update mobile to attacker-controlled number
2. Enable spam via platform notifications
3. Enhance account control through redirected alerts

## Instructions

### Step 1: Locate Mobile Form

**Context**: Find the mobile number input in settings.

No command required; perform UI action:

- Navigate to the 'Mobile Number' or 'Phone' section.

> Field appears for entry. Expected output: Editable input box.

### Step 2: Submit New Number

**Context**: Add or update without verification.

No command required; perform UI action:

- Enter phone number (e.g., +1-555-123-4567) and submit.

> Update saves instantly. Expected output: Confirmation; check for any sent notifications.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Account Manipulation]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[mobile-update]]
- [[no-otp]]
