---
id: proc-craft-uber-xss-payload-001
name: Craft-and-Inject-XSS-Payload-in-Query-Parameter
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:41.166Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
sub_techniques: []
tags:
  - xss
  - reflected-xss
  - javascript-injection
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
---

# Craft-and-Inject-XSS-Payload-in-Query-Parameter

## Summary

This procedure crafts and delivers a reflected XSS payload targeting the _cc parameter in Uber's JS endpoint, breaking out of a string context to inject and execute arbitrary JavaScript, such as an alert or data exfiltration script.

## Description

The attack exploits the unescaped reflection of _cc in a double-quoted JS string within a JSON object. By closing the string and object with "}} and injecting HTML/JS tags, the payload executes in the victim's browser over SSL. This bypasses Chrome's XSS Auditor due to the JS context. Expected outcomes include code execution, enabling theft of login credentials or credit card info. Requires the victim to load the crafted URL.

## Requirements

1. URL encoding knowledge or tool.
2. Browser to test payload execution.
3. Access to the target endpoint.

## Defense

Defensive measures and detection strategies:

- Escape query parameters with JSON.stringify() or equivalent before insertion.
- Deploy strict CSP to block inline scripts and eval().
- Use WAF rules to detect common XSS payloads in query strings.

## Objectives

1. Break out of JS string context for injection.
2. Execute arbitrary JS in victim browser.
3. Demonstrate impact like credential harvesting.

## Instructions

### Step 1: Design the Breakout Payload

**Context**: Create a payload to close the string and object, then inject script.

Use: asdf"}} </script><script>alert(1)</script>

> This closes the quote, braces, and script tag, starting a new executable script.

### Step 2: URL-Encode and Inject

**Context**: Append the encoded payload to the URL and load it.

Full URL: https://m.uber.com/0-dfffb25d2cf6ceeb0a27.js?_cc=asdf%22%7D%7D%3C/script%3E%3Cscript%3Ealert(1)%3C/script%3E

Navigate to the URL in a browser.

> Expected output: The page loads, and an alert(1) dialog appears, confirming execution. Inspect response to see injected code rendered.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[reflected-xss]]
- [[javascript-injection]]
