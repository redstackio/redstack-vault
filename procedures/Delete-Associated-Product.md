---
tags:
  - xss
  - shopify
  - product-deletion
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
updated_at: '2025-12-14T17:28:58.834Z'
sub_techniques: []
id: 4dadabd2-4968-4558-88e3-38ded4b15fe5
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Delete-Associated-Product

## Summary

This procedure deletes the product containing the XSS payload from the Shopify store, forcing the Draft Orders Timeline to render the raw unsanitized description instead of a product link.

## Description

Product deletion removes the sanitized link rendering in the timeline, causing fallback to the raw product name (payload) as description. Performed via Shopify admin UI, this step is crucial for triggering the vulnerability. Requires product management permissions; outcomes include the product gone but order data intact with payload.

## Requirements

1. Authenticated Shopify admin with product deletion rights
2. Identification of the malicious product ID
3. Completed draft order referencing the product

## Defense

Defensive measures and detection strategies:

- Prevent deletion of products in active orders or log such actions
- Sanitize fallback descriptions even without product links
- Alert on bulk or suspicious product deletions

## Objectives

1. Remove the product to break link rendering
2. Ensure order timeline will use raw description
3. Confirm deletion without affecting order

## Instructions

### Step 1: Locate and Delete Product

**Context**: Navigate to products and remove the malicious one.

No specific command; perform via UI:

1. In Shopify admin, go to Products.
2. Search for the product with the payload name.
3. Select it and click 'Delete'.
4. Confirm deletion.

> Product is now deleted, forcing raw description display in timelines.

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
- deletion
