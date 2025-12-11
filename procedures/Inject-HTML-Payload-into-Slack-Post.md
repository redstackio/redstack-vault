---
tags:
  - html-injection
  - slack
type: procedure
tools:
  - '[[tools/HTTP-Proxy]]'
  - '[[tools/HTTPS-Enabled-Server]]'
  - '[[tools/Developer-Tools]]'
  - '[[tools/Email-Client]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/open-calculator-macos]]'
  - '[[commands/open-calculator-windows]]'
  - '[[commands/exec-shell-command-nodejs]]'
  - '[[commands/alert-localstorage]]'
platforms:
  - Desktop
  - Electron
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 62ce7d4e-e8fc-47eb-a418-c4ad30a0ffbd
created_at: '2025-12-11T06:10:22.530Z'
updated_at: '2025-12-11T06:10:22.530Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1059.007]]'
---
# Inject HTML Payload into Slack Post

## Summary

This procedure injects arbitrary HTML into the Slack Post's JSON using web editing or request interception.

## Description

Edit via Slack web UI or intercept /api/files.edit to change filetype to 'docs' and inject tags like map/area for redirects.

## Requirements

1. Private file URL from previous step.
2. HTTP proxy for request modification.
3. Knowledge of allowed HTML tags.

## Defense

Defensive measures and detection strategies:

- Enforce strict tag whitelisting.
- Monitor for anomalous file edits.

## Objectives

1. Inject redirect payload.
2. Bypass tag restrictions.
3. Prepare for victim interaction.

## Instructions

### Step 1: Edit via Web UI or Proxy

**Context**: Access edit URL or intercept request.

Use [[tools/HTTP-Proxy]] to modify request.

```bash
# Use proxy like Burp to intercept and edit /api/files.edit
```

> Expected: JSON updated with HTML payload, filetype 'docs'.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/HTTP-Proxy]]

## Tags

- [[html-injection]]
- [[slack]]
