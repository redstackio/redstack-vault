---
id: p6f7g8h9-j0k1-2345-fghi-678901234567
tags:
  - account-takeover
  - persistence
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
updated_at: '2025-12-14T17:33:24.298Z'
skill_level: beginner
impact_level: critical
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Complete-Account-Takeover-via-Password-Change

## Summary

This final procedure sets a new password during the reset process to achieve persistent control over the victim's DoD account.

## Description

After answering security questions correctly via the exploit, the application presents a form to enter a new password, which the attacker uses to lock out the victim and gain full access to sensitive features.

## Requirements

1. Access to the password reset form from previous step
2. Desired new password
3. No additional verification (e.g., email confirmation)

## Defense

Defensive measures and detection strategies:

- Send email notifications for password changes
- Implement account lockout after resets
- Audit logs for unusual reset patterns

## Objectives

1. Update password to attacker-controlled value
2. Verify login with new credentials
3. Maintain access for further exploitation

## Instructions

### Step 1: Enter New Password

**Context**: Fill the reset form.

**Instructions**: Input a strong new password (e.g., AttackerPass123!) and confirm it.

> Expected output: Success message and login prompt.

### Step 2: Test Access

**Context**: Confirm takeover.

**Instructions**: Log in with victim's email and new password; access member options.

> Expected output: Full dashboard access.

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
- persistence
