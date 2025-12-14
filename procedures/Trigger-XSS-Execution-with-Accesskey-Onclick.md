---
tags:
  - xss
  - javascript-execution
  - accesskey-trigger
  - user-interaction
type: procedure
tools:
  - '[[tools/Firefox-Quantum]]'
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
updated_at: '2025-12-13T23:55:06.125Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 6e1793e7-89b8-4a29-aff9-7fe92028672e
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-Execution-with-Accesskey-Onclick

## Summary

This procedure triggers the injected XSS payload by using platform-specific keyboard shortcuts to activate the accesskey attribute, executing the onclick JavaScript in the victim's browser context.

## Description

Once the payload is reflected, the accesskey='x' allows activation via ALT+SHIFT+X (Windows) or CONTROL+ALT+X (Mac), firing the onclick='confirm`1`' handler. This executes arbitrary JS, such as alerts for proof-of-concept or more malicious actions like keylogging. The attack relies on tricking the victim into pressing the key combo, often via phishing instructions.

## Requirements

1. Loaded 404 page with reflected payload
2. Browser focused on the page (e.g., Firefox)
3. Knowledge of victim's platform for key combo
4. No additional tools beyond browser

## Defense

Defensive measures and detection strategies:

- Disable or restrict accesskey usage in web apps
- Implement strict CSP to prevent onclick handlers
- Educate users on avoiding suspicious interactions on error pages
- Browser-side: Use extensions to block keyboard-triggered scripts

## Objectives

1. Activate accesskey to run onclick
2. Execute JS and observe effects
3. Confirm arbitrary code runs in victim context

## Instructions

### Step 1: Focus on Page

**Context**: Ensure the browser window with the 404 page is active.

No command; click into the page in [[tools/Firefox-Quantum]].

> Page must be in foreground for key events.

### Step 2: Press Key Combination

**Context**: Use OS-specific shortcut to trigger accesskey='x'.

On Windows: Press ALT+SHIFT+X
On Mac: Press CONTROL+ALT+X

> This focuses the link element and fires onclick.

### Step 3: Observe Execution

**Context**: Verify JS runs via dialog or console.

Expected: Confirm dialog with '1' appears.

> Check browser console for errors; success if no blocks and JS executes.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox-Quantum]]

## Tags

- xss
- accesskey-trigger
- user-interaction
