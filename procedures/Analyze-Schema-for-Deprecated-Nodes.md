---
id: proc-analyze-schema-deprecated
tags:
  - graphql
  - schema-analysis
  - deprecation-leak
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
  - GraphQL
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:25:53.446Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Analyze-Schema-for-Deprecated-Nodes

## Summary

This procedure examines the GraphQL schema response to identify deprecated root-level nodes (e.g., Team, Report, User) and their deprecation reasons, revealing internal implementation details and potential query targets.

## Description

After obtaining the schema via introspection, analysis focuses on fields with 'isDeprecated: true' and 'deprecationReason' to uncover nodes still queryable at root level despite deprecation. This targets environments like HackerOne where such nodes expose sensitive data. Prerequisites: Schema JSON file and a JSON parser like jq. Outcomes include lists of exploitable nodes and hints about future changes (e.g., replacements like 'genius_execution').

## Requirements

1. Schema JSON file from introspection
2. JSON processing tool like jq or manual inspection
3. Understanding of GraphQL schema structure

## Defense

Defensive measures and detection strategies:

- Sanitize schema descriptions to remove internal details before introspection responses
- Enforce deprecation by removing resolver functions for deprecated fields
- Log and alert on schema analysis patterns in client queries

## Objectives

1. Identify queryable deprecated nodes
2. Extract deprecation reasons for implementation leaks
3. Map hidden opportunities for data access

## Instructions

### Step 1: Extract Deprecated Fields

**Context**: Use jq to filter types with deprecated fields from the schema.

**Command** (jq filter):
```bash
jq '.data.__schema.types[] | select(has("fields")) | .fields[]? | select(.isDeprecated == true) | {name: .name, deprecationReason: .deprecationReason, type: .type.name}' schema.json > deprecated_fields.json
```

> Outputs deprecated fields like 'team' with reasons, e.g., revealing database hints or future fields.

### Step 2: Review Root Query Types

**Context**: Focus on queryType to find root-level deprecated nodes.

**Command** (jq query):
```bash
jq '.data.__schema.queryType.fields[] | select(.isDeprecated == true)' schema.json
```

> Identifies root nodes like 'team', 'report' marked deprecated but still accessible.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques

- None

## Commands Used

- None (uses jq for analysis)

## Tools Used

- None

## Tags

- schema-analysis
- deprecation
- information-gathering
