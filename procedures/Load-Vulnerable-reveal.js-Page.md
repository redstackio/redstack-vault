---
id: proc-uuid-1
tags:
  - xss
  - postmessage
  - reveal.js
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/embed-revealjs-iframe]]'
  - '[[commands/open-revealjs-window]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T03:16:20.217Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Load-Vulnerable-reveal.js-Page

## Summary

This procedure loads the vulnerable reveal.js 3.8.0 presentation in an iframe or new window, providing a target for subsequent postMessage attacks to exploit the DOM-based XSS.

## Description

The reveal.js library in version 3.8.0 includes a postMessage listener in setupPostMessage that accepts messages from any origin without validation. By loading the page in a controllable context like an iframe, an attacker can target it for method invocation. This step ensures the Reveal object is initialized and accessible.

## Requirements

1. Web browser with JavaScript enabled
2. Access to a page where iframes or window.open are permitted
3. URL of vulnerable reveal.js instance (e.g., https://revealjs.com)

## Defense

Defensive measures and detection strategies:

- Disable iframe embedding via CSP headers (frame-ancestors)
- Monitor for unexpected window.open or iframe loads in client-side logs

## Objectives

1. Establish a target context for cross-origin postMessage
2. Verify Reveal object availability
3. Prepare for payload injection

## Instructions

### Step 1: Embed via Iframe

**Context**: Create an iframe to load the vulnerable page, using onload to confirm readiness.

**Command** ([[commands/embed-revealjs-iframe]]):
```html
<iframe id="frame" src="https://revealjs.com" onload="setTimeout(() => console.log('Loaded'), 1000)"></iframe>
```

> This embeds the page and waits for load. Expected output: Console log confirming load.

### Step 2: Alternative Window Open

**Context**: Open in a new window if iframes are blocked.

**Command** ([[commands/open-revealjs-window]]):
```javascript
let win = window.open('https://revealjs.com', '_blank'); setTimeout(() => console.log('Window ready'), 2000);
```

> Opens the page in a new tab/window. Expected output: New window loads reveal.js.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used

- [[commands/embed-revealjs-iframe]]
- [[commands/open-revealjs-window]]

## Tools Used


## Tags

- xss
- postmessage
- web
