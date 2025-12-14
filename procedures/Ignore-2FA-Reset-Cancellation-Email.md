---
tags:
  - wait-period
  - auto-disable
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Email
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Modify Authentication Process]]'
updated_at: '2025-12-14T17:33:12.284Z'
skill_level: low
impact_level: medium
detection_risk: low
sub_techniques: []
id: b5dc7fc2-09f8-47cc-991c-ab4fecc8ffc6
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Modify Authentication Process]]'
---
# Ignore-2FA-Reset-Cancellation-Email

## Summary

This procedure involves passively waiting for the victim to ignore the 2FA reset cancellation email, allowing the automatic disablement of two-factor authentication after 24 hours.

## Description

Following the reset trigger, HackerOne sends an email to the victim's address with a link to cancel the request. The vulnerability lies in the design where non-response leads to auto-disablement rather than requiring affirmative action to proceed. This step requires no active intervention from the attacker, relying on victim inaction. The target is the email service tied to the account. Expected outcome is 2FA disabled after the timeout period.

## Requirements

1. Reset email successfully sent to victim's address
2. No access to victim's email needed (attacker hopes for ignorance)
3. Patience to wait 24 hours

## Defense

Defensive measures and detection strategies:

- Change design to require explicit approval for disablement via multiple channels (e.g., SMS + email)
- Notify users via alternate methods (app push, phone) on reset attempts
- Log and alert on ignored reset requests approaching timeout

## Objectives

1. Ensure victim does not cancel the reset
2. Allow server-side timer to expire
3. Achieve 2FA disablement without further interaction

## Instructions

### Step 1: Monitor Email Dispatch

**Context**: Confirm the cancellation email was sent post-reset trigger.

If possible, verify via email logs or secondary access that the email arrived (not required for success).

> Email contains subject like 'Cancel 2FA Reset Request' with a unique link.

### Step 2: Wait for Timeout

**Context**: Do nothing to let the process complete automatically.

Avoid any actions that might prompt victim response; wait exactly 24 hours from the reset initiation time.

> After 24 hours, HackerOne's system disables 2FA if no cancellation occurred.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Modify Authentication Process]] Modify Authentication Process

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[wait-period]]
- [[auto-disable]]
