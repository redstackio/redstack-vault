---
id: proc-intercept-modify-graphql-query
tags:
  - graphql
  - interception
  - modification
  - information-disclosure
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/shopify-graphql-shopapps-query]]'
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:53.586Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Intercept-and-Modify-GraphQL-Query

## Summary

This procedure involves intercepting a legitimate GraphQL request in Shopify's admin interface and modifying it to query for a large set of apps, exploiting the lack of access controls to disclose private app details.

## Description

The Shopify GraphQL API at /users/api lacks proper scoping in the shopApps resolver, allowing authenticated Plus users to fetch all apps, including private ones from other stores. By intercepting the POST request triggered in the users section and altering the query to request up to 10,000 results, attackers can extract sensitive fields like API client IDs.

## Requirements

1. Active Shopify Plus admin session
2. Burp Suite or similar proxy tool running and configured (browser proxy set to 127.0.0.1:8080)
3. Knowledge of the target organization ID in the URL path

## Defense

Defensive measures and detection strategies:

- Implement query depth limits and authentication checks in GraphQL resolvers
- Log and monitor GraphQL queries for anomalies like large 'first' parameters
- Use rate limiting on API endpoints and validate user scopes

## Objectives

1. Capture the original shopApps query request
2. Modify it to expand results and include private app fields
3. Send the altered request to trigger disclosure

## Instructions

### Step 1: Trigger and Intercept Request

**Context**: Navigate to the users section to generate the initial API call.

No command required; in the Shopify admin, go to Settings > Users and permissions while proxying traffic through Burp Suite.

> The POST request to /{ID}/users/api will be intercepted. Expected output: Request details in Burp Proxy history.

### Step 2: Forward to Repeater and Modify

**Context**: Prepare the request for editing to exploit the vulnerability.

**Command** ([[commands/shopify-graphql-shopapps-query]]):

In Burp Repeater, update the body to:

```json
{"query":"query xxx { shopApps(first:10000) { edges { node { id isPrivate handle name title shopifyApiClientId } } } }"}
```

> This expands the query to fetch 10,000 apps with private fields. Send the request. Expected output: 200 OK with JSON payload.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used

- [[commands/shopify-graphql-shopapps-query]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- graphql
- interception
- modification
- information-disclosure
