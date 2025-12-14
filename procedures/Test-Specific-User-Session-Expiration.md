---
id: proc-shopify-specific-expiration-001
tags:
  - targeted-expiration
  - bypass
  - shopify
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:44.620Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Test-Specific-User-Session-Expiration

## Summary

This procedure targets a specific user's session for expiration via admin and verifies iOS persistence, showing the flaw affects granular revocations.

## Description

From the admin, select a specific staff user and expire their session individually, then check the iOS app. This tests if the bypass occurs beyond global expiration, due to unsynchronized invalidation. Requires owner access and active mobile session. Result is continued mobile access despite targeted revocation.

## Requirements

1. Owner admin access.
2. Specific staff user profile visible.
3. Active iOS session for that user.

## Defense

Defensive measures and detection strategies:

- Ensure per-user expiration propagates to all clients via unified session store.
- Log and alert on failed mobile session invalidations.

## Objectives

1. Attempt targeted session revocation.
2. Confirm iOS bypass for specific user.
3. Demonstrate comprehensive vulnerability scope.

## Instructions

### Step 1: Navigate to User Profile

**Context**: Access targeted revocation option.

In admin, go to Settings > Users and permissions, select the staff user (e.g., Alpha).

### Step 2: Expire Specific Session

**Context**: Trigger user-specific invalidation.

Click 'Expire User's Session', confirm, and note the notification.

### Step 3: Verify in iOS App

**Context**: Check persistence post-targeting.

Return to iOS app and perform an action like adding a product.

**Expected Output**: Session active; action succeeds.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[targeted-expiration]]
- [[bypass]]
- [[shopify]]
