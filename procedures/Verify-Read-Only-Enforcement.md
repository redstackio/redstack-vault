---
id: proc-006
tags:
  - mattermost
  - verification
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
updated_at: '2025-12-14T17:30:07.513Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Verify Read-Only Enforcement

## Summary

This procedure tests that revoked permissions prevent direct posting in a Mattermost channel, confirming the read-only state before attempting bypass.

## Description

User attempts a post via UI to trigger the error, validating the permission change. Outcome: Error confirms enforcement.

## Requirements

1. Membership in read-only channel
2. UI access

## Defense

Defensive measures and detection strategies:

- Monitor failed post attempts for patterns
- Ensure consistent error messaging

## Objectives

1. Confirm post failure
2. Observe error message

## Instructions

### Step 1: Attempt Post

**Context**: Test restriction.

**Instructions**: In 'mikefourchannel', try posting a message via compose box.

> Error: 'This channel is read only. Only members with permission can post here'.

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
- [[verification]]
