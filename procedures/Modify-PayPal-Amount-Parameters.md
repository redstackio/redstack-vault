---
id: proc-modify-paypal-amounts
tags:
  - parameter-tampering
  - amount-modification
  - business-logic
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
updated_at: '2025-12-14T17:28:20.351Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Modify PayPal Amount Parameters

## Summary

This procedure tampers with the amount parameters in the intercepted PayPal redirect request to set arbitrary payment values, exploiting the lack of server-side validation.

## Description

With the request intercepted, parameters such as amount_1, amount_2 are edited to values like 0.00 while keeping item details (e.g., item_name_1, quantity_1) intact. This business logic flaw allows the attacker to dictate the payment total passed to PayPal, potentially resulting in underpayment or free orders since Uzbey does not recalculate or verify amounts before forwarding.

## Requirements

1. Intercepted request from previous procedure
2. Proxy tool with editing capabilities (e.g., Burp Repeater)
3. Understanding of PayPal cart parameter format (e.g., amount_N for item N)
4. Preservation of non-price parameters to avoid rejection

## Defense

Defensive measures and detection strategies:

- Server-side amount validation and hashing before PayPal redirect
- Compare client-submitted totals against cart session data
- Alert on discrepancies between expected and submitted payment amounts
- Implement client-side integrity checks with JavaScript

## Objectives

1. Reduce payment amounts to minimal values (e.g., 0.00)
2. Ensure modified request remains syntactically valid
3. Prepare for seamless forwarding to PayPal

## Instructions

### Step 1: Inspect and Identify Parameters

**Context**: Review the request to locate all amount fields corresponding to cart items.

In the proxy, examine the query string for amount_1=original_price, amount_2, etc.

> Expected: Identification of 1-5 amount params based on cart size.

### Step 2: Edit Amounts to Arbitrary Values

**Context**: Change prices without altering quantities or names to maintain order integrity.

Set amount_1=0.00, amount_2=0.00, etc. For example, transform amount_1=10.00 to amount_1=0.00.

> Expected: Updated total implies 0.00 payment; request ready for drop/forward.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- parameter-tampering
- amount-modification
- business-logic
