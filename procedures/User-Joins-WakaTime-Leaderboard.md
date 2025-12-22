---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567893
tags:
  - information-disclosure
  - privacy-misconfiguration
  - wakatime
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Employee Names]]'
updated_at: '2025-12-14T17:30:35.733Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Employee Names]]'
---
# User-Joins-WakaTime-Leaderboard

## Summary

This procedure simulates or facilitates the target user's acceptance of the leaderboard invitation, which activates the vulnerability by adding them as a member.

## Description

Upon accepting an invite, WakaTime updates the leaderboard membership without applying privacy filters, leading to email exposure. This step requires coordination if testing ethically, or observation in real scenarios. The target must have private email settings enabled. Outcome: Target listed as an active member.

## Requirements

1. Pending invitation from previous step
2. Target user's access to their WakaTime account
3. No additional tools needed

## Defense

Defensive measures and detection strategies:

- Enforce privacy setting checks on join events
- Notify users of PII exposure risks during acceptance
- Audit join logs for unusual patterns

## Objectives

1. Complete the membership process
2. Trigger backend data synchronization
3. Enable visibility of member details

## Instructions

### Step 1: Target Logs In

**Context**: Prepare for invitation handling.

The target signs into wakatime.com and checks notifications or email for the invite.

### Step 2: Accept Invitation

**Context**: Join the leaderboard.

Click the 'Accept' button on the invitation, confirming addition to the private group.

### Step 3: Confirm Membership

**Context**: Validate join success.

Target verifies their presence on the leaderboard page; attacker checks roster update.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Employee Names]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[information-disclosure]]
- [[privacy-misconfiguration]]
