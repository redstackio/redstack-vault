---
id: p-add-unlisted-items-cart-idor
tags:
  - idor
  - api
  - exploitation
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-add-to-cart]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:29.368Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
# Add Unlisted Items to Cart and Complete Order via IDOR

## Summary

This procedure leverages the IDOR vulnerability to add previously accessed unlisted items to the shopping cart and proceed to order, fully bypassing Instacart's web interface access controls.

## Description

Following item discovery, the /v2/cart/add endpoint accepts the manipulated item ID in the payload without verifying catalog visibility, allowing unauthorized addition to the cart. The attacker can then complete the purchase process, potentially acquiring items not intended for public sale. This requires an active session and targets the cart management API. Impact includes unauthorized transactions, rated high severity.

## Requirements

1. Authenticated token and valid manipulated item ID from prior step.
2. HTTP client for POST requests.
3. Access to checkout flow (API or web).

## Defense

Defensive measures and detection strategies:

- Add server-side checks for item visibility before cart operations.
- Audit cart additions for anomalous item IDs.
- Use session-based access tokens with granular permissions.

## Objectives

1. Add unlisted items to cart without errors.
2. Complete order process successfully.
3. Demonstrate full bypass of intended controls.

## Instructions

### Step 1: Prepare Cart Addition Payload

**Context**: Use the unlisted item ID in the JSON payload for the add endpoint.

No command; construct payload like {"item_id": 99999, "quantity": 1}.

> Expected: Payload ready for request.

### Step 2: Add Item to Cart

**Context**: Submit POST request to add the unlisted item.

**Command** ([[commands/curl-add-to-cart]]):
```bash
curl -X POST -H "Authorization: Bearer YOUR_TOKEN" -H "Content-Type: application/json" -d '{"item_id": 99999, "quantity": 1}' https://api.instacart.com/v2/cart/add
```

> Success if response confirms addition (e.g., 200 OK with cart update).

### Step 3: Proceed to Checkout

**Context**: View cart via web or API and initiate order; no additional bypass needed as item is now in cart.

Use web interface or API checkout endpoint.

> Expected: Order completes with unlisted item included.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Account Discovery]]

### Sub-Techniques

-

## Commands Used

- [[commands/curl-add-to-cart]]

## Tools Used

-

## Tags

- [[idor]]
- [[api]]
- [[exploitation]]
