---
id: proc-uuid-004
tags:
  - race-condition
  - web
  - verification
type: procedure
tools:
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:18.787Z'
skill_level: intermediate
impact_level: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify-Multiple-Team-Joins

## Summary

This procedure confirms the success of the race condition exploitation by checking team membership and related confirmations.

## Description

Post-exploitation, validation involves inspecting the team roster for unexpected members and reviewing email artifacts. In the HackerOne-like platform, the member count should reflect dual joins (e.g., 2 to 4), with emails timestamped identically due to concurrent processing. This step uses the web UI and email client, assuming admin access for full verification. It highlights administrative confusion risks from unauthorized access.

## Requirements

1. Admin access to the target team for member list view
2. Email access for both test accounts
3. Web browser for UI checks

## Defense

Defensive measures and detection strategies:

- Audit logs for invitation events with timestamps
- Real-time notifications for membership changes
- Periodic reconciliation of token usage vs. joins

## Objectives

1. Confirm both accounts gained team access
2. Validate token reuse impact
3. Identify signs of exploitation for reporting

## Instructions

### Step 1: Check Team Member List

**Context**: Observe the increase in members from the single invitation.

**Instructions**: In an admin session via [[tools/Web-Browser]], navigate to the team members page.

> UI Action: Go to 'Team' > 'Members'. Note count change (e.g., from 2 to 4) and presence of both accounts.

### Step 2: Review Confirmation Emails

**Context**: Corroborate with email evidence of concurrent joins.

**Instructions**: Check inboxes for both accounts for invitation acceptance emails.

> Action: Open email client; verify emails received with identical timestamps, confirming parallel success.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Web-Browser]]

## Tags

- race-condition
- web
- verification
