---
id: proc-examine-uber-js-reflection-001
name: Examine-JavaScript-Endpoint-for-Parameter-Reflection
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:41.178Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Active Scanning]]'
sub_techniques: []
tags:
  - xss
  - recon
  - web-vulnerability
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---

# Examine-JavaScript-Endpoint-for-Parameter-Reflection

## Summary

This procedure involves inspecting a web endpoint's response to identify unescaped reflection of query parameters in JavaScript code, specifically targeting the _cc parameter in Uber's mobile JS resource to confirm a reflected XSS vulnerability.

## Description

In this attack scenario, the target is a public-facing JavaScript file served over HTTPS. By appending a test value to the _cc parameter and analyzing the response, attackers can observe how the value is inserted into a JSON-like object string without escaping. This double-quoted string context allows for breakout payloads. The procedure requires only browser access and developer tools, with outcomes including vulnerability confirmation and payload crafting groundwork. Prerequisites include public access to the endpoint.

## Requirements

1. Web browser with developer console (e.g., Chrome or Firefox).
2. Internet access to the target URL: https://m.uber.com/0-dfffb25d2cf6ceeb0a27.js.
3. Basic knowledge of JavaScript and URL parameters.

## Defense

Defensive measures and detection strategies:

- Implement proper input sanitization and escaping for all query parameters reflected in JS.
- Use Content Security Policy (CSP) with strict script-src directives to prevent inline script execution.
- Monitor access logs for unusual query parameter patterns or repeated endpoint hits.

## Objectives

1. Confirm parameter reflection without escaping in JS context.
2. Identify string breakout opportunities for XSS.
3. Gather details for payload development.

## Instructions

### Step 1: Access the Endpoint with Test Parameter

**Context**: Load the JavaScript resource with a benign _cc value to observe reflection.

Open your browser and navigate to: https://m.uber.com/0-dfffb25d2cf6ceeb0a27.js?_cc=asdf

> View the page source or use Network tab in DevTools to inspect the response. Look for the string {"_cc":"asdf"}} – the value 'asdf' should appear unescaped inside double quotes.

### Step 2: Analyze Reflection Context

**Context**: Use developer tools to examine the exact insertion point.

In the browser console or source view, search for '_cc' to locate the JSON object. Note the surrounding syntax, such as closing braces and quotes, to plan breakout.

> Expected output: The parameter is directly concatenated into a JS string, e.g., var obj = {"_cc":"[user input]"}}, vulnerable to injection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[recon]]
- [[web-vulnerability]]
