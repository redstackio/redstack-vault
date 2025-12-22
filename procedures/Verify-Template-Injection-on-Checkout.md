---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567894
tags:
  - verification
  - template-injection
  - angularjs
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
  - WordPress
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:47:12.712Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify-Template-Injection-on-Checkout

## Summary

This procedure tests the evaluation of injected AngularJS templates by rendering the address fields during the checkout process, confirming client-side execution.

## Description

After storing payloads, proceeding to /checkout/ causes AngularJS to parse and evaluate the {{ }} expressions in the rendered addresses. Observing '2' and 'true' proves the vulnerability, as the input is directly inserted into templates without escaping. This step validates the injection path before escalation.

## Requirements

1. Injected payloads in address fields
2. Product available to add to cart
3. Authenticated session

## Defense

Defensive measures and detection strategies:

- Encode user inputs as text nodes in AngularJS templates (e.g., via ng-bind)
- Audit checkout rendering for dynamic content sources
- Log anomalous JS evaluation attempts if instrumented

## Objectives

1. Trigger client-side template processing
2. Observe evaluated output to confirm vulnerability
3. Assess potential for XSS escalation

## Instructions

### Step 1: Add Product to Cart

**Context**: Simulate purchase to access checkout.

Browse https://mercantile.wordpress.org/, select any product, and add to cart.

> Ensure cart is non-empty.

### Step 2: Proceed to Checkout

**Context**: Navigate to render addresses.

Click proceed to https://mercantile.wordpress.org/checkout/.

> Inspect billing and shipping sections.

### Step 3: Observe Evaluation

**Context**: Check for payload results.

Look for '2' in billing fields and 'true' in shipping.

> Expected: Evaluated values instead of raw payloads, confirming injection.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[verification]]
- [[template-injection]]
- [[angularjs]]
