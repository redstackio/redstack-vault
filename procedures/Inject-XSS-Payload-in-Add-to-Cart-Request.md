---
tags:
  - xss
  - injection
  - shopify
type: procedure
tools:
  - '[[tools/XMLHttpRequest]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:37.103Z'
sub_techniques: []
id: 66e1683e-6845-4a8b-a802-d670f33e6010
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
---
---

# Inject-XSS-Payload-in-Add-to-Cart-Request

## Summary

This procedure intercepts the multipart/form-data POST request during cart addition and injects an XSS payload into the 'properties[Artwork file]' parameter, exploiting insufficient sanitization.

## Description

The attack targets the /cart/add endpoint on Shopify sites like hardware.shopify.com, where the property name from form data is reflected unsanitized in the cart view. By modifying the Content-Disposition header, an HTML payload is injected, allowing JS execution on mouseover. This requires a proxy for interception and works in an authenticated or guest session.

## Requirements

1. Web proxy (e.g., Burp Suite) configured to intercept traffic
2. Valid image file (PNG) for upload
3. Access to the product page from previous procedure

## Defense

Defensive measures and detection strategies:

- Sanitize and escape all reflected user inputs in views
- Validate multipart form boundaries and parameter names
- Implement Content Security Policy (CSP) to block inline JS

## Objectives

1. Successfully modify and forward the add-to-cart request
2. Add item with injected payload to cart
3. Confirm no server-side rejection of malformed properties

## Instructions

### Step 1: Trigger Add to Cart

**Context**: Initiate the legitimate request to capture the base form data.

Select an image on the product page and click 'Add to Cart'.

> This sends POST to http://hardware.shopify.com/cart/add. Intercept in proxy.

### Step 2: Modify Payload

**Context**: Alter the specific parameter to inject XSS.

In the intercepted request, change:

Content-Disposition: form-data; name="properties[Artwork file]"

to

Content-Disposition: form-data; name="properties[Artwork file<img src='test' onmouseover='alert(2)'>]"

Include a valid PNG binary in the body after the boundary.

> Ensures the payload is reflected as HTML in the cart. Forward the request.

### Step 3: Verify Addition

**Context**: Check if the item was added without errors.

Forward the request and inspect the response (should be 200 OK or redirect).

> Expected: No validation errors; item queued in session cart.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Drive-by Compromise]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/XMLHttpRequest]]

## Tags

- [[xss]]
- [[injection]]
- [[shopify]]
