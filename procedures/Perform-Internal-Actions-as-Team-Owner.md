---
id: proc-perform-internal-actions
tags:
  - internal-trigger
  - hackerone
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:30:35.575Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Perform-Internal-Actions-as-Team-Owner

## Summary

This procedure simulates internal team operations on a HackerOne report by adding private comments and assignments, updating backend activity fields that can later be disclosed.

## Description

To trigger the vulnerability, the team owner performs actions visible only to team members, such as internal comments and group assignments. This updates latest_activity_id and latest_activity_at without notifying participants. Targeted at HackerOne's report interface, it requires owner privileges. Expected results are modified internal state for API leakage.

## Requirements

1. Team owner login to HackerOne
2. Access to the target report
3. Knowledge of team member usernames for assignments

## Defense

Defensive measures and detection strategies:

- Restrict internal actions to verified team members
- Log all internal updates for anomaly detection

## Objectives

1. Update internal activity metadata
2. Create disclosable artifacts
3. Mimic real team workflows

## Instructions

### Step 1: Add Internal Comment

**Context**: Create a team-only comment to trigger activity update.

In the report, select Internal Comment, enter text like "Discussing resolution privately", set visibility to team-only, and post.

> This updates the latest_activity_at timestamp internally.

### Step 2: Assign to Group

**Context**: Perform an assignment to generate activity ID.

Go to Assignments, select a group member, add a note, and assign the task.

> Assignment creates a new latest_activity_id linked to the internal action.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- internal-trigger
- hackerone
