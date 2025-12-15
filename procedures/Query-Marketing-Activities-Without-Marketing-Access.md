---
tags:
  - information-disclosure
  - marketing
  - graphql
  - shopify
type: procedure
tools:
  - '[[tools/GraphiQL]]'
tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
commands:
  - '[[commands/graphql-query-marketing-activities]]'
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
  - '[[Data from Information Repositories]]'
updated_at: '2025-12-14T17:25:53.070Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 603082d3-aff8-4c38-9e75-fb025fc892b7
validated: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
  - '[[Data from Information Repositories]]'
---
# Query-Marketing-Activities-Without-Marketing-Access

## Summary

This procedure retrieves marketing activities, including budgets, via GraphQL without 'Marketing and Discounts' permissions, exposing campaign details and financial data.

## Description

Shopify's marketingActivities query lacks scope enforcement, allowing low-privilege users to access IDs, titles, dates, and budgets. This can reveal marketing strategies and expenditures. Executed via QueryRoot in GraphiQL, it targets stores with active campaigns.

## Requirements

1. 'Apps' permission session in GraphiQL
2. Target store with marketing activities configured
3. Basic GraphQL query knowledge

## Defense

Defensive measures and detection strategies:

- Enforce marketing scopes in GraphQL resolvers
- Monitor for budget-related queries from non-marketing users
- Use anomaly detection on API access patterns

## Objectives

1. Disclose marketing campaign details
2. Extract budget information for financial reconnaissance
3. Bypass marketing permission requirements

## Instructions

### Step 1: Construct Marketing Query

**Context**: Limit to 100 to manage response size while capturing key data.

**Instructions**: Prepare the query focusing on budget totals.

### Step 2: Execute Query

**Context**: Run to fetch activities, expecting full disclosure.

**Command** ([[commands/graphql-query-marketing-activities]]):

```graphql
query {
  marketingActivities(first: 100) {
    edges {
      node {
        id
        title
        createdAt
        budget {
          total {
            amount
          }
        }
      }
    }
  }
}
```

> Expected output: JSON with up to 100 activities, including budget amounts in the store's currency, no errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery
- [[Collection]] Collection

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information
- [[Data from Information Repositories]] Data from Information Repositories

### Sub-Techniques

- None

## Commands Used

- [[commands/graphql-query-marketing-activities]]

## Tools Used

- [[tools/GraphiQL]]

## Tags

- [[information-disclosure]]
- [[marketing]]
- [[budget-exposure]]
