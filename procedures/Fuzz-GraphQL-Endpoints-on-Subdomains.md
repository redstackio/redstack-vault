---
tags:
  - fuzzing
  - graphql
  - reconnaissance
type: procedure
tools:
  - '[[tools/wfuzz]]'
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Active Scanning]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: ea2a74eb-ff30-42ed-a987-50831aa664af
created_at: '2025-12-14T17:25:59.622Z'
updated_at: '2025-12-14T17:25:59.622Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Fuzz GraphQL Endpoints on Subdomains

## Summary

This procedure uses fuzzing to scan subdomains of a target domain for responsive GraphQL endpoints by sending random queries to /graphql paths and filtering for 200 responses, enabling subsequent introspection.

## Description

In the context of reconnaissance against services like Shopify's cloud infrastructure, subdomain fuzzing identifies hidden APIs. Tools like wfuzz send payloads to potential endpoints, and Burp Repeater handles follow-up introspection. Prerequisites include a list of subdomains (e.g., from crt.sh or subfinder) and basic HTTP knowledge. Expected outcomes: Discovery of endpoints like beerify.shopifycloud.com/graphql, allowing schema mapping without auth.

## Requirements

1. List of subdomains for *.shopifycloud.com
2. wfuzz installed for fuzzing
3. Burp Suite for precise querying
4. Network access to public web

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on API endpoints
- Require authentication for GraphQL introspection
- Monitor for anomalous query patterns in logs
- Use WAF rules to block fuzzing payloads

## Objectives

1. Identify active GraphQL endpoints
2. Download schema for further exploitation
3. Map queryable objects like locations

## Instructions

### Step 1: Collect Subdomains and Fuzz

**Context**: Gather subdomains and use wfuzz to test /graphql with random GraphQL queries, filtering 200s.

**Command** (wfuzz fuzzing):
```bash
wfuzz -c -z file,/path/to/subdomains.txt -z file,/path/to/random_graphql_queries.txt --hc 404,403 https://FUZZ.shopifycloud.com/graphql
```

> This sends payloads to endpoints, capturing responsive ones. Expected output: Hits on beerify.shopifycloud.com with 200 status.

### Step 2: Introspect in Burp Repeater

**Context**: For responsive endpoints, add Content-Type: application/json and send introspection query to avoid errors.

**Command** (Introspection query in Burp):
```bash
POST /graphql HTTP/1.1
Host: beerify.shopifycloud.com
Content-Type: application/json

{"query": "query IntrospectionQuery { __schema { queryType { name } mutationType { name } subscriptionType { name } types { ...FullType } directives { name description locations args { ...InputValue } } } } fragment FullType on __Type { kind name description fields(includeDeprecated: true) { name description args { ...InputValue } type { ...TypeRef } isDeprecated deprecationReason } inputFields { ...InputValue } interfaces { ...TypeRef } enumValues(includeDeprecated: true) { name description isDeprecated deprecationReason } possibleTypes { ...TypeRef } } fragment InputValue on __InputValue { name description type { ...TypeRef } defaultValue } fragment TypeRef on __Type { kind name ofType { kind name ofType { kind name ofType { kind name ofType { kind name ofType { kind name ofType { kind name ofType { kind name } } } } } } } }"}
```

> Downloads full schema. Expected output: JSON with types like allLocations, location, taps.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/wfuzz]]
- [[tools/Burp-Suite]]

## Tags

- fuzzing
- graphql
- reconnaissance
