---
tags:
  - xss
  - web
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 4bf10379-a340-4e3e-a712-b8ccb7b41f90
created_at: '2025-12-14T00:11:16.415Z'
updated_at: '2025-12-14T00:11:16.415Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Edit Scheduled Post

## Summary

This procedure involves accessing and editing a previously created scheduled post on Reddit to expose the injected malicious link.

## Description

Navigating to the scheduled posts section and selecting edit loads the post in the RichText editor, where the unfiltered malicious link becomes visible and interactive. This step is crucial for triggering the XSS in the editing context.

## Requirements

1. Access to the scheduled posts dashboard
2. The modified post must exist
3. Standard web browser

## Defense

Defensive measures and detection strategies:

- Sanitize all rendered content in editors
- Use content security policies to block unsafe schemes

## Objectives

1. Load the post in edit mode
2. Verify presence of malicious link
3. Prepare for execution

## Instructions

### Step 1: Navigate to Scheduled Posts

**Context**: Locate the post in the dashboard.

Go to the scheduled posts section in your Reddit community settings.

### Step 2: Select Edit Option

**Context**: Open the post for editing.

Click the edit button next to the target post to load the editor.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- xss
- web
