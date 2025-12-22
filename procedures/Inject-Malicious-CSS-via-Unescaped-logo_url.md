---
tags:
  - css-injection
  - stored-injection
  - web
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: e52e979f-d710-4981-8bd2-8781d3f3a7bf
created_at: '2025-12-14T03:47:12.683Z'
updated_at: '2025-12-14T03:47:12.683Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inject-Malicious-CSS-via-Unescaped-logo_url

## Summary

This procedure exploits a stored CSS injection vulnerability in the product creation feature by submitting a malicious logo_url parameter that is not properly escaped, allowing CSS code to be injected into a style tag and stored for display to other users.

## Description

In vulnerable web applications like the Coinbase product creation endpoint, the logo_url parameter is directly concatenated into HTML without proper escaping. An attacker can craft input to close the URL attribute and inject a style tag with malicious CSS properties. When the product page is viewed, the injected styles are applied, potentially allowing visual defacement or data exfiltration via CSS selectors (though limited here). The attack requires authenticated access to create products and relies on the storage mechanism to persist the injection. CSP prevents escalation to XSS, confining impact to CSS-only effects. This was reported in HackerOne #315865 on February 14, 2018.

## Requirements

1. Authenticated session with permission to create products
2. Access to the web form or API for product creation
3. Web browser for manual testing or API client like curl for automation

## Defense

Defensive measures and detection strategies:

- Implement proper input sanitization and escaping for all user-controlled parameters, especially those inserted into HTML attributes
- Enforce strict Content Security Policy (CSP) to block inline styles and scripts
- Validate and whitelist allowed URL formats for logo_url, rejecting any containing quotes or style keywords
- Monitor for anomalous product creation requests with suspicious URL patterns

## Objectives

1. Inject and store malicious CSS code via the logo_url parameter
2. Verify style manipulation on product view pages
3. Assess potential for escalation (blocked by CSP in this case)

## Instructions

### Step 1: Prepare Malicious Payload

**Context**: Craft a payload that escapes the URL attribute and injects a style tag with test CSS to change page appearance.

Use a payload like: `https://example.com/logo.png" style="background-color: red; color: blue;" onclick="alert(1)"`. The onclick will be blocked, but the style will apply.

### Step 2: Submit Product Creation Request

**Context**: Use the web form or API to create a new product, inserting the payload into the logo_url field.

Navigate to the product creation page (e.g., /products/new) and fill in required fields. Set logo_url to the payload. Submit the form.

If using API (assuming POST to /api/products):

```bash
curl -X POST https://coinbase.example.com/api/products \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{"name":"Test Product","logo_url":"https://example.com/logo.png\" style=\"background-color: red;\""}'
```

> This command sends the malicious payload. Expected output: JSON response confirming product creation with ID.

### Step 3: Verify Injection

**Context**: View the created product to confirm the CSS injection takes effect.

Navigate to the product page (e.g., /products/{id}). Inspect the HTML source; look for the injected style tag in the logo rendering. The page background should turn red, confirming success.

**Success Indicators**:
- Product page loads with modified styles (e.g., red background)
- No JavaScript alerts (due to CSP)
- HTML source shows injected style attribute

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[css-injection]]
- [[stored-injection]]
- [[web]]
