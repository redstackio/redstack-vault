---
id: proc-6378-empty-cart
tags:
  - csrf
  - preparation
  - web
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:27:15.794Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Empty-Khan-Academy-Shopping-Cart

## Summary

This procedure clears the shopping cart on the Khan Academy shop to establish a baseline state before executing a CSRF attack, ensuring changes are observable.

## Description

In the context of testing CSRF vulnerabilities, starting with an empty cart allows clear verification of unauthorized modifications. The target is the cart endpoint at http://shop.khanacademy.org/cart, which displays and manages cart contents. This step requires the user to be authenticated but performs no automated actions, relying on manual interaction.

## Requirements

1. Web browser with active session to shop.khanacademy.org
2. Network access to the shop domain
3. Authentication as the target user

## Defense

Defensive measures and detection strategies:

- Implement cart state logging to detect unexpected empties
- Require confirmation for cart modifications
- Monitor for rapid cart state changes

## Objectives

1. Reset cart to empty for attack baseline
2. Verify access to cart functionality
3. Prepare for subsequent CSRF exploitation

## Instructions

### Step 1: Access Cart Page

**Context**: Navigate to the cart to view current contents and initiate clearing.

Open a web browser and visit the cart URL.

```html
<!-- No command; manual browser action -->
<!-- Visit: http://shop.khanacademy.org/cart -->
```

> The page loads the current cart items. If items are present, proceed to clear them.

### Step 2: Clear Cart Contents

**Context**: Manually remove all items to empty the cart.

Interact with the page elements to select and delete items, or use any 'Empty Cart' button if available.

```html
<!-- Manual interaction: Click remove buttons or empty option -->
```

> Expected output: Cart shows no items, confirming empty state.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery (adapted to web cart enumeration)

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web]]
- [[preparation]]
