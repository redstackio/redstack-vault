---
id: proc-test-reflected-xss-url
tags:
  - xss
  - reflected-xss
  - testing
  - web
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-test-xss-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:33.908Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Test-for-Reflected-XSS-in-URL-Path

## Summary

This procedure tests web endpoints for reflected cross-site scripting (XSS) vulnerabilities by injecting payloads into URL paths and verifying if they are echoed back unsanitized in the response, as demonstrated on the Uber blog endpoint.

## Description

Reflected XSS occurs when user input from the URL is directly included in the server's HTML response without proper escaping, allowing attackers to inject and execute JavaScript in the victim's browser. In this case, the Uber blog at https://www.uber.com/en-NZ/blog/ reflects the URL path, enabling arbitrary script execution. The procedure involves sending crafted requests to check for reflection and then validating in a browser context. Prerequisites include basic web access and a tool like curl for testing.

## Requirements

1. Internet access to the target endpoint (e.g., https://www.uber.com/en-NZ/blog/)
2. Curl or similar HTTP client installed
3. Web browser for final validation
4. Attacker-controlled domain for payload testing (optional)

## Defense

Defensive measures and detection strategies:

- Implement output encoding (e.g., HTML entity encoding) for all user inputs in responses
- Use Content Security Policy (CSP) headers to restrict script execution
- Monitor access logs for suspicious URL patterns containing script tags
- Employ Web Application Firewall (WAF) rules to block common XSS payloads

## Objectives

1. Confirm if the URL path is vulnerable to reflected XSS
2. Verify JavaScript execution capability
3. Assess potential for data exfiltration

## Instructions

### Step 1: Send Test Payload via Curl

**Context**: Use curl to inject a simple script payload into the URL path and check if it's reflected in the response body.

**Command** ([[commands/curl-test-xss-payload]]):
```bash
curl -s "https://www.uber.com/en-NZ/blog/<script>alert(1)</script>/" | grep "alert(1)"
```

> This command fetches the page silently (-s) and greps for the payload. If output shows the script tag, it's reflected unsanitized.

### Step 2: Validate in Browser

**Context**: Open the crafted URL in a browser to confirm execution, as reflection may only trigger client-side.

**Command** (Manual browser execution):
No command needed; navigate to `https://www.uber.com/en-NZ/blog/<script>alert(1)</script>/` in Chrome/Firefox.

> An alert box should pop up if vulnerable, indicating successful XSS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-test-xss-payload]]

## Tools Used


## Tags

- [[xss]]
- [[reflected-xss]]
- [[web-testing]]
