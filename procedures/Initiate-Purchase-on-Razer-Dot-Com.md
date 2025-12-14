---
id: proc-uuid-1
tags:
  - ecommerce
  - initial-access
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:47.485Z'
skill_level: beginner
impact_level: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Initiate-Purchase-on-Razer-Dot-Com

## Summary

This procedure initiates a standard purchase flow on razer.com to set up the environment for exploiting the Affirm API IDOR vulnerability.

## Description

In the context of testing Affirm's integration with e-commerce sites, this step involves browsing razer.com, adding products to the cart, and proceeding to checkout. It establishes the legitimate transaction context needed to generate the vulnerable 'checkout_ari' parameter without raising suspicions.

## Requirements

1. Web browser access to razer.com
2. Basic understanding of e-commerce navigation
3. Network proxy setup (e.g., Burp Suite) for traffic interception

## Defense

Defensive measures and detection strategies:

- Monitor for unusual checkout initiations from testing IPs
- Implement rate limiting on cart and checkout endpoints

## Objectives

1. Trigger the purchase workflow
2. Prepare for payment option selection
3. Expected outcome: Cart and checkout pages accessible

## Instructions

### Step 1: Browse and Add to Cart

**Context**: Start the shopping process to simulate a real user.

Navigate to razer.com, select products, and add them to the cart.

> This action loads the site and populates the cart with items.

### Step 2: Proceed to Checkout

**Context**: Move to the payment stage to enable financing options.

Click 'Checkout' from the cart summary.

> Expected output: Checkout form appears with shipping and payment sections.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[ecommerce]]
- [[initial-access]]
