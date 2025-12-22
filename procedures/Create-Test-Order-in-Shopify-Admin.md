---
tags:
  - shopify
  - admin
  - setup
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
updated_at: '2025-12-14T03:15:31.684Z'
sub_techniques: []
id: 6266dfb2-dc1b-4c43-9dbe-62c96a7894f0
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Test-Order-in-Shopify-Admin

## Summary

This procedure sets up a test order in the Shopify admin panel using a shippable product, preparing the environment for fulfillment-based exploits like stored XSS.

## Description

In the context of exploiting vulnerabilities in Shopify's order fulfillment, creating a test order with shipping-required items is essential to access the fulfillment workflow. This involves using the admin UI to simulate a real order, ensuring the fulfillment ID can be generated for payload injection. Expected outcome is an order ready for fulfillment without triggering any alerts.

## Requirements

1. Authenticated access to Shopify admin panel
2. A shippable product in the store inventory
3. Basic knowledge of Shopify UI navigation

## Defense

Defensive measures and detection strategies:

- Monitor admin actions for unusual order creations (e.g., test orders from non-customer IPs)
- Implement rate limiting on order creation endpoints

## Objectives

1. Establish a valid order ID for fulfillment exploitation
2. Ensure order requires shipping to enable tracking URL injection
3. Validate setup without alerting security controls

## Instructions

### Step 1: Log In and Access Orders

**Context**: Authenticate and navigate to the orders section to initiate creation.

No command needed; use browser to visit https://<store>.myshopify.com/admin/orders and click 'Create order'.

> Select a customer (create test one if needed) and add a shippable product to the order line items.

### Step 2: Save the Order

**Context**: Finalize the order to generate its ID.

Click 'Save' in the UI.

> Expected output: Order saved with pending fulfillment status.

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
- admin-setup
