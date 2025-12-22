---
tags:
  - twitter
  - subscription-cancellation
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - iOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Access Removal]]'
updated_at: '2025-12-14T17:30:35.405Z'
skill_level: beginner
impact_level: medium
sub_techniques: []
id: db2feb13-e58c-4b7c-a647-ffedf07e2249
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Account Access Removal]]'
---
# Cancel Twitter Blue Subscription

## Summary

This procedure cancels the Twitter Blue subscription via the App Store while the profile review is pending, setting the stage for expiration without interrupting the queue.

## Description

Cancellation through iOS App Store ensures the subscription ends one day later, aligning with the review timeline. This step is critical as it stops payments but keeps the review active, exploiting the lack of status re-check.

## Requirements

1. Active subscription managed via App Store.
2. iOS device access.
3. Profile under review from prior step.

## Defense

Defensive measures and detection strategies:

- Sync subscription status with review queues in real-time.
- Alert on cancellations during active reviews.

## Objectives

1. Initiate subscription end.
2. Maintain review queue integrity.
3. Avoid immediate badge revocation.

## Instructions

### Step 1: Access App Store Subscriptions

**Context**: Locate Twitter Blue in subscriptions.

Open App Store > Profile icon > Subscriptions.

> Expected output: List of active subscriptions including Twitter Blue.

### Step 2: Cancel Subscription

**Context**: Confirm cancellation.

Select Twitter Blue > Cancel Subscription > Confirm.

> Expected output: Cancellation notice; end date set to next day.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Account Access Removal]] Account Access Removal

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[twitter]]
- [[subscription-cancellation]]
