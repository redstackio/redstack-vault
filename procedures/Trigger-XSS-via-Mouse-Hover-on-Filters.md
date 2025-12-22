---
tags:
  - xss-trigger
  - javascript-execution
  - hover-event
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:43.746Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: b2bc623c-33d4-45ad-96db-2a8f27bb314d
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-Mouse-Hover-on-Filters

## Summary

This procedure triggers the reflected XSS payload on the Drugs.com search page by hovering the mouse over interactive elements like 'sort by' or 'amount of results' filters, activating the onpointerover event handler to execute arbitrary JavaScript in the victim's browser context.

## Description

Once the malicious URL is loaded, the reflected payload injects an <x> element with an onpointerover handler. Normal user behavior, such as hovering over search filters to view options, fires the pointerover event, executing the JavaScript. This can lead to cookie theft (e.g., via document.cookie sent to attacker server), redirects, or keylogging. The attack relies on the victim's interaction, making it stealthy. Target environment is any modern browser on the Drugs.com site.

## Requirements

1. Loaded malicious URL from prior procedure
2. Web browser with mouse interaction enabled
3. No additional tools needed

## Defense

Defensive measures and detection strategies:

- Sanitize and escape all reflected inputs, especially in event attributes
- Disable or validate dynamic event handlers
- Implement browser-side protections like XSS auditors or extensions

## Objectives

1. Activate the injected JavaScript through user-like interaction
2. Execute code to collect sensitive data like session cookies
3. Perform unauthorized actions in the victim's session

## Instructions

### Step 1: Load the Vulnerable Page

**Context**: Ensure the crafted URL is open in the browser, displaying search results with the reflected payload.

Navigate to the URL and confirm results are shown (no empty page).

### Step 2: Identify Trigger Elements

**Context**: Locate interactive filters on the page that respond to hover.

Look for 'sort by' dropdown and 'amount of results' selector in the search interface.

### Step 3: Perform Hover Action

**Context**: Simulate user interaction to trigger the onpointerover event.

Move the mouse cursor slowly over the 'sort by' or 'amount of results' elements – the event should fire immediately upon hover.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-trigger]]
- [[javascript-execution]]
