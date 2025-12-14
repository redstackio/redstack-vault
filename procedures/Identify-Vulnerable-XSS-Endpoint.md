---
id: proc-identify-xss-endpoint
tags:
  - xss
  - recon
  - web-testing
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-test-post-parameter]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:41.769Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify Vulnerable XSS Endpoint

## Summary

This procedure involves probing an unauthenticated web endpoint to identify if the `advanced_val` POST parameter is vulnerable to reflected XSS by checking for unsanitized reflection of input.

## Description

In the context of testing web applications, this step examines POST requests to endpoints like `/██████████_flight/images` to see if user input in `advanced_val` is echoed back without proper HTML/JS escaping. This is a reconnaissance step to confirm the vulnerability before exploitation, targeting public-facing web apps without authentication requirements. Successful identification allows progression to payload injection.

## Requirements

1. Access to the target URL (e.g., https://target.com/██████████_flight/images)
2. Tools like curl or a browser/proxy for sending and inspecting requests
3. Basic understanding of HTTP POST and response parsing

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) to restrict script execution
- Use web application firewalls (WAF) to detect anomalous payloads in POST data
- Log and monitor reflection of user input in responses

## Objectives

1. Confirm the endpoint and parameter exist and are reachable
2. Verify lack of input sanitization for XSS
3. Establish baseline for payload testing

## Instructions

### Step 1: Probe the Endpoint with Benign Input

**Context**: Send a simple POST request to check if `advanced_val` is reflected in the response.

**Command** ([[commands/curl-test-post-parameter]]):
```bash
curl -X POST https://target.com/██████████_flight/images -d "advanced_val=test123" -H "Content-Type: application/x-www-form-urlencoded" -v
```

> This command sends a POST with `advanced_val=test123` and verbose output. Inspect the response body for the exact string `test123` appearing unsanitized (e.g., not as `test123`).

### Step 2: Analyze Response for Reflection

**Context**: Review the HTML/JS in the response to confirm context (e.g., inside a script tag or attribute).

No specific command; use browser dev tools or grep the curl output for the test string.

> Expected: Input appears directly, indicating potential for script injection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-test-post-parameter]]

## Tools Used


## Tags

- [[xss]]
- [[recon]]
