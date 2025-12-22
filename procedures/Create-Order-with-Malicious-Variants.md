---
id: 550e8400-e29b-41d4-a716-446655440002
tags:
  - order-creation
  - variants
  - shopify
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:28:44.265Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
---

# Create-Order-with-Malicious-Variants

## Summary

This procedure simulates an order creation in Shopify admin by adding multiple variants from the malicious product, setting up the conditions for formula injection during CSV export.

## Description

Orders in Shopify admin allow adding line items from products with variants. By selecting multiple variants from the pre-created malicious product, the order CSV export will include repeated variant data. The vulnerability arises because the first variant's title is filtered (e.g., '=' replaced with space), but subsequent ones are not, preserving the formula. This requires admin access to create orders, mimicking a scenario where an attacker with store access (e.g., via compromised credentials) sets up the trap for other admins exporting data.

## Requirements

1. Shopify admin access with order creation permissions
2. Pre-existing malicious product with variants from prior procedure
3. Web browser for admin navigation

## Defense

Defensive measures and detection strategies:

- Audit order creation logs for unusual patterns, like multiple variants from suspicious products
- Enforce multi-factor authentication and role-based access for admin order functions
- Sanitize all exported data fields uniformly, regardless of position in CSV

## Objectives

1. Add malicious product variants to a new order
2. Finalize order as paid to enable export
3. Position data for injection trigger on export

## Instructions

### Step 1: Initiate New Order

**Context**: Start order creation to search and add items.

**Instructions**:

Navigate to Orders > Create order in the admin panel. This opens the order editor.

> Expected: Blank order form loads.

### Step 2: Search and Add Malicious Variants

**Context**: Locate the product and add multiple variants to the line items.

**Instructions**:

In the search bar, enter the malicious product title `=cmd|' /C calc'!'D2'`. Select the product, then add at least two variants (e.g., Small and Medium) to the order. Set quantity to 1 each.

> The title may display oddly due to characters, but it should appear in search.

### Step 3: Mark as Paid and Create

**Context**: Complete the order to make it exportable.

**Instructions**:

Click "Mark as paid" in the order totals section. Then, click "Create order" to finalize.

> Expected: Order saved with ID, listed in Orders page.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[order-creation]]
- [[shopify]]
- [[variants]]

---
