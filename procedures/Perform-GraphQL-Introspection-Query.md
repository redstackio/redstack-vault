---
id: proc-graphql-introspection
tags:
  - graphql
  - introspection
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/graphql-introspection-query]]'
verified: false
platforms:
  - Web
  - GraphQL
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T17:25:53.449Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Perform-GraphQL-Introspection-Query

## Summary

This procedure sends a standard GraphQL introspection query to a public endpoint to retrieve the full schema, including types, fields, arguments, deprecations, and descriptions, enabling attackers to map the backend API structure.

## Description

GraphQL introspection is a feature allowing clients to query the schema itself, but when enabled on public endpoints without restrictions, it exposes sensitive backend details. In this scenario, targeting https://hackerone.com/graphql reveals the entire schema, facilitating targeted attacks. Prerequisites include access to the endpoint and a tool like curl for HTTP requests. Expected outcomes include a comprehensive JSON schema that can be analyzed for vulnerabilities like deprecated or hidden fields.

## Requirements

1. Network access to the GraphQL endpoint (e.g., public internet)
2. HTTP client like curl installed
3. Basic GraphQL knowledge for query construction

## Defense

Defensive measures and detection strategies:

- Disable introspection on production public endpoints using tools like GraphQL Armor or server configurations
- Implement rate limiting and authentication on API queries
- Monitor for introspection queries in logs (e.g., patterns matching __schema or __type)

## Objectives

1. Obtain full API schema for reconnaissance
2. Identify deprecated and hidden elements
3. Enable crafting of malicious follow-up queries

## Instructions

### Step 1: Prepare and Send Introspection Query

**Context**: Construct the standard introspection query payload and POST it to the GraphQL endpoint to fetch the schema.

**Command** ([[commands/graphql-introspection-query]]):
```bash
curl -X POST https://hackerone.com/graphql -H "Content-Type: application/json" -d '{"query": "query IntrospectionQuery {__schema {queryType { name },mutationType { name },subscriptionType { name },types {...FullType},directives {name,description,args {...InputValue},onOperation,onFragment,onField}}}\nfragment FullType on __Type {kind,name,description,fields(includeDeprecated: true) {name,description,args {...InputValue},type {...TypeRef},isDeprecated,deprecationReason},inputFields {...InputValue},interfaces {...TypeRef},enumValues(includeDeprecated: true) {name,description,isDeprecated,deprecationReason},possibleTypes {...TypeRef}}\nfragment InputValue on __InputValue {name,description,type { ...TypeRef },defaultValue}\nfragment TypeRef on __Type {kind,name,ofType {kind,name,ofType {kind,name,ofType {kind,name}}}}")}' -o schema.json
```

> This command sends the introspection query and saves the response to schema.json. Expected output is a large JSON object under 'data.__schema' detailing all types and fields.

### Step 2: Validate Response

**Context**: Check the response for successful schema retrieval.

**Command** (jq parse):
```bash
jq '.data.__schema' schema.json | head -20
```

> Verifies the presence of schema elements like queryType and types array.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Vulnerability Scanning]] Vulnerability Scanning

### Sub-Techniques

- None

## Commands Used

- [[commands/graphql-introspection-query]]

## Tools Used

- None

## Tags

- graphql
- introspection
- api-recon
