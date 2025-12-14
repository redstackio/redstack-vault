---
id: uuid-destroy-project
data: >-
  mutation test { destroySnippet(input: {id:
  "gid://gitlab/Project/<project_id>"}) { errors } }
tags:
  - graphql
  - deletion
type: command
output: null
executor: graphql
platforms:
  - Web
  - GitLab
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.128Z'
verified: false
validated: true
submitted: true
---
# destroy-snippet-mutation-project

## Command

```graphql
mutation test { destroySnippet(input: {id: "gid://gitlab/Project/<project_id>"}) { errors } }
```

## Description

Alternative GraphQL mutation using a project global ID to attempt repository deletion, simplifying reproduction for maintainers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| id | Global ID of Project (e.g., gid://gitlab/Project/123) | Yes |

## Examples

### Basic Usage

Replace <project_id> with actual ID from GitLab.

## Expected Output

Potential success or errors; repository deleted if resolved.

## Related

- [[commands/destroy-snippet-mutation-diffnote]]
- [[procedures/Execute-DestroySnippet-Mutation]]
