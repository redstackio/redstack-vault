---
tags:
  - xss
  - payload-craft
type: procedure
tools:
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:12.698Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: a0628ea2-e1e5-4964-8d28-9c1e638a4316
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft Malicious redirect_uri Payload

## Summary

This procedure involves creating a URL-encoded JavaScript payload for the redirect_uri parameter that escapes the anchor tag context and injects an executable SVG element, enabling XSS in the modal.

## Description

By analyzing the client-side code, the redirect_uri is passed via App.param('redirect_uri') to the modal show function. The payload breaks out of the href attribute using a quote close and tag close, then injects <svg onload='alert(document.domain)'> to execute on load. This targets template injection flaws in auth endpoints.

## Requirements

1. Knowledge of URL encoding
2. Web browser for testing
3. Understanding of HTML/JS context breaking

## Defense

Defensive measures and detection strategies:

- Enforce URL validation and encoding on redirect_uri (e.g., reject payloads with < > " characters)
- Use Content Security Policy (CSP) to block inline script execution
- Log and alert on suspicious redirect_uri patterns

## Objectives

1. Generate a breakout payload for the anchor href
2. Ensure JavaScript execution without breaking the page
3. Test payload validity before deployment

## Instructions

### Step 1: Design the Payload

**Context**: Create a string that closes the href quote and anchor, then injects the SVG.

The raw payload is: '><svg onload='alert(document.domain)'>

> This closes the href='...' > and starts a new element.

### Step 2: URL Encode the Payload

**Context**: Encode special characters for safe transmission in the query parameter.

Use a URL encoder to convert to: %27%3E%3Csvg%20onload=%27alert%28document.domain%29%27%3E

> Verify decoding in browser dev tools matches the raw payload.

### Step 3: Append to Base URL

**Context**: Build the full exploit URL.

Combine as: https://www.mapbox.com/authorize/?redirect_uri=%27%3E%3Csvg%20onload=%27alert%28document.domain%29%27%3E

> Copy this URL for the next procedure.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Web-Browser]]

## Tags

- payload-injection
- javascript
