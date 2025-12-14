---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
name: Identify-and-Test-Reflected-XSS-in-JavaScript-File
tags:
  - xss
  - reflected-xss
  - javascript
  - testing
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-13T23:52:24.993Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Identify-and-Test-Reflected-XSS-in-JavaScript-File

## Summary

This procedure identifies a reflected Cross-Site Scripting (XSS) vulnerability in the jquery.base.js file on the Rockstar Games website by testing for inadequate input sanitization in JavaScript contexts, allowing confirmation of payload reflection and execution in the browser.

## Description

In the context of the Rockstar Games site for The Ballad of Gay Tony, the jquery.base.js file fails to properly encode or sanitize reflected user inputs from URL parameters or form data. This enables attackers to inject JavaScript that executes in the victim's browser when the page loads. The procedure involves intercepting traffic, injecting test payloads, and verifying execution across multiple site areas, highlighting the vulnerability's scope for medium-severity impacts like data theft.

## Requirements

1. Access to a web proxy tool like Burp Suite for request interception
2. Modern web browser with developer tools enabled
3. Public network access to http://www.rockstargames.com/theballadofgaytony/

## Defense

Defensive measures and detection strategies:

- Implement content security policy (CSP) to restrict script execution
- Use output encoding libraries like DOMPurify for JavaScript contexts
- Monitor for anomalous script injections via web application firewall (WAF) logs

## Objectives

1. Confirm reflection of unsanitized inputs in jquery.base.js
2. Verify payload execution in browser DOM
3. Assess exploitability across site sections

## Instructions

### Step 1: Intercept Site Traffic

**Context**: Set up a proxy to capture requests to the vulnerable JS file and identify reflection points.

Use Burp Suite to proxy traffic:

Intercept the request to http://www.rockstargames.com/theballadofgaytony/js/jquery.base.js and inspect parameters.

> Expected output: Raw HTTP request showing potential reflection parameters like query strings.

### Step 2: Inject Test Payload

**Context**: Append a benign payload to test for XSS without causing harm.

Modify the request with a payload like ?param=<script>alert('XSS')</script> and forward it.

> Expected output: Alert dialog in the browser confirming execution; check console for errors.

### Step 3: Validate Multi-Area Impact

**Context**: Test payload in different site sections to gauge scope.

Repeat injection in various pages loading jquery.base.js.

> Expected output: Consistent execution, indicating broad vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Vulnerability Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]
- [[tools/Browser-Developer-Tools]]

## Tags

- [[xss]]
- [[reflected-xss]]
- [[web]]
