---
id: proc-uuid-4
name: Trigger Double-Click Authorization
tags:
  - clickjacking
  - double-click
  - ui-manipulation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:30:18.742Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Trigger Double-Click Authorization

## Summary

This procedure exploits the victim's double-click gesture on the aligned buttons to close the popup and submit the OAuth form, authorizing the malicious app.

## Description

The attack.html uses CSS to overlay a 'Double Click' button exactly over the 'Connect my WakaTime account' button on the OAuth page. The first click closes the popup tab (via JavaScript), and the second click hits the underlying authorization button, bypassing user intent checks.

## Requirements

1. Victim on OAuth page with popup open
2. Precise button alignment in attack.html
3. No additional tools needed

## Defense

Defensive measures and detection strategies:

- Add gesture detection (e.g., mouse movement validation) to auth buttons
- Disable popups or use same-origin policies
- Implement multi-factor confirmation for OAuth

## Objectives

1. Trick user into form submission
2. Close distracting popup seamlessly
3. Complete authorization without alert

## Instructions

### Step 1: Position for Interaction

**Context**: Ensure the popup is aligned with the OAuth button.

No command; the CSS in attack.html handles positioning: button { position: absolute; top: Xpx; left: Ypx; z-index: 999; } matching the auth button coordinates.

> Victim sees overlaid 'Double Click' button.

### Step 2: Execute Double-Click

**Context**: Victim performs the double-click, triggering closure and submission.

No command; first click runs JavaScript to window.close(); second click submits the form.

> Expected: Popup closes; OAuth redirects with code.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[clickjacking]]
- [[double-click]]
- [[ui-manipulation]]
