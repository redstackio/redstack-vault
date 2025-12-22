---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - account-manipulation
  - email-change
  - broken-access-control
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
updated_at: '2025-12-14T17:33:12.031Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Change-Email-Address-Without-Verification

## Summary

This procedure exploits the Coursera.org email change feature, which lacks password confirmation or notification to the original email, allowing an attacker to redirect account communications to a controlled address.

## Description

The vulnerability stems from the account settings page on coursera.org not requiring the current password for email updates, unlike password changes. No verification code or alert is sent to the existing email. This enables attackers with session access to alter the email, setting the stage for takeover. The process is purely UI-based and completes in seconds.

## Requirements

1. Active session in the victim's Coursera account
2. Attacker-controlled email address
3. Access to coursera.org settings page

## Defense

Defensive measures and detection strategies:

- Require current password for email changes
- Send notification and verification to the old email
- Log and alert on email modifications from new IPs

## Objectives

1. Redirect account recovery to attacker email
2. Bypass multi-factor verification steps
3. Maintain stealth without user notifications

## Instructions

### Step 1: Navigate to Settings

**Context**: Access the email configuration in the account profile.

From the Coursera dashboard, click on the profile icon and select 'Settings' or 'Account' to reach the email section.

### Step 2: Update Email Field

**Context**: Submit a new email without security prompts.

Enter the attacker-controlled email address in the provided field and click 'Save' or 'Update'. Observe no password prompt or old email notification.

**Expected Output**: Message indicating email change pending verification, with email sent only to the new address.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Account Manipulation]]

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[account-manipulation]]
- [[email-change]]
