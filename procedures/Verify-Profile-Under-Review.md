---
tags:
  - twitter
  - review-monitoring
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
  - iOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:30:35.418Z'
skill_level: beginner
impact_level: low
sub_techniques: []
id: b3d78c99-c14f-4349-91ad-1cb60ce6b8ba
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Verify Profile Under Review

## Summary

This procedure monitors the Twitter profile to confirm it's in the review queue after changes, ensuring the badge removal persists without early restoration.

## Description

Post-profile change, Twitter places the account under review for 1-2 days. This step verifies the status to avoid premature approval, which could require repeating the change. It involves periodic checks via the app or web.

## Requirements

1. Recent profile change completed.
2. Access to the Twitter profile view.
3. Patience for 1-2 day review window.

## Defense

Defensive measures and detection strategies:

- Automate review notifications to users.
- Log repeated review triggers for abuse detection.

## Objectives

1. Confirm badge absence and review status.
2. Detect any early restoration.
3. Prepare for cancellation step.

## Instructions

### Step 1: Check Profile Status

**Context**: Inspect for review indicators.

View the profile; look for missing badge and any review notifications.

> Expected output: No badge; possible 'under review' indicator.

### Step 2: Monitor Over Time

**Context**: Re-check periodically if needed.

Refresh profile every few hours; if badge returns, repeat profile change.

> Expected output: Review persists for 1-2 days.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[twitter]]
- [[review-monitoring]]
