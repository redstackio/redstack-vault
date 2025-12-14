---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567892
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
updated_at: '2025-12-14T17:30:35.738Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Employee Names]]'
---
# Invite-User-to-WakaTime-Leaderboard

## Summary

This procedure details inviting a target user to a private WakaTime leaderboard, which is a prerequisite for triggering the email disclosure upon their acceptance.

## Description

WakaTime's invitation system allows creators to add members via username or profile links. In this vulnerability scenario, the invite bypasses privacy checks, leading to PII exposure post-join. This step assumes the leaderboard is already created and targets a user with private email settings. Expected outcome: Pending invitation status, setting up the join trigger.

## Requirements

1. Existing private leaderboard
2. Target user's WakaTime username or public profile URL
3. Attacker's WakaTime session active

## Defense

Defensive measures and detection strategies:

- Require explicit consent for PII sharing during invites
- Log invitation attempts and validate sender-receiver relationships
- Rate-limit leaderboard invitations to prevent abuse

## Objectives

1. Dispatch a join invitation to the target
2. Maintain stealth by using legitimate platform features
3. Prepare for membership activation

## Instructions

### Step 1: Navigate to Leaderboard Management

**Context**: Access the invite interface.

From the WakaTime dashboard, open the private leaderboard's management page.

### Step 2: Enter Target Details

**Context**: Generate the invitation.

In the 'Invite Members' section, input the target's username or profile link, add an optional message, and click 'Send Invite'.

### Step 3: Verify Invitation

**Context**: Confirm dispatch.

Check the member list for a pending status and review any sent notifications.

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
