---
tags:
  - setup
  - waktime
  - leaderboard
  - invitation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:59.280Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 762ed240-f35d-414d-bc40-2516e8e942ae
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-WakaTime-Private-Leaderboard-and-Invite-Member

## Summary

This procedure sets up a private leaderboard in WakaTime and invites a second account as a member, preparing the environment for testing access controls and role-based permissions.

## Description

In the context of exploiting WakaTime's leaderboard feature, this initial setup involves creating a private leaderboard with one account and inviting another to join. This establishes a controlled environment with multiple roles, essential for demonstrating access control issues. The target is the WakaTime web platform, requiring valid user credentials. Expected outcome is a functional private leaderboard with at least two members.

## Requirements

1. Valid WakaTime account credentials for account A (owner)
2. Second WakaTime account B (can be same user, different email)
3. Web browser with access to waketime.com
4. Email access for invitation acceptance

## Defense

Defensive measures and detection strategies:

- Monitor for unusual leaderboard creation patterns or rapid invitations
- Implement rate limiting on invite features
- Log all leaderboard access and role changes for anomaly detection

## Objectives

1. Establish a private leaderboard for testing
2. Add a member account to simulate team environment
3. Verify initial access controls are in place

## Instructions

### Step 1: Create Private Leaderboard

**Context**: Log in as the owner and create the leaderboard to start the setup.

Navigate to WakaTime dashboard, select 'Create Leaderboard', choose 'Private' visibility, name it 'test1', and submit.

> Expected output: Leaderboard created confirmation and dashboard entry.

### Step 2: Send and Accept Invitation

**Context**: Invite the second account to join as a member.

From the leaderboard settings, use the invite tool to email account B. Switch to account B, log in, and accept the invite.

> Expected output: Account B added to members list.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[setup]]
- [[waktime]]
- [[leaderboard]]
