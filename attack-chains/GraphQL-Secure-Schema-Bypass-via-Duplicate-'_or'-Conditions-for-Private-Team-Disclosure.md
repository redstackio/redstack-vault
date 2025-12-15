---
id: ac-graphql-or-bypass-001
tags:
  - graphql
  - information-disclosure
  - api-bypass
  - schema-bypass
type: attack_chain
tools:
  - '[[tools/GraphiQL]]'
tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - >-
    [[procedures/Exploit-GraphQL-Secure-Schema-Bypass-Using-Duplicate-Conditions]]
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:00.102Z'
description: >-
  Multi-stage attack exploiting a GraphQL schema vulnerability to bypass
  security filters and disclose private team states like 'soft_launched' through
  duplicate '_or' conditions.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# GraphQL Secure Schema Bypass via Duplicate '_or' Conditions for Private Team Disclosure

Multi-stage attack chain demonstrating a complete workflow to bypass HackerOne's GraphQL secure schema, exposing private team states such as 'soft_launched' by exploiting the '_or' operator with duplicate conditions. This allows inference of hidden data from responses showing null states, leading to information disclosure of sensitive program details.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup GraphQL Client] --> B[Execute Duplicate '_or' Query]
    B --> C[Observe Inferred Disclosure]
    C --> D[Verify with Single Condition]
    D --> E[Information Disclosure Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/GraphiQL]]

### Target Environment

- Web platform with GraphQL endpoint (e.g., HackerOne API)
- Access to public GraphQL schema
- No special ports required; standard HTTPS (443)

### Initial Access Requirements

- Valid network access to the GraphQL endpoint
- No authentication required for public queries, but authenticated sessions may enhance results
- Basic knowledge of GraphQL syntax

## Detailed Attack Procedures

### Step 1: Setup GraphQL Client

procedure: [[procedures/Exploit-GraphQL-Secure-Schema-Bypass-Using-Duplicate-Conditions]]

**Objective**: Prepare the environment by opening a GraphQL client to interact with the target endpoint.

**Instructions**: Launch GraphiQL or a similar client and point it to the target's GraphQL endpoint, such as https://api.hackerone.com/graphql.

**Expected Output**: Interactive GraphQL interface ready for query execution.

**Success Indicators**:
- Client connects successfully to the endpoint
- Schema introspection available

### Step 2: Execute Duplicate '_or' Query

procedure: [[procedures/Exploit-GraphQL-Secure-Schema-Bypass-Using-Duplicate-Conditions]]

**Objective**: Run the exploiting query using duplicate conditions in the '_or' filter to bypass the secure schema.

**Instructions**: Execute the following GraphQL query using [[commands/graphql-duplicate-or-query]]:

```graphql
query { teams(where:{_or:[{state:{_eq:soft_launched}}, {state:{_eq:soft_launched}}]}) { edges { node { id state } } } }
```

**Expected Output**: Response includes teams with state: null, indicating hidden 'soft_launched' teams are now inferable.

**Success Indicators**:
- Teams returned with null states
- IDs visible for private teams

### Step 3: Observe Response for Inference

procedure: [[procedures/Exploit-GraphQL-Secure-Schema-Bypass-Using-Duplicate-Conditions]]

**Objective**: Analyze the query response to derive private information from null states.

**Instructions**: Review the response from the duplicate '_or' query; null states in the 'state' field confirm exposure of protected data, as single-condition queries would exclude these entirely.

**Expected Output**: List of team IDs with null states, allowing correlation to private 'soft_launched' programs.

**Success Indicators**:
- Null states observed where none expected
- Ability to infer hidden team statuses

### Step 4: Verify with Single Condition Query

procedure: [[procedures/Exploit-GraphQL-Secure-Schema-Bypass-Using-Duplicate-Conditions]]

**Objective**: Confirm the bypass by contrasting with a secure single-condition query.

**Instructions**: Run the verification query using [[commands/graphql-single-state-query]]:

```graphql
query { teams(where: { state: { _eq: soft_launched } }) { edges { node { id state } } } }
```

**Expected Output**: No teams returned, validating that the secure schema blocks direct access.

**Success Indicators**:
- Empty results from single-condition query
- Confirms duplicate '_or' enables disclosure

## Attack Chain Summary

### Key Achievements

1. Bypassed GraphQL secure schema using duplicate '_or' conditions
2. Disclosed private team states like 'soft_launched' via null inference
3. Demonstrated impact on filterable fields in collections like 'teams'
4. Highlighted root cause in Ruby Set handling for GraphQL resolution

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Discovery]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
