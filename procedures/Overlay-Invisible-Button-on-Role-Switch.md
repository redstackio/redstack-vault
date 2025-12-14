---
id: proc-overlay-button-001
tags:
  - clickjacking
  - overlay
  - invisible-ui
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:28:04.771Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Overlay-Invisible-Button-on-Role-Switch

## Summary

This procedure modifies the iframe setup to make it invisible and overlays a transparent button precisely over the role-switching element in the target application, enabling click hijacking without user awareness.

## Description

Building on the embedded iframe, apply CSS to set opacity to 0, rendering the frame invisible. Then, add an absolutely positioned button with matching opacity and z-index to cover the specific UI element (e.g., role dropdown in Respondly). Coordinates are determined via browser inspection tools. This tricks clicks into interacting with the hidden app.

## Requirements

1. Access to the HTML file from previous step
2. Browser dev tools to identify element positions (e.g., role switch at ~200px top, 300px left)
3. Understanding of CSS positioning

## Defense

Defensive measures and detection strategies:

- Enforce strict CSP to prevent inline styles/scripts that could hide elements
- Client-side detection of opacity:0 iframes or unusual overlays
- Educate users on phishing and unexpected clicks

## Objectives

1. Render the iframe completely invisible
2. Position overlay button accurately over target UI element
3. Ensure clicks propagate to the hidden element

## Instructions

### Step 1: Apply Invisibility Styles

**Context**: Hide the iframe while keeping it functional.

Update the iframe tag:

```html
<iframe id="target" src="https://app.respond.ly" width="100%" height="100%" style="opacity:0; border:none; position:absolute; top:0; left:0;"></iframe>
```

> Expected: Frame loads but screen appears blank.

### Step 2: Add Overlay Button

**Context**: Position a clickable element over the role switch.

Add to body:

```html
<button id="fake" style="position:absolute; top:200px; left:300px; width:100px; height:30px; opacity:0; z-index:1;" onclick="changeRole()">Click Me (Invisible)</button>
```

> Adjust top/left via dev tools inspection. Expected: Button invisible but clickable; test by making opacity 1 temporarily.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[clickjacking]]
- [[overlay]]
