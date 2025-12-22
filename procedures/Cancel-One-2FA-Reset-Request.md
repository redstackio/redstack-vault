---
tags:
  - race-condition
  - cancellation-logic
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Modify Authentication Process]]'
updated_at: '2025-12-14T17:24:48.382Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 2a0c9efd-99c0-4404-80b8-95902e23af02
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Modify Authentication Process]]'
---
# Cancel One 2FA Reset Request

## Summary

This procedure cancels a single 2FA reset request while leaving parallel requests active, exploiting the flawed cancellation logic that fails to invalidate concurrent processes.

## Description

Following the initiation of multiple resets, this step tests the race condition by canceling one request. Due to poor synchronization in HackerOne's backend, the cancellation does not propagate to other active requests, allowing them to proceed independently. This is a business logic error in the notification and cancellation handling. The procedure assumes web access and email notifications from the prior step, leading to the persistence of unauthorized resets.

## Requirements

1. Receipt of multiple reset notification emails with unique identifiers
2. Access to the account dashboard or email links for cancellation
3. No additional tools beyond web browser

## Defense

Defensive measures and detection strategies:

- Ensure cancellation invalidates all pending requests for the same user/action
- Use atomic transactions or database locks for reset state management
- Monitor for patterns of partial cancellations after multiple initiations

## Objectives

1. Confirm that cancellation affects only the targeted request
2. Preserve active parallel requests for later exploitation
3. Validate the race condition without alerting defenses

## Instructions

### Step 1: Identify Requests

**Context**: Review the received emails or account settings to list all active reset requests, noting their unique IDs.

No command; use web interface to view pending actions.

### Step 2: Cancel a Single Request

**Context**: Select one reset (e.g., the first one) and submit the cancellation via the provided link or form.

Example interaction (inferred):

Click the "Cancel" link in one email, or POST to `/api/account/2fa/reset/{id}/cancel`.

```javascript
// Browser console example for cancellation
fetch('/api/account/2fa/reset/{request-id}/cancel', {method: 'POST', credentials: 'include'}).then(r => r.json()).then(console.log);
```

> Expected output: Success message for that specific cancellation; other emails unchanged.

### Step 3: Verify Persistence

**Context**: Check that remaining notifications are still active.

Confirm no auto-cancellation of others.

**Expected Output**: Other resets remain pending.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Modify Authentication Process]] Modify Authentication Process

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- race-condition
- cancellation-logic
