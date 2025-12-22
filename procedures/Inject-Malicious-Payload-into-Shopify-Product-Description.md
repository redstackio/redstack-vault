---
id: proc-uuid-1
tags:
  - xss
  - injection
  - shopify
type: procedure
tools: []
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
updated_at: '2025-12-14T17:25:53.012Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Payload-into-Shopify-Product-Description

## Summary

This procedure injects a malicious HTML/JavaScript payload into a Shopify product's description field using the admin interface, storing it for later execution in a stored XSS attack.

## Description

In the context of Shopify's Handshake plugin, the product description field lacks proper sanitization when updated. An attacker with merchant access can enable HTML mode and insert executable code, such as an image tag with an onerror handler, which will be persisted and rendered unsafely on the Handshake portal. This sets up the stored XSS for propagation via GraphQL.

## Requirements

1. Authenticated access to Shopify admin panel
2. Handshake plugin installed and configured in the store
3. Basic knowledge of HTML/JavaScript payloads

## Defense

Defensive measures and detection strategies:

- Implement client-side and server-side HTML sanitization in product editors (e.g., using libraries like DOMPurify)
- Monitor GraphQL queries for suspicious payloads in productUpdate mutations
- Enable Content Security Policy (CSP) on rendering pages to block inline scripts

## Objectives

1. Store malicious script in product description without triggering errors
2. Prepare payload for propagation to shared domain
3. Enable execution on viewer browsers for impact

## Instructions

### Step 1: Access Product Creation

**Context**: Log into the Shopify admin and navigate to product management to create a new entry.

Go to the Shopify admin dashboard, select "Products" > "Add product".

### Step 2: Enable HTML Mode and Inject Payload

**Context**: Switch to HTML editing mode to bypass rich text restrictions and insert the raw payload.

In the product description field, click the "< >" button to enable HTML mode. Insert the following payload:

```html
<img src=x onerror=prompt(document.domain)>
```

Set the product title (e.g., "Test Product"), status to "Active", and save the product.

> This payload uses an invalid image source to trigger the onerror event, executing JavaScript to prompt the current domain.

### Step 3: Verify Storage

**Context**: Confirm the payload is stored without alteration.

Edit the product again and check that the HTML mode shows the exact payload intact.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[injection]]
- [[shopify]]
