---
id: proc-slack-add-github
tags:
  - slack
  - integration-setup
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:42.942Z'
skill_level: low
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Add-GitHub-Integration-to-Slack-Channel

## Summary

This procedure sets up the GitHub integration in a Slack channel, triggering notifications that expose the vulnerable integration URI to all channel members, enabling subsequent CSRF exploitation.

## Description

In the attack scenario, a channel admin adds the GitHub integration to a common channel like #random. This action is not pre-approved for normal users, but the resulting notification includes a clickable link to the integration URI (e.g., https://vecchiowerther.slack.com/services/B2L476P3P), which lacks proper access controls. The procedure requires admin privileges in the Slack workspace and targets web-based Slack interface. Expected outcome is the generation of a public URI that can be used for CSRF attacks.

## Requirements

1. Channel admin access in Slack workspace
2. Target channel (e.g., #random) with multiple members
3. Web browser access to Slack

## Defense

Defensive measures and detection strategies:

- Pre-approve integrations to avoid manual additions
- Monitor channel notifications for unusual integration adds
- Educate admins on verifying integration URIs

## Objectives

1. Expose integration URI via notification
2. Enable attacker observation as non-admin
3. Set stage for URI extraction

## Instructions

### Step 1: Access Channel Settings

**Context**: Navigate to the target channel and open integration settings to add GitHub.

No specific command; use Slack UI: Click channel name > Integrations > Add GitHub integration.

> This adds the integration and sends a notification to all members.

### Step 2: Confirm Addition

**Context**: Verify the integration is active and notification is sent.

No specific command; check channel for notification message like "added an integration to this channel: github" with URI link.

> Successful addition shows confirmation page retaining the URI.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[slack]]
- [[integration]]
