---
tags:
  - analysis
  - xss
  - javascript
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-fetch-urbandictionary]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:52.796Z'
sub_techniques: []
id: 76e58118-348a-42d8-a738-0d5680064fc4
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Analyze JavaScript Reflection for XSS

## Summary

This procedure analyzes the reflected user input in the JavaScript context to identify breakout points for XSS injection, focusing on the lack of escaping in the Page.globals.normalized property.

## Description

Attackers inspect the <script> tag where the 'term' parameter is inserted as a string value in a JSON-like object. Without proper escaping, inputs containing quotes or script-closing tags can break out of the context, allowing injection of HTML and JS. This is performed after endpoint identification in web vulnerability assessments.

## Requirements

1. Access to the vulnerable endpoint
2. Browser or curl for fetching source
3. Understanding of JS string escaping

## Defense

Defensive measures and detection strategies:

- Use JSON encoders for data in JS objects
- Implement output encoding for script contexts
- Audit JS code for dynamic insertions

## Objectives

1. Confirm vulnerable insertion point
2. Identify escapable characters (e.g., ")
3. Plan payload structure

## Instructions

### Step 1: Fetch and Parse Reflection

**Context**: Retrieve page to examine the exact reflection format.

**Command** ([[commands/curl-fetch-urbandictionary]]):
```bash
curl "http://www.urbandictionary.com/define.php?term=lol" | grep -A5 -B5 "normalized"
```

> Output reveals structure like Page.globals.normalized = "lol"; note double quotes and no escapes.

### Step 2: Identify Breakout

**Context**: Determine how to close the string and script tag.

Manually analyze: Input can be closed with "; </script> to inject new elements.

> Expected: Recognition that </script><svg onload=...> will execute post-closure.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-fetch-urbandictionary]]

## Tools Used


## Tags

- [[analysis]]
- [[xss]]
