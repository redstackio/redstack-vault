---
tags:
  - xss
  - reflected-xss
  - parameter-testing
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 00d05b95-288e-41ff-8320-8f11f5a64eb1
created_at: '2025-12-13T23:55:20.615Z'
updated_at: '2025-12-13T23:55:20.615Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Test-VK-Video-Search-Parameters-for-XSS

## Summary

This procedure tests the 'date', 'len', and 'order' parameters in VK.com's /video search endpoint for reflected XSS vulnerabilities by injecting test payloads and verifying if they are reflected unsanitized in the response, confirming potential for JavaScript execution.

## Description

In the context of web application security testing, this procedure targets the video search functionality of VK.com where user-supplied inputs in specified parameters are not properly escaped, allowing reflected cross-site scripting. The attack scenario involves sending crafted HTTP GET requests to the /video endpoint and inspecting responses for payload reflection. Prerequisites include a web browser or proxy tool; expected outcomes are confirmation of the vulnerability, enabling further exploitation like session theft. This was originally discovered in a HackerOne report (#1052856).

## Requirements

1. Access to VK.com over HTTPS
2. Web proxy tool like Burp Suite for request interception and modification
3. Basic knowledge of HTML and JavaScript payloads

## Defense

Defensive measures and detection strategies:

- Implement input sanitization and output encoding (e.g., HTML entity encoding) for all user-supplied parameters
- Use Content Security Policy (CSP) to restrict script execution
- Monitor for anomalous JavaScript in logs or via Web Application Firewall (WAF) rules detecting common XSS payloads

## Objectives

1. Confirm reflection of payloads in 'date', 'len', and 'order' parameters
2. Validate JavaScript execution in the browser context
3. Assess potential for escalation to data exfiltration

## Instructions

### Step 1: Set Up Proxy and Navigate to Endpoint

**Context**: Configure a proxy to intercept traffic to VK.com's /video search to allow parameter manipulation.

Intercept requests using Burp Suite by setting the browser proxy to 127.0.0.1:8080 and enabling invisible proxying.

Navigate to a video search URL like `https://vk.com/video?q=test` and perform a search to capture a baseline request.

> This establishes control over outgoing requests for payload injection.

### Step 2: Inject Test Payloads

**Context**: Append XSS payloads to the vulnerable parameters to test for reflection and execution.

Modify the intercepted request by adding payloads to the parameters, e.g., `date=<script>alert('XSS')</script>`, `len=<script>alert('XSS')</script>`, `order=<script>alert('XSS')</script>`.

Forward the request and load the response in the browser.

> If successful, the alert triggers, and the payload appears unescaped in the page source, indicating the vulnerability.

### Step 3: Verify Reflection

**Context**: Inspect the response to ensure the payload is reflected without sanitization.

View the page source or use browser dev tools (F12) to search for the injected script tag.

> Expected: Raw `<script>` tag in HTML output, confirming improper escaping.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[xss]]
- [[web]]
- [[testing]]
