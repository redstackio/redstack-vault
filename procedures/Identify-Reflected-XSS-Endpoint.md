---
tags:
  - xss
  - recon
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-xss-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T00:11:15.798Z'
sub_techniques: []
id: fdb443e4-f431-4406-83f3-b1ac4ee534df
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify Reflected XSS Endpoint

## Summary

This procedure involves reconnaissance to identify parameters in a web application's endpoint, such as the Ambassador Manage page on m.tiktok.com, that reflect user input without sanitization, setting the stage for XSS exploitation.

## Description

In a reflected XSS attack, user-supplied input is immediately rendered back in the response without proper encoding, allowing attackers to inject scripts. Target the m.tiktok.com path's Ambassador Manage endpoint, where insufficient input sanitization enables script injection. Prerequisites include access to the web app and tools for request inspection. Expected outcomes: Confirmation of a vulnerable reflection point, enabling payload crafting.

## Requirements

1. Web browser with developer tools or proxy like Burp Suite
2. Network access to the target endpoint (m.tiktok.com)
3. Basic knowledge of HTML and JavaScript payloads

## Defense

Defensive measures and detection strategies:

- Implement content security policy (CSP) to restrict script execution
- Use output encoding (e.g., HTML entity encoding) on all user inputs
- Monitor for anomalous requests with script tags via WAF logs

## Objectives

1. Locate unsanitized input reflection in the endpoint
2. Verify potential for script execution
3. Prepare for payload delivery

## Instructions

### Step 1: Inspect Endpoint Requests

**Context**: Access the Ambassador Manage endpoint and capture requests to identify input parameters.

**Command** ([[commands/curl-xss-test]]):
```bash
curl -X GET "https://m.tiktok.com/ambassador/manage?param=test" -v
```

> This sends a basic request to the endpoint, displaying verbose output to inspect how 'test' is reflected in the response body. Look for direct insertion into HTML.

### Step 2: Test for Reflection

**Context**: Inject a simple payload to check if it executes or appears unsanitized.

**Command** ([[commands/curl-xss-payload]]):
```bash
curl -X GET "https://m.tiktok.com/ambassador/manage?search=<script>alert('test')</script>" -v
```

> If the payload reflects without encoding (e.g., as raw HTML), it confirms vulnerability. In a browser, this would trigger an alert.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-xss-test]]
- [[commands/curl-xss-payload]]

## Tools Used


## Tags

- [[xss]]
- [[recon]]
