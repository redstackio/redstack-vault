---
tags:
  - xss
  - dom-xss
  - recon
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 6a399c63-587e-440e-972d-f6f74bc20287
created_at: '2025-12-14T03:15:31.121Z'
updated_at: '2025-12-14T03:15:31.121Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-Vulnerable-Search-Parameter-for-DOM-XSS

## Summary

This procedure involves testing the search function of a web application, such as gm.com, to identify if GET parameters are non-encoded, allowing DOM-based XSS injection specifically in browsers like Internet Explorer.

## Description

In vulnerable web apps, search parameters passed via GET requests may be reflected into the DOM without proper HTML or JavaScript encoding. This procedure targets such flaws by manually testing parameter reflection. For gm.com, the search input accepts unsanitized data, leading to direct DOM manipulation in IE. Prerequisites include access to the target site and a vulnerable browser version. Expected outcomes: confirmation of injection points for further exploitation.

## Requirements

1. Public access to the target website (e.g., gm.com).
2. Internet Explorer browser for testing.
3. Browser developer tools enabled.

## Defense

Defensive measures and detection strategies:

- Implement output encoding for all user inputs reflected in DOM (e.g., use innerText instead of innerHTML).
- Deploy Content Security Policy (CSP) to restrict script execution.
- Monitor for anomalous search queries in server logs.

## Objectives

1. Confirm non-encoded GET parameter reflection.
2. Identify browser-specific vulnerabilities (e.g., IE).
3. Map injection points in the DOM.

## Instructions

### Step 1: Test Basic Parameter Reflection

**Context**: Append a simple test payload to the search URL to check for direct reflection without encoding.

Navigate to https://www.gm.com/search?search=<script>alert(1)</script> in Internet Explorer. Open developer tools (F12) and inspect the DOM or page source.

> If the <script> tag appears unescaped in a JavaScript context or HTML, the parameter is vulnerable to DOM injection.

### Step 2: Verify DOM Injection

**Context**: Confirm the parameter influences the DOM structure, enabling XSS.

Use dev tools to search for the reflected input. Test variations like ?search=test' to check for context breaks (e.g., string concatenation in JS).

> Successful verification shows input directly altering DOM elements without sanitization, specific to IE's handling.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[dom-xss]]
- [[internet-explorer]]
