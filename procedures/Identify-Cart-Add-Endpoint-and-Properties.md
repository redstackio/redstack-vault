---
id: proc-identify-shopify-endpoint-001
tags:
  - recon
  - web
  - endpoint-discovery
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-shopify-cart-injection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T03:15:53.374Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-Cart-Add-Endpoint-and-Properties

## Summary

This procedure involves inspecting the Shopify hardware subdomain's add-to-cart form to identify the endpoint and custom property fields vulnerable to input injection, setting the stage for stored XSS exploitation.

## Description

In the context of testing Shopify's hardware store, examine the form at http://hardware.shopify.com/cart/add. The form uses multipart/form-data for submissions, including parameters like id, production-time, and custom properties such as properties[Artwork file] and properties[Custom text line 1/2/3]. These fields accept user input without sanitization, allowing storage of malicious content that renders as HTML/JavaScript on cart pages. Prerequisites include browser access and developer tools; no authentication is needed.

## Requirements

1. Public access to http://hardware.shopify.com
2. Browser with developer tools (e.g., Chrome DevTools)
3. Basic knowledge of HTTP forms and parameters

## Defense

Defensive measures and detection strategies:

- Implement client-side and server-side input validation for custom properties
- Use Content Security Policy (CSP) to restrict inline JavaScript execution
- Monitor for anomalous form submissions via web application firewall (WAF)

## Objectives

1. Locate the /cart/add endpoint and confirm POST method
2. Identify injectable fields like properties[Artwork file]
3. Verify lack of sanitization for XSS payloads

## Instructions

### Step 1: Inspect the Add-to-Cart Form

**Context**: Use browser tools to analyze the form structure and parameters.

**Command** ([[commands/curl-shopify-cart-injection]]):

Open http://hardware.shopify.com/cart/add in a browser, right-click the form, and select "Inspect Element". Look for <form> tags with action="/cart/add" method="post" enctype="multipart/form-data". Note input fields for properties[Artwork file], etc.

> This reveals the endpoint and fields. Expected output: Form details in the Elements tab, confirming custom properties support arbitrary strings.

### Step 2: Test Basic Submission

**Context**: Send a benign request to validate the endpoint.

**Command** ([[commands/curl-shopify-cart-injection]]):
```bash
curl -X POST http://hardware.shopify.com/cart/add -F "id=976094353" -F "properties[Artwork file]=test"
```

> Submits a test value. Expected output: HTTP 200 or redirect, item added without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-shopify-cart-injection]]

## Tools Used


## Tags

- [[recon]]
- [[web]]
