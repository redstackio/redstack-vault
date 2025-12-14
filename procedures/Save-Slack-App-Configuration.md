---
id: proc-slack-save-config
tags:
  - slack
  - configuration
  - activation
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
updated_at: '2025-12-14T03:46:14.475Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Save-Slack-App-Configuration

## Summary

This procedure finalizes and activates the custom Slack app configuration, making the SSRF-vulnerable slash command operational in the workspace.

## Description

After setting the malicious URL, saving the app on api.slack.com installs the slash command, allowing invocation. This step is crucial for transitioning from setup to execution in the SSRF attack. Target: Slack workspace. Outcomes: Active command ready for triggering internal requests.

## Requirements

1. Configured slash command URL in the app
2. Permissions to install apps in the target workspace
3. Access to api.slack.com dashboard

## Defense

Defensive measures and detection strategies:

- Require admin approval for app installations
- Audit app configurations for suspicious URLs
- Use Slack's app directory review features

## Objectives

1. Activate the slash command for exploitation
2. Ensure no configuration errors block invocation
3. Prepare workspace for SSRF trigger

## Instructions

### Step 1: Review Settings

**Context**: Double-check configurations before saving.

Scan the app dashboard for the slash command URL (e.g., https://attacker.com/index.php) and ensure all required fields are filled.

> No validation errors displayed.

### Step 2: Save Changes

**Context**: Commit the configuration.

Click 'Save Changes' at the bottom of the slash command or app settings page.

> Confirmation message: Settings saved successfully.

### Step 3: Install to Workspace

**Context**: Make the app available in Slack.

If prompted, select 'Install to Workspace' and authorize permissions for the app.

> App installed; slash command usable in channels.

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
- [[configuration]]
- [[activation]]
