---
tags:
  - xss
  - reflected-xss
  - flash
  - swf
type: procedure
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:20.856Z'
sub_techniques: []
id: 23278f9f-1f55-447c-b797-87cacbdcc970
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-SWF-Parameter

## Summary

This procedure navigates to a vulnerable Flash SWF URL with an injected JavaScript payload in the 'playerready' parameter, triggering reflected XSS execution.

## Description

The JW Player SWF file at http://www.grouplogic.com/jwplayer/player.swf lacks sanitization for the 'playerready' parameter, allowing direct JavaScript injection. By appending a payload like 'alert(document.domain)', the SWF executes it upon loading in the browser. This targets web environments with Flash enabled, leading to arbitrary code execution in the site's domain context. Prerequisites include browser access; outcomes confirm vulnerability exploitation.

## Requirements

1. Open browser session (e.g., Firefox with Flash)
2. HTTP access to www.grouplogic.com
3. Knowledge of the vulnerable parameter ('playerready')

## Defense

Defensive measures and detection strategies:

- Sanitize or validate SWF parameters server-side
- Deprecate Flash usage and migrate to HTML5
- Implement Content Security Policy (CSP) to block inline scripts
- Log and monitor unusual URL parameter patterns

## Objectives

1. Inject and deliver the XSS payload via URL
2. Load the SWF to process the unsanitized input
3. Achieve JavaScript execution in the victim browser

## Instructions

### Step 1: Construct and Navigate to Malicious URL

**Context**: Build the URL with the payload and access it to exploit the reflection.

Enter the following URL in the browser address bar:

`http://www.grouplogic.com/jwplayer/player.swf?playerready=alert(document.domain)`

> This URL loads the SWF and passes the JavaScript to 'playerready', which executes on render. Successful load indicates the payload is processed.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- [[xss]]
- [[reflected-xss]]
- [[flash]]
