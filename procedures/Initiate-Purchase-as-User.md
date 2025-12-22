---
id: proc-shopify-initiate-purchase-001
tags:
  - shopify
  - checkout
  - purchase
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
updated_at: '2025-12-14T03:46:37.798Z'
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
# Initiate-Purchase-as-User

## Summary

This procedure simulates an unauthenticated user starting a purchase on a Shopify store to access the checkout form at checkout.shopify.com, setting the stage for payload injection.

## Description

As part of the stored XSS attack chain, this step involves navigating to the test product's page and initiating a buy action. It requires no authentication and redirects to the hosted checkout service, where customer details can be entered. This targets web storefronts and assumes the product from the previous procedure is live.

## Requirements

1. Public access to the Shopify store frontend
2. Created test product visible on the store
3. Web browser

## Defense

Defensive measures and detection strategies:

- Rate limit checkout initiations per IP to prevent abuse
- Monitor for repeated purchases of zero-priced items
- Log user agents and IPs starting checkouts

## Objectives

1. Gain access to the checkout form
2. Add product to cart without authentication
3. Redirect to vulnerable input fields

## Instructions

### Step 1: Navigate to Store

**Context**: Reach the product page.

Open the store URL (e.g., example.myshopify.com) and locate the test product.

### Step 2: Start Purchase

**Context**: Trigger the buy flow.

Click 'Add to cart' or 'Buy now' on the product page.

### Step 3: Proceed to Checkout

**Context**: Confirm and redirect.

Review cart if needed, then click 'Checkout' to redirect to checkout.shopify.com.

**Expected Output**: Checkout form loads with product in cart.

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
- initiate-checkout
- unauthenticated
