---
tags:
  - verification
  - ui-failure
  - hackerone
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Disable or Modify Tools]]'
updated_at: '2025-12-14T17:32:29.211Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 15f41917-2974-4424-bbce-2ac81c57bc78
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Disable or Modify Tools]]'
---
# Verify-Notifications-and-Timestamp-Failure

## Summary

This procedure checks the HackerOne UI for notifications confirming API actions and reloads the API page to observe the unchanged 'Last request' timestamp, proving the business logic error.

## Description

After API calls, return to the UI to view notifications, which indicate backend success, then reload the token management page. The discrepancy shows the frontend failing to reflect backend timestamps, undermining monitoring. This is key to the vulnerability's impact on security assumptions.

## Requirements

1. Recent API operations performed
2. Access to HackerOne UI
3. Browser with JavaScript enabled

## Defense

Defensive measures and detection strategies:

- Sync frontend timestamps with backend in real-time via API polling
- Alert on notification-API activity mismatches
- Conduct periodic UI-backend integrity checks

## Objectives

1. Confirm backend activity through notifications
2. Identify UI timestamp stagnation
3. Document the monitoring false positive

## Instructions

### Step 1: Check Notifications

**Context**: Validate actions via UI feedback.

Open the notifications popup in HackerOne and review recent entries for API-induced events like report assignments.

**Expected Output**: List of notifications detailing actions (e.g., "Report assigned by API user").

### Step 2: Reload API Page

**Context**: Inspect token status post-usage.

Navigate back to https://hackerone.com/PROGRAM_HANDLE/api and refresh the page.

**Expected Output**: 'Last request' field remains 'Never'.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Disable or Modify Tools]] Disable or Modify Tools

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- verification
- ui-failure
