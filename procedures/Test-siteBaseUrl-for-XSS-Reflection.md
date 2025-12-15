---
tags:
  - xss
  - testing
  - parameter-injection
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/test-sitebaseurl-reflection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:11.124Z'
sub_techniques: []
id: f8a4dd6b-e444-4a08-a59d-e3b8588fe4d8
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-siteBaseUrl-for-XSS-Reflection

## Summary

This procedure tests the siteBaseUrl parameter in the Starbucks API for unsanitized reflection, confirming potential for Reflected XSS by injecting harmless payloads and observing output.

## Description

Reflected XSS occurs when user input is echoed back in the response without proper encoding, allowing script execution. In this API, siteBaseUrl is reflected in HTML contexts, enabling breakout from URL strings using techniques like %0a for line breaks. This step validates the vulnerability before exploitation.

## Requirements

1. Confirmed API access from prior step
2. Knowledge of HTML/JS contexts in responses
3. Browser or proxy to inspect rendered output

## Defense

Defensive measures and detection strategies:

- Output encode all user inputs (e.g., URL-encode siteBaseUrl)
- Validate siteBaseUrl against whitelist of allowed domains
- Monitor for payload patterns in logs

## Objectives

1. Inject test strings to check reflection
2. Identify context (e.g., attribute, body) for payload crafting
3. Confirm no CSP or sanitization blocks execution

## Instructions

### Step 1: Inject Test Payload

**Context**: Use a simple script tag or alert to probe for execution without harm.

**Command** ([[commands/test-sitebaseurl-reflection]]):
```bash
curl "https://openapi.starbucks.com/searchasyoutype/v1/search?x-api-key=██████&query=coffe&partnerid=████:vwt2u5wngbk&siteBaseUrl=http://example.com/<script>alert(1)</script>"
```

> Inspect the response or rendered page for the payload. If reflected without escaping, an alert may trigger in a browser context, indicating vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/test-sitebaseurl-reflection]]

## Tools Used


## Tags

- xss
- testing
- parameter-injection
