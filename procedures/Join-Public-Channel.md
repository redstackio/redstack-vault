---
id: proc-002
tags:
  - mattermost
  - channel-access
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:30:07.523Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Join Public Channel

## Summary

This procedure allows a user to join a public channel in Mattermost, gaining visibility and initial access necessary for posting and request capture in privilege escalation scenarios.

## Description

As a regular user (e.g., User2), search for and join the public channel created in prior steps. This simulates standard user behavior in a team environment. The procedure assumes the channel is public and joinable. Expected outcome: User membership confirmed, setting the stage for permission testing.

## Requirements

1. Valid user account with join permissions
2. Access to Mattermost sidebar or search
3. No prior membership restrictions

## Defense

Defensive measures and detection strategies:

- Limit public channel visibility to verified users
- Log join events and monitor for anomalous access patterns
- Use invitation-only channels for sensitive discussions

## Objectives

1. Gain channel membership as a test user
2. Verify access to channel feed
3. Prepare for posting actions

## Instructions

### Step 1: Search and Join Channel

**Context**: Locate the public channel via UI search.

**Instructions**: In Mattermost, use the search bar to find 'mikefourchannel', click 'Join Channel'.

> User is now a member with read access.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[mattermost]]
- [[channel-access]]
