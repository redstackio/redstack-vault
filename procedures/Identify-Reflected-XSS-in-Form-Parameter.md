---
id: proc-1147949-xss-identify
tags:
  - xss
  - web
  - input-sanitization
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
updated_at: '2025-12-14T17:27:35.751Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Identify-Reflected-XSS-in-Form-Parameter

## Summary

This procedure identifies a reflected cross-site scripting (XSS) vulnerability in the 'frm_email' parameter of a POST request to a web form endpoint by injecting and observing JavaScript payloads without proper sanitization.

## Description

In the context of a DoD subdomain form submission, user input in the 'frm_email' field is reflected back in the response without HTML escaping or JavaScript sanitization. This allows attackers to inject payloads like '<script>alert(document.domain)</script>' or SVG-based onload triggers. The procedure uses traffic interception to test and confirm reflection, enabling subsequent chaining with other attacks like CSRF for broader exploitation, such as session hijacking on *.██████████.

## Requirements

1. Access to Burp Suite or similar proxy for intercepting HTTP requests.
2. Ability to submit forms to the target endpoint (https://██████████/██████).
3. Basic knowledge of JavaScript payloads for XSS testing.

## Defense

Defensive measures and detection strategies:

- Implement input sanitization and output encoding (e.g., HTML entity encoding) for user inputs.
- Use Content Security Policy (CSP) to restrict inline script execution.
- Monitor for anomalous JavaScript in request parameters via WAF logs.

## Objectives

1. Confirm reflection of unsanitized input in the response.
2. Validate JavaScript execution in the browser context.
3. Assess potential for payload delivery to authenticated users.

## Instructions

### Step 1: Intercept Form Submission

**Context**: Set up a proxy to capture the legitimate POST request to the vulnerable endpoint.

Use Burp Suite to intercept the request to /██████ on https://██████████, which includes parameters like action=F█████, token=████████, frm_email, frm_zip5=12121, and cmd_submit=Submit.

### Step 2: Inject XSS Payload

**Context**: Modify the 'frm_email' parameter with a test payload to check for reflection and execution.

Inject the payload '"&gt;&lt;svg/onload=alert(document.domain)&gt;' into frm_email and forward the request.

**Expected Output**: The response reflects the payload unescaped, triggering an alert with the document domain (e.g., sub.██████████).

### Step 3: Validate Execution

**Context**: Observe the browser behavior to confirm XSS.

Submit the modified request and check for the alert popup, indicating successful JavaScript execution.

**Expected Output**: Alert box displays the domain, proving the vulnerability.

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

- xss
- reflected-xss
- web-vulnerability
