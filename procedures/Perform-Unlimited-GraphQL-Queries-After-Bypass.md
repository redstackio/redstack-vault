---
tags:
  - graphql
  - shopify
  - unlimited-api-calls
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
updated_at: '2025-12-14T17:25:53.306Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 0c3ef3f5-5e4f-49fb-a803-55141ec58d93
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
---
# Perform-Unlimited-GraphQL-Queries-After-Bypass

## Summary

With the rate limit bucket refilled, execute repeated standard or high-cost GraphQL queries to confirm the bypass, demonstrating indefinite API access without throttling.

## Description

Post-refill, the manipulated bucket allows continuous queries, potentially leading to excessive resource usage, data exfiltration, or denial of service against the Shopify backend.

## Requirements

1. Refilled bucket from prior procedure
2. GraphiQL app ready
3. Target queries prepared

## Defense

Defensive measures and detection strategies:

- Implement secondary rate limits based on time windows
- Use anomaly detection for refill-like bucket behaviors
- Rate limit per IP or app key independently of cost bucket

## Objectives

1. Verify no throttling on subsequent queries
2. Demonstrate sustained high-volume access
3. Highlight DoS potential

## Instructions

### Step 1: Execute Standard Queries

**Context**: Run normal queries to test persistence.

**Command** ([[commands/high-cost-appinstallations-query]]):
```graphql
{
  appInstallations(first: 10) {
    edges {
      node {
        id
      }
    }
  }
}
```

> Repeat multiple times; expect no throttleStatus errors.

### Step 2: Scale to High Volume

**Context**: Increase frequency to simulate abuse.

Repeat the command indefinitely.

> Expected: All queries succeed, bucket stays manageable via repeats of refill if needed.

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
- unlimited-api-calls
