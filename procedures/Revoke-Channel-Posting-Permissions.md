---
id: proc-005
tags:
  - mattermost
  - permission-revocation
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
updated_at: '2025-12-14T17:30:07.515Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Revoke Channel Posting Permissions

## Summary

This procedure revokes posting permissions in a Mattermost channel via System Console, transitioning it to read-only to test enforcement against replay attacks.

## Description

Admin updates permissions to deny posts from members and guests, simulating a security hardening step. This exposes the vulnerability if requests bypass checks. Outcome: Channel in read-only state.

## Requirements

1. Admin access to System Console
2. Target channel identified

## Defense

Defensive measures and detection strategies:

- Regularly review and audit permission changes
- Combine with API validation to prevent bypasses

## Objectives

1. Enforce read-only mode
2. Verify restriction via test post

## Instructions

### Step 1: Update Permissions

**Context**: Revoke access rights.

**Instructions**: System Console > Permissions > Channels, disable 'Allow guests/members to post' for public channels, apply to 'mikefourchannel'.

> Permissions revoked.

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
- [[permission-revocation]]
