---
id: proc-coinbase-navigate-settings-001
tags:
  - web
  - ios
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - iOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:52.118Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Navigate-to-Coinbase-Settings

## Summary

This procedure involves accessing the Coinbase account settings page directly after the bypassed login, without triggering any authorization checks.

## Description

From the dashboard, the settings endpoint (https://www.coinbase.com/settings) is reachable without verification, allowing escalation to account management functions. This step bridges information disclosure to potential manipulation, exploiting the same session flaw.

## Requirements

1. Active unauthorized session from iOS login
2. iOS browser access
3. Basic navigation knowledge

## Defense

Defensive measures and detection strategies:

- Endpoint authorization enforcement for sensitive pages
- User-agent based session scrutiny for mobile access
- Audit logs for settings navigation patterns

## Objectives

1. Reach account settings without barriers
2. Prepare for modification actions
3. Validate session scope

## Instructions

### Step 1: Direct URL Access

**Context**: Use the browser to load the settings page URL.

No command required; enter https://www.coinbase.com/settings in the address bar.

> Page loads fully, confirming no checks.

### Step 2: Menu Navigation Alternative

**Context**: Use the app's UI if URL fails.

No command required; click profile or settings icon from dashboard.

> Redirects to settings without prompts.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- web
- ios
