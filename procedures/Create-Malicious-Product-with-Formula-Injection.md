---
id: 550e8400-e29b-41d4-a716-446655440001
tags:
  - formula-injection
  - product-creation
  - shopify
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/excel-formula-injection-cmd]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:28:44.268Z'
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

# Create-Malicious-Product-with-Formula-Injection

## Summary

This procedure creates a product in Shopify admin with a title embedding an Excel formula injection payload, then adds multiple variants to enable bypass of filtering during CSV export.

## Description

In the Shopify admin panel, products can have titles that include dangerous characters like '=', which are intended to be filtered in CSV exports to prevent formula injection. However, this filtering is inconsistent for multi-variant products. By setting a title like '=cmd|' /C calc'!'D2'', the payload injects a command execution formula. Adding variants ensures the first is filtered, but subsequent ones retain the payload, executing when the CSV is opened in Excel. This targets admin users exporting orders, potentially leading to RCE in their local environment.

## Requirements

1. Shopify admin access with product creation permissions
2. Web browser for admin interface navigation
3. Knowledge of Excel formula syntax for injection payloads

## Defense

Defensive measures and detection strategies:

- Implement consistent server-side escaping of formula characters ('=', '+', '-') in all CSV fields, including variants
- Warn users about risks of opening CSV exports in spreadsheet software; recommend plain text viewers
- Monitor admin actions for creation of products with suspicious titles containing formula-like strings

## Objectives

1. Establish a product with injectable payload in title
2. Configure multiple variants to exploit filtering inconsistency
3. Prepare for order creation to trigger export vulnerability

## Instructions

### Step 1: Add New Product with Malicious Title

**Context**: Log in and create a product to embed the formula injection payload in the title field.

**Command** ([[commands/excel-formula-injection-cmd]]):

Set product title to:

```text
=cmd|' /C calc'!'D2'
```

> This payload uses Excel's formula syntax to invoke cmd.exe with /C calc, opening the Windows calculator. The quotes and exclamation marks help evade partial filtering. Save the product after setting title and basic details (e.g., price $0).

### Step 2: Add Multiple Variants

**Context**: Edit the product to add variants, ensuring at least three to test filtering bypass on export.

**Instructions**:

In the product edit page, scroll to Variants section. Click "Add variant" and create options like "Size: Small", "Size: Medium", "Size: Large". Assign the same malicious title propagation if needed, then save.

> No specific command; this is UI-based. Expected: Variants listed under product without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used

- [[commands/excel-formula-injection-cmd]]

## Tools Used


## Tags

- [[formula-injection]]
- [[shopify]]
- [[product-creation]]

---
