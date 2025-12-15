---
id: proc-uuid-002
name: Leave-Group-and-Send-Message
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:28.830Z'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Account Discovery]]'
sub_techniques: []
tags:
  - twitter
  - dm
  - leave
commands: []
platforms:
  - Web
tools: []
skill_level: basic
impact_level: medium
detection_risk: low
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---

# Leave-Group-and-Send-Message

## Summary

This procedure removes a participant from a Twitter group DM and introduces new content to test for persistent access, highlighting the IDOR flaw.

## Description

Once the group is set up, this step has the target account (C) exit the conversation, followed by sending a message from remaining participants. The DM ID is captured from the URL. This simulates a real departure and tests if access is properly revoked. The environment is Twitter's web DM interface, with outcomes confirming the vulnerability setup.

## Requirements

1. Active group DM with multiple participants.
2. Login sessions for all accounts.
3. Ability to inspect browser URLs.

## Defense

Defensive measures and detection strategies:

- Enforce server-side checks on group membership before serving DM content.
- Log and alert on access attempts to left conversations.

## Objectives

1. Remove account C from the group.
2. Send a post-departure message.
3. Capture the DM ID for exploitation.

## Instructions

### Step 1: Leave the Group DM

**Context**: From account C, exit the conversation to trigger access revocation.

In the group DM, click the info icon and select 'Leave conversation'.

> Confirm the departure; the group should no longer appear in C's DM list.

### Step 2: Send Message and Capture ID

**Context**: From account A or B, add new content and note the conversation identifier.

Send a test message in the group. Copy the DM ID from the URL (e.g., twitter.com/messages/123456-composed).

> The ID is the numeric or hashed part after /messages/.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[twitter]]
- [[dm]]
- [[leave]]
