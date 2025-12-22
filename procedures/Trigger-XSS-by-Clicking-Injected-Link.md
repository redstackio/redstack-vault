---
tags:
  - xss
  - trigger
  - javascript
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
impact_level: medium
detection_risk: medium
sub_techniques: []
id: f53b2a2c-140a-480b-943f-7f2dce771112
created_at: '2025-12-14T17:30:07.274Z'
updated_at: '2025-12-14T17:30:07.274Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-by-Clicking-Injected-Link

## Summary

This procedure activates the stored XSS payload by clicking the injected link, executing JavaScript to open a new window to the Shopify admin themes page for further exploitation.

## Description

Once the payload is stored, clicking the link invokes the `attack()` function, which opens a blank-targeted window to `/admin/themes`. This step relies on the DOM-based nature of the XSS, where the javascript: URI scheme executes without additional sanitization. It sets the stage for cross-window communication to manipulate the admin state, ultimately allowing injection of arbitrary content.

## Requirements

1. Stored payload from prior procedure
2. Access to the page displaying the injected link
3. No CSP blocking javascript: URIs or window.open

## Defense

Defensive measures and detection strategies:

- Enforce CSP with 'unsafe-inline' disallowed for script-src
- Log and alert on window.open calls from admin contexts
- User training to avoid clicking suspicious links in admin panels

## Objectives

1. Execute the stored JavaScript payload
2. Open a manipulable admin window
3. Confirm no immediate execution blocks

## Instructions

### Step 1: Navigate to Injected Page

**Context**: Load the admin page where the payload resides to expose the clickable link.

Browse to the stored content location and inspect the DOM to confirm the link presence (e.g., <a href="javascript:attack()">).

> Expected: Link renders without sanitization, visible in page source.

### Step 2: Click to Trigger

**Context**: Interact with the link to run the attack function, opening the new window.

Click the link: `javascript:attack()`. Observe the new tab/window loading `/admin/themes`.

```javascript
// Internally executes: window.open(location.origin + '/admin/themes', '_blank');
```

> Expected: New window opens successfully. Check console for any errors; success if themes page loads.

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
- [[trigger]]
- [[JavaScript]]
