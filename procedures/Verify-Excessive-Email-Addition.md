---
id: proc-uuid-004
tags:
  - verification
  - web
  - bypass-check
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
updated_at: '2025-12-14T17:24:22.784Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Verify-Excessive-Email-Addition

## Summary

This procedure checks the user settings page post-exploitation to confirm that more than 5 emails have been successfully added, validating the race condition bypass.

## Description

After concurrent requests, the server state should reflect additional emails due to the sync failure. Refreshing the UI retrieves the updated list from the backend.

## Requirements

1. Active session from exploitation
2. Access to /user/settings

## Defense

Defensive measures and detection strategies:

- Periodic counter reconciliation jobs
- Audit logs for email additions
- UI-server consistency checks

## Objectives

1. List all added emails
2. Count exceeds 5
3. No errors in monitoring status

## Instructions

### Step 1: Refresh Settings Page

**Context**: Reload to fetch current state.

Visit https://stage.firefoxmonitor.nonprod.cloudops.mozgcp.net/user/settings.

> Expected: Page updates with full email list.

### Step 2: Review Email List

**Context**: Inspect the monitored emails section.

Count the entries and check statuses.

> Expected: >5 emails displayed as active.

### Step 3: Test Functionality

**Context**: Verify one added email triggers breach scan.

Select an email and initiate a scan if available.

> Expected: Scan proceeds without limit errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- verification
- web
- bypass-check
