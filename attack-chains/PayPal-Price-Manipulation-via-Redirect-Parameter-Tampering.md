---
id: ac-paypal-price-manip-uzbey
tags:
  - price-manipulation
  - paypal
  - business-logic
  - parameter-tampering
  - drupal
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Initiate-Order-Completion-on-Uzbey]]'
  - '[[procedures/Intercept-PayPal-Redirect-Request]]'
  - '[[procedures/Modify-PayPal-Amount-Parameters]]'
  - '[[procedures/Forward-Modified-Request-to-PayPal]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:20.358Z'
description: >-
  A business logic vulnerability in the Uzbey platform's PayPal integration
  allows attackers to tamper with payment amount parameters in the redirect
  request, enabling arbitrary pricing such as setting amounts to 0.00 for free
  item acquisition.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# PayPal Price Manipulation via Redirect Parameter Tampering

Multi-stage attack chain demonstrating a complete workflow for exploiting a business logic flaw in the Uzbey platform's PayPal payment integration. By intercepting and modifying the redirect request to PayPal, an attacker can alter payment amounts to arbitrary values, such as 0.00, potentially acquiring paid items for free or at reduced cost. This vulnerability stems from the lack of server-side validation of client-generated payment parameters. Testing in staging environments may fail due to unrelated payment issues, but the flaw is assumed functional in production.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initiate Order] --> B[Intercept Redirect]
    B --> C[Modify Parameters]
    C --> D[Forward to PayPal]
    D --> E[Complete Payment]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]] (or similar proxy for request interception and modification)

### Target Environment

- Web platform: Uzbey e-commerce site built on Drupal
- Services: PayPal payment gateway
- Tech stack: Drupal with Ubercart (inferred from form_id=uc_paypal_wps_form)
- No specific ports required; operates over HTTPS

### Initial Access Requirements

- Valid user account on Uzbey platform (no authentication bypass needed)
- Ability to place orders (e.g., add items to cart)
- Network access to the target site and PayPal
- Proxy tool configured to intercept browser traffic

## Detailed Attack Procedures

### Step 1: Initiate Order Completion
procedure: [[procedures/Initiate-Order-Completion-on-Uzbey]]

**Objective**: Start the order process to generate the PayPal cart request with predefined amount fields based on item prices and quantities.

**Instructions**: Log in to the Uzbey platform, add items (e.g., '128x128 Square') to the cart, and proceed to checkout. Select PayPal as the payment method to trigger the redirect form generation.

**Expected Output**: A form submission or auto-redirect to PayPal with parameters like cmd=_cart, amount_1=original_price, quantity_1, etc.

**Success Indicators**:
- Cart populated with items
- Checkout page loads PayPal option
- Initial redirect request captured in proxy

### Step 2: Intercept PayPal Redirect Request
procedure: [[procedures/Intercept-PayPal-Redirect-Request]]

**Objective**: Capture the GET request to PayPal's endpoint before it reaches the gateway, allowing inspection of payment parameters.

**Instructions**: Configure a proxy tool like Burp Suite to intercept traffic from the browser. Proceed with order completion to trigger the request to https://www.paypal.com/cgi-bin/webscr.

**Expected Output**: Intercepted request showing parameters such as cmd=_cart, amount_1=original_price, item_name_1, quantity_1 for multiple items.

**Success Indicators**:
- Request paused in proxy
- Parameters visible and match order details
- No immediate errors in interception

### Step 3: Modify Amount Parameters
procedure: [[procedures/Modify-PayPal-Amount-Parameters]]

**Objective**: Alter the amount fields to arbitrary values while preserving other parameters to bypass payment validation.

**Instructions**: In the intercepted request, edit parameters like amount_1=0.00, amount_2=0.00 (for multiple items). Keep item_name_1, quantity_1, and other non-price params unchanged.

**Expected Output**: Modified request with tampered amounts, ready for forwarding.

**Success Indicators**:
- Parameters successfully edited without breaking request syntax
- Total payment amount reflects changes (e.g., 0.00)
- Request structure remains valid for PayPal

### Step 4: Forward Modified Request to PayPal
procedure: [[procedures/Forward-Modified-Request-to-PayPal]]

**Objective**: Submit the tampered request to complete the payment at the manipulated price.

**Instructions**: Release the modified request from the proxy to forward it to PayPal. Monitor the payment flow for completion.

**Expected Output**: PayPal processes the low/no payment, potentially confirming the order on Uzbey if validation is absent.

**Success Indicators**:
- Payment accepted by PayPal
- Order confirmed on Uzbey platform
- Items acquired without full payment (note: may fail in staging due to unrelated issues)

## Attack Chain Summary

### Key Achievements

1. Successful initiation of order to trigger PayPal integration
2. Interception and tampering of payment parameters without server-side checks
3. Arbitrary pricing control, enabling free or underpaid acquisitions
4. Potential bypass of payment verification in production environments

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access

---

*Last updated: 2023-10-01T00:00:00Z*
