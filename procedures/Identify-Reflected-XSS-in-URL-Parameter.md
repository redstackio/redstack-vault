---
id: proc-uuid-1-1171403
tags:
  - xss
  - reflected-xss
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:28:12.744Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Identify-Reflected-XSS-in-URL-Parameter

## Summary

This procedure identifies a reflected cross-site scripting (XSS) vulnerability in a URL parameter on a web application, such as a U.S. Department of Defense site, by testing for unsanitized input reflection that allows JavaScript payload injection.

## Description

In this attack scenario, the target is a public-facing web application where a URL parameter (e.g., ?URL=) echoes user input directly into the HTML without proper encoding or sanitization. By appending a javascript: URI payload, an attacker can confirm execution of arbitrary JavaScript in the victim's browser context. This is particularly effective on high-security sites lacking input validation, leading to potential session hijacking or data exfiltration. Prerequisites include access to a web browser and the target URL.

## Requirements

1. Web browser with developer tools for inspecting page source
2. Knowledge of the target URL structure (e.g., https://███████?URL=)
3. No authentication required for public endpoints

## Defense

Defensive measures and detection strategies:

- Implement output encoding (e.g., HTML entity encoding) for all user inputs reflected in pages
- Use Content Security Policy (CSP) to block inline JavaScript execution
- Deploy Web Application Firewall (WAF) rules to detect and block javascript: payloads in parameters
- Monitor server logs for anomalous parameter values containing script tags or URIs

## Objectives

1. Confirm reflection of user input without sanitization
2. Validate JavaScript execution capability via alert payload
3. Assess potential for chaining with other exploits like clickjacking

## Instructions

### Step 1: Test Parameter Reflection

**Context**: Append a benign test string to observe if input is echoed back unsanitized.

Navigate to https://███████?URL=test and inspect the page source to see if 'test' appears unencoded in HTML.

> If reflected as-is, proceed to payload testing.

### Step 2: Inject JavaScript Payload

**Context**: Craft a payload to execute JavaScript, using a decoy to mask intent.

Modify the URL to https://███████?URL=javascript:alert(document.domain)//https://google.com and load it. Observe if an alert pops up showing the domain.

> Successful execution indicates XSS vulnerability; the // comments out the decoy to prevent URL parsing errors.

### Step 3: Validate Impact

**Context**: Test for broader implications like cookie access.

Replace alert with a payload to log document.cookie in console, confirming data access potential.

> Expected: Console logs session cookies, proving theft risk.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[reflected-xss]]
