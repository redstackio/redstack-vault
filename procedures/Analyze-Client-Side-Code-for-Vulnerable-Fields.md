---
id: proc-analyze-js-001
tags:
  - reconnaissance
  - javascript-analysis
  - api-endpoints
type: procedure
tools:
  - '[[tools/Firefox-Browser]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-13T23:55:38.332Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Analyze Client-Side Code for Vulnerable Fields

## Summary

This procedure involves inspecting the JavaScript code of a web application to identify modifiable input fields and output rendering mechanisms that could lead to vulnerabilities like stored XSS.

## Description

In the context of the 8x8 API, analyze the client-side JavaScript to discover that the ipAddress field in payment methods can be updated via /api/patchPaymentMethod/ID and that the /api/paymentMethodInfoById/ID endpoint renders the response as HTML with Content-Type: text/html;charset=UTF-8, enabling script execution without sanitization. This step requires access to the application's frontend and developer tools.

## Requirements

1. Authenticated access to the 8x8 web application
2. Browser with developer tools enabled (e.g., Firefox)
3. Basic knowledge of JavaScript and API interactions

## Defense

Defensive measures and detection strategies:

- Implement client-side code obfuscation and minification to hinder analysis
- Use Content Security Policy (CSP) to restrict script execution
- Monitor for unusual developer tools usage or network requests

## Objectives

1. Identify unsanitized input fields like ipAddress
2. Confirm HTML rendering on output endpoints
3. Establish foundation for payload injection

## Instructions

### Step 1: Inspect JavaScript Sources

**Context**: Open the browser's developer console and examine loaded JavaScript files for API handling logic.

No specific command; use browser tools to search for 'ipAddress' and 'patchPaymentMethod' references.

> Locate code snippets showing ipAddress modification and HTML insertion in payment info views.

### Step 2: Verify Endpoint Behaviors

**Context**: Test API endpoints manually to confirm behaviors identified in code.

Use browser network tab to send test requests and observe response headers.

> Expected: /api/paymentMethodInfoById/ID returns text/html, allowing HTML parsing.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Hardware]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox-Browser]]

## Tags

- [[Reconnaissance]]
- [[javascript-analysis]]
