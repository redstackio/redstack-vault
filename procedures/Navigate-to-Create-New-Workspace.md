---
id: 123e4567-e89b-12d3-a456-426614174001
tags:
  - web
  - ui-interaction
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques: []
updated_at: '2025-12-13T23:52:39.140Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
---
# Navigate-to-Create-New-Workspace

## Summary

This procedure involves interacting with the Mattermost connect-workspace page to select the option for creating a new workspace, exposing the vulnerable input form.

## Description

From the loaded connect-workspace page, users typically see options to connect existing workspaces or create new ones. Clicking the 'Create New Workspace' button or link transitions to a form where the workspace name is entered. This step is manual and relies on standard web UI navigation. Success confirms the availability of the creation interface without additional authentication hurdles.

## Requirements

1. Successful completion of prior page access
2. Functional web browser capable of form interactions
3. Visibility of UI elements on the page

## Defense

Defensive measures and detection strategies:

- Ensure UI elements are protected behind authentication where appropriate
- Log user interactions with creation flows for anomaly detection

## Objectives

1. Transition to the workspace creation form
2. Expose the unsanitized input field
3. Maintain session continuity

## Instructions

### Step 1: Select Create Option

**Context**: Identify and click the UI element that leads to new workspace creation.

No command required; locate and click the 'Create New Workspace' button or link on the page.

> The screen should change to display the creation form, including the workspace name input.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[web]]
- [[ui-interaction]]
