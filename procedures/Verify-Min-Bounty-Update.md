---
id: p6q7r8s9-t0u1-2345-ghij-kl6789012345
tags:
  - verification
  - query
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:53.505Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify-Min-Bounty-Update

## Summary

This procedure queries the updated invitation settings via GraphQL to confirm the arbitrary min_bounty value is persisted, demonstrating the bypass success and its impact on future invitations.

## Description

Post-modification, a UserInvitationSettingsQuery to /graphql retrieves current preferences. This validates the lack of server validation. In the web environment, it shows min_bounty exceeding the user's average (e.g., 7000 vs 600.625), filtering low-payout programs.

## Requirements

1. Successful mutation replay
2. Burp for query execution

## Defense

Defensive measures and detection strategies:

- Audit GraphQL queries for inconsistencies
- Cross-validate settings against user history

## Objectives

1. Retrieve updated settings
2. Confirm bypass
3. Observe invitation impact

## Instructions

### Step 1: Craft Verification Query

**Context**: Send a query to fetch settings.

In Burp Repeater, POST to /graphql with query: mutation UserInvitationSettingsQuery { userInvitationSettings { minBounty } }.

> Response includes {"data":{"userInvitationSettings":{"minBounty":7000.0}}}.

### Step 2: Check UI and Impact

**Context**: Validate persistence.

Refresh preferences page or monitor invitations.

> Slider may not reflect change, but backend confirms; future invites limited to high bounties.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- query
- confirmation
