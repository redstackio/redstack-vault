---
id: proc-zaption-access-quick-question
tags:
  - xss
  - web
  - interactive
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:14.320Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Access-Quick-Question-Feature-in-Zaption-Presentation

## Summary

This procedure details navigating to the 'Quick question' interactive tool during a Zaption presentation, exposing the vulnerable input field for question text that lacks proper sanitization.

## Description

The 'Quick question' feature allows presenters to add on-the-fly polls or questions during live sessions, enhancing interactivity. However, the input for question text is directly reflected into the HTML without escaping, creating an XSS entry point. Accessing this feature requires an active presentation session and involves selecting the tool from the interface controls.

## Requirements

1. Active Zaption presentation session as presenter
2. Viewer session for observation (optional but recommended)
3. No additional tools; browser-based interaction only

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs in interactive features with HTML entity encoding
- Implement content security policies to block inline scripts in presentation views
- Log and alert on suspicious input patterns in question fields

## Objectives

1. Reach the editable question input area in the presentation interface
2. Confirm the feature is active and accepting inputs
3. Set up for payload injection targeting the rendering pipeline

## Instructions

### Step 1: Select Quick Question Option

**Context**: From the presenter's controls, activate the interactive question tool.

In the presentation toolbar, click the 'Quick question' button to open the feature.

### Step 2: Open Response Section

**Context**: Access the specific input field where the vulnerable question text is entered.

Within the Quick question interface, expand or click into the response/question text area to make it editable.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[web]]
- [[interactive]]
