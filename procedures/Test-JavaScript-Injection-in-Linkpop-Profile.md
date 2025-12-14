---
id: proc-test-js-injection
tags:
  - xss
  - javascript-injection
  - script-tag-closure
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
updated_at: '2025-12-13T23:52:20.873Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Test-JavaScript-Injection-in-Linkpop-Profile

## Summary

This procedure tests for XSS by injecting a payload that closes an existing script tag and inserts new JavaScript, confirming arbitrary code execution in the profile page context.

## Description

User-controlled data in Linkpop profile pages is rendered without proper escaping in a JavaScript context, allowing attackers to break out of script tags and execute custom code. This demonstrates the vulnerability's severity, enabling attacks like alert popups for proof-of-concept or more malicious actions like keylogging.

## Requirements

1. Web browser with developer tools
2. Access to a Linkpop profile URL
3. Basic knowledge of XSS payloads

## Defense

Defensive measures and detection strategies:

- Escape user inputs in JavaScript contexts using JSON encoding or safe templating
- Validate and sanitize URL parameters before rendering
- Implement client-side validation and server-side checks for injection patterns

## Objectives

1. Inject payload to close and reopen script tags
2. Execute arbitrary JavaScript
3. Confirm via visible alert

## Instructions

### Step 1: Access Profile Page

**Context**: Navigate to a profile URL to prepare for injection.

No command; visit https://linkpop.com/nagli123 in the browser.

> The page loads with potential script tags in the source.

### Step 2: Inject Payload

**Context**: Append the injection payload to the URL to test reflection and execution.

Modify the URL to https://linkpop.com/nagli123?</script><script>alert(1)</script> or similar parameter that reflects.

> Expected output: Browser displays an alert box with '1', confirming XSS.

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
- [[javascript-injection]]
