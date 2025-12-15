---
id: proc-007
tags:
  - mattermost
  - request-replay
  - bypass
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
updated_at: '2025-12-14T17:30:07.511Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Replay Captured Request to Bypass Permissions

## Summary

This procedure replays a captured HTTP POST request in Burp Suite to post unauthorized messages in a read-only Mattermost channel, exploiting missing server-side re-validation.

## Description

Using the stored request from legitimate posting, replay it post-revocation. The server fails to check updated permissions, allowing escalation. Target: /api/v4/posts endpoint. Outcome: Successful unauthorized post.

## Requirements

1. Captured request in Burp Repeater
2. Valid session token in request
3. Auxiliary channel for optional fresh capture

## Defense

Defensive measures and detection strategies:

- Re-validate permissions on every API call
- Implement request signing or nonces
- Detect replay via timestamp or sequence checks

## Objectives

1. Modify and send replayed request
2. Achieve unauthorized post
3. Demonstrate escalation

## Instructions

### Step 1: Optional Auxiliary Post Capture

**Context**: Ensure request format if needed.

**Instructions**: Post in 'privilegeescalation' with Burp intercepting, capture similar POST.

> Fresh request for reference.

### Step 2: Replay Original Request

**Context**: Bypass via replay.

**Instructions**: In Repeater, load Step 3 request, update payload to {"message": "commenting in mike4 channel even no privilege", "channel_id": "mikefourchannel_id"}, send.

> 200 OK, message posted.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[mattermost]]
- [[request-replay]]
- [[bypass]]
