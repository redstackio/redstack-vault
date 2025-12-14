---
tags:
  - information-disclosure
  - inventory
  - graphql
  - shopify
type: procedure
tools:
  - '[[tools/GraphiQL]]'
tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Software]]'
  - '[[Data from Information Repositories]]'
updated_at: '2025-12-14T17:25:53.072Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 64fda83f-7c6d-4c90-b84c-16dbb68a4abf
validated: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Software]]'
  - '[[Data from Information Repositories]]'
---
# Query-Inventory-Levels-Without-Inventory-Permissions

## Summary

This procedure demonstrates accessing inventory levels via the 'inventoryLevel' query using an inventoryItemId, bypassing required 'inventory' permissions in Shopify's GraphQL API.

## Description

The API allows querying inventory data by ID without validating user scopes, potentially exposing stock levels and supply chain details. This is executed on the QueryRoot endpoint and assumes knowledge of an inventoryItemId from prior product queries. The vulnerability aids in business intelligence gathering or competitive analysis.

## Requirements

1. GraphQL session with 'Apps' permissions
2. Known inventoryItemId (e.g., from product variant queries)
3. GraphiQL for query execution

## Defense

Defensive measures and detection strategies:

- Validate inventory scopes before resolving item IDs in queries
- Audit GraphQL logs for inventory queries from unauthorized scopes
- Implement field-level authorization in the GraphQL resolver

## Objectives

1. Retrieve inventory quantities without permissions
2. Validate lack of access controls on inventory endpoints
3. Collect supply data for further exploitation

## Instructions

### Step 1: Obtain Inventory Item ID

**Context**: If not known, query products to get variant IDs, then derive inventoryItemId.

**Instructions**: Use a basic product query to find an item ID.

### Step 2: Query Inventory Level

**Context**: Directly query the inventory level using the ID.

**Command** ([[Custom GraphQL Query]]):

```graphql
query {
  inventoryLevel(inventoryItemId: "gid://shopify/InventoryItem/EXAMPLE_ID") {
    id
    available
    updatedAt
    location {
      name
    }
  }
}
```

> Replace EXAMPLE_ID with a real ID. Expected output includes available stock count and update timestamp, confirming disclosure.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery
- [[Collection]] Collection

### Techniques

- [[Software]] Gather Victim Host Information: Software
- [[Data from Information Repositories]] Data from Information Repositories

### Sub-Techniques

- None

## Commands Used

- Custom GraphQL query for inventory

## Tools Used

- [[tools/GraphiQL]]

## Tags

- [[information-disclosure]]
- [[inventory]]
- [[graphql]]
