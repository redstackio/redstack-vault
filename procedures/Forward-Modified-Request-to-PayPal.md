---
id: proc-forward-modified-paypal
tags:
  - forward-request
  - payment-completion
  - exploit
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
updated_at: '2025-12-14T17:28:20.348Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Forward Modified Request to PayPal

## Summary

This procedure submits the tampered PayPal request to complete the order at the manipulated price, exploiting the vulnerability for potential free acquisition.

## Description

After modification, the request is forwarded to PayPal, where the altered amounts are processed. Due to absent validation on Uzbey's side, PayPal accepts the parameters as-is, charging the low amount. In production, this may succeed in confirming the order; staging failures are attributed to unrelated payment errors.

## Requirements

1. Modified request from previous procedure
2. Proxy tool to release traffic
3. Active PayPal account for testing (sandbox recommended)
4. Monitoring for order confirmation on Uzbey

## Defense

Defensive measures and detection strategies:

- Post-payment webhook validation from PayPal to Uzbey for amount matching
- Fraud detection rules on low-value transactions for high-value items
- Audit logs of all payment redirects and compare against order totals
- Block or flag requests with tampered indicators (e.g., via WAF)

## Objectives

1. Successfully process the manipulated payment
2. Confirm order fulfillment on the platform
3. Validate exploit success through item acquisition

## Instructions

### Step 1: Review Modified Request

**Context**: Double-check edits to ensure no syntax errors that could cause rejection.

In the proxy, verify amounts are 0.00 and other params intact.

> Expected: Request URL clean, e.g., ...&amount_1=0.00&quantity_1=1...

### Step 2: Forward and Monitor Completion

**Context**: Release the request and observe the payment flow.

Click 'Forward' in Burp or drop interception. Watch for PayPal login/approval and Uzbey order confirmation.

> Expected: Payment succeeds at 0.00; order status updates to paid/shipped (in production).

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

- forward-request
- payment-completion
- exploit
