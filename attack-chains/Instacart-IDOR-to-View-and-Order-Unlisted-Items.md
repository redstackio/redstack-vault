---
id: ac-instacart-idor-unlisted-items
tags:
  - idor
  - api
  - web
  - access-bypass
  - instacart
type: attack_chain
tools: []
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Identify-Instacart-API-Endpoints-for-Item-Management]]'
  - '[[procedures/Manipulate-Item-IDs-to-Access-Unlisted-Items-via-IDOR]]'
  - '[[procedures/Add-Unlisted-Items-to-Cart-and-Complete-Order-via-IDOR]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:29.390Z'
description: >-
  Multi-stage exploitation of an Insecure Direct Object Reference (IDOR)
  vulnerability in Instacart's API, allowing authenticated users to access and
  order items not visible in the web catalog by manipulating item IDs.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
# Instacart IDOR to View and Order Unlisted Items

Multi-stage attack chain demonstrating the exploitation of an IDOR vulnerability in Instacart's API to bypass web catalog visibility controls and access unlisted items.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Identify API Endpoints] --> B[Manipulate Item IDs]
    B --> C[Add to Cart and Order]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools or [[tools/curl]]
- Authenticated Instacart account

### Target Environment

- Instacart web platform (API endpoints)
- No specific ports required (HTTPS/443)
- Network access to Instacart API

### Initial Access Requirements

- Valid authenticated session (user login)
- API access via web or direct HTTP requests
- No prior elevated access needed

## Detailed Attack Procedures

### Step 1: Identify API Endpoints
procedure: [[procedures/Identify-Instacart-API-Endpoints-for-Item-Management]]

**Objective**: Locate API endpoints responsible for viewing and adding items to the cart, which accept item IDs without visibility checks.

**Instructions**: Use browser developer tools to inspect network requests during normal item browsing, or send test API calls with [[commands/curl-view-item]] to confirm endpoints.

```bash
curl -H "Authorization: Bearer YOUR_TOKEN" -H "Content-Type: application/json" https://api.instacart.com/v2/items/12345
```

Then test cart addition with [[commands/curl-add-to-cart]]:

```bash
curl -X POST -H "Authorization: Bearer YOUR_TOKEN" -H "Content-Type: application/json" -d '{"item_id": 12345, "quantity": 1}' https://api.instacart.com/v2/cart/add
```

**Expected Output**: JSON response with item details or successful addition confirmation.

**Success Indicators**:
- API endpoints return item data without errors
- Cart addition succeeds for visible items

### Step 2: Manipulate Item IDs
procedure: [[procedures/Manipulate-Item-IDs-to-Access-Unlisted-Items-via-IDOR]]

**Objective**: Exploit IDOR by using arbitrary item IDs to retrieve details of unlisted items not shown in the web catalog.

**Instructions**: Increment or guess item IDs beyond visible catalog range using [[commands/curl-view-item]] with manipulated IDs (e.g., start from known ID +1).

```bash
curl -H "Authorization: Bearer YOUR_TOKEN" -H "Content-Type: application/json" https://api.instacart.com/v2/items/99999
```

Validate by checking if the response contains item data not visible in the web interface.

**Expected Output**: JSON with unlisted item details (name, price, etc.).

**Success Indicators**:
- Response includes hidden item information
- No authorization error for the manipulated ID

### Step 3: Add Unlisted Items to Cart and Complete Order
procedure: [[procedures/Add-Unlisted-Items-to-Cart-and-Complete-Order-via-IDOR]]

**Objective**: Bypass access controls to add unlisted items to the cart and proceed to checkout.

**Instructions**: Use the manipulated item ID in a cart addition request with [[commands/curl-add-to-cart]], then simulate checkout via API or web interface.

```bash
curl -X POST -H "Authorization: Bearer YOUR_TOKEN" -H "Content-Type: application/json" -d '{"item_id": 99999, "quantity": 1}' https://api.instacart.com/v2/cart/add
```

Follow up by viewing cart and initiating order.

**Expected Output**: Confirmation of item added to cart; order proceeds without visibility checks.

**Success Indicators**:
- Unlisted item appears in cart
- Checkout completes successfully

## Attack Chain Summary

### Key Achievements

1. Identified vulnerable API endpoints lacking visibility authorization.
2. Accessed unlisted items via IDOR manipulation.
3. Added and ordered hidden items, bypassing web controls.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Account Discovery]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*
