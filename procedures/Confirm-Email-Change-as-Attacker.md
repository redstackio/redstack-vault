---
id: confirm-email-change-attacker
tags:
  - email-hijack
  - confirmation
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:06.531Z'
skill_level: low
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Confirm Email Change as Attacker

## Summary

This procedure allows the attacker to receive and act on the IRCCloud email confirmation sent after the CSRF-induced change, verifying the new email on the victim's account.

## Description

IRCCloud sends a confirmation email to the newly set address (attacker's) containing a verification link. By clicking it, the attacker completes the email update process, ensuring all future account emails (including password resets) route to them. This exploits the logic flaw where email updates occur pre-confirmation but enable immediate reset flows.

## Requirements

1. Access to the controlled email account
2. Successful prior CSRF email change
3. Valid confirmation link in email

## Defense

Defensive measures and detection strategies:

- Delay email updates until confirmation to prevent premature reset access
- Notify original email of changes for approval
- Rate-limit confirmation requests
- Audit logs for rapid email switches

## Objectives

1. Intercept and verify the email change confirmation
2. Secure control over account notifications
3. Prepare for password reset exploitation

## Instructions

### Step 1: Monitor Inbox

**Context**: Wait for IRCCloud's automated email post-submission.

**Instructions**: Check email (e.g., hacker@example.com) for message from IRCCloud with subject like "Confirm your email change".

**Expected Output**: Email arrives with unique verification link.

### Step 2: Complete Verification

**Context**: Use the link to finalize the change.

**Instructions**: Click the link in the email; browser redirects to IRCCloud confirmation page.

**Expected Output**: Success message; email now officially tied to account.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[email-hijack]]
- [[confirmation]]
