---
tags:
  - account-takeover
  - broken-access-control
  - email-manipulation
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
updated_at: '2025-12-14T17:32:57.805Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques:
  - '[[Additional Cloud Credentials]]'
id: 1c0d3bdc-3fae-4187-b6ca-459305499314
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Change-Email-Without-Confirmation

## Summary

This procedure exploits the Infogram email change feature by submitting a new email address without any verification, immediately redirecting account recovery and access to the attacker's control.

## Description

The vulnerability stems from the email update form applying changes instantly upon submission, without sending a confirmation to the original email or requiring verification. In an attack scenario, an attacker with session access modifies the email to their own, severing the victim's tie to the account. This targets web-based SaaS platforms like Infogram and leads to complete takeover, with prerequisites being an active session.

## Requirements

1. Logged-in session in Infogram account settings
2. Attacker's valid email address for substitution
3. Standard web browser

## Defense

Defensive measures and detection strategies:

- Require confirmation emails and OTP for email changes
- Log and alert on profile modifications from suspicious sessions
- Use email verification tokens that expire quickly

## Objectives

1. Redirect account ownership silently
2. Prevent victim recovery
3. Establish attacker persistence

## Instructions

### Step 1: Edit Email Field

**Context**: Locate and modify the email attribute.

On the profile settings page, find the email input field displaying the current value (e.g., victim@example.com). Enter the new email (e.g., attacker@evil.com).

> No command; UI form edit. Expected: Field accepts input without validation errors.

### Step 2: Submit the Form

**Context**: Trigger the update to apply changes immediately.

Click the "Save" or "Update Profile" button to submit.

> Expected: Page refreshes or shows success; email updated in backend without notifications.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Account Manipulation]]

### Sub-Techniques

- [[Additional Cloud Credentials]]

## Commands Used


## Tools Used


## Tags

- [[account-takeover]]
- [[broken-access-control]]
- [[email-manipulation]]
