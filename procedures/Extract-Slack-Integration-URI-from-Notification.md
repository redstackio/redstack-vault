---
id: proc-slack-extract-uri
tags:
  - slack
  - uri-extraction
  - recon
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:27:42.937Z'
skill_level: low
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Extract-Slack-Integration-URI-from-Notification

## Summary

This procedure involves observing and copying the integration URI from a Slack channel notification, which is publicly accessible and sets up the target for CSRF exploitation.

## Description

After the integration is added, non-admin users receive a notification with a clickable link to the URI (e.g., https://vecchiowerther.slack.com/services/88143227125). The attacker, as a channel member, accesses this without authentication. The target environment is Slack's web or app interface. Expected outcome is obtaining the exact URI for appending the ?no_auth_mode=1 parameter.

## Requirements

1. Membership in the target Slack channel
2. Access to view notifications
3. Web browser or Slack client

## Defense

Defensive measures and detection strategies:

- Restrict integration notifications to admins only
- Audit channel members for suspicious activity
- Use Slack's approval workflows for integrations

## Objectives

1. Gather vulnerable endpoint URI
2. Confirm public accessibility
3. Prepare for CSRF payload construction

## Instructions

### Step 1: View Notification

**Context**: Monitor the channel for the integration addition message.

No specific command; open Slack channel and locate message: "added an integration to this channel: github".

> The message includes a clickable URI link.

### Step 2: Copy URI

**Context**: Extract the full URI from the link.

No specific command; right-click the link > Copy link address, e.g., https://vecchiowerther.slack.com/services/B2L476P3P.

> Verify by pasting into browser; it should show integration details without login.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[slack]]
- [[recon]]
