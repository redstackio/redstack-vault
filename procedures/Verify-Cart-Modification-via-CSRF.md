---
id: proc-6378-verify-cart
tags:
  - csrf
  - verification
  - web
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:27:15.771Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Verify-Cart-Modification-via-CSRF

## Summary

This procedure checks the victim's shopping cart after a CSRF attack to confirm unauthorized changes, such as the addition of an item, validating the exploit's success.

## Description

Post-exploitation verification involves revisiting the cart page to inspect contents. For the Khan Academy shop, this reveals if the forged updates[211669705]=1 parameter took effect, showing the item despite no legitimate user action. This step confirms the impact of the CSRF vulnerability.

## Requirements

1. Access to the victim's authenticated session
2. Web browser
3. Prior execution of the CSRF PoC

## Defense

Defensive measures and detection strategies:

- Audit logs for cart views following updates
- User notifications for cart changes
- Anomaly detection on item additions without form submissions

## Objectives

1. Observe added item in cart
2. Confirm CSRF bypass
3. Assess potential for further modifications (remove/add)

## Instructions

### Step 1: Revisit Cart Page

**Context**: Load the cart endpoint to display current state.

Navigate to the cart URL in the browser.

```html
<!-- Manual action: Visit http://shop.khanacademy.org/cart -->
```

> The page refreshes and lists cart items.

### Step 2: Inspect Cart Contents

**Context**: Check for the unauthorized item.

Look for product ID 211669705 with quantity 1.

```html
<!-- Expected: Item listed as added, e.g., "Product Name - Quantity: 1" -->
```

> Expected output: New item appears, proving the attack worked.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Active Scanning]] Active Scanning (adapted to post-exploit verification)

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[verification]]
- [[web]]
