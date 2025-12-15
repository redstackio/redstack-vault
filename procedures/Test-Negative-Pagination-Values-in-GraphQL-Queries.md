---
tags:
  - graphql
  - shopify
  - parameter-testing
type: procedure
tools:
  - '[[tools/Shopify-GraphiQL-App]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/negative-pagination-test-query]]'
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:53.344Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 895f07b9-baf7-4c88-9e9b-c92aa9f1d081
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-Negative-Pagination-Values-in-GraphQL-Queries

## Summary

Test GraphQL queries with negative pagination values like 'first: -100' to observe if they result in negative costs, revealing the business logic flaw for rate limit manipulation.

## Description

In Shopify's GraphQL API, pagination parameters such as 'first' in fields like appInstallations are not validated against negative integers. Executing queries with these values deducts negative points from the cost bucket, effectively refilling it. This procedure uses the GraphiQL app to test and confirm the vulnerability.

## Requirements

1. Access to Shopify GraphiQL App at https://example.myshopify.com/admin/apps/shopify-graphiql-app
2. Valid authentication as an app developer
3. Full rate limit bucket to observe changes clearly

## Defense

Defensive measures and detection strategies:

- Enforce server-side validation on pagination parameters to reject negatives
- Log and alert on queries with negative parameters
- Use query cost calculators to detect anomalies

## Objectives

1. Confirm negative 'first' values cause negative costs
2. Measure bucket impact from a single test query
3. Validate exploitability for refill scenarios

## Instructions

### Step 1: Prepare GraphiQL Interface

**Context**: Open the GraphiQL app and ensure a fresh session with full bucket.

No command; navigate to the app URL.

> Expected: Interface ready for query input, bucket at 1000 points.

### Step 2: Execute Test Query

**Context**: Run a simple query with negative pagination to check cost.

**Command** ([[commands/negative-pagination-test-query]]):
```graphql
{
  appInstallations(first: -100) {
    edges {
      node {
        id
      }
    }
  }
}
```

> Execute via GraphiQL; observe the 'extensions' in response showing cost: -100 or similar, increasing bucket points.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/negative-pagination-test-query]]

## Tools Used

- [[tools/Shopify-GraphiQL-App]]

## Tags

- graphql
- shopify
- parameter-testing
