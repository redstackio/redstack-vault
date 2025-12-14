---
id: 123e4567-e89b-12d3-a456-426614174002
name: Discover-GraphQL-Mutations-via-Introspection
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:36.827Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - graphql
  - introspection
  - discovery
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Discover-GraphQL-Mutations-via-Introspection

## Summary

This procedure uses GraphQL introspection on the vulnerable Shopify endpoint to enumerate available mutations, revealing exploitable operations like templateInstall for workflow creation.

## Description

The /admin/internal/web/graphql/flow endpoint lacks introspection disablement, allowing schema discovery. This exposes mutations intended for higher-privilege use, enabling low-priv staff to proceed with unauthorized workflow installation.

## Requirements

1. Modified request from prior interception step
2. Burp Suite Repeater access
3. Valid session with low-priv account

## Defense

Defensive measures and detection strategies:

- Disable GraphQL introspection in production
- Log and alert on introspection queries
- Apply permission gates to schema exposure

## Objectives

1. Identify accessible mutations without prior knowledge
2. Confirm endpoint vulnerability to low-priv access
3. Prepare for targeted mutation exploitation

## Instructions

### Step 1: Craft Introspection Query

**Context**: Send a standard GraphQL introspection query to fetch the schema.

**Instructions**: In Burp Repeater, set body to a query like: {"query": "query IntrospectionQuery { __schema { queryType { name } mutationType { name } types { ...FullType } directives { name description locations args { ...InputValue } } } } fragment FullType on __Type { kind name description fields(includeDeprecated: true) { name description args { ...InputValue } type { ...TypeRef } isDeprecated deprecationReason } inputFields { ...InputValue } interfaces { ...TypeRef } enumValues(includeDeprecated: true) { name description isDeprecated deprecationReason } possibleTypes { ...TypeRef } } fragment InputValue on __InputValue { name description type { ...TypeRef } defaultValue } fragment TypeRef on __Type { kind name ofType { kind name ofType { kind name ofType { kind name ofType { kind name ofType { kind name ofType { kind name ofType { kind name } } } } } } } }"}

> Send and parse response for mutations section.

### Step 2: Analyze Response

**Context**: Extract mutation names from the schema response.

**Instructions**: Review JSON response for mutationType.fields, noting templateInstall and workflowActivate.

> Expected: List of mutations accessible despite low perms.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[graphql]]
- [[introspection]]
- [[Discovery]]
