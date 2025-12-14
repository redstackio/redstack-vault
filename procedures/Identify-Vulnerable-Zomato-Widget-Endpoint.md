---
id: proc-uuid-1
tags:
  - recon
  - xss
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
  - '[[Active Scanning]]'
updated_at: '2025-12-14T03:15:10.459Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-Vulnerable-Zomato-Widget-Endpoint

## Summary

This procedure involves reconnaissance to identify the vulnerable 'language_id' parameter in the Zomato widget API endpoint, confirming reflection without sanitization for potential XSS exploitation.

## Description

In a web-based attack scenario targeting public-facing APIs like Zomato's restaurant search widget, examine the endpoint https://www.zomato.com/widgets/res_search_widget.php. The 'language_id' parameter is reflected into JavaScript output without proper escaping, allowing attackers to inject code. This step is crucial for validating the vulnerability before crafting payloads. Expected outcome: Confirmation of unsanitized input reflection, setting the stage for XSS exploitation in a user's browser session.

## Requirements

1. Web browser with developer tools (e.g., Chrome DevTools)
2. Public internet access to zomato.com
3. Basic knowledge of HTTP requests and JavaScript contexts

## Defense

Defensive measures and detection strategies:

- Implement content security policy (CSP) to restrict script execution
- Sanitize and validate all user inputs, especially reflected parameters
- Monitor for anomalous requests to widget endpoints with encoded payloads

## Objectives

1. Locate and verify the vulnerable API parameter
2. Understand reflection context for payload design
3. Establish proof-of-concept for further exploitation

## Instructions

### Step 1: Examine Widget Documentation and Endpoint

**Context**: Review Zomato's widget integration docs to identify parameters like 'language_id'.

No specific command; use browser to navigate to https://www.zomato.com/widgets/res_search_widget.php?language_id=test and inspect the response source.

> Look for 'language_id' value echoed in JS, e.g., var lang = 'test';. If unescaped, proceed.

### Step 2: Test for Reflection

**Context**: Inject simple breakers like quotes to check sanitization.

Use browser or manual request: Append " to language_id and observe if it breaks JS syntax in the page.

> Expected: Syntax error or visible reflection without escaping, indicating vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[xss]]
