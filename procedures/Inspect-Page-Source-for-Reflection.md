---
tags:
  - xss
  - source-inspection
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
updated_at: '2025-12-14T00:11:15.881Z'
sub_techniques: []
id: b90f2230-ee91-421e-ac47-87161e91a1fd
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
---

# Inspect-Page-Source-for-Reflection

## Summary

This procedure involves examining the HTML source code of the search results page to locate and analyze the reflection of the test input, determining if it's in a dangerous context like JavaScript.

## Description

Following input submission, this step uses browser developer tools to view the raw HTML and search for the test string. In the Equifax scenario, reflection in client-side JavaScript (e.g., within Analytics.trackEvent) exposes the site to XSS. This is a reconnaissance step in web vulnerability assessment, requiring only browser access. Outcomes include pinpointing the injection vector for payload development.

## Requirements

1. Web browser with 'View Page Source' or developer console
2. Loaded search page from previous step
3. Knowledge of HTML/JS structure

## Defense

Defensive measures and detection strategies:

- Encode user inputs when inserting into JavaScript (e.g., JSON.stringify)
- Employ web application firewalls (WAF) to scan for reflection patterns
- Regular code audits for dynamic script generation

## Objectives

1. Locate the exact reflection point in the response
2. Assess if it's in an executable context
3. Gather details for payload construction

## Instructions

### Step 1: View Page Source

**Context**: Access the underlying HTML to search for unsanitized input echoes.

**Instructions**: Right-click anywhere on the loaded search page and select 'View Page Source' (or Ctrl+U in most browsers). Use Ctrl+F to search for 'broook'.

> Expected: The string appears in the source, ideally highlighted in a <script> tag or inline JS.

### Step 2: Analyze Reflection Location

**Context**: Determine the context (e.g., HTML attribute, JS string) to evaluate exploitability.

**Instructions**: Note the surrounding code, such as proximity to JavaScript functions.

> Expected: Reflection inside a JS object literal, confirming high-risk context.

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
- [[inspection]]
