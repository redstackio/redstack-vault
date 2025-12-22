---
id: f817a0d2-6f1f-49f3-a29e-19760314ccb1
name: Price-Tampering-in-E-commerce-Applications
type: procedure
verified: true
submitted: true
created_at: '2020-08-04T19:24:11.462445+00:00'
updated_at: '2023-05-26T15:56:13.268534+00:00'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - parameter-tampering
  - web-applications
  - e-commerce
commands:
  - '[[commands/curl-modify-price-parameter]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: beginner
impact_level: high
detection_risk: low
validated: true
---

# Price-Tampering-in-E-commerce-Applications

## Summary

This procedure demonstrates how to tamper with price parameters in e-commerce web applications by intercepting and modifying HTTP requests during the purchase process, allowing an attacker to acquire products at reduced or zero cost. It targets applications that fail to validate or server-side enforce price values sent from the client.

## Description

Price tampering exploits insufficient input validation in e-commerce platforms where the client-side price is reflected in purchase requests without server-side verification. An attacker intercepts the request (e.g., using a proxy tool) and alters the price parameter before forwarding it to the server. If successful, the order processes at the tampered price, deducting only the modified amount from the user's wallet or payment method. This is common in applications using JavaScript for dynamic pricing without backend checks. The technique requires an authenticated session and applies to web-based shopping carts handling POST requests for order placement.

## Requirements

1. Access to an e-commerce account with sufficient wallet balance or payment method.
2. Ability to intercept and modify HTTP traffic (e.g., via browser proxy).
3. Target application must transmit price data in client requests without server-side validation.
4. Tools like Burp Suite for request interception or curl for scripted testing.

## Defense

Defensive measures and detection strategies:

- Implement server-side validation of all pricing data, ignoring client-submitted values and recalculating prices based on database records.
- Use signed or encrypted price tokens in requests to prevent tampering (e.g., HMAC signatures).
- Monitor for anomalies in order pricing, such as prices below configured minimums or discrepancies between client and server calculations.
- Enable web application firewall (WAF) rules to detect unusual parameter modifications in purchase endpoints.

## Objectives

1. Intercept the purchase request containing the price parameter.
2. Modify the price to a lower value while preserving other order details.
3. Forward the tampered request to complete the order at the reduced price.
4. Verify the order confirmation and wallet deduction reflect the tampered amount.

## Instructions

### Step 1: Authenticate and Add Item to Cart

**Context**: Log in to the e-commerce application and add the target product to the cart to initiate the purchase flow. Ensure the wallet balance covers the original price.

No specific command required; perform this via the web interface. Note the original price (e.g., 250) and quantity (e.g., 1).

### Step 2: Intercept the Purchase Request

**Context**: Configure a proxy tool like [[tools/Burp-Suite]] to intercept traffic from the browser. Proceed to the checkout and submit the order to capture the POST request containing the price parameter.

Use [[commands/curl-modify-price-parameter]] to simulate or replay the request if scripting outside a proxy:

```bash
curl -X POST https://target-ecommerce.com/api/purchase \ 
  -H "Content-Type: application/json" \ 
  -H "Authorization: Bearer $_SESSION_TOKEN" \ 
  -d '{"product_id": $_PRODUCT_ID, "quantity": $_QUANTITY, "price": $_ORIGINAL_PRICE, "total": $_TOTAL}' \ 
  -k
```

> This sends the initial request; intercept it in the proxy to modify before forwarding. Expected output: HTTP 200 with order details if unmodified.

### Step 3: Modify the Price Parameter

**Context**: In the intercepted request, locate the price field (e.g., in JSON body as "price": 250) and change it to a lower value (e.g., 50). Ensure the total is also adjusted if present to maintain consistency, though server-side checks may vary.

Forward the modified request using the proxy or update the curl command with the tampered price:

```bash
curl -X POST https://target-ecommerce.com/api/purchase \ 
  -H "Content-Type: application/json" \ 
  -H "Authorization: Bearer $_SESSION_TOKEN" \ 
  -d '{"product_id": $_PRODUCT_ID, "quantity": $_QUANTITY, "price": 50, "total": 50}' \ 
  -k
```

> Explanation: The command replaces the price and total with tampered values. Expected output: HTTP 200 confirming order placement at the modified price.

### Step 4: Verify Order Success

**Context**: After forwarding, check the order confirmation page or API response for successful placement. Review the account dashboard to confirm the wallet deduction matches the tampered price (e.g., reduced by 50 instead of 250).

No command needed; inspect the response body for order ID and updated balance.

### Step 5: Validate Impact

**Context**: Navigate to the order history or home page to ensure the product is booked at the lower price without errors.

Expected success: Order listed with tampered price; no reversal or fraud alerts triggered.
