---
tags:
  - notification
  - team-invite
  - serialization
type: procedure
tools:
  - '[[tools/Python-Pickle-Module]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: ee052ac5-8992-4531-8cde-ebb73cbfcce8
created_at: '2025-12-14T03:46:19.804Z'
updated_at: '2025-12-14T03:46:19.804Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-Notification-via-Team-Invitation

## Summary

This procedure creates a notification in Liberapay by inviting a user to a team, which serializes context data using Python's pickle module and stores it in the notifications table, setting up a vector for further exploitation.

## Description

In Liberapay's notification system, inviting a user to a team calls the notify function in liberapay/models/participant.py, which uses pickle.dumps to serialize context (e.g., team details) and inserts it into the PostgreSQL notifications table's context field. This step is prerequisite for injecting malicious payloads, as it creates a deserializable record without direct input to the context field due to restrictions on inputs like team names.

## Requirements

1. Authenticated session in Liberapay
2. Access to create or manage teams
3. Target user email or username for invitation

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all inputs before serialization
- Use safe serialization formats like JSON instead of pickle
- Monitor database inserts into notifications table for anomalies

## Objectives

1. Establish a notification record for payload injection
2. Ensure context is pickled and stored
3. Prepare for SQLi escalation

## Instructions

### Step 1: Authenticate and Navigate to Team Management

**Context**: Log in to gain permissions to invite users.

No command required; use the web interface to log in at liberapay.com.

> Successful login grants access to team features.

### Step 2: Invite User to Team

**Context**: Trigger the notification creation, which serializes context.

Use the Liberapay UI to invite a user (e.g., enter email and send invite).

> This calls notify(), pickles context like {'team': team_data}, and inserts into notifications table.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Python-Pickle-Module]]

## Tags

- [[notification]]
- [[team-invite]]
- [[serialization]]
