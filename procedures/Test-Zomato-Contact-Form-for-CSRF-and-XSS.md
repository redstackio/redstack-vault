---
id: proc-test-zomato-csrf-xss
tags:
  - csrf
  - xss
  - testing
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:26.777Z'
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
# Test-Zomato-Contact-Form-for-CSRF-and-XSS

## Summary

This procedure tests Zomato's contact form at https://www.zomato.com/contact for CSRF vulnerabilities by attempting cross-origin submissions and for reflected XSS by injecting script payloads into 'name' and 'email' fields, confirming lack of input sanitization.

## Description

In a web security assessment, access the contact form and use interception tools to simulate submissions. Without proper CSRF tokens, forms can be submitted from external sites. Reflected XSS occurs when user input in fields is echoed back unsanitized, allowing JavaScript injection. This targets unauthenticated and authenticated users, potentially leading to data submission or script execution on victim browsers.

## Requirements

1. Burp Suite Professional for traffic interception and manipulation
2. Access to a browser for form interaction
3. Target URL: https://www.zomato.com/contact

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens validated on server-side for all forms
- Sanitize and escape user inputs in 'name' and 'email' fields using HTML entity encoding
- Monitor for anomalous form submissions from unexpected referers

## Objectives

1. Confirm absence of CSRF protection
2. Verify reflected XSS in form response
3. Document vulnerable endpoints for reporting

## Instructions

### Step 1: Intercept Form Submission

**Context**: Set up proxy to capture traffic and test basic form functionality.

Configure Burp Suite as a browser proxy and navigate to https://www.zomato.com/contact. Fill and submit the form with benign data, observing the POST request to identify parameters like 'name', 'email', and any 'csrf_token'.

### Step 2: Test for CSRF

**Context**: Attempt submission from a different origin to check protection.

Create a simple HTML page on a local server with a form posting to https://www.zomato.com/contact using the same parameters but without a valid token. Load the page in a browser and submit; if successful, CSRF is vulnerable.

### Step 3: Test for Reflected XSS

**Context**: Inject payloads to check if input reflects unsanitized.

In the intercepted request, modify 'name' to `<script>alert(1)</script>` and 'email' to `vibhuti123i"><script>alert(1)</script>`. Forward the request and observe the response; if an alert triggers, XSS is confirmed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[csrf]]
- [[xss]]
