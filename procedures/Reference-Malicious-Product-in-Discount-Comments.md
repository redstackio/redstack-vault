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
updated_at: '2025-12-13T23:55:06.676Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 640a97f3-fe8b-4867-bc47-4d05c5769efa
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Reference-Malicious-Product-in-Discount-Comments

## Summary

This procedure embeds the stored XSS payload by referencing the infected product in a Shopify discount's comments field, propagating the vulnerability to the discounts section.

## Description

After creating a product with an XSS payload, reference it in the comments or notes of a discount code. Shopify's discounts section fails to escape product names when rendered from comments, allowing the payload to persist. This step requires discounts permission and sets up the final trigger. The attack relies on the recent changes to discount timelines that introduced the escaping flaw.

## Requirements

1. Authenticated Shopify staff account with discounts creation permission
2. Access to the admin panel (https://store.myshopify.com/admin/discounts)
3. Existing product with injected XSS payload

## Defense

Defensive measures and detection strategies:

- Escape all referenced entity names (e.g., products) in discount comments using context-aware sanitization
- Implement content security policy (CSP) to block inline scripts in admin views
- Log and review discount creation events for suspicious references to products

## Objectives

1. Link the malicious product to a discount without alerting sanitization
2. Store the reference in comments for rendering
3. Prepare for payload execution on discount view

## Instructions

### Step 1: Access Discounts Section

**Context**: Navigate to the discounts area in the admin panel.

Use the UI to go to Discounts and select or create a new discount code.

> For example, access a URL like https://store.myshopify.com/admin/discounts/367541518396 if editing an existing one.

### Step 2: Add Product Reference in Comments

**Context**: Insert a reference to the infected product in the comments field.

In the comments or internal notes section, type something like "Test discount for product: [Product Name with Payload]" or directly reference by ID.

> The product name containing the payload (e.g., '"'><img src=x onerror=alert(domain.domain)>"') will be stored raw. Save the discount.

### Step 3: Verify Reference Storage

**Context**: Confirm the comment includes the unsanitized product name.

Save and preview the discount details.

> The comments should display the full payload string without HTML rendering at this stage, indicating successful embedding.

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
- stored-xss
- shopify-discounts
