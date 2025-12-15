---
id: complete-payment-001
name: Complete Manipulated Payment
type: procedure
verified: false
submitted: true
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:48.034Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - payment-gateway
  - financial-loss
  - gopay
  - bitcoin
platforms:
  - Web
commands: []
tools: []
skill_level: beginner
impact_level: high
detection_risk: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Complete Manipulated Payment

## Summary

This procedure finalizes the exploited checkout by processing payment through integrated gateways like GoPay or Bitcoin, where the manipulated low price is honored, resulting in underpayment and financial loss to the vendor.

## Description

Following price modification, the request reaches the payment stage where gateways reflect the altered amount without independent verification. Attackers use valid payment methods to complete the transaction, receiving confirmation for the minimal price (e.g., 1 unit). This exploits the lack of end-to-end validation in web e-commerce flows integrated with third-party payments, leading to direct economic impact.

## Requirements

1. Valid payment details for GoPay or Bitcoin
2. Successful price modification from prior steps
3. Access to email for confirmation

## Defense

Defensive measures and detection strategies:

- Gateway-side price confirmation against vendor API
- Transaction monitoring for outliers (e.g., prices below threshold)
- Post-payment reconciliation audits

## Objectives

1. Execute payment with the tampered low price
2. Obtain confirmation of underpayment
3. Realize financial impact on the target

## Instructions

### Step 1: Proceed to Payment Gateway

**Context**: Follow the redirect after forwarding the modified request.

The site redirects to the gateway (e.g., GoPay); the price shown is the altered value.

> Expected output: Payment form with low amount.

### Step 2: Submit Payment

**Context**: Complete the transaction to lock in the manipulation.

Enter payment credentials and confirm.

> Expected output: Success page and email with reduced amount.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[payment-gateway]]
- [[financial-loss]]
- [[gopay]]
- [[bitcoin]]
