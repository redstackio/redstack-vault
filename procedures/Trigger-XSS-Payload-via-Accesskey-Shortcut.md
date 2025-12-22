---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - xss
  - javascript-execution
  - accesskey
type: procedure
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:49.586Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-Payload-via-Accesskey-Shortcut

## Summary

This procedure activates a pre-injected XSS payload on a reflected 404 page by using browser accesskey shortcuts, executing JavaScript like confirm(1) to demonstrate control over the victim's browser for information theft or unauthorized actions.

## Description

After WAF bypass, the payload sets an accesskey='x' and onclick event on a reflected element. Browsers like Firefox support accesskeys via keyboard shortcuts (e.g., ALT+SHIFT+X on Windows), triggering the JS without further interaction. This executes in the site's context, affecting multiple Starbucks domains and bypassing client-side protections. Expected outcomes include arbitrary JS for cookie theft or form submissions on behalf of victims.

## Requirements

1. Loaded 404 page with reflected payload (from prior bypass).
2. Browser supporting accesskeys (Firefox 69.0.3).
3. Knowledge of OS-specific shortcuts (Mac: CONTROL+ALT+X; Windows: ALT+SHIFT+X).

## Defense

Defensive measures and detection strategies:

- Sanitize all URL parameters before reflection on error pages.
- Disable or filter accesskey and onclick attributes in responses.
- Log and alert on unusual JS execution or shortcut-triggered events in web apps.

## Objectives

1. Execute injected JavaScript in victim context.
2. Demonstrate payload viability for data collection.
3. Enable escalation to account takeover or exfiltration.

## Instructions

### Step 1: Focus on the Reflected Page

**Context**: Ensure the 404 page is active and the payload is reflected, setting up the accesskey.

No command; simply keep the page loaded in the browser.

> Verify via page inspection: Look for accesskey='x' in the reflected HTML.

### Step 2: Press Accesskey Shortcut

**Context**: Use the browser's built-in shortcut to activate the accesskey, firing the onclick event.

Keyboard input:

```bash
# On Mac: Press CONTROL+ALT+X
# On Windows: Press ALT+SHIFT+X
```

> This triggers confirm(1), popping a dialog. Success confirms XSS; replace with alert(document.cookie) for theft proof.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- [[xss]]
- [[JavaScript]]
- [[web]]
