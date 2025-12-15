---
tags:
  - graphql
  - shopify
  - rate-limit-bypass
  - business-logic
  - api-abuse
type: attack_chain
tools:
  - '[[tools/Shopify-GraphiQL-App]]'
tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
verified: false
platforms:
  - Web
  - Shopify
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Review-Shopify-GraphQL-Rate-Limiting-Documentation]]'
  - '[[procedures/Test-Negative-Pagination-Values-in-GraphQL-Queries]]'
  - '[[procedures/Deplete-Shopify-GraphQL-Rate-Limit-Bucket]]'
  - '[[procedures/Refill-Shopify-GraphQL-Bucket-with-Negative-Query-Cost]]'
  - '[[procedures/Perform-Unlimited-GraphQL-Queries-After-Bypass]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:25:53.362Z'
description: >-
  Multi-stage attack exploiting a business logic flaw in Shopify's GraphQL API
  to bypass rate limiting by manipulating query costs with negative pagination
  values, enabling unlimited API calls and potential denial of service.
skill_level: intermediate
impact_level: high
id: ae200f38-ea92-4a5b-83fd-38da4005ac53
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Denial of Service]]'
---
# Bypass Shopify GraphQL Rate Limit Using Negative Pagination Costs

Multi-stage attack chain demonstrating a business logic vulnerability in Shopify's GraphQL API, where negative values for pagination parameters like 'first' result in negative query costs. This allows attackers to deplete the rate limit bucket and then refill it, bypassing throttling and enabling indefinite API calls. Discovered via parameter testing in the GraphiQL app, this can lead to denial of service or unfair API usage advantages for app developers.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Review Documentation] --> B[Test Negative Values]
    B --> C[Deplete Bucket]
    C --> D[Refill with Negative Cost]
    D --> E[Unlimited Queries]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#f39c12
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Shopify-GraphiQL-App]]

### Target Environment

- Shopify Admin API platform
- GraphQL endpoint access
- Valid app developer credentials for the target store

### Initial Access Requirements

- Authenticated access to Shopify Admin via GraphiQL app
- Network access to the store's admin URL (e.g., https://example.myshopify.com/admin)
- No prior exploits needed; requires legitimate API access

## Detailed Attack Procedures

### Step 1: Review Rate Limiting Documentation
procedure: [[procedures/Review-Shopify-GraphQL-Rate-Limiting-Documentation]]

**Objective**: Understand the GraphQL rate limiting mechanism to identify potential manipulation points.

**Instructions**: Access and analyze Shopify's official documentation on GraphQL query costs and rate limits. Note that each app has a 1000-point bucket that refreshes over time.

**Expected Output**: Confirmation of the cost-based throttling system, where queries deduct points and exceedance leads to throttling.

**Success Indicators**:
- Documentation reviewed, understanding of bucket mechanics confirmed
- Identification of pagination parameters like 'first' as potential vectors

### Step 2: Test Negative Pagination Values
procedure: [[procedures/Test-Negative-Pagination-Values-in-GraphQL-Queries]]

**Objective**: Verify if negative values in pagination parameters cause negative query costs.

**Instructions**: Use the GraphiQL app to execute a query with a negative 'first' value, such as appInstallations(first: -100), and observe the cost impact on the bucket.

**Expected Output**: Query executes with a negative cost deduction, effectively adding points back to the bucket.

**Success Indicators**:
- Negative cost observed in the response (e.g., cost: -100)
- Bucket points increase instead of decrease

### Step 3: Deplete the Rate Limit Bucket
procedure: [[procedures/Deplete-Shopify-GraphQL-Rate-Limit-Bucket]]

**Objective**: Exhaust the query cost bucket using high-cost legitimate queries to set up the refill.

**Instructions**: Execute a complex GraphQL query with nested fields multiple times until the bucket is low (around 50 points). Use [[commands/high-cost-appinstallations-query]] via the GraphiQL app.

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

Repeat 10-15 times until bucket is depleted.

**Expected Output**: Bucket points drop to near zero, triggering near-throttle state.

**Success Indicators**:
- Bucket at ~50 points or less
- Queries start approaching throttle limits

### Step 4: Refill the Bucket with Negative Cost
procedure: [[procedures/Refill-Shopify-GraphQL-Bucket-with-Negative-Query-Cost]]

**Objective**: Exploit the negative cost to restore the bucket to maximum capacity.

**Instructions**: Modify the high-cost query by changing one 'first' parameter to -1000, then execute [[commands/negative-cost-appinstallations-query]].

**Expected Output**: Bucket refills to 1000 points, with the query succeeding despite the negative value.

**Success Indicators**:
- Bucket restored to 1000 points
- No throttling error received

### Step 5: Perform Unlimited Queries After Bypass
procedure: [[procedures/Perform-Unlimited-GraphQL-Queries-After-Bypass]]

**Objective**: Confirm the bypass by executing additional queries without throttling.

**Instructions**: Run standard high-cost queries repeatedly, verifying no rate limit enforcement.

**Expected Output**: Indefinite successful API calls, potentially overwhelming the service.

**Success Indicators**:
- Multiple queries execute without errors
- Sustained high-volume API usage possible

## Attack Chain Summary

### Key Achievements

1. Identified business logic flaw in pagination parameter validation
2. Bypassed rate limiting to enable unlimited GraphQL queries
3. Demonstrated potential for denial of service or API abuse

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Network Denial of Service]] Network Denial of Service

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Impact]] Impact

---
*Last updated: 2023-10-01T00:00:00Z*
