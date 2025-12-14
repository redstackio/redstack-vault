---
id: proc-execute-call
tags:
  - xss
  - dom
  - externalinterface
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:53.892Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Execute-ExternalInterface-Call-for-DOM-Click

## Summary

Use the SWF's ExternalInterface to invoke a click() method on the plugin install button via DOM traversal from the opener window.

## Description

The _fireEvent method in plupload.flash.swf processes the injected flashVars, executing ExternalInterface.call with the target payload to traverse and click the specific DOM element, bypassing same-origin restrictions during loading.

## Requirements

1. SWF loaded with payload
2. Admin page loaded
3. Flash enabled

## Defense

Defensive measures and detection strategies:

- Patch WordPress to 4.6+ (removes vulnerable SWF)
- Monitor for anomalous Flash calls
- Content Security Policy

## Objectives

1. Traverse DOM to install button
2. Simulate user click
3. Initiate installation

## Instructions

### Step 1: Process Payload in SWF

**Context**: SWF's Utils.sanitize fails on encoded '%#target%g=', allowing injection.

**Command** (Flash Internal; observed):
```actionscript
// In _fireEvent: ExternalInterface.call(target, ...)
```

> Callback executes. Expected output: JS method invoked.

### Step 2: Perform DOM Traversal and Click

**Context**: Use opener reference for traversal.

**Command** (Injected JS):
```javascript
opener.document.body.firstElementChild.nextElementSibling.nextElementSibling.nextElementSibling.firstElementChild.click();
```

> Button clicked. Expected output: Install dialog or download starts.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[dom]]
