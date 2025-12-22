---
id: proc-starbucks-test-redirects
tags:
  - open-redirect
  - web-testing
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-test-redirect]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:47:23.416Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-Open-Redirects-in-GET-Parameters

## Summary

This procedure tests for open redirect vulnerabilities by modifying GET parameters with malformed inputs to observe unexpected redirect behaviors in web applications like Starbucks sites.

## Description

In the context of Starbucks websites, incomplete input sanitization allows malformed parameters starting with '<>' to bypass validation, leading to chained redirects. This step initiates the discovery by appending simple malformed values like '>cofee' to query strings and monitoring HTTP responses for anomalies. It targets public-facing web apps without authentication, focusing on GET-based interactions.

## Requirements

1. Access to a web browser or command-line tool like curl for sending HTTP requests.
2. Target URL from affected sites (e.g., shop.starbucks.de).
3. Network connectivity to the target.

## Defense

Defensive measures and detection strategies:

- Implement strict URL validation to whitelist allowed domains.
- Use Content Security Policy (CSP) to block unexpected redirects.
- Log and monitor anomalous GET parameters for '<>' patterns.

## Objectives

1. Probe for redirect flaws in input handling.
2. Identify sites vulnerable to parameter manipulation.
3. Gather evidence of sanitization bypass.

## Instructions

### Step 1: Craft and Send Malformed Request

**Context**: Modify an existing GET parameter to include a malformed value and send the request to trigger potential redirects.

**Command** ([[commands/curl-test-redirect]]):
```bash
curl -v "https://shop.starbucks.de/?param=>cofee" 2>&1 | grep Location
```

> This command sends a GET request with the malformed parameter and extracts the Location header from the verbose output to inspect the redirect target. Expect a 302 response if vulnerable.

### Step 2: Analyze Response

**Context**: Review the redirect location for unexpected behavior, such as chaining to external sites.

No specific command; inspect output manually for anomalies like unintended URLs.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-test-redirect]]

## Tools Used


## Tags

- [[open-redirect]]
- [[web-testing]]
