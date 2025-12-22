---
tags:
  - shopify
  - fulfillment
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
updated_at: '2025-12-14T03:15:31.674Z'
sub_techniques: []
id: d7dfc709-d263-4dc0-9ad4-b365fb1372b8
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Fulfill-Shopify-Order-to-Generate-ID

## Summary

This procedure fulfills items in a Shopify test order via the admin UI, generating a fulfillment ID necessary for updating tracking details in subsequent exploit steps.

## Description

To exploit stored XSS in fulfillment tracking, an initial fulfillment must be created without tracking info. This uses the Shopify admin interface to process items, producing a fulfillment ID for API updates. The process assumes authenticated access and targets orders with shippable items.

## Requirements

1. Existing order ID from prior setup
2. Admin privileges to fulfill orders
3. No prior tracking added to avoid conflicts

## Defense

Defensive measures and detection strategies:

- Log fulfillment actions and review for anomalies (e.g., immediate updates)
- Require approval for test order fulfillments

## Objectives

1. Generate a valid fulfillment ID
2. Update order status to fulfilled
3. Prepare for payload injection without errors

## Instructions

### Step 1: Access Order Details

**Context**: Load the order page to access fulfillment options.

Navigate to https://<store>.myshopify.com/admin/orders/<order_id>.

> Ensure fulfillment section shows pending items.

### Step 2: Initiate Fulfillment

**Context**: Process the items to create the fulfillment record.

Click 'Fulfill items', select all items, and submit without adding tracking.

> Expected output: Fulfillment ID appears in the UI under the order details.

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
- order-fulfillment
