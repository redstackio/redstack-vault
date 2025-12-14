---
id: proc-uuid-2
tags:
  - xss
  - javascript-injection
  - map-attribution
type: procedure
tools:
  - '[[tools/Mapbox-Studio-Classic]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:30.270Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
---

# Inject-XSS-into-Map-Attribution

## Summary

This procedure embeds a JavaScript-based XSS payload into the attribution field of a custom Mapbox style, exploiting the lack of sanitization to enable persistent execution on Mapbox.com and integrated sites.

## Description

The vulnerability stems from unsanitized user input in the TileJSON attribution property, allowing HTML/JS injection that renders in the map control. In the attack, a simple onerror handler steals cookies. The target is the Mapbox style editor, with outcomes including arbitrary JS execution in victims' browsers. Requires an open style project in Mapbox Studio Classic.

## Requirements

1. Active Mapbox Studio Classic session with a new style project
2. Knowledge of basic XSS payloads
3. No network restrictions for local editing

## Defense

Defensive measures and detection strategies:

- Implement HTML/JS sanitization in attribution fields (e.g., using DOMPurify)
- Validate TileJSON sources before integration in Mapbox.js
- Browser CSP to block inline scripts from untrusted origins

## Objectives

1. Insert payload without breaking style syntax
2. Ensure payload persists in TileJSON output
3. Test local execution if possible

## Instructions

### Step 1: Access Attribution Field

**Context**: Locate the control for map attribution in the style editor.

In Mapbox Studio Classic, open the 'Style' properties panel and find the 'Attribution' section under metadata or components.

> Expected output: Editable text field for attribution content.

### Step 2: Insert Payload

**Context**: Enter the XSS payload to close tags and trigger JS on load.

Type the following into the attribution field: `'><img src=x onerror=alert(document.cookie)>`. This breaks out of any surrounding HTML and executes on render.

> Expected output: Field accepts input; preview may show altered attribution text.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Mapbox-Studio-Classic]]

## Tags

- [[xss]]
- [[javascript-injection]]

