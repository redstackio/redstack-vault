---
tags:
  - xss
  - bypass
  - shopify
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 173c3602-4f4e-4831-bfbd-21fb9aaff521
created_at: '2025-12-14T03:16:25.341Z'
updated_at: '2025-12-14T03:16:25.341Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Delete-Product-from-Draft-Order

## Summary

This procedure removes the product from the completed draft order to prevent automatic rendering as a sanitized hyperlink, forcing the timeline to display the raw, unsanitized product description containing the XSS payload.

## Description

Shopify typically renders product names as safe links, which sanitizes output. Deleting the product eliminates this, causing the backend description to render directly as HTML. This bypasses protections and requires edit access to the order. Outcomes: Order updated, payload ready for unsafe rendering in timeline views.

## Requirements

1. Completed draft order with malicious product
2. Edit permissions on orders
3. Browser access to admin panel

## Defense

Defensive measures and detection strategies:

- Sanitize all rendered text fields regardless of link presence
- Log product deletions in orders for anomaly detection
- Implement output encoding for all admin UI elements

## Objectives

1. Eliminate product link to trigger raw description rendering
2. Preserve XSS payload in order data
3. Enable vulnerable timeline display

## Instructions

### Step 1: Edit Order

**Context**: Open the completed draft for modification.

UI action: Navigate to order URL and click Edit.

> Expected: Order details editable.

### Step 2: Remove Product

**Context**: Delete the line item to remove link generation.

UI action: Select malicious product and delete from order lines.

> Expected: Product removed; save confirms.

### Step 3: Save Changes

**Context**: Persist the deletion.

UI action: Click Save.

> Expected: Order updated without product; payload in description.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[bypass]]
- [[shopify]]
