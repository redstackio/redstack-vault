---
id: proc-uuid-003
tags:
  - xss
  - trigger
  - accesskey
  - javascript-execution
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
updated_at: '2025-12-13T23:52:34.245Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-Accesskey-Key-Combination

## Summary

This procedure activates the injected XSS payload by pressing the browser-specific key combination, executing arbitrary JavaScript in the victim's session and enabling actions like session hijacking or data theft.

## Description

Following payload injection, the accesskey='X' attribute binds to a platform-specific shortcut in Firefox, firing the onclick handler when pressed. On Windows/Linux, use ALT+SHIFT+X; on macOS, CTRL+ALT+X. This requires social engineering to prompt the key press (e.g., fake instructions). The outcome is immediate JS execution in the page context, with potential for stealing cookies or tokens. The attack is limited to Firefox and user interaction.

## Requirements

1. Payload already injected and page loaded in Firefox
2. Knowledge of victim's OS for correct key combo
3. Social engineering to induce key press

## Defense

Defensive measures and detection strategies:

- Disable or filter accesskey attributes server-side
- Train users against pressing unsolicited key combinations
- Monitor client-side JS execution via browser logs or endpoint detection

## Objectives

1. Execute injected JavaScript code
2. Achieve client-side compromise (e.g., alert, data exfil)
3. Demonstrate impact like session theft

## Instructions

### Step 1: Identify Key Combination

**Context**: Determine the correct shortcut based on the victim's operating system to ensure activation.

- Windows/Linux: ALT + SHIFT + X
- macOS: CTRL + ALT + X

> Review OS via reconnaissance if possible. Expected output: Selected combo.

### Step 2: Press Key Combination

**Context**: With focus on the page, press the keys to trigger the accesskey and onclick.

Press the identified combination while the login page is active.

> This focuses the element and runs confirm('H4CK3D BY PRAKHAR0X01'). Expected output: Dialog box appears, confirming execution. For real attacks, replace with document.cookie exfil.

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

- [[xss]]
- [[trigger]]
- [[accesskey]]
- [[javascript-execution]]
