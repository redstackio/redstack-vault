---
id: p-identify-instacart-api-endpoints
tags:
  - api
  - recon
  - idor
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-view-item]]'
  - '[[commands/curl-add-to-cart]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:25:29.377Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify Instacart API Endpoints for Item Management

## Summary

This procedure involves discovering the API endpoints in Instacart's platform used for viewing item details and adding items to the cart, which rely on item IDs without enforcing web catalog visibility checks.

## Description

In the context of Instacart's web application, authenticated users interact with the API to manage shopping carts. The endpoints accept direct item ID parameters but fail to validate if the item is listed in the public web catalog, setting the stage for IDOR exploitation. This step requires an authenticated session and focuses on mapping the API surface through inspection or direct requests. Expected outcomes include confirmation of endpoint functionality for both GET (view) and POST (add) operations.

## Requirements

1. Authenticated Instacart account with valid API token (obtained via login).
2. Access to browser developer tools or curl for HTTP requests.
3. Network connectivity to Instacart's API (https://api.instacart.com).

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on API endpoints to detect enumeration.
- Log and monitor unusual item ID requests outside catalog ranges.
- Enforce visibility checks by cross-referencing item IDs against user-accessible catalogs.

## Objectives

1. Locate vulnerable API endpoints for item retrieval and cart management.
2. Verify that endpoints accept arbitrary item IDs without immediate rejection.
3. Establish baseline for ID manipulation in subsequent steps.

## Instructions

### Step 1: Inspect Network Traffic

**Context**: Use browser tools to capture legitimate API calls during normal usage, identifying endpoints like /v2/items/{id} and /v2/cart/add.

No specific command; observe in DevTools Network tab while browsing items.

> Expected: Requests reveal endpoint URLs and required headers (Authorization, Content-Type).

### Step 2: Test View Endpoint

**Context**: Send a request to the item view endpoint with a known visible item ID to confirm functionality.

**Command** ([[commands/curl-view-item]]):
```bash
curl -H "Authorization: Bearer YOUR_TOKEN" -H "Content-Type: application/json" https://api.instacart.com/v2/items/12345
```

> This retrieves item details; success indicates the endpoint is active and lacks basic auth checks.

### Step 3: Test Add to Cart Endpoint

**Context**: Attempt to add a known item to the cart to map the POST endpoint.

**Command** ([[commands/curl-add-to-cart]]):
```bash
curl -X POST -H "Authorization: Bearer YOUR_TOKEN" -H "Content-Type: application/json" -d '{"item_id": 12345, "quantity": 1}' https://api.instacart.com/v2/cart/add
```

> Response should confirm addition; note the payload structure for later manipulation.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques

-

## Commands Used

- [[commands/curl-view-item]]
- [[commands/curl-add-to-cart]]

## Tools Used

-

## Tags

- [[api]]
- [[recon]]
- [[idor]]
