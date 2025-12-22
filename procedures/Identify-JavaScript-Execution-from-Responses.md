---
id: proc-uuid-002
tags:
  - xss
  - javascript
  - web
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
updated_at: '2025-12-13T23:52:24.326Z'
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
# Identify-JavaScript-Execution-from-Responses

## Summary

This procedure tests whether AJAX responses with content-type application/javascript are automatically executed as script when inserted into the DOM, revealing a key weakness for XSS exploitation in the rockstargames.com application.

## Description

The procedure simulates fetching JavaScript resources via the tags parameter to observe browser behavior. In the target web environment, if the response headers indicate application/javascript, the browser treats the content as executable script during DOM insertion, bypassing typical security checks. This is essential for chaining with path traversal to load malicious scripts from internal endpoints.

## Requirements

1. Browser with developer console enabled
2. Ability to modify URL fragments and monitor network responses
3. Optional proxy for header manipulation

## Defense

Defensive measures and detection strategies:

- Enforce strict content-type checks and avoid executing non-HTML/JSON responses as script
- Implement DOMPurify or similar sanitization for inserted content
- Log and alert on application/javascript responses from AJAX endpoints

## Objectives

1. Verify automatic script execution from AJAX responses
2. Identify content-type handling flaws
3. Prepare for payload injection via executable responses

## Instructions

### Step 1: Fetch a Test JavaScript Resource

**Context**: Use the tags parameter to request a known JS file and check execution.

Append #/?tags= to point to a public JS file, e.g., #/?tags=https://example.com/test.js (adjust for path). Monitor the Network tab for the response.

> Look for content-type: application/javascript in headers; if present, add alert('test') to the JS and reload to see execution.

### Step 2: Observe DOM Insertion and Execution

**Context**: Confirm the response is inserted and run without explicit script tags.

Inspect the Elements tab post-load to see where the response is placed (e.g., via document.write or innerHTML). Check console for execution traces.

> Success if script runs automatically, indicating vulnerability to JS payloads.

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
- javascript
- web
