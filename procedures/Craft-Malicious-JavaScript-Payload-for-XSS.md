---
id: proc-uuid-2
tags:
  - xss
  - javascript
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
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:10.458Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-Malicious-JavaScript-Payload-for-XSS

## Summary

This procedure crafts a JavaScript payload to escape string context in the reflected 'language_id' parameter, enabling arbitrary code execution like domain alerts or token theft in the Zomato context.

## Description

Targeting the unsanitized reflection in Zomato's widget, create a payload that closes the JavaScript string with `'}');` and injects code such as `alert(document.domain)` to verify execution. URL-encode to bypass basic filters. In an attack, this could extend to stealing CSRF tokens via `document.querySelector('input[name=csrf]').value`. Prerequisites include knowledge of the reflection point; outcomes include successful JS execution in the victim's session.

## Requirements

1. Text editor for payload creation
2. URL encoder tool (built-in browser or online)
3. Understanding of JS string escaping

## Defense

Defensive measures and detection strategies:

- Use strict input validation and output encoding (e.g., htmlspecialchars in PHP)
- Employ WAF rules to block common XSS payloads and encodings
- Log and alert on URL-encoded anomalies in parameters

## Objectives

1. Break out of the reflected string context
2. Execute proof-of-concept code
3. Prepare for advanced payloads like token exfiltration

## Instructions

### Step 1: Design Raw Payload

**Context**: Analyze the reflection, e.g., if it's `var lang = 'USER_INPUT';`, close with `'}');`.

Raw payload: `'}');alert(document.domain);console.log('`

> This closes the string, executes alert, and reopens for syntax.

### Step 2: URL-Encode Payload

**Context**: Encode to transmit via URL without breaking.

Encoded: `%22%7D%27)%3Balert(document.domain)%3Bconsole.log(%27`

> Use browser console or tool: encodeURIComponent(payload). Test in a non-production endpoint.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[JavaScript]]
