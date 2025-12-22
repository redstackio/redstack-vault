---
tags:
  - discovery
  - collection
  - pii-exposure
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:51.692Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 4fa4e76a-57e2-48d3-886f-9e365e8e0a8c
validated: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Add-Widgets-to-Expose-Sensitive-Data

## Summary

This procedure exploits the dashboard's Add Widgets feature to display unauthorized sensitive data, including PII such as full names, emails, addresses, phone numbers, and diagnostic metrics like memory usage and incident counts, due to missing authorization checks.

## Description

The DoD application's dashboard allows any verified user to add widgets that pull from restricted data sources without validation. This targets the web interface at `███████`, where widgets reveal operational details. Prerequisites include dashboard access; outcomes enable bulk data viewing and potential screenshots for documentation.

## Requirements

1. Active session in the dashboard
2. Web browser for UI interaction
3. No additional tools needed

## Defense

Defensive measures and detection strategies:

- Implement server-side authorization checks for all widget data queries.
- Log widget additions and data accesses, alerting on anomalies from standard users.
- Restrict widget types available to non-privileged roles.

## Objectives

1. Expose PII and diagnostics via customizable widgets.
2. Demonstrate lack of access controls.
3. Collect evidence of vulnerability impact.

## Instructions

### Step 1: Initiate Widget Addition

**Context**: Access the widget customization tool in the dashboard.

Click the 'Add Widgets' button or icon in the dashboard interface.

> A menu or dialog opens listing available widgets.

### Step 2: Select and Add Widgets

**Context**: Choose widgets that query sensitive endpoints.

Browse and select multiple widgets (e.g., user list, diagnostics). Add them to the dashboard layout.

> Widgets render immediately, populating with data like user PII and system stats (e.g., memory usage, incident types/counts).

### Step 3: Verify Data Exposure

**Context**: Inspect the loaded content for unauthorized information.

Scroll through added widgets and note exposed details; use browser dev tools to inspect network requests if needed.

> Confirm PII (names, emails, etc.) and diagnostics are visible without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery
- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Discovery]]
- [[Collection]]
- [[pii-exposure]]
