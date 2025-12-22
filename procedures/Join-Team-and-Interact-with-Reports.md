---
id: proc-join-team-interact
tags:
  - team-management
  - report-interaction
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
updated_at: '2025-12-14T17:28:20.652Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Join-Team-and-Interact-with-Reports

## Summary

This procedure involves using a test account to join a HackerOne team and engage with private reports, establishing notification subscriptions for later testing of access controls.

## Description

In the context of testing HackerOne's team features, log in with a controlled account (e.g., @lccunha) to join a team like 'Test' and participate in a report (e.g., #45958). This simulates legitimate membership and triggers email notifications, setting up the scenario for removal testing. Expected outcomes include full visibility of report details during membership.

## Requirements

1. Valid HackerOne account with team join permissions
2. Access to create or select a test team and report
3. Web browser for interface navigation

## Defense

Defensive measures and detection strategies:

- Monitor team join events for anomalous patterns
- Implement rate limiting on team interactions

## Objectives

1. Gain legitimate access to team resources
2. Subscribe to report notifications
3. Prepare for removal simulation

## Instructions

### Step 1: Log In and Join Team

**Context**: Authenticate and become a team member to enable interactions.

Navigate to HackerOne login, enter credentials for @lccunha, and join the 'Test' team via the teams section.

> Successful login shows dashboard with team invitation acceptance.

### Step 2: Interact with Report

**Context**: Engage with a private report to trigger notifications.

Select report #45958, view details, and perform actions like commenting to ensure subscription.

> Report page displays full access, confirming interaction.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[team-management]]
- [[report-interaction]]
