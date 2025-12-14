---
id: proc-verify-degradation
tags:
  - verification
  - post-exploit
  - slack
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Software Discovery]]'
updated_at: '2025-12-14T17:27:42.922Z'
skill_level: low
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Software Discovery]]'
---
# Verify-Integration-Degradation

## Summary

This procedure checks the Slack channel to confirm the GitHub integration has switched to unauthenticated mode, validating the CSRF success and resulting disruption.

## Description

Post-exploit, the integration URI endpoint processes the request, showing a confirmation page (e.g., slack6.png). Testing a GitHub event reveals failed notifications. Target is Slack UI. Expected outcome: Visible loss of functionality, such as no auth for GitHub pushes.

## Requirements

1. Access to the channel
2. Ability to test GitHub events
3. Admin or observer role

## Defense

Defensive measures and detection strategies:

- Automated alerts for integration changes
- Regular audits of channel settings
- Backup integrations for redundancy

## Objectives

1. Confirm mode switch
2. Assess impact on notifications
3. Validate attack success

## Instructions

### Step 1: Check Settings

**Context**: Inspect integration status in channel.

No specific command; go to channel > Integrations > View GitHub; note unauthenticated mode.

> Settings reflect the change.

### Step 2: Test Functionality

**Context**: Trigger a GitHub event to verify disruption.

No specific command; push to a repo linked to Slack; observe no notification or error.

> Integration disabled for channel.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Software Discovery]] Software Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[verification]]
- [[slack]]
