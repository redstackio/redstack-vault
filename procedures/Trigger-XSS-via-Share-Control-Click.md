---
tags:
  - xss
  - stored-xss
  - javascript-execution
  - mapbox
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
updated_at: '2025-12-14T03:16:08.167Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 85b46bfa-05d7-4d0c-b8c5-bf2a65c1e9c0
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-Share-Control-Click

## Summary

This procedure triggers the stored XSS payload by having the victim click the share control on the api.mapbox.com page, causing the L.mapbox.shareControl in mapbox.js to render the unsanitized title in a modal and execute JavaScript.

## Description

The vulnerability lies in mapbox.js where the share control modal inserts the map title without escaping, leading to arbitrary JS execution. The victim clicks the arrow button under the zoom control, opening the modal and firing events like onerror or onload in the payload. Prerequisites: Victim on the share page. Outcomes: Code execution in victim's browser context, enabling data theft or redirects.

## Requirements

1. Victim on the malicious share page
2. Functional mapbox.js loaded
3. Payload designed for modal context (e.g., img onerror)

## Defense

Defensive measures and detection strategies:

- Sanitize all dynamic content in modals and controls
- Add JS event handlers to prevent execution in UI elements
- Detect anomalous JS execution via browser security tools or CSP violations

## Objectives

1. Execute the stored payload in victim context
2. Achieve arbitrary JS for further exploitation
3. Confirm impact like session cookie access

## Instructions

### Step 1: Instruct Victim Interaction

**Context**: Guide to the trigger.

Direct the victim to click the share arrow button below the zoom controls on the map.

### Step 2: Modal Opens and Executes

**Context**: Payload fires on render.

The modal dialog for social sharing loads, inserting the title and triggering the XSS (e.g., alert or confirm popup).

> Execution occurs due to lack of escaping in L.mapbox.shareControl.

### Step 3: Validate Execution

**Context**: Check for success.

Observe if the victim sees a popup or reports unusual behavior; inspect console for alerts.

**Expected Output**: JavaScript executes, e.g., `alert('XSS')` displays.

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
- [[javascript-execution]]
- [[mapbox]]
