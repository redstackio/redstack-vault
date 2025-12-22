---
id: p5e6f7g8-i9j0-1234-efgh-567890123456
tags:
  - password-reset
  - bypass
type: procedure
tools: []
tactics:
  - '[[Lateral Movement]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:24.301Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Initiate-Password-Reset-with-Known-Answers

## Summary

This procedure uses the attacker-known security answers to initiate and proceed through the forgot password flow, gaining access to the reset interface.

## Description

Post-CSRF, the attacker visits the forgot password page at https://www.██████/forgotpassword/, enters the victim's email, selects 'On Screen Reset', and answers the questions with 'hacked' to advance to password change.

## Requirements

1. Victim's email address
2. Known security answers from CSRF
3. Access to the public forgot password endpoint

## Defense

Defensive measures and detection strategies:

- Rate-limit reset attempts per IP/email
- Require additional factors (e.g., 2FA) for resets
- Log failed/successful answer attempts

## Objectives

1. Bypass security question verification
2. Reach the password change form
3. Prepare for account control

## Instructions

### Step 1: Access Forgot Password Page

**Context**: Start the reset process.

**Instructions**: Navigate to https://www.██████/forgotpassword/?redirect_to=%2Fmember%2Foptions%2Fcurrenttab%2Femail and enter victim's email.

> Expected output: Prompt for security questions.

### Step 2: Submit Known Answers

**Context**: Provide the forged answers.

**Instructions**: For each question (IDs 1,2,3), enter 'hacked' and submit.

> Expected output: Approval and redirect to set new password.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]] Lateral Movement

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- password-reset
- bypass
