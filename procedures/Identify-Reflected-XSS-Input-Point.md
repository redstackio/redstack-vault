---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
name: Identify-Reflected-XSS-Input-Point
tags:
  - xss
  - recon
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T03:46:37.419Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-Reflected-XSS-Input-Point

## Summary

This procedure involves scanning a web application, specifically a third-party service integrated with Informatica, to identify user inputs that are reflected back into the response without proper sanitization, enabling reflected XSS attacks.

## Description

Reflected XSS occurs when user-supplied input is immediately included in the response without encoding, allowing attackers to inject scripts. In this case, the vulnerability was found in a third-party service used by Informatica during security testing. The procedure targets URL parameters, form fields, or error messages that echo input directly into HTML, JavaScript, or attributes. Prerequisites include access to the web interface and basic knowledge of HTML/JS. Expected outcomes are pinpointing the exact reflection point for payload crafting.

## Requirements

1. Web browser with developer tools (e.g., Chrome DevTools)
2. Network access to the Informatica service and third-party endpoint
3. Optional: Intercepting proxy like Burp Suite for request manipulation

## Defense

Defensive measures and detection strategies:

- Implement content security policy (CSP) to restrict script execution
- Sanitize all user inputs with HTML entity encoding on output
- Use web application firewalls (WAF) to detect and block XSS payloads

## Objectives

1. Discover unsanitized input reflection points
2. Verify lack of output encoding in the third-party service
3. Prepare for payload injection to confirm exploitability

## Instructions

### Step 1: Inspect Application Inputs

**Context**: Examine common entry points like search boxes, URL query strings, or redirect parameters in the third-party service.

Open the web application in a browser and navigate to the Informatica-integrated service. Use the URL bar to append a test string, e.g., `?search=test<abc>`, and submit forms with similar inputs.

> Inspect the page source (right-click > View Page Source) or use DevTools Network tab to see if `<abc>` appears unencoded.

### Step 2: Test for Reflection

**Context**: Inject a harmless script tag to check for execution.

Modify the input to include `<script>alert('XSS')</script>` and observe if an alert pops up upon reflection.

> If reflected without escaping (e.g., as raw tags in source), the vulnerability is confirmed. No command-line tool is needed; this is browser-based.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[web]]
