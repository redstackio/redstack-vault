---
tags:
  - twitter
  - badge-restoration
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
  - iOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:30:35.393Z'
skill_level: beginner
impact_level: high
sub_techniques: []
id: f07653e8-9c07-4365-a3f1-3f5bfb5b2320
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Wait for Review Completion and Badge Restoration

## Summary

This final procedure waits for Twitter's team to approve the queued profile changes, restoring the verified badge despite the expired subscription.

## Description

The review process, lasting 2-3 days, approves changes without re-verifying subscription status, granting permanent badge access. This exploits the lack of timestamp validation in the queue.

## Requirements

1. Profile under review post-expiration.
2. No further interventions.
3. Monitoring capability.

## Defense

Defensive measures and detection strategies:

- Integrate subscription checks into review approval.
- Audit restored badges for active payments.

## Objectives

1. Achieve badge reinstatement.
2. Confirm persistence without payments.
3. Complete the exploit chain.

## Instructions

### Step 1: Monitor Review Progress

**Context**: Allow time for team approval.

Wait 2-3 days without actions.

> Expected output: Notification or automatic update.

### Step 2: Verify Badge Restoration

**Context**: Check final status.

View profile for blue badge.

> Expected output: Badge present; subscription inactive.

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

- [[twitter]]
- [[badge-restoration]]
