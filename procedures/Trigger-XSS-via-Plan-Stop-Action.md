---
tags:
  - xss-trigger
  - execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: e84c92fa-d947-4318-ba0c-3a941fc3b0d6
created_at: '2025-12-13T23:52:50.020Z'
updated_at: '2025-12-13T23:52:50.021Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-Plan-Stop-Action

## Summary

This procedure triggers the stored XSS payload by performing the 'Stop' action on the malicious protection plan, causing the onerror event to execute JavaScript in the current browser context.

## Description

Once the payload is stored, interacting with the plan via the Actions pane renders the unsanitized name, firing the <video> tag's source onerror handler. This executes alert(document.domain) or more malicious code, allowing theft of session cookies, keylogging, or phishing against viewers. The trigger is specific to the 'Stop' confirmation dialog.

## Requirements

1. Created plan with injected XSS payload
2. Authenticated session viewing the plans list
3. Browser developer tools open to observe execution

## Defense

Defensive measures and detection strategies:

- Output encode all stored data when rendering in HTML contexts
- Avoid using user input in event handlers or media elements
- Monitor browser console for unexpected JavaScript errors or alerts

## Objectives

1. Execute arbitrary JavaScript in victim context
2. Demonstrate impact like domain alert or cookie access
3. Highlight exploitation vector for reporting

## Instructions

### Step 1: Select the Malicious Plan

**Context**: Target the plan containing the payload for action.

Return to 'PLANS' > 'Protection', check the box next to the plan with the payload name.

> Plan is highlighted for actions.

### Step 2: Access Actions and Stop

**Context**: Initiate the trigger via UI interaction.

In the right-side Actions pane, click 'Stop'.

> A confirmation dialog appears.

### Step 3: Confirm and Observe Execution

**Context**: Finalize the action to fire the XSS.

Click the red 'Confirm' button.

> The onerror event triggers, executing the JavaScript (e.g., alert pops up showing document.domain).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-execution]]
- [[onerror-trigger]]
