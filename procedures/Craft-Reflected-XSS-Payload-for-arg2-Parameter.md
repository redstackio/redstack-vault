---
id: proc-uuid-2
tags:
  - xss
  - payload-crafting
  - javascript
type: procedure
tools: []
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:42.470Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft Reflected XSS Payload for arg2 Parameter

## Summary

This procedure crafts a JavaScript payload tailored for injection into the 'arg2' parameter of a PHP endpoint, encoding it to evade basic filters and ensure execution upon reflection.

## Description

The attack targets the unsanitized 'arg2' in POST requests, often appearing in JSON-like arrays in the response. Payloads must handle encoding (e.g., URL or JSON) and use event handlers like onerror for reliability. In this case, the payload <img src=a onerror=alert(1)> is embedded in a encoded string array to simulate legitimate input. Prerequisites include knowledge of the reflection context from prior reconnaissance. Outcomes: Reliable JS execution confirming self-XSS, ready for CSRF chaining.

## Requirements

1. Understanding of the endpoint's input handling (e.g., JSON array reflection).
2. Text editor for payload testing.
3. Browser for validation.

## Defense

Defensive measures and detection strategies:

- Sanitize all reflected inputs using htmlspecialchars() in PHP.
- Validate input types and lengths for parameters like 'arg2'.
- Monitor for suspicious encodings in logs.

## Objectives

1. Create an executable JS snippet for the reflection point.
2. Encode to bypass filters.
3. Test for successful alert or console execution.

## Instructions

### Step 1: Design Basic Payload

**Context**: Select a simple, reliable XSS vector that works in reflected contexts without onload dependencies.

Use <img src=a onerror=alert(1)> as it triggers on non-existent image load.

**Expected Output**: Raw payload string ready for encoding.

### Step 2: Encode for Parameter

**Context**: Wrap and encode the payload to match the endpoint's expected format, e.g., as a JSON array element.

Encode as ["_d_","raygame2222%40af.miljvbi9<img src=a onerror=alert(1)>lk2ko"], where %40 is @ and the img tag is embedded post-decoding.

**Expected Output**: Encoded string that decodes to include the executable tag.

### Step 3: Test Payload

**Context**: Submit via POST to verify reflection and execution.

Use browser dev tools or a tool like curl to POST arg2=encoded_payload and check for alert.

**Expected Output**: Alert(1) fires upon response rendering.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[JavaScript]]
