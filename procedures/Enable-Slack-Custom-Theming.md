---
id: proc-slack-enable-theming-001
tags:
  - slack
  - custom-theming
  - macos
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-13T23:52:33.516Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Enable-Slack-Custom-Theming

## Summary

This procedure activates the custom theming feature in Slack's Sidebar preferences on macOS, unlocking the vulnerable Column Background input field for CSS injection.

## Description

Custom theming in Slack allows users to apply personal styles but lacks validation, enabling injection attacks. This step toggles the feature on within the app's GUI. It assumes access to preferences from the prior step and results in exposure of CSS input fields. On macOS, this persists in app storage, amplifying exploit impact.

## Requirements

1. Access to Slack Sidebar preferences
2. macOS environment with Slack running
3. No external dependencies

## Defense

Defensive measures and detection strategies:

- Disable custom theming by default in enterprise deployments
- Log toggles of experimental features in app analytics
- Sandbox CSS application to prevent global DOM changes

## Objectives

1. Expose the vulnerable CSS input field
2. Enable arbitrary style application
3. Set stage for malicious payload injection

## Instructions

### Step 1: Locate Theming Toggle

**Context**: Identify the custom theming option in Sidebar settings.

Scroll to the theming section in Preferences > Sidebar.

> The toggle appears labeled as 'Custom Theming' or similar.

### Step 2: Activate Feature

**Context**: Switch on the feature to reveal input fields.

Click the toggle to enable custom theming.

> Fields like Column Background become editable for CSS entry.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[slack]]
- [[custom-theming]]
- [[macos]]
