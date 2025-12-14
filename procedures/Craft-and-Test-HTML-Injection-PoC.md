---
id: proc-craft-html-injection-poc
tags:
  - xss
  - html-injection
  - poc
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
updated_at: '2025-12-14T03:47:23.435Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft and Test HTML Injection PoC

## Summary

This procedure crafts and tests a proof-of-concept (PoC) for HTML injection in the DOM-based XSS vulnerability on nutty.ubnt.com, confirming that arbitrary HTML tags can be rendered without sanitization.

## Description

By injecting HTML tags into the 'user' parameter of the URL hash, attackers can manipulate the page's DOM visually. This step validates the vulnerability's existence before escalating to JavaScript execution, using browsers like Chrome and IE to observe rendering differences.

## Requirements

1. Web browser (Chrome or Internet Explorer)
2. Ability to craft and encode URLs manually
3. Target URL accessible

## Defense

Defensive measures and detection strategies:

- Sanitize all URL-derived inputs before DOM insertion
- Employ strict CSP to block unsafe HTML
- Log and alert on suspicious URL patterns

## Objectives

1. Inject and render custom HTML elements
2. Verify cross-browser consistency
3. Confirm no filtering on HTML tags

## Instructions

### Step 1: Construct the Malicious URL

**Context**: Build a URL with HTML payload in the 'user' parameter.

Create: http://nutty.ubnt.com/github-btn.html?#&user=<h1><marquee>HTML<br>HTML<br>HTML<br>HTML<br>HTML<br>HTML<br>&type=follow. No encoding needed for basic tags.

**Expected Output**: URL ready for testing.

### Step 2: Load URL in Browser

**Context**: Test injection in Chrome or IE.

Paste the URL into the browser address bar and hit Enter. Observe the page content.

**Expected Output**: Scrolling marquee and <h1> headings appear in the 'Follow @' text area.

### Step 3: Validate Rendering

**Context**: Inspect the DOM to confirm injection.

Use DevTools Elements tab to check if injected tags are present in the innerHTML.

**Expected Output**: DOM shows <h1><marquee>HTML... structure.

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
- [[html-injection]]
- [[poc]]
