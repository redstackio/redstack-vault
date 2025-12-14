---
tags:
  - xss
  - modal-trigger
type: procedure
tools:
  - '[[tools/H1-Triage-Wizard-Chrome-Extension]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Chrome Browser Extension
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T00:11:09.487Z'
sub_techniques: []
id: 9cf154af-6ff0-43e7-a9e1-4985f5db3ccd
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Triage-Questionnaire-Modal

## Summary

This procedure activates the triage questionnaire modal in the H1 Triage Wizard extension, interpolating stored user responses into an HTML template without sanitization, enabling XSS.

## Description

Right-clicking on the report page and selecting 'View Triage Questionnaire (Beta)' invokes the extension's buildTriageQuestionnaireModal function, which uses .replace() to insert questionnaireResponses directly into HTML, allowing malicious payloads to render and execute in the browser.

## Requirements

1. Enabled H1 Triage Wizard extension
2. Loaded vulnerable report page
3. User interaction capability (mouse/keyboard)

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs before HTML interpolation
- Employ DOMPurify or similar libraries for escaping
- Monitor for anomalous modal popups in browser extensions

## Objectives

1. Load the unsanitized modal to expose the injection point
2. Interpolate controlled responses for payload delivery
3. Achieve execution in the extension's browser context

## Instructions

### Step 1: Right-Click on Report

**Context**: Use the extension's context menu to initiate the modal.

Position the cursor on the report content, right-click, and select 'View Triage Questionnaire (Beta)' from the menu.

> The modal should open, pulling in stored responses.

### Step 2: Confirm Modal Rendering

**Context**: Observe the modal's HTML structure for injection readiness.

Inspect the modal element in browser dev tools (F12) to see questionnaireResponses being inserted.

> Success: Modal displays with potential for HTML rendering.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/H1-Triage-Wizard-Chrome-Extension]]

## Tags

- xss-trigger
- html-interpolation
