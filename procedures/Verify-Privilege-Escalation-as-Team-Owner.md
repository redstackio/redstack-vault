---
id: proc-uuid-3
name: Verify Privilege Escalation as Team Owner
tags:
  - verification
  - slack
  - discovery
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
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:28:44.778Z'
skill_level: basic
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Verify Privilege Escalation as Team Owner

## Summary

This procedure confirms the success of the privilege escalation by logging in as the team owner and inspecting the modified team settings in the admin panel.

## Description

After the API modification, verification as the team owner reveals the unauthorized change in the message editing and deletion section. This step targets the /admin/settings endpoint and assumes owner credentials. It demonstrates the persistence of the escalation without immediate detection.

## Requirements

1. Valid team owner credentials
2. Web browser access to Slack admin panel
3. Prior execution of the modification procedure

## Defense

Defensive measures and detection strategies:

- Enable notifications for setting changes
- Require owner approval for permission modifications
- Periodic audits of admin settings

## Objectives

1. Confirm 'allow_message_deletion' is enabled
2. Identify the scope of escalated privileges
3. Highlight detection gaps in owner controls

## Instructions

### Step 1: Log In as Team Owner

**Context**: Authenticate to access owner-only views.

Use browser to log in at https://app.slack.com/signin with owner credentials.

> Redirects to team workspace with owner dashboard.

### Step 2: Navigate to Permissions Settings

**Context**: Inspect the affected section for changes.

Go to https://teamname.slack.com/admin/settings#permissions, expand 'Message editing & deletion'.

> Expected output: 'Only administrators may delete messages' checkbox checked, confirming escalation.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- verification
- slack
- discovery
