---
id: proc-uuid-2
tags:
  - badge-unlock
  - unpinning
  - reddit
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:25:33.831Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Unlock-and-Hide-New-Share-Badge

## Summary

This procedure unlocks the 'New Share' achievement badge (ID 10) on a Reddit account by embedding a post, then unpins it to hide it from public view, setting up the conditions for IDOR exploitation.

## Description

Reddit's achievements system awards badges for actions like sharing posts via embed. Unpinning hides them per official support docs. This simulates a user's intent to conceal activity. Target environment is the Reddit web app; outcomes include a hidden badge ready for revelation via IDOR.

## Requirements

1. Logged-in primary Reddit account
2. Access to any Reddit post
3. Knowledge of achievements URL: https://www.reddit.com/user/<username>/achievements/

## Defense

Defensive measures and detection strategies:

- Educate users on pinning visibility
- Log badge unpinning events
- Audit achievement endpoint access

## Objectives

1. Trigger badge unlock via embed action
2. Unpin the badge to hide it
3. Confirm hiding per support documentation

## Instructions

### Step 1: Generate Embed to Unlock Badge

**Context**: Perform the sharing action to earn the badge.

Go to any post on reddit.com. Click Share -> Embed to generate the embed code. This unlocks the 'New Share' badge.

### Step 2: Access Achievements and Unpin

**Context**: Hide the badge after unlocking.

Visit https://www.reddit.com/user/<username>/achievements/. Locate the 'New Share' badge (ID 10), click it, and select unpin to hide.

### Step 3: Reference Support Article

**Context**: Validate hiding behavior.

Read https://support.reddithelp.com/hc/en-us/articles/27063106698004-What-are-achievements to confirm unpinning removes visibility.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[badge-unlock]]
- [[unpinning]]
- [[reddit]]
