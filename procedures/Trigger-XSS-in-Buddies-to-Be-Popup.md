---
tags:
  - xss-trigger
  - popup-execution
  - session-hijack
type: procedure
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
updated_at: '2025-12-14T03:46:37.281Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: bee3c1f7-a0e2-401c-a0e3-9b2158d4be38
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-in-Buddies-to-Be-Popup

## Summary

This procedure covers navigating to the Buddies-to-Be tab in lemlist and interacting with contact elements to trigger a popup that renders the stored XSS payload from the Campaign Name, resulting in JavaScript execution.

## Description

After payload injection, the unsanitized Campaign Name is displayed in popups within the Buddies-to-Be section, which handles contact lists and additions. Clicking specific buttons or lists causes the application to fetch and render the campaign data without escaping, executing the SVG onload handler. This leads to arbitrary code execution in the authenticated user's browser, enabling theft of session cookies (e.g., via fetch to an attacker server) or other DOM manipulations. The procedure assumes the payload is already stored.

## Requirements

1. Stored campaign with injected payload
2. Active session in the same account or victim access
3. Browser console open for monitoring execution

## Defense

Defensive measures and detection strategies:

- Escape HTML in all dynamic content rendering, especially popups
- Implement output encoding for user-generated content in UI components
- Detect JavaScript alerts or errors in browser logs for anomalous behavior

## Objectives

1. Render the vulnerable popup to execute the payload
2. Verify JavaScript execution through observable effects
3. Demonstrate potential for data exfiltration or hijacking

## Instructions

### Step 1: Navigate to Buddies-to-Be

**Context**: Access the tab where the popup is triggered.

From the dashboard, select the 'Buddies-to-Be' tab.

> The section loads, showing contact management options.

### Step 2: Interact to Open Popup

**Context**: Force rendering of the campaign name in a popup.

Click 'Add one' in the top right or select a contact list.

> A popup opens, displaying the unsanitized campaign name.

### Step 3: Observe Execution

**Context**: Confirm the payload runs.

Watch for the confirm dialog popping up with the document domain.

> Success is indicated by the alert; in a real attack, replace confirm with code to exfiltrate document.cookie to an attacker-controlled endpoint.

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
- [[Execution]]
- [[web]]
