---
id: proc-uuid-001
name: Test-Contact-Form-for-CSRF-and-XSS-Vulnerabilities
tags:
  - csrf
  - xss
  - testing
type: procedure
tools:
  - '[[tools/Burp-Suite-Professional]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:03.341Z'
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
# Test-Contact-Form-for-CSRF-and-XSS-Vulnerabilities

## Summary

This procedure tests Zomato's contact form for CSRF and XSS vulnerabilities by submitting various payloads to identify missing protections.

## Description

The contact form at https://www.zomato.com/contact accepts POST requests with fields like name, email, phone, message, and csrf_token. Testing reveals no enforcement of CSRF tokens and inadequate sanitization of name and email fields, allowing cross-site submissions and script injection. This is performed in a browser environment to simulate real attacks.

## Requirements

1. Access to a modern browser like Firefox
2. Network connectivity to https://www.zomato.com/contact
3. Optional: Burp Suite for intercepting requests

## Defense

Defensive measures and detection strategies:

- Implement and validate CSRF tokens on all state-changing forms
- Sanitize and encode user inputs in name and email fields
- Monitor for anomalous form submissions from external referers

## Objectives

1. Confirm lack of CSRF protection
2. Identify XSS entry points in input fields
3. Validate vulnerability for chaining attacks

## Instructions

### Step 1: Manual Form Submission Testing

**Context**: Submit legitimate and malformed requests to check for validation errors.

No specific command; use browser dev tools or Burp Suite to send POST to https://www.zomato.com/contact with parameters: name=test, email=test@example.com, phone=123, message=hi, csrf_token=anyvalue. Test logged-in and anonymous.

> Expected: Submissions succeed without token validation, indicating CSRF risk.

### Step 2: XSS Payload Testing

**Context**: Inject script tags into fields to test reflection.

Intercept with Burp Suite and modify name to <script>alert(1)</script>, email to "<script>alert(document.cookie)</script>.

> Expected: Payloads accepted, setting up for XSS confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite-Professional]]

## Tags

- [[csrf]]
- [[xss]]
