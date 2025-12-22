---
tags:
  - xss
  - recon
  - concrete5
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-xss-test]]'
platforms:
  - Web
techniques:
  - '[[Active Scanning]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: e60c723b-2057-471a-b1c4-c26d54b77ca4
created_at: '2025-12-14T03:15:35.621Z'
updated_at: '2025-12-14T03:15:35.621Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-Reflected-XSS-Endpoints-in-Concrete5

## Summary

This procedure involves systematically testing user input fields in Concrete5 5.7.3.1 to identify points where inputs are reflected back into the HTML output without proper encoding, enabling reflected XSS attacks.

## Description

In Concrete5 5.7.3.1, various application features like search functions, error handling, and form submissions fail to sanitize or encode user inputs before inclusion in the response. An attacker tests these by submitting payloads like `<script>alert(1)</script>` and checking if they appear unescaped in the browser-rendered page. This reconnaissance step is crucial for targeting exploitable endpoints and understanding the application's reflection behavior in a PHP-based web environment.

## Requirements

1. Access to the target Concrete5 instance over HTTP/HTTPS
2. Tools for sending HTTP requests (e.g., curl or browser)
3. Knowledge of common Concrete5 URLs (e.g., /search, /login)

## Defense

Defensive measures and detection strategies:

- Implement output encoding using htmlspecialchars() in PHP templates
- Deploy Content Security Policy (CSP) to block inline scripts
- Monitor for anomalous script tags in web logs

## Objectives

1. Locate all reflected input points in the application
2. Confirm lack of validation/encoding
3. Prepare for payload injection

## Instructions

### Step 1: Probe Common Endpoints

**Context**: Target typical user input areas in Concrete5, such as search queries or redirect parameters, to check for direct reflection.

**Command** ([[commands/curl-xss-test]]):
```bash
curl -G "http://target.concrete5.site/search" --data-urlencode "query=<script>alert(1)</script>" -v
```

> This sends a GET request with an encoded XSS payload. Inspect the response body for the unencoded `<script>` tag, indicating reflection.

### Step 2: Verify in Browser

**Context**: Load the crafted URL in a browser to confirm JavaScript execution.

**Command** ([[commands/curl-xss-test]]):
```bash
curl -G "http://target.concrete5.site/dashboard/users/search" --data-urlencode "keywords=<img src=x onerror=alert(1)>" -v
```

> Check the page source or console for payload execution. Repeat for other endpoints like error pages or file uploads.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-xss-test]]

## Tools Used


## Tags

- [[xss]]
- [[recon]]
- [[concrete5]]
