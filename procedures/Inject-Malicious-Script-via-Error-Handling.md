---
tags:
  - xss
  - stored-xss
  - injection
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/curl-inject-xss]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:24.758Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 0dd2a0d8-5a2e-43c7-a406-974c5d571117
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Inject-Malicious-Script-via-Error-Handling

## Summary

This procedure exploits improper error handling on web applications to inject and store malicious JavaScript payloads in cacheable responses, leading to stored XSS execution when users access the affected pages. In the Acronis case, this allowed scripts to persist and impact multiple users without further interaction from the attacker.

## Description

Stored XSS occurs when user-supplied input, such as error reports, is not properly sanitized and is stored server-side, then reflected in responses to other users. Here, the vulnerability stems from inadequate input validation in the error handling mechanism on https://www.acronis.com/, enabling payloads to be cached and served broadly. The attack scenario involves submitting a payload via a form or API, confirming storage, and observing execution on victim browsers. Prerequisites include public access to the site and basic web testing tools. Expected outcomes: Arbitrary JavaScript execution in victims' sessions, potentially leading to data theft or defacement.

## Requirements

1. Public access to the target website (https://www.acronis.com/ or similar)
2. Knowledge of the error handling endpoint (e.g., /error-report form or API)
3. Tools for HTTP requests (curl or browser) and inspection (dev tools)

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and output encoding (e.g., HTML entity encoding) for all user inputs
- Use Content Security Policy (CSP) to restrict script execution
- Monitor for anomalous JavaScript in cached responses via WAF logs or server-side scanning
- Regularly audit error handling and caching mechanisms for reflection vulnerabilities

## Objectives

1. Inject persistent malicious script to compromise viewing users
2. Verify storage and execution in cached responses
3. Demonstrate medium-impact XSS for reporting or exploitation

## Instructions

### Step 1: Identify and Test Injection Point

**Context**: Locate the error handling input field or endpoint on the target site, which accepts user data without proper escaping.

**Command** ([[commands/curl-inject-xss]]):
```bash
curl -X POST https://www.acronis.com/error-report \
  -d "error_details=<script>alert('XSS Test');</script>" \
  -H "Content-Type: application/x-www-form-urlencoded"
```

> This command submits a basic XSS payload to the error report endpoint. Expected output: HTTP 200 or success response indicating submission. If the endpoint differs, adjust the URL and parameters based on site inspection.

### Step 2: Verify Storage and Execution

**Context**: Access the affected page to confirm the payload is stored and executes in the browser context.

**Instructions**: Navigate to the page that caches the error response (e.g., a dashboard or error page). Open browser dev tools (F12) and check for script execution, such as an alert or console log.

No specific command needed; use manual browser access. If automating, use curl to fetch the page and grep for the payload:

```bash
echo "Fetching cached page..."
curl -s https://www.acronis.com/affected-page | grep -i "alert('XSS"
```

> Expected output: The payload appears in the response HTML, and execution is confirmed via alert in a real browser session.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/curl-inject-xss]]

## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[web]]
- [[injection]]
