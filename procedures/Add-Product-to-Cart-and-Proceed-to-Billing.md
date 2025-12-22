---
tags:
  - recon
  - web
  - checkout
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
id: ed31abeb-70d5-4c5c-853a-5653e58290cc
created_at: '2025-12-14T03:15:35.907Z'
updated_at: '2025-12-14T03:15:35.907Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Add-Product-to-Cart-and-Proceed-to-Billing

## Summary

This procedure initiates the checkout flow on the ExpressionEngine store to access the vulnerable billing form, setting the stage for XSS payload injection.

## Description

In the context of exploiting stored XSS in the billing form, this step involves navigating the public store interface to add a product to the cart and advance to the billing page. It requires no authentication and simulates a legitimate customer checkout, allowing access to input fields that lack proper sanitization. Expected outcomes include reaching the form at https://store.ellislab.com/billing, where subsequent payload injection can occur.

## Requirements

1. Web browser with internet access
2. Public access to https://store.ellislab.com
3. No credentials or special permissions needed

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on checkout attempts to detect automated testing
- Monitor access logs for repeated cart additions without completion

## Objectives

1. Gain access to the vulnerable billing input fields
2. Establish a legitimate-looking session for payload injection
3. Prepare for exploitation without raising immediate alarms

## Instructions

### Step 1: Navigate to Store and Select Product

**Context**: Locate and add a product to initiate the cart.

Browse to https://store.ellislab.com, select any product, and click 'Add to Cart'.

> This loads the cart summary; no code execution, just UI interaction.

### Step 2: Proceed to Checkout

**Context**: Advance to the billing section to expose input fields.

From the cart page, click 'Checkout' or 'Proceed to Billing' to reach https://store.ellislab.com/billing.

> Form loads with fields for name, address, and payment; verify all address fields are present.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[web]]
