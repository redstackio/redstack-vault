---
tags:
  - xss
  - dom-xss
  - postmessage
type: procedure
tools: []
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
updated_at: '2025-12-14T03:47:12.859Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: df914c42-b3cb-4dce-9600-c9c720b03bce
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Observe-XSS-Payload-Execution

## Summary

This procedure verifies the success of the XSS by observing the execution of the injected JavaScript payload in the vulnerable page's context.

## Description

Upon receiving the postMessage, the notes plugin's JavaScript (likely using Marked.js for markdown) parses event.data as JSON without origin validation, then sets notes.innerHTML = parsed.notes. This directly injects the <script> tag, executing alert or other JS, potentially allowing cookie theft or keylogging in the Lyst domain context.

## Requirements

1. Successful postMessage delivery
2. Browser dev tools open for inspection
3. Vulnerable page loaded

## Defense

Defensive measures and detection strategies:

- Avoid innerHTML for user-controlled data; use createTextNode or sanitized insertion
- Enable XSS Auditor or similar browser protections
- Scan JS code for unsafe postMessage patterns

## Objectives

1. Confirm script execution
2. Assess impact (e.g., alert, data exfil)
3. Document for reporting

## Instructions

### Step 1: Monitor the Vulnerable Page Load

**Context**: Watch for the payload processing after navigation.

**Instructions**: With dev tools open (F12), navigate via the POC link and observe the console/network tabs.

> Look for postMessage reception; the handler code resembles: window.addEventListener('message', function(event) { var data = JSON.parse(event.data); notes.innerHTML = data.notes; })

### Step 2: Validate Execution

**Context**: Check for the injected script's effect.

**Instructions**: Observe the alert dialog popping up on the notes page.

> If successful, 'XSS via postMessage' alert appears; inspect DOM to see <script> inserted into notes element.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- payload-execution
- javascript
