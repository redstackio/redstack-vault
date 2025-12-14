---
id: proc-trigger-xss-redirect-001
tags:
  - xss-execution
  - cookie-theft
  - phishing
  - redirect-trigger
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T03:15:52.885Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
---
# Trigger-XSS-via-Redirect-Link

## Summary

This procedure activates the injected XSS payload by accessing the generated redirect link in the Shopify admin, resulting in JavaScript execution for data exfiltration or phishing.

## Description

After creating a malicious redirect, clicking the generated link (e.g., https://[shop].myshopify.com/malicious-test) causes the browser to interpret the javascript: or data: URI, executing the embedded script in the admin's session context. Simple payloads alert the domain for proof, while advanced ones steal cookies (e.g., via alert(document.cookie)) and redirect to external sites like Google for phishing. This exploits the trust in admin-generated links, potentially leading to full account compromise.

## Requirements

1. Successfully created malicious redirect (from prior procedure)
2. Active admin session in the browser
3. Payload designed for execution (e.g., non-breaking script)

## Defense

Defensive measures and detection strategies:

- Block or warn on non-HTTP redirect schemes in admin interfaces
- Implement client-side validation and CSP to prevent URI-based execution
- Monitor for unexpected JavaScript alerts or redirects in admin sessions
- Educate admins on verifying generated links before clicking

## Objectives

1. Execute arbitrary JavaScript in the admin browser
2. Steal sensitive data like cookies or session tokens
3. Facilitate follow-on attacks like phishing or hijacking

## Instructions

### Step 1: Locate Generated Link

**Context**: Identify the entry to access.

In the redirects list, find the new entry for /malicious-test.

> The full URL is displayed and clickable.

### Step 2: Access the Redirect Link

**Context**: Trigger the payload interpretation.

Click the redirect URL in the admin panel.

> Browser processes the URI scheme, executing the JavaScript.

### Step 3: Observe Execution

**Context**: Validate impact and potential exfiltration.

For the alert payload, a dialog shows document.domain. For data: URI, an alert displays cookies, then redirects to http://www.google.com.

> Network tools (e.g., dev console) may show exfiltration if payload sends data outbound.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-execution]]
- [[cookie-theft]]
