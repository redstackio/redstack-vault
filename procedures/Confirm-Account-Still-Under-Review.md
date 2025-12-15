---
tags:
  - twitter
  - review-confirmation
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
updated_at: '2025-12-14T17:30:35.396Z'
skill_level: intermediate
impact_level: medium
sub_techniques: []
id: 8d544faf-72e3-449e-9b76-770212c205c4
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Confirm Account Still Under Review

## Summary

This procedure tests the profile by attempting changes post-expiration to verify the review queue is still active, confirming the exploit's continuation.

## Description

With subscription expired, attempting edits should show a review-pending message, indicating the queue hasn't checked status. This validates the business logic gap in Twitter's review process.

## Requirements

1. Subscription expired.
2. Profile previously under review.
3. Edit access attempted.

## Defense

Defensive measures and detection strategies:

- Re-validate subscriptions on edit attempts during reviews.
- Flag prolonged review states.

## Objectives

1. Test review persistence.
2. Confirm no revocation.
3. Proceed to final wait.

## Instructions

### Step 1: Attempt Profile Edit

**Context**: Trigger potential review response.

Go to Edit Profile and try changing details.

> Expected output: Message like 'Account under review'.

### Step 2: Validate No Badge Change

**Context**: Ensure status quo.

Check profile for badge absence.

> Expected output: Review confirmed; no restoration yet.

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
- [[review-confirmation]]
