---
id: proc-upserve-negative-qty
tags:
  - business-logic
  - json-manipulation
  - negative-quantity
type: procedure
tools:
  - '[[tools/order-py]]'
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
updated_at: '2025-12-14T17:28:36.499Z'
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
# Manipulate-Order-JSON-with-Negative-Quantity

## Summary

This procedure crafts a tampered JSON payload for Upserve's OLO system by introducing items with negative quantities, allowing the client-side total calculation to reflect a reduced amount while appearing arithmetically correct.

## Description

In the context of exploiting business logic flaws, attackers fuzz and manually edit the order JSON during submission. The 'charges.items' array is modified to include negative quantities (e.g., -1 for an item priced at 900 cents) alongside legitimate items (e.g., 2 units at 1200 cents each), with taxes adjusted to 290 cents, yielding a total of 1870 cents. The server relies on this client-calculated total without re-validating quantities or prices against business rules, enabling financial manipulation.

## Requirements

1. Access to Upserve OLO order form or API documentation for JSON structure.
2. Text editor or scripting tool like Python for JSON modification.
3. Valid store_pretty_url (e.g., 'upserve-lounge-test-providence-2').

## Defense

Defensive measures and detection strategies:

- Implement server-side validation to reject negative quantities and enforce minimum prices.
- Re-calculate totals independently on the server using canonical item prices from the database.
- Monitor for anomalous order totals or negative item counts in logs.

## Objectives

1. Create a manipulated JSON payload that bypasses client-side checks.
2. Ensure the total appears consistent to avoid arithmetic validation failures.
3. Prepare for submission to achieve undercharging.

## Instructions

### Step 1: Identify Order JSON Structure

**Context**: Intercept or view the base JSON payload from a legitimate order attempt to understand the 'charges.items' array format.

No specific command; manually inspect via browser dev tools or proxy like Burp Suite.

> Expected: JSON with fields like items (array of {name, quantity, price}), taxes, and total.

### Step 2: Add Negative Quantity Item

**Context**: Append or modify an item in 'charges.items' with quantity: -1 and a price that offsets legitimate items.

Example JSON snippet:

```json
{
  "charges": {
    "items": [
      {"name": "ChickenBurger", "quantity": 2, "price": 1200},
      {"name": "BreadPudding", "quantity": -1, "price": 900}
    ],
    "taxes": 290,
    "total": 1870
  }
}
```

> This reduces the subtotal by 900 cents, leading to a lower total.

### Step 3: Validate Payload

**Context**: Ensure the JSON is well-formed and the total matches the calculation (legitimate subtotal - negative offset + taxes).

Use a JSON validator or Python's json.loads() to parse.

> Expected: No syntax errors; arithmetic consistency confirmed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/order-py]]

## Tags

- [[business-logic]]
- [[json-manipulation]]
