---
tags:
  - web-access
  - ecommerce
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: e7de9bf8-6d5f-446b-96bc-00cad24e70e5
created_at: '2025-12-13T23:56:20.524Z'
updated_at: '2025-12-13T23:56:20.524Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Navigate and Add to Cart

## Summary

This procedure involves accessing an e-commerce website, selecting a product, adding it to the shopping cart, and proceeding to checkout to reach vulnerable input fields.

## Description

In web application testing, initial access to the target site is crucial for identifying input points. This procedure sets up the environment for injecting payloads into forms like billing addresses, targeting platforms such as ColdFusion-based shops. Expected outcome is reaching the checkout page without authentication barriers.

## Requirements

1. Web browser with JavaScript enabled
2. Access to the public URL https://shop.aaf.com/
3. No prior credentials needed

## Defense

Defensive measures and detection strategies:

- Monitor for unusual cart activity or rapid product additions
- Implement rate limiting on checkout processes

## Objectives

1. Gain access to the checkout form
2. Prepare for payload injection
3. Confirm redirection to vulnerable endpoint

## Instructions

### Step 1: Access the Shop

**Context**: Navigate to the e-commerce site and browse products.

Visit https://shop.aaf.com/ and select a product like a t-shirt.

> This establishes the initial session.

### Step 2: Add to Cart and Proceed

**Context**: Add the selected product to the cart and initiate checkout.

Click 'Add to Cart' and then 'Proceed' to reach https://shop.aaf.com/Order/step1/index.cfm.

> This loads the billing activity page with address fields.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- web-access
- ecommerce
