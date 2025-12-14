---
id: proc-test-xss-001
tags:
  - xss
  - payload-testing
  - curl
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-version-verbose]]'
  - '[[commands/curl-xss-payload-test]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:25.576Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Test-XSS-Payloads-in-curl-URL-Processing

## Summary

This procedure tests curl's response to encoded XSS payloads in URLs, observing if unsanitized input could lead to attacks like cookie theft or redirects in dependent applications.

## Description

By sending URLs with payloads like <script>alert(1)</script> (URL-encoded), this verifies if curl's glob_url and urlnode handling propagates unescaped data, potentially enabling XSS in browser contexts or pipelines processing curl outputs. The curl team noted server-side responsibility, but risks remain in client-side usage.

## Requirements

1. Installed curl tool
2. Access to a test HTTP endpoint (e.g., http://test.com)
3. Knowledge of URL encoding for payloads

## Defense

Defensive measures and detection strategies:

- Sanitize curl outputs before rendering in web apps
- Use HTTPS and validate redirects
- Log and monitor anomalous curl requests in CI/CD

## Objectives

1. Inject and observe XSS payload processing
2. Check for reflection or effective URL changes
3. Evaluate exploitability in real scenarios

## Instructions

### Step 1: Verify curl Version

**Context**: Confirm the curl version under test for reproducibility.

**Command** ([[commands/curl-version-verbose]]):
```bash
curl -v
```

> Runs curl in verbose mode to display version. Expected output: Version string like 'curl 8.4.0' at the start.

### Step 2: Send XSS Payload Test

**Context**: Test if encoded XSS in query params is handled insecurely.

**Command** ([[commands/curl-xss-payload-test]]):
```bash
curl "http://test.com?param=%3Cscript%3Ealert(1)%3C/script%3E" -w "%{url_effective}"
```

> Sends GET request with encoded payload and prints effective URL. Expected output: The final URL, potentially unchanged or reflected, indicating lack of sanitization.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] Command and Scripting Interpreter: JavaScript

### Sub-Techniques


## Commands Used

- [[commands/curl-version-verbose]]
- [[commands/curl-xss-payload-test]]

## Tools Used

- [[tools/curl]]

## Tags

- [[xss]]
- [[payload-testing]]
- [[tools/curl]]
