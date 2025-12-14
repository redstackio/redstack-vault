---
id: proc-craft-xss-payload-rocket-chat
tags:
  - xss
  - payload-crafting
  - markdown
  - autolinker
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
updated_at: '2025-12-13T23:52:38.764Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
---

# Craft-Malicious-XSS-Payload-for-Rocket-Chat

## Summary

This procedure crafts a specialized XSS payload that exploits the combination of Markdown inline code parsing and AutoLinker URL handling in Rocket.Chat to break out of HTML attributes and inject executable JavaScript, enabling stored XSS attacks.

## Description

In Rocket.Chat, messages are processed server-side using a Markdown parser followed by AutoLinker for URL detection. By nesting malformed URL structures within inline code blocks, attackers can manipulate the parsing order to inject attributes like onanimationiteration into generated <a> tags. This allows arbitrary JavaScript execution when a victim views the message. The payload targets the browser's animation event handlers or prototype pollution via instanceof to eval malicious code, potentially loading external scripts.

## Requirements

1. Access to a text editor or browser console for payload construction
2. Basic knowledge of HTML attribute injection and JavaScript event handlers
3. Target Rocket.Chat version vulnerable to this parser interaction (pre-patch for CVE or similar)

## Defense

Defensive measures and detection strategies:

- Implement strict HTML sanitization using libraries like DOMPurify before rendering
- Validate and escape URLs with new URL() constructor to prevent malformed inputs
- Monitor for anomalous animation or event attributes in parsed HTML

## Objectives

1. Generate a payload that survives server-side parsing without sanitization
2. Ensure breakout from attribute context to script execution
3. Prepare for external script loading to extend capabilities

## Instructions

### Step 1: Understand Parser Interaction

**Context**: Analyze how Markdown treats inline code (`[ ]`) and how AutoLinker wraps URLs in <a> tags, creating opportunities for attribute injection.

No command required; review documentation on Markdown and AutoLinker.

> Expected: Insight into nesting malformed URLs inside code blocks to confuse parsers.

### Step 2: Construct Base Payload

**Context**: Build the core structure using a URL prefix followed by nested code and attribute injections.

Use this template in a text editor:

```text
https://a?p=[ ](https:// style=animation-duration:1s;animation-name:blink;animation-iteration-count:2 onanimationiteration=Array.prototype[Symbol.hasInstance]=eval,'alert\x28\x27XSS\x27\x29;'instanceof[] target=_blank data-x=`.)`
```

> Explanation: The outer URL triggers AutoLinker, while the inner code block allows attribute smuggling. Escaped characters like \x28 prevent premature parsing.

### Step 3: Test Payload Parsing

**Context**: Simulate parsing in a local environment or inspect network requests to verify malformed HTML output.

Paste into a Markdown renderer and inspect the HTML.

**Expected Output**: <a> tag with injected onanimationiteration="...eval('alert\x28\x27XSS\x27\x29;')..."

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
- [[payload-crafting]]

