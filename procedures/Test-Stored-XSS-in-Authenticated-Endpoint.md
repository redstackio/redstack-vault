---
tags:
  - xss
  - stored-xss
  - input-sanitization
  - web-testing
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:49.569Z'
sub_techniques: []
id: 5bb60c99-6070-434c-b65e-fde81e7b5025
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Test-Stored-XSS-in-Authenticated-Endpoint

## Summary

This procedure tests for stored Cross-Site Scripting (XSS) vulnerabilities in an authenticated endpoint of a third-party vendor system by injecting payloads and verifying persistence and execution.

## Description

Stored XSS occurs when user input is inadequately sanitized and stored, then rendered without encoding, allowing arbitrary JavaScript execution for any user viewing the content. In this scenario, the vendor's event management system, accessible via the HackerOne subdomain, lacks proper validation in an authenticated input field. Prerequisites include valid login credentials; expected outcomes are payload persistence leading to alerts on page reload.

## Requirements

1. Valid authentication credentials for the vendor endpoint.
2. Access to https://events.hackerone.com.
3. Browser with developer tools for payload testing.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and output encoding (e.g., HTML entity encoding).
- Use Content Security Policy (CSP) to block inline scripts.
- Log and monitor anomalous JavaScript execution attempts.

## Objectives

1. Inject and store malicious payload.
2. Confirm execution on subsequent views.
3. Assess impact on the integrated subdomain.

## Instructions

### Step 1: Authenticate and Locate Input Field

**Context**: Log in to the vendor system and identify a storable input field, such as an event description or comment section.

Navigate to the authenticated endpoint via https://events.hackerone.com and inspect forms.

### Step 2: Inject Test Payload

**Context**: Submit a benign XSS payload to test for sanitization flaws.

Enter `<script>alert('Stored XSS')</script>` into the input field and submit.

> Upon submission, the payload is stored; reload the page or view the content to trigger execution, confirming the vulnerability.

**Expected Output**: Alert box displaying 'Stored XSS' on page render.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[xss]]
- [[web-testing]]
