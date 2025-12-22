---
id: proc-uuid-004
name: Bypass-Fix-with-Alternative-SVG-Payload
type: procedure
verified: false
submitted: true
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T03:47:18.354Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - bypass
  - svg-payload
  - uri-scheme
platforms:
  - Web
tools:
  - '[[tools/DOMPurify]]'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Bypass-Fix-with-Alternative-SVG-Payload

## Summary

This procedure tests a bypass of Simplenote's initial XSS fix by using an alternative SVG payload with case-varied 'javaScriPt:' scheme and %0a line break to evade URI sanitization, re-enabling stored XSS.

## Description

After an initial patch targeting javascript: URIs, this bypass uses mixed case and URL-encoded newline in the from attribute to trick the filter. Adapted from DOMPurify references, it follows the same injection and execution flow but with the updated payload. Outcomes: Confirms vulnerability persistence post-fix, allowing continued exploitation.

## Requirements

1. Knowledge of the initial fix (URI scheme blocking)
2. Access to create and publish notes
3. DOMPurify for payload validation

## Defense

Defensive measures and detection strategies:

- Normalize URI schemes to lowercase and block variations like javaScriPt:
- Decode and inspect URL-encoded characters in attributes
- Regularly test sanitizers against known bypasses from DOMPurify

## Objectives

1. Evade updated sanitization rules
2. Restore XSS execution capability
3. Demonstrate incomplete fix efficacy

## Instructions

### Step 1: Craft Bypass Payload

**Context**: Modify the original payload to include case variation and encoded newline.

Use this updated payload:

```html
<div id="137"><svg><a xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="?"><circle r="400"></circle><animate attributeName="xlink:href" begin="0" from="javaScriPt://www.simplenote.com/test%0aalert(document.domain)" to="&" /></a>//\\["'\\`-->\\]]></div>
```

> Payload ready for injection; test locally if possible.

### Step 2: Inject, Publish, and Execute

**Context**: Repeat prior procedures with the new payload to trigger the bypass.

Follow creation, injection, publish, access, and click steps using the new payload.

> Alert executes via the bypassed URI, confirming success.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/DOMPurify]]

## Tags

- [[bypass]]
- [[svg-payload]]
- [[uri-scheme]]
