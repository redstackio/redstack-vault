---
id: proc-observe-notifications
tags:
  - notifications
  - information-disclosure
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:20.646Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Observe-Unauthorized-Notifications

## Summary

This procedure captures continued email notifications and dashboard remnants for a removed user, disclosing private report information.

## Description

After removal, trigger a report update (e.g., scheduling #45958 to public) from another account and monitor the ex-member's (@lccunha) email for notifications containing report ID, team, and title. Also check dashboard for uncleaned team areas.

## Requirements

1. Remaining team member account to trigger updates
2. Email access for removed account
3. Dashboard login for removed account

## Defense

Defensive measures and detection strategies:

- Revoke notification subscriptions on removal
- Monitor for anomalous email sends post-removal

## Objectives

1. Receive unauthorized report details
2. Identify persistent dashboard elements
3. Confirm disclosure impact

## Instructions

### Step 1: Trigger Report Update

**Context**: Perform an action that generates a notification.

From @brdoors2, edit report #45958 to schedule public release.

> Update saves, notification queued.

### Step 2: Monitor Email and Dashboard

**Context**: Check for incoming sensitive data.

Log in to @lccunha email and dashboard; observe notification with details and lingering team views.

> Email arrives with report ID, team 'Test', and title.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[notifications]]
- [[information-disclosure]]
