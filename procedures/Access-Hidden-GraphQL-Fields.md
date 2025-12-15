---
id: proc-access-hidden-fields
tags:
  - graphql
  - hidden-fields
  - sla-metrics
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/query-hidden-sla-fields]]'
verified: false
platforms:
  - Web
  - GraphQL
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:25:53.427Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Access-Hidden-GraphQL-Fields

## Summary

This procedure uses schema information from introspection to query undisclosed or hidden fields on nodes, such as SLA failure counts on the team entity, leading to exposure of sensitive metrics.

## Description

Full schema exposure allows discovery of fields not documented or intended for public use, like sla_failed_count and sla_missed_count on HackerOne's team node. These can be queried directly once known, bypassing standard API limitations. Prerequisites: Prior schema analysis. Outcomes: Leakage of internal operational metrics and potential for broader data enumeration.

## Requirements

1. Schema details identifying hidden fields
2. Node identifiers (e.g., team handle)
3. HTTP client for query execution

## Defense

Defensive measures and detection strategies:

- Omit sensitive fields from introspection responses using schema stitching or partial schemas
- Apply field-level access controls based on authentication
- Detect anomalous queries for undocumented fields in API logs

## Objectives

1. Query hidden fields for sensitive data
2. Expose metrics like SLA failures
3. Highlight risks of full schema disclosure

## Instructions

### Step 1: Query Hidden SLA Fields

**Context**: Target hidden fields on the team node using the known handle.

**Command** ([[commands/query-hidden-sla-fields]]):
```bash
curl -X POST https://hackerone.com/graphql -H "Content-Type: application/json" -d '{"query": "query {team(handle:\"security\"){sla_failed_count,sla_missed_count}}"}' -o sla_data.json
```

> Returns metrics; expected output: {"data": {"team": {"sla_failed_count": 0, "sla_missed_count": 0 }}}

### Step 2: Review for Additional Leaks

**Context**: Inspect deprecation reasons in schema for future hints.

**Command** (jq review):
```bash
jq '.data.__schema.types[] | .deprecationReason' schema.json | grep -i "genius_execution"
```

> Reveals upcoming features like 'genius_execution' replacing fields.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques

- None

## Commands Used

- [[commands/query-hidden-sla-fields]]

## Tools Used

- None

## Tags

- hidden-fields
- metrics-leak
- graphql-exploit
