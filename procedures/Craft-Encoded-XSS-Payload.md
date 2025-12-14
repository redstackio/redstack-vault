---
tags:
  - xss
  - payload-crafting
type: procedure
tools:
  - '[[tools/Python-Char-Code-Converter]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/encoded-xss-variable-alert]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 2abb98ce-6b0c-42c5-8dcd-47eeeb131127
created_at: '2025-12-14T00:11:16.597Z'
updated_at: '2025-12-14T00:11:16.597Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft Encoded XSS Payload

## Summary

This procedure converts JavaScript code into char code arrays to create XSS payloads that bypass space and quote restrictions in iframe src attributes.

## Description

Using a Python script, JS is encoded into numerical char codes and wrapped in eval(String.fromCharCode()) for execution, enabling complex payloads for actions like profile edits or role changes.

## Requirements

1. Python environment
2. JavaScript code to encode
3. Knowledge of target site's JS structure (e.g., jQuery usage)

## Defense

Defensive measures and detection strategies:

- Filter eval and fromCharCode in inputs
- Strict CSP to block inline JS

## Objectives

1. Create obfuscated payload
2. Ensure execution despite restrictions
3. Prepare for specific exploits like username change

## Instructions

### Step 1: Prepare JS Code

**Context**: Write the desired JavaScript.

For example, a simple variable alert: let test = 123; alert(test);

> Defines the code to encode.

### Step 2: Convert to Char Codes

**Context**: Use tool to encode.

Run [[tools/Python-Char-Code-Converter]] on the JS code to get the array.

> Outputs numerical array.

### Step 3: Embed in Iframe

**Context**: Form the full payload.

Wrap in eval and iframe like [[commands/encoded-xss-variable-alert]]:

```html
<iframe src=javascript:eval(String.fromCharCode.apply(null,[108,101,116,32,116,101,115,116,32,61,32,49,50,51,59,10,97,108,101,114,116,40,116,101,115,116,41,59])) width=0 height=0 style=display:none;></iframe>
```

> Ready for insertion.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used

- [[commands/encoded-xss-variable-alert]]

## Tools Used

- [[tools/Python-Char-Code-Converter]]

## Tags

- xss
- encoding
