---
tags:
  - cookie-injection
  - javascript
type: procedure
tools:
  - '[[tools/Browser-DevTools]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/set-malicious-cookie]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:23:53.860Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 42f0a376-6aa7-4b3e-b881-543d0eff03e8
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Cookie-via-DevTools

## Summary

This procedure injects a malicious cookie payload into the browser using DevTools, exploiting the lack of single-quote escaping in the Burp extension's cookie handling to enable code injection in generated Node.js code.

## Description

By setting a cookie value like 'test=\/require(\'child_process\').exec(\'calc.exe\')//', the payload escapes the single-quoted string in the extension's output (BurpExtender.java lines 123-125), injecting arbitrary Node.js code such as spawning a child process. This targets developers who copy and execute Burp-generated code.

## Requirements

1. Web browser with DevTools (e.g., Chrome)
2. Target website accessible
3. Basic JavaScript knowledge

## Defense

Defensive measures and detection strategies:

- Sanitize inputs in browser extensions and tools
- Avoid executing untrusted generated code
- Use cookie security flags like HttpOnly and Secure

## Objectives

1. Set cookie with breakout payload
2. Ensure payload survives in HTTP headers
3. Prepare for request interception

## Instructions

### Step 1: Open DevTools

**Context**: Access the browser's developer console to execute JavaScript.

**Instructions**: Right-click on the page, select Inspect, and switch to Console tab.

### Step 2: Execute Cookie Injection

**Context**: Run the command to set the malicious cookie.

**Command** ([[commands/set-malicious-cookie]]):
```javascript
document.cookie = "test='/require('child_process').exec('calc.exe')//"
```

> This sets the cookie with escaped single quotes to break out of the string literal in Node.js code. Verify with `document.cookie` in console; expected output shows the full payload string.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/set-malicious-cookie]]

## Tools Used

- [[tools/Browser-DevTools]]

## Tags

- cookie-injection
- javascript
