---
id: proc-identify-xss-url
tags:
  - xss
  - reflected-xss
  - web-testing
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:16:30.816Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify Reflected XSS in URL Parameter

## Summary

This procedure outlines how to discover a reflected cross-site scripting (XSS) vulnerability by testing URL parameters on a web application for lack of input sanitization, specifically on a DoD website where user input is directly reflected into the page without encoding.

## Description

In a reflected XSS attack, user-supplied data from a URL parameter is immediately rendered back in the server's response without proper escaping, allowing attackers to inject and execute JavaScript. This procedure targets public-facing web pages, such as search functions, where parameters like 'q' or 'id' are common vectors. On the DoD site, this led to potential exposure of session information. Prerequisites include basic web knowledge and access to the target site; no authentication is needed for initial discovery.

## Requirements

1. Web browser with developer tools (e.g., Chrome DevTools)
2. Knowledge of JavaScript payloads
3. Public access to the target DoD website

## Defense

Defensive measures and detection strategies:

- Implement output encoding (e.g., HTML entity encoding) for all user inputs reflected in pages
- Use Content Security Policy (CSP) to restrict script execution
- Monitor for anomalous JavaScript in logs or WAF alerts

## Objectives

1. Confirm reflection of unsanitized input in page source
2. Validate script execution capability
3. Assess potential for data exfiltration

## Instructions

### Step 1: Inspect Target Page Parameters

**Context**: Identify URL parameters that are reflected in the response, such as query strings in search or error pages.

Navigate to the DoD website and examine URLs for parameters. Use browser dev tools to view the page source and search for the parameter value.

Example: For `https://dod.example.gov/search?q=test`, check if 'test' appears unencoded in the HTML.

> If reflected without changes, proceed to payload testing.

### Step 2: Test Basic Payload Injection

**Context**: Inject a harmless script to verify execution.

Append a script tag to the parameter: `https://dod.example.gov/search?q=<script>alert('XSS')</script>`.

Visit the URL and observe if an alert dialog appears.

> Successful execution indicates the vulnerability; encode payload if basic test fails (e.g., use %3Cscript%3E for <script>).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Reconnaissance]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[web]]
