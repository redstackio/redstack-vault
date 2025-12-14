---
tags:
  - xss-execution
  - javascript-trigger
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
updated_at: '2025-12-13T23:52:49.872Z'
sub_techniques: []
id: 0d88725a-3fba-4f08-8798-b8b3b2054c5d
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger Reflected XSS Payload

## Summary

This procedure activates the reflected XSS payload through user interaction, confirming arbitrary JavaScript execution in the browser context.

## Description

After reflection, interacting with the payload (e.g., right-clicking) fires events like `onauxclick`, executing code such as `confirm(document.domain)`. This demonstrates impacts like data exfiltration or session hijacking. The scenario targets the Messages section; prerequisites are a reflected payload. Outcomes include proof-of-concept execution via popup.

## Requirements

1. Reflected payload visible on the page
2. Browser supporting JavaScript events
3. Victim-like interaction simulation

## Defense

Defensive measures and detection strategies:

- Strip or escape event handlers in reflected content
- Monitor for anomalous JavaScript execution via browser logs
- Use strict CSP to prevent event-based script execution

## Objectives

1. Execute the injected JavaScript
2. Demonstrate control over the victim's browser
3. Highlight potential for further exploitation

## Instructions

### Step 1: Interact with Reflected Content

**Context**: Perform an action on the reflected payload to trigger the event handler.

No specific command; manual interaction.

> Right-click on the reflected text "RIGHT CLICK HERE". A confirmation popup should appear displaying the document domain (e.g., www.mtn.bj), confirming XSS execution.

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

- [[xss-execution]]
- [[javascript-trigger]]
