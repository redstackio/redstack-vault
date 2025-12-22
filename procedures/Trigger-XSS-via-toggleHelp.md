---
id: proc-uuid-3
tags:
  - xss
  - dom-xss
  - postmessage
  - help-modal
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/toggleHelp-iframe]]'
  - '[[commands/toggleHelp-window]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:20.208Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-toggleHelp

## Summary

This procedure triggers the XSS by calling toggleHelp via postMessage, rendering the help modal's HTML table with the injected unescaped payload, executing arbitrary JavaScript.

## Description

The showHelp method in reveal.js concatenates key binding descriptions directly into an HTML table without escaping. Invoking toggleHelp displays this modal, processing the malicious img tag and firing the onerror event for code execution.

## Requirements

1. Malicious key binding injected from previous procedure
2. Access to frame or win object
3. Victim viewing the presentation

## Defense

Defensive measures and detection strategies:

- Escape HTML in showHelp (e.g., use textContent or DOMPurify)
- Restrict postMessage to trusted origins
- Monitor for unexpected alerts or JS execution in browser console

## Objectives

1. Render the injected payload as HTML
2. Execute XSS for arbitrary JS in victim context
3. Demonstrate impact like account access

## Instructions

### Step 1: Iframe Trigger

**Context**: Send postMessage to toggleHelp, opening the modal and executing XSS.

**Command** ([[commands/toggleHelp-iframe]]):
```javascript
frame.postMessage('{"method":"toggleHelp"}','*');
```

> Calls toggleHelp on Reveal. Expected output: Help modal opens, alert(document.domain) fires.

### Step 2: Window Trigger

**Context**: For window.open setup.

**Command** ([[commands/toggleHelp-window]]):
```javascript
win.postMessage('{"method":"toggleHelp"}','*');
```

> Triggers in window. Expected output: Alert in new window context.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/toggleHelp-iframe]]
- [[commands/toggleHelp-window]]

## Tools Used


## Tags

- xss
- execution
- trigger
