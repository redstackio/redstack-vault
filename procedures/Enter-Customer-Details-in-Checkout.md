---
id: proc-shopify-enter-details-001
tags:
  - shopify
  - checkout
  - input
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
updated_at: '2025-12-14T03:46:37.793Z'
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
# Enter-Customer-Details-in-Checkout

## Summary

This procedure involves filling in required customer information on the Shopify checkout form to progress toward the vulnerable first name field injection.

## Description

During the XSS exploitation, this step populates fields like last name, address, and email on checkout.shopify.com to satisfy form validation, while deferring the first name for payload insertion. It operates in an unauthenticated context and prepares for the injection step.

## Requirements

1. Active checkout session at checkout.shopify.com
2. Valid but fake details for non-vulnerable fields
3. Web browser

## Defense

Defensive measures and detection strategies:

- Validate all input fields for length and format
- Implement client-side and server-side checks for suspicious patterns
- Log incomplete checkouts for anomaly detection

## Objectives

1. Satisfy form requirements
2. Advance to payload injection
3. Maintain session integrity

## Instructions

### Step 1: Locate Form Fields

**Context**: Identify required inputs.

On the checkout page, scroll to the customer information section.

### Step 2: Fill Non-Vulnerable Fields

**Context**: Enter data to pass validation.

Input last name (e.g., 'Doe'), email (e.g., 'test@example.com'), address (e.g., '123 Test St'), and phone if required.

### Step 3: Prepare for Next Step

**Context**: Leave first name blank.

Do not enter first name yet; click 'Continue to shipping' if prompted.

**Expected Output**: Form advances without errors.

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
- customer-details
- form-filling
