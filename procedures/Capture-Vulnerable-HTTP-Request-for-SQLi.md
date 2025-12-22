---
tags:
  - recon
  - web
  - http
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T03:15:05.269Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: b33c7615-0522-4fe4-bd88-a7bc14207ea9
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Capture-Vulnerable-HTTP-Request-for-SQLi

## Summary

This procedure involves intercepting and saving a POST request to a web application to identify parameters potentially vulnerable to SQL injection, specifically targeting the 'log' parameter in the Acronis application.

## Description

In web penetration testing, capturing HTTP requests is essential to analyze user inputs for vulnerabilities like SQL injection. This procedure focuses on the Acronis web app at https://www.acronis.cz/, where the 'log' parameter in a POST request lacks proper sanitization, allowing injection attacks. Prerequisites include access to the target URL and tools for request interception. Expected outcomes include a saved request file ready for automated exploitation tools.

## Requirements

1. Network access to https://www.acronis.cz/
2. Browser with developer tools (e.g., Chrome DevTools) or a proxy tool like Burp Suite
3. File system access to save the request

## Defense

Defensive measures and detection strategies:

- Implement web application firewalls (WAF) to monitor and block suspicious request patterns
- Use parameterized queries in backend code to prevent injection
- Log and alert on anomalous request captures or proxy traffic

## Objectives

1. Capture the exact POST request structure including the vulnerable 'log' parameter
2. Save it in a format compatible with exploitation tools like sqlmap
3. Prepare for subsequent vulnerability testing

## Instructions

### Step 1: Intercept the Request

**Context**: Navigate to the target application and trigger the action that sends the POST request with the 'log' parameter, such as submitting a login or log-related form.

**Command** (Manual via DevTools):
Open browser developer tools (F12), go to the Network tab, and perform the action that triggers the POST to https://www.acronis.cz/. Right-click the request and copy it as cURL or raw.

> This captures the full request including method, URL, headers, and body with the 'log' parameter. Save the output to request-cz.txt for use in sqlmap.

### Step 2: Save and Verify

**Context**: Ensure the captured request is complete and includes the vulnerable parameter.

**Command** (Manual save):
Paste the captured request into a text file named request-cz.txt.

> Verify the file contains POST / HTTP/1.1, Host: www.acronis.cz, and Content-Type: application/x-www-form-urlencoded with log=... in the body. This confirms readiness for injection testing.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- recon
- web
- http
