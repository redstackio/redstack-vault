---
id: proc-trigger-xss-ie-compat
tags:
  - xss
  - ie-xss
  - cookie-theft
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
  - JavaScript
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:12.853Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-in-Internet-Explorer-Compatibility-Mode

## Summary

This procedure exploits the DOM-based XSS by forcing Internet Explorer compatibility mode to bypass modern browser protections, injecting a <script> tag via the 'user' parameter to execute alerts revealing domain and cookies.

## Description

IE's lenient parsing in compatibility mode (IE=9) allows <script> tags to execute when inserted via innerHTML. The PoC uses an iframe with a meta tag to enforce this mode, embedding a URL with payload like user=yrdy<script>alert(document.domain);alert(document.cookie);//. This triggers JavaScript execution, enabling theft of sensitive data like cookies in the browser context.

## Requirements

1. Browser supporting IE compatibility (e.g., Edge or IE)
2. HTML file or iframe capable environment
3. Target URL accessible

## Defense

Defensive measures and detection strategies:

- Avoid innerHTML; use textContent or createTextNode for dynamic content
- Enforce strict CSP to block script execution
- Detect compatibility mode usage and alert on suspicious iframes

## Objectives

1. Execute arbitrary JavaScript
2. Exfiltrate cookies and domain info
3. Demonstrate impact in legacy environments

## Instructions

### Step 1: Prepare Compatibility HTML

**Context**: Create an HTML snippet to force IE mode.

Write: <meta http-equiv="X-UA-Compatible" content="IE=9"><iframe src='https://github.algolia.com/github-btn.html?#&user=yrdy%3Cscript%3Ealert(document.domain);alert(document.cookie);//%26type=follow'></iframe>. Save as an HTML file or use in a local page.

**Expected Output**: HTML ready with encoded payload.

### Step 2: Load the PoC

**Context**: Render the iframe to trigger execution.

Open the HTML file in IE or a compatible browser. The iframe loads the vulnerable URL.

**Expected Output**: Alert popups showing domain and cookies.

### Step 3: Verify Execution

**Context**: Check console for errors or additional output.

In DevTools, confirm script ran without blocking.

**Expected Output**: No errors; alerts confirmed data theft potential.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[ie-xss]]
- [[cookie-theft]]
