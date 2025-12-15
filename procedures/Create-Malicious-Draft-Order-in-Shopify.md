---
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
updated_at: '2025-12-14T17:28:58.840Z'
sub_techniques: []
id: 5fe260b9-e6ee-40d2-b097-194dd4356650
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-Draft-Order-in-Shopify

## Summary

This procedure involves creating a product in Shopify with a malicious XSS payload in its name field, then incorporating it into a draft order to set up for later exploitation in the timeline feature.

## Description

In the Shopify Admin Site, product names are not sufficiently sanitized when rendered as descriptions in certain contexts, such as the Draft Orders Timeline after the product is deleted. This procedure injects a JavaScript payload into the product name, creates a draft order with it, preparing for payload persistence and execution. The target environment is the web-based Shopify admin interface, requiring authenticated access. Expected outcomes include a draft order containing the payload without immediate execution.

## Requirements

1. Authenticated Shopify admin account with product creation permissions
2. Web browser access to Shopify admin (e.g., https://admin.shopify.com)
3. Basic knowledge of XSS payloads

## Defense

Defensive measures and detection strategies:

- Implement client-side and server-side input sanitization for all product fields using libraries like DOMPurify
- Monitor for unusual product names containing script tags or event handlers
- Enable Content Security Policy (CSP) to restrict inline script execution in admin interfaces

## Objectives

1. Inject XSS payload into product data
2. Create a draft order referencing the malicious product
3. Ensure payload persists without triggering alerts prematurely

## Instructions

### Step 1: Create Malicious Product

**Context**: Log in to Shopify admin and navigate to create a new product to inject the payload.

No specific command; perform via UI:

1. Go to Products > Add product.
2. Set the product title to: "><img src=x onerror=alert('XSS')>
3. Fill minimal other details (e.g., price) and save.

> This injects the payload into the product name, which will later act as the description.

### Step 2: Create Draft Order with Product

**Context**: Use the malicious product in a new draft order.

No specific command; perform via UI:

1. Navigate to Orders > Drafts > Create draft order.
2. Add the malicious product to the order line items.
3. Save the draft.

> The draft now includes the product with the embedded payload.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- shopify
- injection
