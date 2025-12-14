---
tags:
  - xss
  - payload
  - injection
  - saml
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:20.051Z'
skill_level: intermediate
impact_level: high
sub_techniques: []
id: c9b07a93-3676-403a-81e2-52a94ff4ed2d
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-SAMLResponse

## Summary

This procedure modifies the SAMLResponse parameter in a captured request to inject a JavaScript payload, exploiting reflected XSS to execute code in the browser upon resubmission.

## Description

The vulnerability stems from lack of sanitization in the SAML ACS endpoint, allowing the injected payload to be reflected into the HTML response. Using a polyglot payload like `"><svg/onload=alert('0xElkot')>` breaks out of the attribute context and executes via onload. This was tested on the DoD application's `/+CSCOE+/saml/sp/acs?tgname=a` endpoint. Prerequisites: Intercepted request in Burp Repeater. Expected outcome: JavaScript alert or equivalent execution, confirming XSS.

## Requirements

1. Burp Suite with request in Repeater
2. Knowledge of HTTP request structure
3. Target endpoint that reflects input

## Defense

Defensive measures and detection strategies:

- Sanitize and encode all user inputs, especially SAML assertions
- Implement Content Security Policy (CSP) to block inline scripts
- Monitor for JavaScript errors or unusual onload events in logs

## Objectives

1. Craft and insert the XSS payload
2. Resend the modified request
3. Verify execution through browser interaction

## Instructions

### Step 1: Edit Request Body

**Context**: Target the SAMLResponse parameter for injection.

In Burp Repeater, locate the body (Content-Type: application/x-www-form-urlencoded).

Modify SAMLResponse to: `SAMLResponse="><svg/onload=alert('0xElkot')>`

Update Content-Length: 46

> Expected output: Request body reflects the change; no syntax errors in Burp.

### Step 2: Resend and Observe

**Context**: Submit the tampered request to trigger reflection.

Click 'Send' in Repeater.

Inspect the response and browser for execution.

> Payload executes if alert('0xElkot') pops up. Success confirms vulnerability; extend payload for real attacks like document.cookie theft.

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
- [[injection]]
