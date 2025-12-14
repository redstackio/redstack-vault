---
id: proc-uuid-002
tags:
  - reflected-xss
  - cookies
  - parameters
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
updated_at: '2025-12-14T17:26:55.835Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Identify-Reflected-XSS-in-Cookies-and-Parameters-on-Job-Pages

## Summary

This procedure discovers reflected XSS vulnerabilities in the combination of cookies and URL parameters on /Job/ pages, where user input is reflected without proper encoding, allowing script injection.

## Description

On platforms like Glassdoor's /Job/ endpoints, inputs from cookies and query parameters are concatenated and output without sanitization, leading to reflected XSS. Though individually unexploitable, the combination enables payload delivery that can be escalated when cached.

## Requirements

1. Access to /Job/ pages
2. Ability to set custom cookies and parameters
3. JavaScript knowledge for payload crafting

## Defense

Defensive measures and detection strategies:

- Implement strict output encoding for all user inputs (e.g., HTML entity encoding)
- Validate and sanitize cookie values server-side
- Use Content-Security-Policy (CSP) to block inline scripts

## Objectives

1. Inject and reflect XSS payload via cookie-parameter combo
2. Confirm executability in browser context
3. Prepare payloads for cache poisoning integration

## Instructions

### Step 1: Set Malicious Cookie

**Context**: Inject XSS into a cookie that interacts with parameters.

Use browser dev tools or curl to set a cookie:

```bash
curl -v -b "testcookie=<script>alert(1)</script>" "https://target.com/Job/?param=<script>alert(1)</script>"
```

> Check response for reflection of both cookie and param values unencoded.

### Step 2: Verify Reflection and Execution

**Context**: Load the page in a browser to test execution.

Navigate to the URL with the cookie set; observe if alert pops or inspect source for unencoded script.

**Expected Output**: Script tag appears in HTML, executes on load.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques

- None

## Commands Used

- None specific

## Tools Used

- None specific

## Tags

- reflected-xss
- job-pages
- glassdoor
