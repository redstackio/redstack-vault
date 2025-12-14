---
id: proc-uuid-1
tags:
  - csrf
  - analysis
  - web-vuln
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:49.389Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
  - '[[Exploit Public-Facing Application]]'
---
---

# Analyze-Login-Page-for-CSRF-Vulnerabilities

## Summary

This procedure involves inspecting the login form on www.drive2.ru to detect missing FCTX anti-CSRF token validation, reCAPTCHA bypass opportunities, and XSS in the rememberMe parameter, confirming the feasibility of a CSRF attack combined with script injection.

## Description

In the context of web security testing, analyze the login endpoint at https://www.drive2.ru/reception/?.AMRU=https%3A%2F%2Fwww.drive2.ru%2F. The target environment is a web application using FCTX for CSRF protection, but validation is absent. Expected outcomes include identifying that login requests succeed without the FCTX token, fake reCAPTCHA responses are accepted, and the rememberMe field allows arbitrary HTML/JS injection, enabling session hijacking via CSRF and XSS.

## Requirements

1. Browser with developer tools (e.g., Chrome DevTools)
2. Access to the target login page
3. Optional: Proxy tool like Burp Suite for request interception

## Defense

Defensive measures and detection strategies:

- Implement strict FCTX token validation on all state-changing endpoints
- Enforce valid reCAPTCHA responses server-side
- Sanitize and escape all user inputs, including rememberMe, to prevent XSS
- Monitor for anomalous login patterns from the same IP

## Objectives

1. Confirm absence of CSRF protection to enable forged requests
2. Verify reCAPTCHA bypass for automated exploitation
3. Test XSS injection in rememberMe for code execution

## Instructions

### Step 1: Inspect Login Form Elements

**Context**: Load the login page and examine the HTML source and network requests to identify token usage.

Open https://www.drive2.ru/login in a browser, right-click the form, and select "Inspect Element". Look for FCTX token input and g-recaptcha-response field. Submit a test login without modifying the FCTX token.

> Observe in the Network tab that the request succeeds without token validation.

### Step 2: Test reCAPTCHA Bypass

**Context**: Attempt login with a fabricated reCAPTCHA token to check enforcement.

In developer tools, edit the g-recaptcha-response value to a fake string like "fake-token". Submit the form with valid credentials.

> Expected: Login proceeds without CAPTCHA challenge, confirming bypass.

### Step 3: Probe rememberMe for XSS

**Context**: Inject a test payload into rememberMe to detect sanitization flaws.

Set rememberMe to `<img src=x onerror=alert(document.domain)>` and submit. Check if an alert pops on the response page.

> Expected: JavaScript executes, indicating reflected XSS vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[xss]]
- [[web]]
