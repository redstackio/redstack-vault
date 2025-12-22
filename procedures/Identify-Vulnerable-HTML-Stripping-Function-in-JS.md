---
id: proc-uuid-1
tags:
  - xss
  - javascript
  - analysis
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
updated_at: '2025-12-14T03:47:18.419Z'
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
# Identify-Vulnerable-HTML-Stripping-Function-in-JS

## Summary

This procedure involves inspecting client-side JavaScript on a web application to identify inadequate HTML stripping functions that can lead to DOM-based XSS vulnerabilities.

## Description

In the context of the Grab.com vulnerability, the stripHtml function uses a regex to remove HTML tags before setting innerHTML on a div and extracting textContent. The regex /<\/?\w+\[^>\]*\/?>/g fails against crafted malformed or encoded tags, allowing scriptable elements to persist and execute. This step requires reviewing JS source code via browser dev tools to pinpoint the flaw.

## Requirements

1. Web browser with developer tools enabled
2. Access to the target website's pages
3. Basic knowledge of JavaScript and regex patterns

## Defense

Defensive measures and detection strategies:

- Implement comprehensive server-side input validation and output encoding
- Use established libraries like DOMPurify for client-side sanitization instead of custom regex
- Monitor for anomalous JS execution in browser consoles or via CSP headers

## Objectives

1. Locate the stripHtml function and its regex implementation
2. Understand how it processes input via innerHTML and textContent
3. Identify weaknesses in tag removal for malformed HTML

## Instructions

### Step 1: Inspect Network and Download JS Files

**Context**: Load the target page and capture client-side scripts to analyze for sanitization functions.

Open the browser dev tools (F12), navigate to the Network tab, reload https://www.grab.com/, and filter for JS files. Download and search for functions like 'stripHtml' or similar sanitizers.

### Step 2: Analyze the Function Logic

**Context**: Examine the code to reveal the vulnerable regex and processing steps.

In the downloaded JS, locate the function: it creates a div, applies html.replace(/<\/?\w+\[^>\]*\/?>/g, ""), sets innerHTML, and returns textContent. Note that this does not handle encoded or malformed tags like <a/:<"a"> properly.

### Step 3: Test Regex Locally

**Context**: Verify the regex failure in a controlled environment.

Use browser console or a JS editor to test the regex against sample inputs, confirming it strips standard tags but leaves crafted ones intact.

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
- [[JavaScript]]
