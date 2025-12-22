---
id: a6e2d7b8-13a9-4a3b-b21b-ffacb242c445
name: Parameter-Tampering-in-Ecommerce-Checkout
type: procedure
verified: true
submitted: true
created_at: '2020-08-23T17:16:02.852469+00:00'
updated_at: '2023-05-26T01:24:18.902855+00:00'
platforms:
  - Web
tags:
  - parameter-tampering
  - web-applications
  - business-logic-bypass
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
commands: []
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Parameter-Tampering-in-Ecommerce-Checkout

## Summary

This procedure demonstrates how to manipulate HTTP request parameters in an e-commerce application's checkout process to bypass business logic controls, such as altering shipping charges and item amounts to reduce the total payment. It targets web applications that fail to validate parameters server-side, allowing attackers to commit fraud by paying less than intended.

## Description

Parameter tampering involves intercepting and modifying data sent from the client to the server, exploiting insufficient input validation or client-side-only price calculations. In an e-commerce scenario, this can lead to unauthorized discounts or free shipping by changing values like 'shipping_charge' or 'amount' in POST requests during checkout. The technique assumes the attacker has unauthenticated access to the site and uses a proxy tool to inspect and alter traffic. Success relies on the application trusting client-submitted values without re-verifying against server-side logic. This is common in legacy or poorly designed web apps and maps to exploiting public-facing applications.

## Requirements

1. Access to a vulnerable e-commerce web application with a checkout flow supporting payment gateways like PayPal.
2. Burp Suite or similar proxy tool installed and configured to intercept browser traffic.
3. A product available for purchase on the target site.
4. Basic knowledge of HTTP requests and browser developer tools for initial inspection.
5. Network connectivity to the target domain without restrictions.

## Defense

Defensive measures and detection strategies:

- Implement server-side validation for all financial parameters, recalculating totals independently of client input.
- Use parameterized queries and input sanitization to prevent tampering.
- Monitor for anomalies in transaction data, such as zero shipping fees or mismatched amounts between client and server logs.
- Employ web application firewalls (WAFs) to detect unusual request modifications.
- Log all checkout requests with client IP and session data for forensic analysis.

## Objectives

1. Intercept and identify key parameters in the checkout request related to pricing and shipping.
2. Modify these parameters to favorable values (e.g., zero shipping, minimal amount) without triggering validation errors.
3. Complete the payment flow with tampered values reflected in the gateway, achieving reduced or fraudulent payment.
4. Verify the transaction succeeds, demonstrating the bypass of business logic.

## Instructions

### Step 1: Select and Add Product to Cart

**Context**: Begin the purchase process to reach the checkout flow where parameters can be intercepted. This step simulates legitimate user behavior to generate the necessary session and cart state.

Navigate to the vulnerable e-commerce domain in your browser. Browse to a product page, select the desired item, and add it to the shopping cart. Ensure the cart reflects the correct initial price and any default shipping charges.

> This establishes the baseline transaction data that will be tampered with later.

### Step 2: Proceed to Checkout

**Context**: Advance to the billing stage to trigger the payment initiation, setting up the intercept point for request modification.

From the cart page, click 'Proceed to Checkout'. Fill in all required billing details, such as name, address, email, and payment method (select PayPal or similar gateway). Do not submit yet; ensure Burp Suite is actively proxying the traffic.

> Configuring the proxy ensures all subsequent requests pass through Burp for inspection and alteration.

### Step 3: Intercept the Checkout Request

**Context**: Capture the HTTP POST request containing pricing parameters during payment submission, identifying fields like 'amount', 'shipping_charge', and 'total'.

With Burp Suite's Proxy tab set to intercept, submit the checkout form by clicking 'Pay Now' or equivalent. In Burp, locate the relevant POST request to the payment endpoint (often containing form data with JSON or URL-encoded parameters for item details, shipping, and totals).

> Look for parameters in the request body, such as 'shipping_charge=10.00' or 'amount=50.00'. The request may be to an endpoint like '/checkout' or '/paypal/initiate'.

### Step 4: Tamper with Parameters

**Context**: Modify the identified parameters to bypass pricing logic, setting shipping to zero and reducing the amount to a minimal value while preserving other data to avoid detection.

In the Burp Repeater or Proxy intercept, edit the request body: change 'shipping_charge' to '0.00', 'amount' to '1.00', and adjust 'total' accordingly if present. Ensure the modifications align with the expected format (e.g., decimal places). Forward the tampered request to the server.

> This step exploits client-trusted values; if the server re-validates, the request may fail—retry with subtle changes if needed.

### Step 5: Complete and Verify the Transaction

**Context**: Disable interception to allow the response to reach the browser and confirm the tampered values propagate to the payment gateway.

Turn off Burp's intercept mode, then observe the browser. The PayPal (or chosen gateway) page should display the altered prices (e.g., $1.00 total with $0.00 shipping). Proceed with payment to verify success.

> Success is indicated if the gateway processes the reduced amount without errors, confirming the bypass.
