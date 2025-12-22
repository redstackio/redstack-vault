---
tags:
  - xss
  - reflected-xss
  - joomla
type: procedure
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Google-Chrome]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T03:47:18.583Z'
sub_techniques: []
id: 9c11e2ce-ddf0-40c5-a60b-f006aae596f1
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Identify Reflected XSS in arg2 Parameter

## Summary

This procedure tests for reflected XSS in the 'arg2' parameter of a POST request to /index.php in a Joomla-based application by injecting a JavaScript payload and observing unsanitized reflection.

## Description

In Joomla registration endpoints, the arg2 parameter accepts JSON-like strings for email checks but fails to sanitize HTML/JS, allowing injection. This self-XSS can execute in the attacker's browser but sets up escalation. Target environments include PHP web apps with parameters like task=azrul_ajax, option=community, func=register,ajaxCheckEmail. Expected outcome: Confirmation of vulnerability via alert execution.

## Requirements

1. Access to send POST requests to the target /index.php (browser dev tools or curl).
2. Knowledge of endpoint parameters (e.g., from source code or prior recon).
3. Browser for testing payload execution.

## Defense

Defensive measures and detection strategies:

- Implement output encoding (e.g., htmlspecialchars) for user inputs in responses.
- Use Content Security Policy (CSP) to block inline scripts.
- Monitor for anomalous JS payloads in logs.

## Objectives

1. Confirm unsanitized reflection of arg2 in response.
2. Verify JavaScript execution capability.
3. Assess self-XSS impact on attacker session.

## Instructions

### Step 1: Prepare Test Payload

**Context**: Craft a simple XSS payload to inject into arg2 as a JSON array element.

Use browser dev tools or a tool like curl to send the POST request. No specific command, but example via browser console or Postman.

### Step 2: Submit POST Request

**Context**: Send the request and inspect the response for reflection.

Example request (via curl for reproducibility, though manual in original):

```bash
curl -X POST https://target/index.php \
  -d "task=azrul_ajax" \
  -d "option=community" \
  -d "func=register,ajaxCheckEmail" \
  -d "arg2=[\"test\",\"<img src=a onerror=alert(1)>\"]" \
  -d "no_html=1"
```

> This sends the payload; if reflected, open in browser to trigger alert(1). Expected output: Response contains unescaped <img> tag, executing on load.

### Step 3: Validate Execution

**Context**: Load the response in a browser to confirm JS runs.

Open [[tools/Firefox]] or [[tools/Google-Chrome]], paste the full request into dev tools Network tab, and replay. Observe alert.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]
- [[tools/Google-Chrome]]

## Tags

- xss
- reflected-xss
