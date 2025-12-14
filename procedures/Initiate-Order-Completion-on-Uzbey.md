---
id: proc-initiate-order-uzbey
tags:
  - price-manipulation
  - ecommerce
  - drupal
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
updated_at: '2025-12-14T17:28:20.356Z'
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
# Initiate Order Completion on Uzbey

## Summary

This procedure initiates the order completion process on the Uzbey platform to generate a PayPal cart request, setting the stage for parameter interception and manipulation in a price manipulation attack.

## Description

In the context of exploiting the PayPal integration vulnerability, this step involves logging into the Uzbey e-commerce site (built on Drupal), adding items to the cart, and proceeding to checkout with PayPal selected. This triggers the generation of a client-side form with payment parameters based on item prices and quantities, which are vulnerable to tampering due to lack of server-side validation. The expected outcome is the creation of a redirect request to PayPal that can be intercepted.

## Requirements

1. Valid user account on Uzbey platform
2. Proxy tool (e.g., Burp Suite) configured to intercept HTTPS traffic
3. Browser with developer tools or proxy integration
4. Access to add items to cart (no admin privileges needed)

## Defense

Defensive measures and detection strategies:

- Implement server-side recalculation of payment totals before redirecting to payment gateways
- Use signed or hashed parameters in payment requests to prevent tampering
- Monitor for anomalous payment amounts in logs (e.g., frequent 0.00 transactions)
- Enable Content Security Policy (CSP) and validate form submissions

## Objectives

1. Generate the initial PayPal cart request with legitimate parameters
2. Position the attack for request interception
3. Ensure the order includes multiple items to demonstrate multi-parameter tampering

## Instructions

### Step 1: Log In and Add Items to Cart

**Context**: Authenticate and populate the cart to simulate a real purchase, triggering the payment flow.

Browse to the Uzbey site, log in with credentials, and add test items like '128x128 Square' to the cart. Verify quantities and prices in the cart summary.

> No specific command; perform via browser UI. Expected: Cart shows total based on item prices (e.g., $10 for one item).

### Step 2: Proceed to Checkout and Select PayPal

**Context**: Advance to the payment stage to generate the vulnerable redirect form.

Click 'Checkout', enter shipping details if required, and select PayPal as the payment method. Submit to initiate the redirect.

> The form_id=uc_paypal_wps_form indicates Drupal's Ubercart module. Expected: Page prepares redirect to https://www.paypal.com/cgi-bin/webscr with cmd=_cart parameters.

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

- price-manipulation
- ecommerce
- drupal
