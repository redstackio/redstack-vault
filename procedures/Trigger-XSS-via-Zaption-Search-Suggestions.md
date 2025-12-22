---
id: proc-zaption-trigger-suggestions-001
tags:
  - xss
  - trigger
  - search
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
updated_at: '2025-12-14T03:15:27.016Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger XSS via Zaption Search Suggestions

## Summary

This procedure triggers the stored XSS payload by interacting with the gallery search box, causing the suggestion dropdown to render the malicious title and execute JavaScript automatically.

## Description

Zaption's search suggestions dynamically load and display titles without sanitization, allowing the injected payload to execute in the dropdown HTML. This low-interaction vector affects users as they type in the search field, leading to immediate JS execution in their browser context. It requires the payload to be already injected and works on any user's session viewing suggestions.

## Requirements

1. Injected XSS payload in a gallery title
2. Access to Zaption gallery search interface
3. Web browser

## Defense

Defensive measures and detection strategies:

- Sanitize outputs in dynamic UI elements like dropdowns using libraries like DOMPurify
- Implement client-side escaping for all rendered user content
- Log and alert on search queries containing suspicious patterns (e.g., script tags)

## Objectives

1. Load search suggestions containing the malicious title
2. Execute JavaScript via dropdown rendering
3. Demonstrate automatic trigger without full search

## Instructions

### Step 1: Navigate to Search Box

**Context**: Position the browser at the gallery search interface to prepare for typing.

Go to https://www.zaption.com/gallery and focus on the search input field.

### Step 2: Type Trigger Query

**Context**: Input text matching the payload prefix to fetch and render suggestions.

Start typing `xyz123` (or the prefix of your malicious title) in the search box. The dropdown will populate with matching items, including the injected title.

The payload executes as the suggestion HTML is inserted into the DOM.

> Observe the `prompt("XSS")` alert or check console for errors/execution.

### Step 3: Verify Execution

**Context**: Confirm JS ran in the current browser session.

Use developer tools (F12) to inspect the dropdown HTML for the `<img>` tag and monitor network requests to the search endpoint.

**Expected Output**: JavaScript alert fires; console shows execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- search-suggestions
- trigger
