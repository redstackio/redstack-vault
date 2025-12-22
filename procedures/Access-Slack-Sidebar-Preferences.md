---
id: proc-slack-access-prefs-001
tags:
  - slack
  - macos
  - preferences
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-13T23:52:33.518Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Access-Slack-Sidebar-Preferences

## Summary

This procedure navigates to the Slack app's Sidebar preferences on macOS to access custom theming settings, serving as the initial entry point for CSS injection exploits.

## Description

In the context of exploiting CSS injection in Slack's theming feature, this step involves launching the app and opening the relevant preferences panel. It targets the desktop client on macOS where theming is configurable via GUI. Prerequisites include having the Slack app installed and running. Expected outcome is visibility of the Sidebar settings, enabling further manipulation without authentication barriers.

## Requirements

1. Slack desktop app installed on macOS
2. User-level access to the app
3. No additional tools or network access needed

## Defense

Defensive measures and detection strategies:

- Monitor app preference changes via macOS logging (e.g., unified logs for Slack processes)
- Implement app sandboxing to restrict UI modifications
- User training to avoid enabling experimental features like custom theming

## Objectives

1. Gain access to vulnerable theming configuration
2. Prepare for enabling custom CSS input
3. Establish baseline for injection workflow

## Instructions

### Step 1: Launch Slack App

**Context**: Open the Slack application to access its internal menus.

No command required; use macOS Launchpad or Spotlight to start Slack.

> The app window opens, displaying the main workspace interface.

### Step 2: Open Preferences

**Context**: Navigate to the settings menu to reach Sidebar options.

Click on the Slack menu bar > Preferences, then select the Sidebar tab.

> Sidebar preferences panel loads, showing theming options.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[slack]]
- [[macos]]
- [[preferences]]
