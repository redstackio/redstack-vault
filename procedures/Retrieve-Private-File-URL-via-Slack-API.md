---
tags:
  - slack
  - api
type: procedure
tools:
  - '[[tools/HTTP-Proxy]]'
  - '[[tools/HTTPS-Enabled-Server]]'
  - '[[tools/Developer-Tools]]'
  - '[[tools/Email-Client]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/open-calculator-macos]]'
  - '[[commands/open-calculator-windows]]'
  - '[[commands/exec-shell-command-nodejs]]'
  - '[[commands/alert-localstorage]]'
platforms:
  - Desktop
  - Electron
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: d3b59638-3889-444d-9023-cff907bc0d9e
created_at: '2025-12-11T06:10:22.535Z'
updated_at: '2025-12-11T06:10:22.535Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1190]]'
---
# Retrieve Private File URL via Slack API

## Summary

This procedure retrieves the private URL of a Slack Post's JSON file using the Slack API for editing access.

## Description

Calling /api/files.info provides the url_private, allowing access to the JSON for modification in the injection step.

## Requirements

1. Slack API access token.
2. File ID from created Post.
3. Network access to Slack API.

## Defense

Defensive measures and detection strategies:

- Rate limit API calls.
- Audit file access logs.

## Objectives

1. Obtain editable file URL.
2. Facilitate JSON editing.
3. Advance to payload injection.

## Instructions

### Step 1: Call API Endpoint

**Context**: Use API to get file details.

No command; use tools like curl or Postman to call /api/files.info.

> Expected: Response with url_private in format https://files.slack.com/files-pri/{TEAM_ID}-{FILE_ID}/TITLE.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[slack]]
- [[api]]
