---
id: ac-upserve-olo-price-manip
tags:
  - business-logic
  - api-manipulation
  - price-manipulation
  - financial-fraud
type: attack_chain
tools:
  - '[[tools/order-py]]'
  - '[[tools/order2-py]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Manipulate-Order-JSON-with-Negative-Quantity]]'
  - '[[procedures/Submit-Manipulated-JSON-to-Order-API]]'
  - '[[procedures/Verify-Order-Acceptance-and-Reduced-Charge]]'
  - '[[procedures/Further-Manipulate-Prices-and-Taxes]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:36.500Z'
description: >-
  Multi-stage attack exploiting business logic flaws in Upserve's Online
  Ordering system to manipulate order totals using negative quantities,
  arbitrary prices, and zeroed taxes, resulting in undercharging and financial
  loss.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Upserve OLO Total Price Manipulation via Negative Quantities and Arbitrary Prices

Multi-stage attack chain demonstrating exploitation of business logic errors in Upserve's Online Ordering (OLO) system, allowing attackers to reduce order totals through negative item quantities, arbitrary low prices, and zeroed taxes. Discovered via fuzzing and manual JSON payload modification, this leads to undercharging, financial losses for restaurants, and out-of-balance orders requiring manual reconciliation.

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
    A[Payload Manipulation] --> B[API Submission]
    B --> C[Order Verification]
    C --> D[Advanced Price/Tax Tampering]
    D --> E[Financial Exploitation]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/order-py]]
- [[tools/order2-py]]

### Target Environment

- Web-based Upserve OLO platform
- Access to order submission API (e.g., via store_pretty_url like 'upserve-lounge-test-providence-2')
- No specific ports required; operates over HTTPS

### Initial Access Requirements

- Valid customer session or API access to place orders
- Network access to Upserve's OLO endpoints
- Basic knowledge of JSON structure for order payloads

## Detailed Attack Procedures

### Step 1: Payload Manipulation with Negative Quantity
procedure: [[procedures/Manipulate-Order-JSON-with-Negative-Quantity]]

**Objective**: Craft a tampered JSON payload by adding items with negative quantities to reduce the calculated total while maintaining client-side arithmetic consistency.

**Instructions**: Modify the order JSON in the 'charges.items' array to include a legitimate item (e.g., 2 ChickenBurgers at 1200 cents each) and a negative quantity item (e.g., BreadPudding at quantity -1 and price 900 cents). Adjust taxes to 290 cents and ensure the total is 1870 cents (2*1200 -1*900 + 290).

**Expected Output**: Validated JSON payload ready for submission, with manipulated total reflecting the discount.

**Success Indicators**:
- JSON parses without errors
- Client-side total calculation matches the tampered values

### Step 2: Submit Manipulated JSON to Order API
procedure: [[procedures/Submit-Manipulated-JSON-to-Order-API]]

**Objective**: Send the tampered payload to the Upserve OLO API endpoint to process the order with the reduced total.

**Instructions**: Use a Python script like [[tools/order-py]] to POST the JSON to the order submission endpoint, including store_pretty_url (e.g., 'upserve-lounge-test-providence-2'), submission_id, customer details, fulfillment_info for delivery, and a payments array.

**Expected Output**: API response confirming order placement with a confirmation_code (e.g., 'upserve-hacker-cafe-32870').

**Success Indicators**:
- HTTP 200/201 response
- Order ID generated without validation errors

### Step 3: Verify Order Acceptance and Reduced Charge
procedure: [[procedures/Verify-Order-Acceptance-and-Reduced-Charge]]

**Objective**: Confirm the system accepts the order and processes payment at the manipulated lower amount.

**Instructions**: Check the order history or confirmation details for the processed total (e.g., $18.70 charge) and ensure the negative quantity impacts the final billing without server-side rejection.

**Expected Output**: Order history screenshot or log showing the reduced total and out-of-balance items.

**Success Indicators**:
- Payment charged at manipulated amount
- Order stored in database with tampered values

### Step 4: Further Manipulate Prices and Taxes
procedure: [[procedures/Further-Manipulate-Prices-and-Taxes]]

**Objective**: Extend the exploitation by setting item prices to minimal values (e.g., 1 cent) and zeroing taxes to achieve even lower totals.

**Instructions**: Update the JSON in 'charges.items' to set prices to 1 cent, taxes to 0, and ensure the total matches client calculation. Submit via [[tools/order2-py]] to endpoints yielding orders like 'upserve-hacker-cafe-999999'.

**Expected Output**: Additional orders processed with near-zero charges, complicating restaurant reconciliation.

**Success Indicators**:
- Successful submission without tax/fee validation
- Database stores modified prices and zero taxes

## Attack Chain Summary

### Key Achievements

1. Successful reduction of order total using negative quantities, leading to undercharging.
2. API acceptance of arbitrary prices and zero taxes without server-side checks.
3. Creation of out-of-balance orders skewing analytics and requiring manual fixes.
4. Demonstration of scalable financial exploitation via repeated submissions.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
