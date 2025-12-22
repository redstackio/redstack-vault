---
tags:
  - idor
  - graphql
  - discovery
  - stripe
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:53.458Z'
sub_techniques: []
id: 5f3ff1ce-753b-4d17-a50d-cd3470a4ce2f
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Discover-IDOR-in-Stripe-GraphQL-API

## Summary

This procedure outlines how to identify an Insecure Direct Object Reference (IDOR) vulnerability in Stripe's GraphQL API, specifically in the UpdateAtlasApplicationPerson mutation, by inspecting the schema and testing for missing authorization checks on cross-tenant IDs.

## Description

In a scenario where an attacker has admin access to a Stripe account, they can use GraphQL introspection to examine the API schema for the UpdateAtlasApplicationPerson operation. The vulnerability arises from the mutation accepting direct object IDs (e.g., application and person IDs) without verifying tenant ownership, allowing manipulation of resources across tenants. This procedure focuses on discovery through schema analysis and initial testing, assuming access to Stripe's GraphQL endpoint at api.stripe.com/graphql. Expected outcomes include confirmation of vulnerable parameters, setting the stage for exploitation.

## Requirements

1. Valid admin API key or session for a Stripe merchant account
2. Access to a GraphQL client or tool for introspection (e.g., browser GraphQL playground if available, or curl)
3. Knowledge of basic GraphQL queries and Stripe Atlas application structure

## Defense

Defensive measures and detection strategies:

- Implement tenant-specific authorization checks in all GraphQL mutations
- Use schema introspection restrictions or tools like GraphQL Armor to limit discovery
- Monitor API logs for anomalous ID usage across tenants

## Objectives

1. Expose lack of isolation in object references
2. Baseline normal mutation behavior on same-tenant IDs
3. Identify potential for cross-tenant access

## Instructions

### Step 1: Authenticate and Introspect Schema

**Context**: Gain access to the GraphQL endpoint and query the schema to locate the UpdateAtlasApplicationPerson mutation.

Authenticate using your Stripe API key. Send an introspection query to retrieve the mutation's input types and fields.

Example introspection query:

```graphql
query IntrospectionQuery {
  __schema {
    mutationType {
      fields {
        name
        args {
          name
          type {
            name
          }
        }
      }
    }
  }
}
```

Submit via HTTP POST to https://api.stripe.com/graphql with Authorization header.

> This reveals that UpdateAtlasApplicationPerson accepts inputs like atlasApplicationId and person details without embedded tenant checks.

### Step 2: Test Baseline Mutation

**Context**: Execute the mutation on your own tenant's IDs to confirm functionality and observe normal responses.

Use known IDs from your account to update a person in your Atlas application.

Example mutation (as shown in attack chain):

```graphql
mutation {
  updateAtlasApplicationPerson(input: {atlasApplicationId: "your_app_id", person: {id: "your_person_id"}}) {
    atlasApplication { id }
  }
}
```

> Successful response includes updated IDs, confirming the endpoint works as expected for authorized use.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- idor
- graphql
- discovery
