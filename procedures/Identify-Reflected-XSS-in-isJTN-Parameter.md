---
id: proc-uuid-1
tags:
  - xss
  - reflection-identification
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
updated_at: '2025-12-13T23:52:43.740Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Identify Reflected XSS in isJTN Parameter

## Summary

This procedure identifies if the 'isJTN' parameter on the /apply endpoint reflects user input directly into JavaScript code without encoding, confirming a potential reflected XSS vulnerability.

## Description

In the context of web applications like Informatica's careers site running on Tomcat, user-supplied values in query parameters may be echoed back into the HTML response. Here, 'isJTN' is inserted into a JavaScript object, allowing script tags to break out and execute. This step uses manual inspection or proxy tools to spot the reflection point, setting the stage for payload testing. Expected outcome: Unsanitized input in response, vulnerable to JS injection.

## Requirements

1. Access to the target URL: https://careers.informatica.com/apply
2. Browser with developer tools or intercepting proxy (e.g., Burp Suite)
3. Basic knowledge of HTML/JS inspection

## Defense

Defensive measures and detection strategies:

- Input validation and output encoding for all parameters reflected into JS contexts
- Content Security Policy (CSP) to block inline scripts and external loads
- Web Application Firewall (WAF) rules to detect script tags in queries

## Objectives

1. Locate exact reflection point in response
2. Confirm lack of sanitization
3. Prepare for payload injection

## Instructions

### Step 1: Inspect Endpoint Response

**Context**: Send a request with a benign value in isJTN and examine the HTML for reflection.

**Command** (Manual via browser or curl):

Use browser: Append ?isJTN=test to https://careers.informatica.com/apply and view source.

```bash
curl "https://careers.informatica.com/apply?isJTN=test" | grep -i isJTN
```

> This command fetches the response and greps for 'isJTN' to spot reflection like 'isJTN: 'test''. Expected output: Line showing direct insertion into JS object.

### Step 2: Analyze Reflection Context

**Context**: Check if the reflection is in a JS-executable context, such as inside a <script> tag or object literal.

**Command** (Manual inspection):

In dev tools, search for 'isJTN' in the response HTML.

> Look for patterns like var payload = { ... isJTN: 'test' ... }. Success: Value appears unescaped in JS code.

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
- [[web-vulnerability]]
