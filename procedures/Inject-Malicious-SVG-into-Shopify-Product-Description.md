---
id: proc-uuid-1
tags:
  - xss
  - injection
  - shopify
type: procedure
tools:
  - '[[tools/Browser]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:56:03.908Z'
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
# Inject-Malicious-SVG-into-Shopify-Product-Description

## Summary

This procedure injects a stored XSS payload into Shopify's rich text editors by embedding a malicious SVG image using a data: URL, which evades initial sanitization and persists in product descriptions.

## Description

In Shopify's admin interface, rich text editors for products, pages, and gifts allow HTML input including <img> tags with data: URLs. Attackers can base64-encode an SVG containing JavaScript in an onload attribute. When saved, the data: URL converts to a blob: URL, but the payload remains executable upon direct access. This targets authenticated users viewing or editing content, leading to script execution in their session. Prerequisites include a Shopify account with content creation permissions.

## Requirements

1. Authenticated access to Shopify admin (e.g., staff or owner account)
2. Browser with developer tools for encoding payloads
3. Target store URL (e.g., https://shop.myshopify.com/admin/products)

## Defense

Defensive measures and detection strategies:

- Sanitize data: URLs in rich text editors to prevent SVG embedding
- Disable direct blob: URL access for images or strip onload handlers
- Monitor for anomalous JavaScript execution in admin logs

## Objectives

1. Persist malicious payload in store content
2. Evade client-side sanitization
3. Set up for victim-triggered execution

## Instructions

### Step 1: Prepare Malicious SVG Payload

**Context**: Encode an SVG with JavaScript to execute on load, such as alerting or making requests.

No command needed; manually craft and base64-encode the SVG in the browser console:

```javascript
// Example SVG content
'<svg xmlns="http://www.w3.org/2000/svg" width="1" height="1"><circle/><script onload="var req = new XMLHttpRequest(); req.open(\'GET\', \'/admin\', false); req.send(null); console.log(req.responseText);"/></svg>'
// Then base64 encode: btoa(that string)
```

> This generates the base64 string for the src attribute.

### Step 2: Insert into Product Description

**Context**: Create or edit a product and embed the <img> tag in the rich text editor.

Navigate to /admin/products/new and in the description field, insert:

```html
<img src="data:image/svg+xml;base64,[YOUR_BASE64_ENCODED_SVG]" alt="Product Image">
```

Save the product.

> The editor accepts the input without stripping the data: URL, storing it persistently.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser]]

## Tags

- xss
- injection
