---
tags:
  - xss
  - stored-xss
  - trigger
  - accesskey
  - javascript
  - wordpress
  - buddypress
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: f084274a-0e89-4fe9-84e1-066e90dfa441
created_at: '2025-12-13T23:56:03.779Z'
updated_at: '2025-12-13T23:56:03.779Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-Payload-Using-Accesskey-Keyboard-Shortcut

## Summary

This procedure activates the stored XSS payload on the BuddyPress group page using platform-specific keyboard shortcuts tied to the accesskey attribute, resulting in JavaScript execution.

## Description

The injected anchor tag uses the HTML accesskey attribute ('x') to bind to keyboard events. On the rendered group page, pressing the appropriate modifier keys plus 'X' focuses the element and invokes the onclick handler, executing `alert(document.domain)`. This runs in the site's origin context, allowing theft of cookies, localStorage, or DOM manipulation. Cross-platform differences (macOS vs. Windows) require adaptation, but execution confirms the vuln and enables escalation to RCE via further JS payloads.

## Requirements

1. Loaded group page with rendered payload
2. Web browser supporting accesskeys (most modern browsers)
3. Knowledge of OS-specific shortcuts (macOS: Shift+Ctrl+Option+X; Windows: Shift+Alt+X)

## Defense

Defensive measures and detection strategies:

- Strip or encode accesskey and event attributes in user-generated content
- Disable accesskeys site-wide via CSS (e.g., `a[accesskey] { outline: none; }`)
- Monitor browser consoles and JS errors for unexpected alerts
- Educate users on avoiding suspicious group pages and enable XSS auditors in browsers

## Objectives

1. Execute arbitrary JavaScript in the victim's browser session
2. Demonstrate impact like domain alerting or data exfiltration
3. Pave way for advanced payloads (e.g., keyloggers or beaconing)

## Instructions

### Step 1: Load Vulnerable Page

**Context**: Ensure the group page is open and focused in the browser.

Navigate to the group URL and wait for full load.

> Verify the malicious link is present via inspection.

### Step 2: Press Accesskey Combination

**Context**: Use the OS-specific shortcut to activate the accesskey and trigger onclick.

On macOS: Hold Shift + Control + Option, then press X. On Windows: Hold Shift + Alt, then press X.

> The browser should focus the anchor (possible outline or cursor change) and execute the JS.

### Step 3: Observe Execution

**Context**: Confirm JS runs and assess impact.

Look for the alert dialog showing the document domain. Check console for errors or further logs.

> Success if alert appears; replace alert() with exfil payload for real attacks.

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
- [[stored-xss]]
- [[accesskey]]
- [[JavaScript]]
- [[wordpress]]
- [[buddypress]]
