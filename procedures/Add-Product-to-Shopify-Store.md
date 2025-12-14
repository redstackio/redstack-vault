---
tags:
  - shopify
  - product
  - creation
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Client Configurations]]'
updated_at: '2025-12-14T17:24:56.755Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 521e88ed-3cdf-45be-a5e9-f431859d2039
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Client Configurations]]'
---
# Add-Product-to-Shopify-Store

## Summary

This procedure creates a new product in a Shopify store to generate a valid product ID, which is required as a parameter for querying the vulnerable Google Sales Channel endpoint.

## Description

Products in Shopify are assigned unique numeric IDs upon creation, visible in the admin interface. This ID is used in the exploitation URL to trigger the information disclosure. The procedure is straightforward via the admin panel and ensures the store has content for testing. In real attacks, product IDs might be discovered through enumeration if partially public, but here it's for controlled setup.

## Requirements

1. Admin access to Products section
2. Basic product details (title, description optional)
3. Google Sales Channel already installed

## Defense

Defensive measures and detection strategies:

- Limit product creation to trusted admins
- Monitor for unusual product additions in logs
- Use inventory management to track changes

## Objectives

1. Generate a usable product ID for endpoint testing
2. Populate the store minimally without affecting sales
3. Verify product visibility in admin

## Instructions

### Step 1: Access Products Section

**Context**: Log in and navigate to create a new product.

Web interface:

- Shopify admin > Products > Add product

> Expected output: Blank product form loads.

### Step 2: Create and Save Product

**Context**: Fill minimal details and save to assign an ID.

Web-based:

- Enter title (e.g., "Test Product")
- Add description if needed
- Set status to Active
- Click Save

> Product saves with auto-generated ID. Expected output: Product detail page with ID in URL (e.g., /products/1234567890).

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Client Configurations]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[shopify]]
- [[product]]
- [[creation]]
