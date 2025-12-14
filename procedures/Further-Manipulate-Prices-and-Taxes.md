---
id: proc-upserve-further-manip
tags:
  - price-tampering
  - tax-zeroing
  - advanced-exploitation
type: procedure
tools:
  - '[[tools/order2-py]]'
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
updated_at: '2025-12-14T17:28:36.495Z'
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
# Further-Manipulate-Prices-and-Taxes

## Summary

This procedure extends the initial exploitation by setting item prices to arbitrary low values (e.g., 0.01) and zeroing taxes, ensuring client-side total consistency to process near-free orders.

## Description

Building on negative quantities, attackers modify 'charges.items' prices to 1 cent and set 'charges.taxes' to 0, omitting mandatory delivery fees if absorbed in the total. The system stores these values in the database without validation, leading to severe undercharging and reconciliation issues.

## Requirements

1. Base JSON from prior steps.
2. Python scripting for payload generation.
3. Repeated API access for multiple orders.

## Defense

Defensive measures and detection strategies:

- Hardcode minimum prices and enforce tax calculations server-side.
- Require delivery fees as separate validated fields.
- Flag orders with zero taxes or sub-cent prices for review.

## Objectives

1. Achieve minimal order totals through price and tax manipulation.
2. Confirm storage of tampered data.
3. Escalate financial impact.

## Instructions

### Step 1: Update Prices in JSON

**Context**: Set item prices to 1 cent in 'charges.items'.

Example:

```json
{
  "charges": {
    "items": [
      {"name": "Item", "quantity": 1, "price": 1}
    ],
    "taxes": 0,
    "total": 1
  }
}
```

> Ensures total matches low value.

### Step 2: Zero Taxes and Submit

**Context**: Remove tax values and use [[tools/order2-py]] for POST.

Similar to prior submission: `python order2.py`

> Expected: Order like 'upserve-hacker-cafe-999999' with modified values.

### Step 3: Validate Storage

**Context**: Check if database retains low prices and zero taxes.

Query order details post-submission.

> Success: Tampered data persisted, complicating analytics.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/order2-py]]

## Tags

- [[price-tampering]]
- [[tax-zeroing]]
