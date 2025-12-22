---
id: proc-shopify-create-product-001
tags:
  - shopify
  - setup
  - testing
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:37.803Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Zero-Price-Product-for-Testing

## Summary

This procedure sets up a test product in a Shopify store with zero price and zero shipping taxes, facilitating vulnerability testing in the checkout process without requiring real payments or credit card details.

## Description

In the context of exploiting the stored XSS vulnerability in Shopify's checkout, this initial setup creates a simple product that can be purchased for free. This simplifies the attack by avoiding financial hurdles and focuses on the injection and execution phases. The procedure assumes admin access to the Shopify dashboard and targets web-based store management.

## Requirements

1. Valid Shopify admin account with product creation permissions
2. Access to the store's admin dashboard at admin.shopify.com
3. Web browser for navigation

## Defense

Defensive measures and detection strategies:

- Monitor admin actions for creation of zero-priced products, which may indicate testing or abuse
- Implement rate limiting on product creation in admin panels
- Log and alert on unusual product configurations like $0 pricing

## Objectives

1. Establish a testable purchase flow
2. Avoid payment complications during exploitation
3. Prepare the environment for unauthenticated checkout

## Instructions

### Step 1: Access Admin Dashboard

**Context**: Log in to manage store products.

Navigate to your Shopify admin at `admin.shopify.com` and select 'Products' from the sidebar.

### Step 2: Create New Product

**Context**: Define a basic product with minimal details.

Click 'Add product', enter a title like 'Test Product', set price to $0.00, and in inventory, ensure it's available.

### Step 3: Configure Shipping and Taxes

**Context**: Eliminate costs to enable free checkout.

In the shipping section, set taxes to $0, and save the product. Publish it to the online store.

**Expected Output**: Product appears on the store frontend with $0 price.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- shopify
- product-creation
- testing-setup
