---
id: uuid-create-test
tags:
  - test-order
  - comment-creation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:47.326Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
---

# Create-Test-Order-and-Comment

## Summary

This procedure simulates a customer purchase to generate a legitimate comment in the Judge.me system, providing a baseline request for interception and modification.

## Description

By creating a test order with a comment, attackers establish a valid comment_id and capture the curation API format. This targets Shopify's checkout process integrated with Judge.me. Prerequisites: Installed addon and store products. Outcomes: Comment appears in admin, ready for publishing action.

## Requirements

1. Product available in store for checkout
2. Test payment method or free product
3. Enabled Checkout Comments in addon settings

## Defense

Defensive measures and detection strategies:

- Log all test orders and flag unusual patterns
- Require CAPTCHA on checkout for suspicious activity

## Objectives

1. Generate valid comment data
2. Enable request capture during curation
3. Validate addon functionality

## Instructions

### Step 1: Initiate Checkout

**Context**: Add product and proceed to checkout.

No command; browse store frontend, add item to cart, click checkout.

> Cart populated, checkout page loads.

### Step 2: Add Comment and Complete Order

**Context**: Enter comment during purchase.

No command; in checkout form, fill comments field with sample text (e.g., "Test comment"), complete order.

> Order confirmation email or page; comment attached to order.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- test-order
- comment-creation

