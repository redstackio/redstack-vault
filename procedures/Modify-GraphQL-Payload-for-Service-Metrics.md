---
id: proc-modify-graphql-payload
tags:
  - payload-modification
  - graphql
  - bypass
  - shopify
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/shopify-graphql-service-metrics-query]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:20.456Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Modify-GraphQL-Payload-for-Service-Metrics

## Summary

This procedure modifies an intercepted GraphQL request in Shopify's partner dashboard to query serviceMetrics totalEarnings, bypassing the 'View financials' permission check and enabling unauthorized data retrieval.

## Description

The original notification request payload is edited to include a query for { serviceMetrics { totalEarnings { amount } } }. Forwarding this to the endpoint at https://partners.shopify.com/:id/api/graphql exploits the missing authorization validation, allowing low-priv users to access financial amounts.

## Requirements

1. Intercepted GraphQL request from previous step
2. Browser dev tools or proxy for payload editing
3. Valid session cookie for the request

## Defense

Defensive measures and detection strategies:

- Enforce permission checks on all GraphQL resolvers, especially for financial queries
- Log and audit GraphQL queries for permission mismatches
- Use schema introspection limits and query validation

## Objectives

1. Craft and send unauthorized GraphQL query
2. Bypass permission enforcement
3. Trigger response with sensitive data

## Instructions

### Step 1: Edit Payload

**Context**: Replace the original query with the exploitative one.

In dev tools or proxy, update the request body to use [[commands/shopify-graphql-service-metrics-query]]:

```json
{ "query":"{ serviceMetrics { totalEarnings { amount } } }" }
```

> This queries totalEarnings without permission validation.

### Step 2: Forward Request

**Context**: Send the modified request to the server.

Resume or forward the request in the interception tool.

> Server processes the query and prepares response.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/shopify-graphql-service-metrics-query]]

## Tools Used


## Tags

- [[payload-modification]]
- [[graphql-bypass]]
- [[financial-access]]
