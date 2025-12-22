---
tags:
  - graphql
  - shopify
  - recon
type: procedure
tools:
  - '[[tools/Shopify-GraphiQL-App]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:25:53.351Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 8d509f1d-994b-47df-9533-28469996a50b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Review-Shopify-GraphQL-Rate-Limiting-Documentation

## Summary

This procedure involves reviewing Shopify's GraphQL Admin API documentation to understand the rate limiting mechanism, identifying the query cost bucket system as a potential attack vector for manipulation.

## Description

Shopify's GraphQL API uses a cost-based rate limiting system where each app has a 1000-point bucket that deducts points per query and refreshes over time. Insufficient validation on parameters like 'first' in pagination fields allows negative values to cause negative costs. This procedure sets the stage for exploiting this by confirming the mechanics via official docs at https://help.shopify.com/en/api/graphql-admin-api/call-limit.

## Requirements

1. Internet access to Shopify documentation
2. Basic understanding of GraphQL and API rate limiting
3. Valid Shopify developer account for context

## Defense

Defensive measures and detection strategies:

- Regularly audit API documentation for changes in rate limiting
- Implement client-side validation to prevent negative parameter submission
- Monitor for unusual query patterns in API logs

## Objectives

1. Understand the 1000-point cost bucket and refresh mechanics
2. Identify pagination parameters as manipulation targets
3. Prepare for testing negative value impacts

## Instructions

### Step 1: Access Documentation

**Context**: Locate and read the official rate limiting guide to grasp the system.

No specific command; browse https://help.shopify.com/en/api/graphql-admin-api/call-limit.

> Review sections on query costs, bucket limits, and throttling. Note that complex queries with nested fields cost more points.

### Step 2: Note Key Mechanics

**Context**: Document the bucket behavior for later exploitation.

No command; manually note that buckets reset over time and negative costs could theoretically refill them.

> Expected: Confirmation that 'first' parameter controls result limits but lacks negative value checks.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Shopify-GraphiQL-App]]

## Tags

- graphql
- shopify
- recon
